"""Criptografa somente laboratorio/teste.txt e preserva o original."""
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from config import CIFRADO, KEY, MAGIC, NONCE_SIZE, ORIGINAL
#AES-GCM detecta alteracoes no conteudo

def main():
    if ORIGINAL.is_symlink() or CIFRADO.is_symlink():
        raise ValueError("O laboratório não aceita links simbólicos nos arquivos.")
    dados = ORIGINAL.read_bytes()
    nonce = os.urandom(NONCE_SIZE)
    conteudo = AESGCM(KEY).encrypt(nonce, dados, MAGIC)
    # Criação exclusiva: nunca sobrescreve um resultado existente.
    with CIFRADO.open("xb") as arquivo:
        arquivo.write(MAGIC + nonce + conteudo)
    print("Criptografia concluída: laboratorio/teste.txt.aes")
    print("Original preservado: laboratorio/teste.txt")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as erro:
        raise SystemExit(f"Criptografia interrompida: {erro}") from erro
