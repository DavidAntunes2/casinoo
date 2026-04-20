from utils import *

carregar_dados()


# ══════════════════════════════════════════════════════════════════════════════
#  REGISTO
# ══════════════════════════════════════════════════════════════════════════════

def registar_utilizador(p_nome, u_nome, nif, iban, saldo, nasc, mail):

    ok, p_nome = validar_nome_parte(p_nome, "Primeiro nome")
    if not ok:
        return 400, p_nome

    ok, u_nome = validar_nome_parte(u_nome, "Último nome")
    if not ok:
        return 400, u_nome

    nome_completo = f"{p_nome} {u_nome}"

    if ofensivo(nome_completo):
        return 400, "Nome contém termos proibidos."

    ok, mail = validar_email(mail)
    if not ok:
        return 400, mail

    if ofensivo(mail):
        return 400, "Email contém termos proibidos."

    ok, nif = validar_nif(nif)
    if not ok:
        return 400, nif

    ok, iban = validar_iban(iban)
    if not ok:
        return 400, iban

    ok, idade = validar_idade(nasc)
    if not ok:
        return 400, idade

    try:
        saldo = float(str(saldo).replace(',', '.'))
        if saldo < 0:
            return 400, "Depósito negativo."
    except Exception:
        return 400, "Saldo inválido."

    id_vip = f"VIP-{nif[-3:]}{p_nome[0]}"

    if id_vip in jogadores:
        return 409, f"Já existe: {id_vip}"

    jogadores[id_vip] = {
        "nome":  nome_completo,
        "idade": idade,
        "nif":   nif,
        "iban":  iban,
        "saldo": saldo,
        "rank":  "💎 HIGH ROLLER" if saldo >= 5000 else "♠ VIP",
        "mail":  mail
    }

    guardar_dados()
    return 201, id_vip


# ══════════════════════════════════════════════════════════════════════════════
#  ECRÃ — REGISTAR CLIENTE
# ══════════════════════════════════════════════════════════════════════════════

def ecra_registar():
    cabecalho()
    moldura("✦  Novo Cliente VIP  ✦")
    espaco()

    print(C.pintar("  Preencha os dados do novo membro:", C.DIM, C.CINZA))
    espaco()

    p    = prompt("Primeiro nome")
    u    = prompt("Último nome")
    nif  = prompt("NIF (9 dígitos)")
    iban = prompt("IBAN (PT + 23 dígitos)")
    saldo= prompt("Depósito inicial (€)")
    nasc = prompt("Data de nascimento (DD-MM-AAAA)")
    mail = prompt("Email")

    espaco()
    animacao_loading("A validar dados")

    cod, msg = registar_utilizador(p, u, nif, iban, saldo, nasc, mail)

    espaco()
    if cod == 201:
        sucesso(f"Cliente registado com sucesso!")
        espaco()
        # mostra ficha do cliente recém-criado
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
        total   = len(jogadores)
        saldo_t = sum(v['saldo'] for v in jogadores.values())
        hr      = sum(1 for v in jogadores.values() if "HIGH ROLLER" in v['rank'])

        # estatísticas rápidas
        print(C.pintar("  RESUMO", C.BOLD, C.OURO2))
        linha_pontilhada()
        info("Total de membros",   str(total),            C.CREME)
        info("Saldo total",        f"{saldo_t:,.2f} €",   C.VERDE)
        info("High Rollers",       str(hr),               C.OURO)
        info("VIP Standard",       str(total - hr),       C.CINZA)

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
            print(centro(C.pintar("Até à próxima.  Boa sorte! ♠", C.BOLD, C.OURO)))
            espaco()
            linha_dupla()
            espaco()
            break

        else:
            espaco()
            erro("Opção inválida. Escolha 0, 1 ou 2.")
            time.sleep(1.2)
