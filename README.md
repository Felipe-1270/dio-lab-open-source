# Laboratórios DIO — Felipe-1270

Este repositório reúne o material existente do laboratório de contribuição open source e o estudo de phishing adicionado em uma pasta própria.

## Desafio de cibersegurança: phishing

Acesse o **[README detalhado do projeto](desafio-phishing/README.md)** para consultar os objetivos, ferramentas, metodologia, instruções de execução, resultados, limitações e referências.

| Recurso | Conteúdo |
| --- | --- |
| [Projeto completo](desafio-phishing/README.md) | Documentação principal do desafio |
| [Metodologia](desafio-phishing/docs/metodologia.md) | Análise da referência e modelo utilizado |
| [Simulação Python](desafio-phishing/simulacao.py) | Demonstração offline com dados fictícios |
| [Resultados](desafio-phishing/docs/resultados.md) | Interpretação e atividades efetivamente realizadas |
| [Evidência da execução](desafio-phishing/evidencias/saida-simulacao.txt) | Saída real dos três cenários |
| [Prevenção](desafio-phishing/docs/prevencao.md) | Controles e resposta |
| [Pasta de imagens](desafio-phishing/images/README.md) | Orientações para futuras capturas |

### Executar

Com Python 3.10 ou superior, na raiz do repositório:

```bash
python3 desafio-phishing/simulacao.py
```

No Windows, pode ser necessário usar `py` em lugar de `python3`. Não há dependências externas.

### Estado da entrega

A documentação e a simulação offline estão concluídas. A simulação validou três cenários com dados fictícios, sem acessar serviços externos ou coletar senhas.

**A prática original com Kali Linux e SET não foi executada.** Se o desafio exigir essa prática, ela ainda precisa ser realizada e documentada; a simulação complementar não comprova essa etapa.

Referência: [cibersecurity-desafio-phishing — cassiano-dio](https://github.com/cassiano-dio/cibersecurity-desafio-phishing).

## Material de contribuição open source

O material anterior continua disponível em [CONTRIBUTING.md](CONTRIBUTING.md), [community/](community/), [docs/](docs/), [scripts/](scripts/) e [utils/](utils/).
