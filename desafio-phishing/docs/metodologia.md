# Metodologia

## 1. Análise da referência
Foi lido o README do repositório cassiano-dio/cibersecurity-desafio-phishing. Ele descreve um exercício com Kali Linux e SET para estudar clonagem de página e recebimento de credenciais. O README oficial do SET também foi consultado para identificar sua finalidade como framework de avaliações autorizadas.

A imagem de resultados do autor original não foi usada como evidência deste projeto.

## 2. Entendimento das etapas do laboratório original
| Conceito | O que representa | O que seria necessário verificar em um laboratório |
| --- | --- | --- |
| Ambiente Kali | Sistema que disponibiliza ferramentas de segurança | Versão, instalação e isolamento |
| Interface de rede | Conectividade entre máquinas de teste | Endereço e segmento do laboratório |
| Vetor web | Uso de uma página como parte da engenharia social | Página fictícia e escopo autorizado |
| Clonagem | Reprodução da apresentação de uma página | Recursos carregados e destino do formulário |
| Recebimento de campos | Chegada de dados de teste ao receptor | Registro sanitizado e correspondência com o envio |

A tabela descreve o exercício conceitualmente. Nenhuma dessas verificações foi executada com SET neste projeto.

## 3. Modelo implementado
A simulação usa cenários definidos no próprio código. Cada cenário contém:
- identificação fictícia;
- URL de destino fictícia;
- indicador booleano de presença hipotética de senha;
- indicador de confirmação de envio.

A função de origem compara esquema, host e porta efetiva. As URLs são constantes de exemplo, e a função não foi projetada como um filtro de produção contra URLs maliciosas.

A regra de exposição potencial é:
```text
envio confirmado E campo de senha presente E origem diferente da esperada
```

O modelo não coleta ou armazena valores de senha. Seu propósito é tornar explícita a relação entre destino e envio.

## 4. Verificação
O script valida três expectativas:
1. Origem esperada com envio: sem exposição por desvio de origem no modelo.
2. Origem diferente com envio: exposição potencial indicada.
3. Origem diferente sem envio: sem exposição pelo mecanismo modelado.

Essas verificações não afirmam que uma origem esperada está livre de comprometimento ou de outras vulnerabilidades. Também não abrangem preenchimento automático, código malicioso em páginas ou vazamento antes do envio.

## 5. Evidência
O arquivo evidencias/saida-simulacao.txt contém a saída da execução local. As conclusões estão limitadas ao comportamento do script incluído.
