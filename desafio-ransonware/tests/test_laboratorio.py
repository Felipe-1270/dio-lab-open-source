"""Integração: scripts executados em cópias temporárias com dados fictícios."""
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJETO = Path(__file__).resolve().parents[1]


class LaboratorioTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        for nome in ("config.py", "encrypter.py", "decrypter.py"):
            shutil.copy2(PROJETO / nome, self.base / nome)
        self.lab = self.base / "laboratorio"
        self.lab.mkdir()
        self.original = self.lab / "teste.txt"
        self.cifrado = self.lab / "teste.txt.aes"
        self.recuperado = self.lab / "teste.recuperado.txt"
        self.dados = "Conteúdo fictício, acentos e bytes: áéç\n".encode() + bytes(range(256))
        self.original.write_bytes(self.dados)

    def executar(self, nome):
        return subprocess.run(
            [sys.executable, str(self.base / nome)],
            cwd=self.base.parent,
            text=True,
            capture_output=True,
            timeout=15,
        )

    def criptografar(self):
        resultado = self.executar("encrypter.py")
        self.assertEqual(resultado.returncode, 0, resultado.stderr)

    def test_recuperacao_integral_e_preservacao(self):
        self.criptografar()
        pacote = self.cifrado.read_bytes()
        self.assertTrue(pacote.startswith(b"DIOAES1"))
        self.assertEqual(len(pacote), len(self.dados) + 35)
        resultado = self.executar("decrypter.py")
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertEqual(self.recuperado.read_bytes(), self.dados)
        self.assertEqual(self.original.read_bytes(), self.dados)
        self.assertEqual(self.cifrado.read_bytes(), pacote)

    def test_recusa_sobrescrita_cifrado(self):
        self.criptografar()
        antes = self.cifrado.read_bytes()
        self.assertNotEqual(self.executar("encrypter.py").returncode, 0)
        self.assertEqual(self.cifrado.read_bytes(), antes)
        self.assertEqual(self.original.read_bytes(), self.dados)

    def test_recusa_sobrescrita_recuperado(self):
        self.criptografar()
        self.recuperado.write_bytes(b"resultado anterior")
        self.assertNotEqual(self.executar("decrypter.py").returncode, 0)
        self.assertEqual(self.recuperado.read_bytes(), b"resultado anterior")

    def test_rejeita_conteudo_adulterado(self):
        self.criptografar()
        pacote = bytearray(self.cifrado.read_bytes())
        pacote[-1] ^= 1
        self.cifrado.write_bytes(pacote)
        resultado = self.executar("decrypter.py")
        self.assertNotEqual(resultado.returncode, 0)
        self.assertIn("Falha de autenticação", resultado.stderr)
        self.assertFalse(self.recuperado.exists())

    def test_rejeita_chave_incorreta(self):
        self.criptografar()
        config = self.base / "config.py"
        config.write_text(config.read_text().replace("batata10batata10", "0000000000000000"))
        resultado = self.executar("decrypter.py")
        self.assertNotEqual(resultado.returncode, 0)
        self.assertIn("Falha de autenticação", resultado.stderr)
        self.assertFalse(self.recuperado.exists())

    def test_rejeita_pacote_incompleto(self):
        self.cifrado.write_bytes(b"DIOAES1")
        self.assertNotEqual(self.executar("decrypter.py").returncode, 0)
        self.assertFalse(self.recuperado.exists())


if __name__ == "__main__":
    unittest.main()
