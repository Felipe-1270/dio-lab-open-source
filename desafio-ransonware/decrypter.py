"""Recupera somente o arquivo cifrado do laboratório, sem excluir entradas."""
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from config import CIFRADO, KEY, MAGIC, NONCE_SIZE, RECUPERADO


def main():
    if CIFRADO.is_symlink() or RECUPERADO.is_symlink():
        raise ValueError("O laboratório não aceita links simbólicos nos arquivos.")
    pacote = CIFRADO.read_bytes()
    inicio = len(MAGIC)
    if not pacote.startswith(MAGIC) or len(pacote) < inicio + NONCE_SIZE + 16:
        raise ValueError("Formato inválido ou arquivo incompleto.")
    nonce = pacote[inicio:inicio + NONCE_SIZE]
    conteudo = pacote[inicio + NONCE_SIZE:]
    # Verifica a autenticação antes de criar o arquivo recuperado.
    dados = AESGCM(KEY).decrypt(nonce, conteudo, MAGIC)
    with RECUPERADO.open("xb") as arquivo:
        arquivo.write(dados)
    print("Descriptografia concluída: laboratorio/teste.recuperado.txt")
    print("Arquivo cifrado preservado: laboratorio/teste.txt.aes")


if __name__ == "__main__":
    try:
        main()
    except InvalidTag as erro:
        raise SystemExit(
            "Falha de autenticação: chave incorreta ou arquivo alterado."
        ) from erro
    except (OSError, ValueError) as erro:
        raise SystemExit(f"Descriptografia interrompida: {erro}") from erro
