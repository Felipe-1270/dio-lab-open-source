# Resultados

## Escopo executado
Foi executado o arquivo simulacao.py em ambiente local com Python 3, sem rede e sem entrada de dados reais.

| Cenário | Destino | Envio confirmado | Exposição potencial no modelo |
| --- | --- | --- | --- |
| Destino esperado | https://portal.example/login | Sim | Não |
| Destino diferente | https://acesso.example/login | Sim | Sim |
| Desistência | https://acesso.example/login | Não | Não |

As três asserções do programa passaram. A saída está em [saida-simulacao.txt](../evidencias/saida-simulacao.txt).

## Interpretação
O segundo cenário satisfaz as três condições da regra: envio confirmado, campo de senha hipoteticamente presente e destino com origem diferente. O terceiro demonstra que, neste modelo, desistir antes de enviar interrompe esse mecanismo específico de exposição.

A execução confirma que o programa aplica a regra declarada. Não demonstra um ataque real nem mede a segurança de um sistema.

## Atividades não realizadas
- Instalação ou uso de Kali Linux e SET.
- Clonagem da página de um serviço.
- Hospedagem de página ou abertura de receptor de dados.
- Envio de mensagens ou interação com vítimas.
- Captura de credenciais ou acesso a contas.
- Validação prática de MFA ou de ferramentas de proteção.

## Evidências futuras
Capturas futuras devem mostrar apenas laboratório autorizado com dados fictícios, incluindo ambiente utilizado, configuração relevante e resultado observado. Cada captura deverá conter descrição suficiente para relacioná-la à etapa executada. O material atual não inclui essas evidências.
