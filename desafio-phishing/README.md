# Desafio de cibersegurança — estudo de phishing
Autor: [Felipe-1270](https://github.com/Felipe-1270)

## Apresentação
Projeto educacional baseado no desafio [cibersecurity-desafio-phishing](https://github.com/cassiano-dio/cibersecurity-desafio-phishing), de cassiano-dio. O objetivo é compreender a engenharia social por páginas de autenticação falsas e relacionar esse mecanismo a medidas de prevenção.

**Estado do projeto:** estudo documentado com simulação local em Python executada usando exclusivamente dados fictícios. O exercício original com Kali Linux, SET e clonagem de uma página não foi executado. Não há evidência de captura real de credenciais.

## Objetivos
- Explicar a diferença entre a aparência de uma página e a origem que recebe seus dados.
- Identificar o papel do Kali Linux e do Social-Engineer Toolkit (SET) no exercício de referência.
- Demonstrar, com um modelo offline, por que enviar informações a uma origem incorreta representa risco.
- Documentar limitações e controles de prevenção.

## O desafio de referência
O README original apresenta Kali Linux e SET, incluindo os conceitos de ataques de engenharia social, vetores web, coleta de credenciais e clonagem de sites. O exemplo usa uma página do Facebook como referência visual.

Neste projeto, essa sequência foi analisada conceitualmente. A demonstração complementar usa nomes fictícios e não acessa Facebook, não clona páginas e não recebe dados de pessoas.

| Elemento | Papel no exercício de referência | Situação nesta entrega |
| --- | --- | --- |
| Kali Linux | Ambiente de ferramentas de segurança | Não instalado nem utilizado |
| SET | Framework para avaliações autorizadas de engenharia social | Documentação consultada; não executado |
| Site Cloner | Reprodução de página para o cenário de laboratório | Apenas estudado |
| Credential Harvester | Recebimento de dados enviados a uma página do laboratório | Apenas estudado |
| Python 3 | Execução da simulação complementar offline | Executado |
| Capturas de tela de um ataque | Evidência de execução do laboratório original | Não disponíveis |

## Como funciona o risco
Uma página pode apresentar nome, logotipo e campos parecidos com os de um serviço conhecido. Se a pessoa fornecer informações e o formulário enviá-las a uma origem controlada por terceiros, esses dados podem ser expostos sem que o servidor legítimo seja comprometido.

A origem é composta por esquema, host e porta efetiva. Ela ajuda a distinguir destinos, mas sua verificação isolada não é um mecanismo completo de segurança. Nesta simulação, a origem fictícia esperada é `https://portal.example`; `https://acesso.example` representa uma origem diferente.

## Estrutura
| Arquivo | Finalidade |
| --- | --- |
| [README.md](README.md) | Visão geral, instruções e limitações |
| [docs/metodologia.md](docs/metodologia.md) | Análise conceitual do desafio e método da simulação |
| [docs/resultados.md](docs/resultados.md) | Resultados efetivamente observados |
| [docs/prevencao.md](docs/prevencao.md) | Controles e resposta a incidentes |
| [simulacao.py](simulacao.py) | Modelo offline com cenários fixos e fictícios |
| [evidencias/saida-simulacao.txt](evidencias/saida-simulacao.txt) | Saída real da execução do modelo |
| [images/README.md](images/README.md) | Orientações para futuras capturas de laboratório |

## Executar a simulação
Pré-requisito: Python 3.10 ou superior; não há dependências externas.

Na raiz do projeto:
```bash
python3 simulacao.py
```

No Windows, pode ser necessário usar `py simulacao.py`.

O script processa três cenários fixos em memória: envio à origem esperada, envio à origem diferente e desistência antes do envio. Ele imprime uma tabela e valida os resultados esperados por meio de asserções.

Não abre portas, não realiza requisições de rede, não lê dados do usuário e não implementa autenticação. O campo de senha é representado somente por um booleano que indica sua presença hipotética. A indicação de exposição descreve a regra do modelo, não uma captura observada em rede.

## Resultados e evidências
A simulação foi executada com sucesso. Houve exposição potencial no cenário em que o envio foi destinado à origem diferente; o modelo não indicou exposição nos outros dois cenários. Consulte [o relatório](docs/resultados.md) e [a saída da execução](evidencias/saida-simulacao.txt).

Esses resultados validam o modelo didático. Não validam funcionamento do SET, clonagem de páginas atuais, entrega de campanhas ou eficácia de controles em ambiente real.

## Limitações e próxima etapa
- A etapa prática do desafio de referência permanece pendente.
- Não foram configurados Kali Linux, SET, rede de laboratório ou página de teste.
- Não existem capturas de tela do exercício original.
- O modelo não inclui navegador, HTTP real, TLS, cookies, sessões ou mecanismos de MFA.
- Se a avaliação exigir execução prática com SET, esta documentação e a simulação complementar não bastam para comprovar essa etapa.

Uma futura execução deve usar ambiente isolado e autorizado, página fictícia e dados de teste. Depois, seus resultados reais podem ser acrescentados à documentação com as evidências correspondentes.

## Prevenção
Verificar o domínio antes de inserir dados, usar um gerenciador de senhas e preferir autenticação resistente a phishing são controles complementares. Para organizações, treinamento, filtragem de mensagens e monitoramento também podem reduzir o risco. Veja as ressalvas em [prevenção](docs/prevencao.md).

## Uso e atribuição
Material destinado a estudo. Não contém contas, senhas, tokens ou dados de terceiros. O conteúdo foi organizado com apoio de IA; a execução comprovada aqui é somente a do script incluído.

O desafio original é citado como referência, sem copiar sua imagem de resultado ou apresentar trabalho de terceiros como execução própria.

## Referências
- [Desafio original — cassiano-dio](https://github.com/cassiano-dio/cibersecurity-desafio-phishing)
- [Social-Engineer Toolkit — TrustedSec](https://github.com/trustedsec/social-engineer-toolkit)
- [Documentação oficial do Python: urllib.parse](https://docs.python.org/3/library/urllib.parse.html)
