from utilizador import *


# ══════════════════════════════════════════════════════════════════════════════
#  ECRÃ — REGISTAR CLIENTE
# ══════════════════════════════════════════════════════════════════════════════

def ecra_registar():
    cabecalho()
    moldura("✦  Novo Cliente VIP  ✦")
    espaco()

    print(C.pintar("  Preencha os dados do novo membro:", C.DIM, C.CINZA))
    espaco()

    p     = prompt("Primeiro nome")
    u     = prompt("Último nome")
    nif   = prompt("NIF (9 dígitos)")
    iban  = prompt("IBAN (PT + 23 dígitos)")
    saldo = prompt("Depósito inicial (€)")
    nasc  = prompt("Data de nascimento (DD-MM-AAAA)")
    mail  = prompt("Email")

    espaco()
    animacao_loading("A validar dados")

    cod, msg = registar_utilizador(p, u, nif, iban, saldo, nasc, mail)

    espaco()
    if cod == 201:
        sucesso("Cliente registado com sucesso!")
        tabela_cliente(msg, jogadores[msg])
    elif cod == 409:
        erro(f"Cliente já existe  →  {msg}")
    else:
        erro(msg)

    espaco()
    input(C.pintar("  Pressione ENTER para continuar...", C.DIM, C.CINZA))


# ══════════════════════════════════════════════════════════════════════════════
#  ECRÃ — LISTAR CLIENTES
# ══════════════════════════════════════════════════════════════════════════════

def ecra_listar():
    cabecalho()
    moldura("♠  Membros VIP  ♠")
    espaco()

    if not jogadores:
        espaco()
        print(centro(C.pintar("Nenhum cliente registado ainda.", C.DIM, C.CINZA)))
        espaco()
    else:
        r = obter_resumo()

        print(C.pintar("  RESUMO", C.BOLD, C.OURO2))
        linha_pontilhada()
        info("Total de membros", str(r['total']),          C.CREME)
        info("Saldo total",      f"{r['saldo_t']:,.2f} €", C.VERDE)
        info("High Rollers",     str(r['hr']),             C.OURO)
        info("VIP Standard",     str(r['vip']),            C.CINZA)

        espaco()
        print(C.pintar("  FICHAS", C.BOLD, C.OURO2))

        for id_vip, dados in jogadores.items():
            tabela_cliente(id_vip, dados)

    espaco()
    input(C.pintar("  Pressione ENTER para continuar...", C.DIM, C.CINZA))


# ══════════════════════════════════════════════════════════════════════════════
#  MENU PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════

def menu():
    while True:
        cabecalho()
        moldura("Menu Principal")
        espaco()

        menu_opcao("1", "Registar novo cliente")
        menu_opcao("2", "Listar clientes VIP")
        menu_opcao("0", "Sair")

        espaco()
        linha_simples(C.CINZA2)

        op = prompt("Escolha uma opção")

        if op == "1":
            ecra_registar()

        elif op == "2":
            ecra_listar()

        elif op == "0":
            cabecalho()
            print(centro(C.pintar("♠  Até à próxima, Membro VIP.  ♠", C.BOLD, C.OURO)))
            espaco()
            linha_dupla()
            espaco()
            break

        else:
            espaco()
            erro("Opção inválida. Escolha 0, 1 ou 2.")
            time.sleep(1.2)


if __name__ == "__main__":
    menu()
