from colorama import Fore, Style, init
from utilizador import registar_utilizador
from casino import Casino
init(autoreset=True)
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
            casino.jogar_quiz(utilizador)
        elif opcao == "2":
            casino.jogar_slots(utilizador)
        elif opcao == "3":
            utilizador.mostrar()
        elif opcao == "4":
            print(Fore.LIGHTCYAN_EX + f"\n  Obrigado por jogar no {casino.nome}!")
            print(Fore.LIGHTWHITE_EX + f"  Saldo final: {utilizador.saldo:.2f} €")
            print(Fore.LIGHTBLUE_EX + "  Até à próxima!\n")
            break
        else:
            print(Fore.LIGHTRED_EX + "  Opção inválida.")
def main():
    casino = Casino()
    casino.apresentar()
    print(Fore.LIGHTBLUE_EX + "\n╔══════════════════════════════════════╗")
    print(Fore.LIGHTBLUE_EX + "║          BEM-VINDO AO CASINO         ║")
    print(Fore.LIGHTBLUE_EX + "╚══════════════════════════════════════╝")
    print(Fore.LIGHTWHITE_EX + "  1) Registar utilizador")
    print(Fore.LIGHTWHITE_EX + "  2) Sair")
    opcao = input(Fore.LIGHTYELLOW_EX + "\n  Escolha: " + Style.RESET_ALL).strip()
    if opcao != "1":
        print(Fore.LIGHTRED_EX + "  Inválido!!!\n")
        return
    utilizador = registar_utilizador()
    if utilizador is None:
        return
    print(Fore.LIGHTGREEN_EX + f"\n  Registo concluído com sucesso! Bem-vindo, {utilizador.nome}!")
    menu_jogos(casino, utilizador)
if __name__ == "__main__":
    main()
