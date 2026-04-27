# ==============================
# main.py
# menu terminal para testar CRUD
# ==============================

import os, time
from utilizador import (
    criar_utilizador_casino,
    listar_utilizadores_casino,
    consultar_utilizador_casino,
    atualizar_utilizador_casino,
    remover_utilizador_casino
)
from casino import (
    criar_casino,
    listar_casinos,
    consultar_casino,
    atualizar_casino,
    remover_casino
)

# ══════════════════════════════
#  CORES ANSI
# ══════════════════════════════
R   = "\033[0m"
B   = "\033[1m"
DIM = "\033[2m"

OURO   = "\033[38;5;220m"
OURO2  = "\033[38;5;178m"
CREME  = "\033[38;5;230m"
VERDE  = "\033[38;5;40m"
VERM   = "\033[38;5;160m"
CINZA  = "\033[38;5;244m"
CINZA2 = "\033[38;5;238m"
ROXO   = "\033[38;5;135m"
AZUL   = "\033[38;5;75m"

BG_VERDE = "\033[48;5;22m"
BG_VERM  = "\033[48;5;88m"

W = 52

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def ok(msg):
    print(f"\n  {B}{BG_VERDE}{CREME} OK {R}{B}{VERDE} {msg}{R}")

def erro(msg):
    print(f"\n  {B}{BG_VERM}{CREME} ERRO {R}{B}{VERM} {msg}{R}")

def inp(label):
    return input(f"  {OURO2}{B}>  {label}: {R}")

def pausa():
    print()
    input(f"  {DIM}{CINZA}Pressione ENTER para continuar...{R}")

def cabecalho():
    limpar()
    titulo = "[ ROYAL CASINO  --  Gestao de Membros ]"
    pad_esq = (W - len(titulo)) // 2
    pad_dir = W - len(titulo) - pad_esq
    print()
    print(OURO + "  +" + "=" * W + "+" + R)
    print(OURO + "  |" + " " * pad_esq + B + CREME + titulo + R + OURO + " " * pad_dir + "|" + R)
    print(OURO + "  +" + "=" * W + "+" + R)
    print()

def secao(titulo):
    print()
    print(f"  {OURO2}{'-' * W}{R}")
    print(f"  {B}{OURO}  {titulo}{R}")
    print(f"  {OURO2}{'-' * W}{R}")
    print()

def mostrar_utilizador(id_uc, dados):
    print(f"  {CINZA2}{'- ' * (W // 2)}{R}")
    print(f"  {B}{OURO}# {id_uc}{R}")
    print(f"  {CINZA}Nome        {CINZA2}......{R}  {CREME}{dados['nome']}{R}")
    print(f"  {CINZA}Email       {CINZA2}......{R}  {ROXO}{dados['email']}{R}")
    print(f"  {CINZA}Tipo        {CINZA2}......{R}  {OURO2}{dados['tipo_conta']}{R}")
    print(f"  {CINZA}Nascimento  {CINZA2}......{R}  {CREME}{dados['data_nascimento']}{R}")
    print(f"  {CINZA}NIF         {CINZA2}......{R}  {CINZA}{dados['nif']}{R}")
    print(f"  {CINZA}IBAN        {CINZA2}......{R}  {CINZA}{dados['iban']}{R}")

def mostrar_casino(id_c, dados):
    print(f"  {CINZA2}{'- ' * (W // 2)}{R}")
    print(f"  {B}{AZUL}# {id_c}{R}")
    print(f"  {CINZA}Nome        {CINZA2}......{R}  {CREME}{dados['nome']}{R}")
    print(f"  {CINZA}Localizacao {CINZA2}......{R}  {OURO2}{dados['localizacao']}{R}")
    print(f"  {CINZA}Licenca     {CINZA2}......{R}  {ROXO}{dados['licenca']}{R}")
    print(f"  {CINZA}Inauguracao {CINZA2}......{R}  {CREME}{dados['data_inauguracao']}{R}")
    print(f"  {CINZA}Saldo       {CINZA2}......{R}  {VERDE}EUR {dados['saldo']:,.2f}{R}")


# ══════════════════════════════
#  MENU PRINCIPAL
# ══════════════════════════════

def menu_principal():
    cabecalho()
    print(f"  {DIM}{CINZA}Escolha uma area:{R}")
    print()
    print(f"  {B}{OURO}[1]{R}  {OURO2}Gestao de Utilizadores{R}")
    print(f"  {B}{OURO}[2]{R}  {AZUL}Gestao de Casinos{R}")
    print(f"  {B}{OURO}[0]{R}  {CINZA}Sair{R}")
    print()
    print(f"  {OURO2}{'-' * W}{R}")
    return input(f"\n  {B}{OURO2}>  Opcao: {R}").strip()


# ══════════════════════════════
#  MENU UTILIZADOR
# ══════════════════════════════

def menu_utilizador():
    cabecalho()
    print(f"  {DIM}{CINZA}Gestao de Utilizadores -- Escolha uma operacao:{R}")
    print()
    ops = [
        ("1", "Criar utilizador",     VERDE),
        ("2", "Listar utilizadores",  OURO2),
        ("3", "Consultar utilizador", OURO2),
        ("4", "Atualizar utilizador", OURO2),
        ("5", "Remover utilizador",   VERM),
        ("0", "Voltar",               CINZA),
    ]
    for num, texto, cor in ops:
        print(f"  {B}{OURO}[{num}]{R}  {cor}{texto}{R}")
    print()
    print(f"  {OURO2}{'-' * W}{R}")
    return input(f"\n  {B}{OURO2}>  Opcao: {R}").strip()


def ecra_criar_utilizador():
    cabecalho()
    secao("Registar Novo Membro")
    nome  = inp("Nome completo")
    email = inp("Email")
    tipo  = inp("Tipo de conta  (standard / vip / high roller)")
    nasc  = inp("Data de nascimento  (DD-MM-AAAA)")
    nif   = inp("NIF  (9 digitos)")
    iban  = inp("IBAN  (PT + 23 digitos)")
    print(f"\n  {DIM}{CINZA}A validar dados...{R}", end="", flush=True)
    time.sleep(0.6)
    code, obj = criar_utilizador_casino(nome, email, tipo, nasc, nif, iban)
    print("\r" + " " * 30 + "\r", end="")
    if code == 201:
        ok("Membro registado com sucesso!")
        from utilizador import utilizadores_casino
        id_novo = list(utilizadores_casino.keys())[-1]
        mostrar_utilizador(id_novo, obj)
    else:
        erro(str(obj))
    pausa()

def ecra_listar_utilizadores():
    cabecalho()
    secao("Membros Registados")
    code, obj = listar_utilizadores_casino()
    if code == 200:
        print(f"  {DIM}{CINZA}Total: {len(obj)} membro(s){R}")
        for id_uc, dados in obj.items():
            mostrar_utilizador(id_uc, dados)
    else:
        erro(str(obj))
    pausa()

def ecra_consultar_utilizador():
    cabecalho()
    secao("Consultar Membro")
    id_uc = inp("ID do utilizador")
    code, obj = consultar_utilizador_casino(id_uc)
    if code == 200:
        mostrar_utilizador(id_uc, obj)
    else:
        erro(str(obj))
    pausa()

def ecra_atualizar_utilizador():
    cabecalho()
    secao("Atualizar Membro")
    id_uc = inp("ID do utilizador")
    print(f"\n  {DIM}{CINZA}(Enter para manter o valor atual){R}\n")
    nome  = inp("Novo nome")
    email = inp("Novo email")
    tipo  = inp("Novo tipo de conta")
    data  = inp("Nova data de nascimento")
    nif   = inp("Novo NIF")
    iban  = inp("Novo IBAN")
    code, obj = atualizar_utilizador_casino(
        id_uc,
        nome  or None, email or None, tipo or None,
        data  or None, nif   or None, iban or None
    )
    if code == 200:
        ok("Membro atualizado com sucesso!")
        mostrar_utilizador(id_uc, obj)
    else:
        erro(str(obj))
    pausa()

def ecra_remover_utilizador():
    cabecalho()
    secao("Remover Membro")
    id_uc   = inp("ID do utilizador")
    confirm = inp(f"Confirmar remocao de {id_uc}? (s/n)")
    if confirm.lower() != "s":
        print(f"\n  {CINZA}Operacao cancelada.{R}")
        pausa()
        return
    code, obj = remover_utilizador_casino(id_uc)
    if code == 200:
        ok(f"Membro {obj} removido com sucesso.")
    else:
        erro(str(obj))
    pausa()


# ══════════════════════════════
#  MENU CASINO
# ══════════════════════════════

def menu_casino():
    cabecalho()
    print(f"  {DIM}{CINZA}Gestao de Casinos -- Escolha uma operacao:{R}")
    print()
    ops = [
        ("1", "Criar casino",     VERDE),
        ("2", "Listar casinos",   AZUL),
        ("3", "Consultar casino", AZUL),
        ("4", "Atualizar casino", AZUL),
        ("5", "Remover casino",   VERM),
        ("0", "Voltar",           CINZA),
    ]
    for num, texto, cor in ops:
        print(f"  {B}{OURO}[{num}]{R}  {cor}{texto}{R}")
    print()
    print(f"  {OURO2}{'-' * W}{R}")
    return input(f"\n  {B}{OURO2}>  Opcao: {R}").strip()


def ecra_criar_casino():
    cabecalho()
    secao("Registar Novo Casino")
    nome  = inp("Nome do casino")
    local = inp("Localizacao")
    lic   = inp("Licenca")
    data  = inp("Data de inauguracao  (DD-MM-AAAA)")
    saldo = inp("Saldo inicial do casino  (EUR)")
    print(f"\n  {DIM}{CINZA}A validar dados...{R}", end="", flush=True)
    time.sleep(0.6)
    code, obj = criar_casino(nome, local, lic, data, saldo)
    print("\r" + " " * 30 + "\r", end="")
    if code == 201:
        ok("Casino registado com sucesso!")
        from casino import casinos
        id_novo = list(casinos.keys())[-1]
        mostrar_casino(id_novo, obj)
    else:
        erro(str(obj))
    pausa()

def ecra_listar_casinos():
    cabecalho()
    secao("Casinos Registados")
    code, obj = listar_casinos()
    if code == 200:
        print(f"  {DIM}{CINZA}Total: {len(obj)} casino(s){R}")
        for id_c, dados in obj.items():
            mostrar_casino(id_c, dados)
    else:
        erro(str(obj))
    pausa()

def ecra_consultar_casino():
    cabecalho()
    secao("Consultar Casino")
    id_c  = inp("ID do casino")
    code, obj = consultar_casino(id_c)
    if code == 200:
        mostrar_casino(id_c, obj)
    else:
        erro(str(obj))
    pausa()

def ecra_atualizar_casino():
    cabecalho()
    secao("Atualizar Casino")
    id_c  = inp("ID do casino")
    print(f"\n  {DIM}{CINZA}(Enter para manter o valor atual){R}\n")
    nome  = inp("Novo nome")
    local = inp("Nova localizacao")
    lic   = inp("Nova licenca")
    data  = inp("Nova data de inauguracao")
    saldo = inp("Novo saldo (EUR)")
    code, obj = atualizar_casino(
        id_c,
        nome  or None, local or None,
        lic   or None, data  or None,
        saldo or None
    )
    if code == 200:
        ok("Casino atualizado com sucesso!")
        mostrar_casino(id_c, obj)
    else:
        erro(str(obj))
    pausa()

def ecra_remover_casino():
    cabecalho()
    secao("Remover Casino")
    id_c    = inp("ID do casino")
    confirm = inp(f"Confirmar remocao de {id_c}? (s/n)")
    if confirm.lower() != "s":
        print(f"\n  {CINZA}Operacao cancelada.{R}")
        pausa()
        return
    code, obj = remover_casino(id_c)
    if code == 200:
        ok(f"Casino {obj} removido com sucesso.")
    else:
        erro(str(obj))
    pausa()


# ══════════════════════════════
#  MAIN
# ══════════════════════════════

def main():
    while True:
        op = menu_principal()

        if op == "1":
            while True:
                op_u = menu_utilizador()
                if   op_u == "1": ecra_criar_utilizador()
                elif op_u == "2": ecra_listar_utilizadores()
                elif op_u == "3": ecra_consultar_utilizador()
                elif op_u == "4": ecra_atualizar_utilizador()
                elif op_u == "5": ecra_remover_utilizador()
                elif op_u == "0": break
                else:
                    erro("Opcao invalida.")
                    time.sleep(1)

        elif op == "2":
            while True:
                op_c = menu_casino()
                if   op_c == "1": ecra_criar_casino()
                elif op_c == "2": ecra_listar_casinos()
                elif op_c == "3": ecra_consultar_casino()
                elif op_c == "4": ecra_atualizar_casino()
                elif op_c == "5": ecra_remover_casino()
                elif op_c == "0": break
                else:
                    erro("Opcao invalida.")
                    time.sleep(1)

        elif op == "0":
            limpar()
            print()
            msg = "  Ate a proxima, Membro VIP.  "
            n = len(msg)
            print(OURO + "  +" + "=" * n + "+" + R)
            print(OURO + "  |" + B + CREME + msg + R + OURO + "|" + R)
            print(OURO + "  +" + "=" * n + "+" + R)
            print()
            break

        else:
            erro("Opcao invalida.")
            time.sleep(1)

if __name__ == "__main__":
    main()
