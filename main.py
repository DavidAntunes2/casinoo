from colorama import Fore, Style, init
from utilizador import registar_utilizador
from casino import Casino

init(autoreset=True)


def http_status(code: int, mensagem: str = ""):
    cores = {
        2: Fore.LIGHTGREEN_EX,
        4: Fore.LIGHTYELLOW_EX,
        5: Fore.LIGHTRED_EX,
    }
    familia = code // 100
    cor = cores.get(familia, Fore.WHITE)
    print(cor + f"  [{code}] {mensagem}")


def menu_jogos(casino: Casino, utilizador) -> None:
    while True:
        print(Fore.LIGHTBLUE_EX + "\n╔══════════════════════════════════════╗")
        print(Fore.LIGHTBLUE_EX + "║              MENU DE JOGOS           ║")
        print(Fore.LIGHTBLUE_EX + "╚══════════════════════════════════════╝")
        print(Fore.LIGHTWHITE_EX + f"  Saldo: {utilizador.saldo:.2f} €\n")
        print(Fore.WHITE + "  1) Quiz de Futebol")
        print(Fore.WHITE + "  2) Slot Machine")
        print(Fore.WHITE + "  3) Ver os meus dados")
        print(Fore.WHITE + "  4) Sair")

        opcao = input(Fore.LIGHTYELLOW_EX + "\n  Escolha: " + Style.RESET_ALL).strip()

        if opcao == "1":
            http_status(200, "OK — A carregar Quiz de Futebol")
            casino.jogar_quiz(utilizador)
        elif opcao == "2":
            http_status(200, "OK — A carregar Slot Machine")
            casino.jogar_slots(utilizador)
        elif opcao == "3":
            http_status(200, "OK — A carregar dados do utilizador")
            utilizador.mostrar()
        elif opcao == "4":
            http_status(200, "OK — Sessão terminada com sucesso")
            print(Fore.LIGHTCYAN_EX + f"\n  Obrigado por jogar no {casino.nome}!")
            print(Fore.LIGHTWHITE_EX + f"  Saldo final: {utilizador.saldo:.2f} €")
            print(Fore.LIGHTBLUE_EX + "  Até à próxima!\n")
            break
        else:
            http_status(400, "Bad Request — Opção inválida")


def main():
    casino = Casino()
    casino.apresentar()

    print(Fore.LIGHTBLUE_EX + "\n╔══════════════════════════════════════╗")
    print(Fore.LIGHTBLUE_EX + "║          BEM-VINDO AO CASINO         ║")
    print(Fore.LIGHTBLUE_EX + "╚══════════════════════════════════════╝")
    print(Fore.LIGHTWHITE_EX + "  1) Registar utilizador")
    print(Fore.LIGHTWHITE_EX + "  2) Sair")

    opcao = input(Fore.LIGHTYELLOW_EX + "\n  Escolha: " + Style.RESET_ALL).strip()

    if opcao == "2":
        http_status(200, "OK — Saída solicitada pelo utilizador")
        return

    if opcao != "1":
        http_status(400, "Bad Request — Opção inválida")
        return

    http_status(102, "Processing — A processar registo...")
    utilizador = registar_utilizador()

    if utilizador is None:
        http_status(403, "Forbidden — Acesso negado (menor de idade ou dados inválidos)")
        return

    http_status(201, "Created — Utilizador registado com sucesso")
    print(Fore.LIGHTGREEN_EX + f"\n  Bem-vindo, {utilizador.nome}!")
    menu_jogos(casino, utilizador)


if __name__ == "__main__":
    main()
