"""Modelo offline sobre envio de dados a uma origem diferente.
Não coleta senhas, não abre conexões e não recebe entrada do usuário.
Python 3.10+; somente biblioteca padrão.
"""
from dataclasses import dataclass
from urllib.parse import urlsplit


@dataclass(frozen=True)
class Cenario:
    nome: str
    destino: str
    campo_senha_presente: bool
    envio_confirmado: bool


def origem(url: str) -> tuple[str, str, int]:
    """Normaliza origem das URLs HTTP(S) fixas usadas nesta demonstração."""
    partes = urlsplit(url)
    esquema = partes.scheme.lower()
    host = partes.hostname
    if esquema not in {"http", "https"} or host is None:
        raise ValueError("O modelo exige uma URL HTTP(S) com host.")
    porta = partes.port
    if porta is None:
        porta = 443 if esquema == "https" else 80
    return esquema, host.lower(), porta


ORIGEM_ESPERADA = origem("https://portal.example")
CENARIOS = (
    Cenario("Destino esperado", "https://portal.example/login", True, True),
    Cenario("Destino diferente", "https://acesso.example/login", True, True),
    Cenario("Desistência", "https://acesso.example/login", True, False),
)


def exposicao_potencial(cenario: Cenario) -> bool:
    return (
        cenario.envio_confirmado
        and cenario.campo_senha_presente
        and origem(cenario.destino) != ORIGEM_ESPERADA
    )


def main() -> None:
    print("SIMULAÇÃO DIDÁTICA OFFLINE — DADOS FICTÍCIOS")
    print("Nenhum serviço foi acessado; nenhum valor de senha foi utilizado.")
    print()
    print("Cenário | Destino | Envio | Exposição potencial")
    resultados = []
    for cenario in CENARIOS:
        exposto = exposicao_potencial(cenario)
        resultados.append(exposto)
        print(
            f"{cenario.nome} | {cenario.destino} | "
            f"{'sim' if cenario.envio_confirmado else 'não'} | "
            f"{'sim' if exposto else 'não'}"
        )
    assert resultados == [False, True, False], "Resultado divergente do modelo."
    print()
    print("Verificação: 3 cenários validados.")
    print("Limite: modelo conceitual; não executa o laboratório Kali/SET.")


if __name__ == "__main__":
    main()
