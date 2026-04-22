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

# ══════════════════════════════
#  CORES ANSI
# ══════════════════════════════
R  = "\033[0m"
B  = "\033[1m"
DIM = "\033[2m"

OURO    = "\033[38;5;220m"
OURO2   = "\033[38;5;178m"
CREME   = "\033[38;5;230m"
VERDE   = "\033[38;5;40m"
VERM    = "\033[38;5;160m"
CINZA   = "\033[38;5;244m"
CINZA2  = "\033[38;5;238m"
ROXO    = "\033[38;5;135m"

BG_VERDE = "\033[48;5;22m"
BG_VERM  = "\033[48;5;88m"
BG_OURO  = "\033[48;5;136m"

W = 52

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def ok(msg):
    print(f"\n  {B}{BG_VERDE}{CREME} ✔ {R}{B}{VERDE} {msg}{R}")

def erro(msg):
    print(f"\n  {B}{BG_VERM}{CREME} ✖ {R}{B}{VERM} {msg}{R}")

def inp(label):
    return input(f"  {OURO2}{B}▶  {label}: {R}")

def pausa():
    print()
    input(f"  {DIM}{CINZA}Pressione ENTER para continuar...{R}")

def cabecalho():
    limpar()
    print()
    print(OURO + "  ╔" + "═" * W + "╗" + R)
    titulo = "♠  ROYAL CASINO  —  Gestão de Membros  ♠"
    pad = (W - len(titulo)) // 2
    print(OURO + "  ║" + " " * pad + B + CREME + titulo + R + OURO + " " * (W - pad - len(titulo)) + "║" + R)
    print(OURO + "  ╚" + "═" * W + "╝" + R)
    print()

def secao(titulo):
    print()
    print(f"  {OURO2}{'─' * W}{R}")
    print(f"  {B}{OURO}  {titulo}{R}")
    print(f"  {OURO2}{'─' * W}{R}")
    print()

def mostrar_utilizador(id_uc, dados):
    print(f"  {CINZA2}{'· ' * (W // 2)}{R}")
    print(f"  {B}{OURO}◆ {id_uc}{R}")
    print(f"  {CINZA}Nome  {CINZA2}{'·' * 10}{R}  {CREME}{dados['nome']}{R}")
    print(f"  {CINZA}Email {CINZA2}{'·' * 10}{R}  {ROXO}{dados['email']}{R}")
    print(f"  {CINZA}Tipo  {CINZA2}{'·' * 10}{R}  {OURO2}{dados['tipo_conta']}{R}")
    print(f"  {CINZA}Nasc. {CINZA2}{'·' * 10}{R}  {CREME}{dados['data_nascimento']}{R}")
    print(f"  {CINZA}NIF   {CINZA2}{'·' * 10}{R}  {CINZA}{dados['nif']}{R}")
    print(f"  {CINZA}IBAN  {CINZA2}{'·' * 10}{R}  {CINZA}{dados['iban']}{R}")

def menu():
    cabecalho()
    print(f"  {DIM}{CINZA}Escolha uma operação:{R}")
    print()
    ops = [
        ("1", "Criar utilizador",    VERDE),
        ("2", "Listar utilizadores", OURO2),
        ("3", "Consultar utilizador",OURO2),
        ("4", "Atualizar utilizador",OURO2),
        ("5", "Remover utilizador",  VERM),
        ("0", "Sair",               CINZA),
    ]
    for num, texto, cor in ops:
        print(f"  {B}{OURO}[{num}]{R}  {cor}{texto}{R}")
    print()
    print(f"  {OURO2}{'─' * W}{R}")
    return input(f"\n  {B}{OURO2}▶  Opção: {R}").strip()


# ══════════════════════════════
#  ECRÃS
# ══════════════════════════════

def ecra_criar():
    cabecalho()
    secao("✦  Registar Novo Membro")
    nome  = inp("Nome completo")
    email = inp("Email")
    tipo  = inp("Tipo de conta  (standard / vip / high roller)")
    nasc  = inp("Data nascimento  (DD-MM-AAAA)")
    nif   = inp("NIF  (9 dígitos)")
    iban  = inp("IBAN  (PT + 23 dígitos)")
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

def ecra_listar():
    cabecalho()
    secao("♠  Membros Registados")
    code, obj = listar_utilizadores_casino()
    if code == 200:
        print(f"  {DIM}{CINZA}Total: {len(obj)} membro(s){R}")
        for id_uc, dados in obj.items():
            mostrar_utilizador(id_uc, dados)
    else:
        erro(str(obj))
    pausa()

def ecra_consultar():
    cabecalho()
    secao("🔍  Consultar Membro")
    id_uc = inp("ID do utilizador")
    code, obj = consultar_utilizador_casino(id_uc)
    if code == 200:
        mostrar_utilizador(id_uc, obj)
    else:
        erro(str(obj))
    pausa()

def ecra_atualizar():
    cabecalho()
    secao("✎  Atualizar Membro")
    id_uc = inp("ID do utilizador")
    print(f"\n  {DIM}{CINZA}(Enter para manter o valor atual){R}\n")
    nome  = inp("Novo nome")
    email = inp("Novo email")
    tipo  = inp("Novo tipo de conta")
    data  = inp("Nova data nascimento")
    nif   = inp("Novo NIF")
    iban  = inp("Novo IBAN")
    code, obj = atualizar_utilizador_casino(
        id_uc,
        nome  or None, email or None, tipo  or None,
        data  or None, nif   or None, iban  or None
    )
    if code == 200:
        ok("Membro atualizado com sucesso!")
        mostrar_utilizador(id_uc, obj)
    else:
        erro(str(obj))
    pausa()

def ecra_remover():
    cabecalho()
    secao("✖  Remover Membro")
    id_uc = inp("ID do utilizador")
    confirm = inp(f"Confirmar remoção de {id_uc}? (s/n)")
    if confirm.lower() != "s":
        print(f"\n  {CINZA}Operação cancelada.{R}")
        pausa()
        return
    code, obj = remover_utilizador_casino(id_uc)
    if code == 200:
        ok(f"Membro {obj} removido com sucesso.")
    else:
        erro(str(obj))
    pausa()


# ══════════════════════════════
#  MAIN
# ══════════════════════════════

def main():
    while True:
        op = menu()
        if   op == "1": ecra_criar()
        elif op == "2": ecra_listar()
        elif op == "3": ecra_consultar()
        elif op == "4": ecra_atualizar()
        elif op == "5": ecra_remover()
        elif op == "0":
            limpar()
            print()
            print(f"  {B}{OURO}♠  Até à próxima, Membro VIP.  ♠{R}")
            print()
            print(OURO + "  " + "═" * W + R)
            print()
            break
        else:
            erro("Opção inválida.")
            time.sleep(1)

if __name__ == "__main__":
    main()