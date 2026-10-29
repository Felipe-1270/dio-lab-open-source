"""Constantes do laboratório; a chave publicada é apenas didática."""
from pathlib import Path

BASE = Path(__file__).resolve().parent
LAB = BASE / "laboratorio"
ORIGINAL = LAB / "teste.txt"
CIFRADO = LAB / "teste.txt.aes"
RECUPERADO = LAB / "teste.recuperado.txt"
KEY = b"batata10batata10"
MAGIC = b"DIOAES1"
NONCE_SIZE = 12
