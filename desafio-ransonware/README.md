# Laboratório DIO — criptografia de arquivos em Python

Autor: [Felipe-1270](https://github.com/Felipe-1270)

## Objetivo e contexto

Implementar e compreender o ciclo de criptografia e descriptografia de um arquivo em Python.


## Arquivos

| Arquivo | Função |
| --- | --- |
| [encrypter.py](encrypter.py) | Criptografa |
| [decrypter.py](decrypter.py) | Descriptografa  |
| [config.py](config.py) | Mantém caminhos e chave comuns, auxilia para dar escalabilidade |
| [requirements.txt](requirements.txt) | Dependência Python fixada |
| [tests/test_laboratorio.py](tests/test_laboratorio.py) | Testes do fluxo e das falhas relevantes |


## Decisões técnicas

- **AES-128-GCM:** usa uma chave de 16 bytes e permite detectar alterações no conteúdo autenticado.
- **Chave comum:** `batata10batata10`, compartilhada pelos dois scripts por meio de `config.py`. A chave está publicada e é previsível: serve somente ao exercício, sem oferecer sigilo para informações reais.
- **Nonce:** 12 bytes aleatórios por criptografia, armazenados junto ao resultado. Não é uma segunda chave e não precisa ser secreto. A combinação de chave e nonce não deve se repetir.
- **Preservação:** original e arquivo cifrado são mantidos. O texto recuperado usa um nome diferente.
- **Sem sobrescrita:** o modo `xb` recusa saídas já existentes.
- **Escopo fixo:** os scripts usam caminhos relativos à sua própria pasta, sem aceitar diretórios ou arquivos arbitrários pela linha de comando.

### Relação com os scripts das aulas

A implementação foi adaptada do vídeo assistido. O original utiliza a biblioteca `pyaes` com AES-CTR e removem o arquivo de entrada antes de concluir a gravação. Nesta versão, foi adotada a biblioteca `cryptography` com AES-GCM, preservando as entradas e acrescentando autenticação e verificação.


## Pré-requisitos

Python 3.10 ou superior e a dependência de `requirements.txt`. Execute os comandos abaixo dentro de `desafio-ransonware/`.


## Referências

- [Documentação oficial: AESGCM](https://cryptography.io/en/stable/hazmat/primitives/aead/#cryptography.hazmat.primitives.ciphers.aead.AESGCM)
- [Python: abertura de arquivos](https://docs.python.org/3/library/functions.html#open)
- Material de aula: duas imagens dos scripts fornecidas pelo aluno nesta atividade; não republicadas.
