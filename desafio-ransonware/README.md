# Laboratório DIO — criptografia de arquivos em Python

Autor: [Felipe-1270](https://github.com/Felipe-1270)

## Objetivo e contexto

Implementar e compreender o ciclo de criptografia e descriptografia de um arquivo de teste em Python, documentando as decisões técnicas e os resultados.

O enunciado do curso utiliza o tema ransomware para contextualizar o uso indevido da criptografia. Esta entrega demonstra o mecanismo criptográfico em um arquivo fictício, mantendo o original disponível. Não implementa extorsão, exclusão de originais, busca de arquivos, execução automática, persistência ou propagação.

## Arquivos

| Arquivo | Função |
| --- | --- |
| [encrypter.py](encrypter.py) | Criptografa somente o arquivo de exemplo |
| [decrypter.py](decrypter.py) | Descriptografa o resultado em um novo arquivo |
| [config.py](config.py) | Mantém caminhos e chave comuns |
| [requirements.txt](requirements.txt) | Dependência Python fixada |
| [laboratorio/teste.txt](laboratorio/teste.txt) | Conteúdo fictício para o exercício |
| [tests/test_laboratorio.py](tests/test_laboratorio.py) | Testes do fluxo e das falhas relevantes |
| [evidencias/resultados.txt](evidencias/resultados.txt) | Registro real da validação |

## Decisões técnicas

- **AES-128-GCM:** usa uma chave de 16 bytes e permite detectar alterações no conteúdo autenticado.
- **Chave comum:** `batata10batata10`, compartilhada pelos dois scripts por meio de `config.py`. A chave está publicada e é previsível: serve somente ao exercício, sem oferecer sigilo para informações reais.
- **Nonce:** 12 bytes aleatórios por criptografia, armazenados junto ao resultado. Não é uma segunda chave e não precisa ser secreto. A combinação de chave e nonce não deve se repetir.
- **Preservação:** original e arquivo cifrado são mantidos. O texto recuperado usa um nome diferente.
- **Sem sobrescrita:** o modo `xb` recusa saídas já existentes.
- **Escopo fixo:** os scripts usam caminhos relativos à sua própria pasta, sem aceitar diretórios ou arquivos arbitrários pela linha de comando.

### Relação com os scripts das aulas

A implementação foi adaptada das imagens fornecidas pelo aluno. As imagens utilizam `pyaes` com AES-CTR e removem o arquivo de entrada antes de concluir a gravação. Nesta versão, foi adotada a biblioteca `cryptography` com AES-GCM, preservando as entradas e acrescentando autenticação.

**Os formatos são diferentes:** este decrypter não recupera arquivos produzidos pelo script AES-CTR original. Não se trata de uma transcrição literal das imagens.

## Pré-requisitos

Python 3.10 ou superior e a dependência de `requirements.txt`. Execute os comandos abaixo dentro de `desafio-ransonware/`.

### Instalação

```bash
python -m venv .venv
```

Ative o ambiente no Linux/macOS:
```bash
source .venv/bin/activate
```

No PowerShell do Windows:
```powershell
.venv\Scripts\Activate.ps1
```

Se a política local bloquear a ativação, use diretamente `.venv\Scripts\python.exe` nos comandos seguintes.

```bash
python -m pip install -r requirements.txt
```

No Linux, o executável inicial pode se chamar `python3`; no Windows, também pode estar disponível como `py`.

## Execução

O arquivo fictício já está em `laboratorio/teste.txt`.

```bash
python encrypter.py
python decrypter.py
```

Resultado:
1. O original permanece em `laboratorio/teste.txt`.
2. A criptografia cria `laboratorio/teste.txt.aes`.
3. A descriptografia cria `laboratorio/teste.recuperado.txt`.

Compare os bytes:
```bash
python -c "from pathlib import Path; a=Path('laboratorio/teste.txt').read_bytes(); b=Path('laboratorio/teste.recuperado.txt').read_bytes(); print('Conteúdo idêntico:', a == b)"
```

Uma segunda execução é recusada se a saída correspondente já existir. Para repetir, utilize uma cópia nova do diretório de laboratório ou mova os resultados anteriores para outra pasta.

## Formato do arquivo cifrado

| Campo | Tamanho |
| --- | --- |
| Identificador `DIOAES1` | 7 bytes |
| Nonce | 12 bytes |
| Texto cifrado | Mesmo tamanho do texto original |
| Tag de autenticação | 16 bytes, acrescentados pela biblioteca |

O identificador também é fornecido como dado associado autenticado. O decrypter verifica o formato e a autenticação antes de gravar o resultado.

## Validação

```bash
python -m unittest discover -s tests -v
```

Os testes executam cópias temporárias dos scripts e verificam:
- recuperação byte a byte e preservação das entradas;
- recusa de sobrescrita;
- rejeição de conteúdo adulterado;
- rejeição de chave incorreta;
- rejeição de pacote incompleto.

Os resultados observados estão em [evidencias/resultados.txt](evidencias/resultados.txt). Arquivos cifrados e recuperados não são versionados, pois podem ser reproduzidos pelos scripts. A execução foi validada em Linux com Python 3.12.14 e cryptography 50.0.2; Windows não foi testado.

## Limitações

A chave publicada não protege dados reais. Os arquivos são lidos integralmente em memória; o código foi pensado para um pequeno exemplo didático. O nonce aleatório reduz a probabilidade de repetição, mas o projeto não gerencia o ciclo de vida de chaves. A escrita exclusiva impede sobrescrita, mas uma falha de disco pode deixar uma saída parcial. Não é uma ferramenta de backup nem um utilitário de proteção para produção.

## Aprendizados

A recuperação depende da mesma chave, do nonce e do formato correto. O modo de operação importa: AES-GCM permite autenticar o conteúdo. Preservar entradas e testar falhas evita confundir um exercício criptográfico com perda de dados.

## Referências

- [Documentação oficial: AESGCM](https://cryptography.io/en/stable/hazmat/primitives/aead/#cryptography.hazmat.primitives.ciphers.aead.AESGCM)
- [Python: abertura de arquivos](https://docs.python.org/3/library/functions.html#open)
- Material de aula: duas imagens dos scripts fornecidas pelo aluno nesta atividade; não republicadas.
