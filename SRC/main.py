import os
import time
import sys

# --- Módulos ---
from utilizador import *
from casino import *
from jogo import *
from transacao import *

# ══════════════════════════════════════════════════════════════════
#  PALETA DE CORES — Royal Casino  (256-color ANSI)
# ══════════════════════════════════════════════════════════════════
R   = "\033[0m"          # Reset
B   = "\033[1m"          # Bold
D   = "\033[2m"          # Dim
IT  = "\033[3m"          # Italic
UL  = "\033[4m"          # Underline

# Dourado (progressão)
G1  = "\033[38;5;220m"   # Ouro brilhante
G2  = "\033[38;5;214m"   # Âmbar
G3  = "\033[38;5;178m"   # Ouro escuro
G4  = "\033[38;5;136m"   # Bronze

# Neutros
CR  = "\033[38;5;230m"   # Creme claro  (texto principal)
C2  = "\033[38;5;223m"   # Creme médio
C3  = "\033[38;5;180m"   # Creme escuro
GR  = "\033[38;5;244m"   # Cinza médio
GD  = "\033[38;5;238m"   # Cinza escuro
WH  = "\033[38;5;255m"   # Branco puro

# Status
VE  = "\033[38;5;83m"    # Verde néon
VM  = "\033[38;5;196m"   # Vermelho vivo
AZ  = "\033[38;5;39m"    # Azul ciano
AM  = "\033[38;5;227m"   # Amarelo suave
MG  = "\033[38;5;207m"   # Magenta rosa
CY  = "\033[38;5;51m"    # Ciano puro

# Fundos
BG_DARK  = "\033[48;5;235m"   # Fundo escuro
BG_MID   = "\033[48;5;237m"   # Fundo médio
BG_GOLD  = "\033[48;5;136m"   # Fundo dourado

# Decoração
NAIPE = ["♠", "♥", "♦", "♣"]

W = 58   # Largura interna da caixa


# ══════════════════════════════════════════════════════════════════
#  UTILITÁRIOS BÁSICOS
# ══════════════════════════════════════════════════════════════════

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def _centro(texto, largura):
    """Centra texto simples (sem escape codes) dentro de 'largura'."""
    pad = largura - len(texto)
    e = pad // 2
    d = pad - e
    return " " * e + texto + " " * d


def _barra_dourada():
    """Linha ornamental com naipes."""
    return f"{G3}{B}  ─── {G1}♠{G3} ─── {G1}♥{G3} ─── {G1}♦{G3} ─── {G1}♣{G3} ───{R}"


def _linha_dupla(c_esq="╔", c_dir="╗", c_mid="═"):
    return f"{G1}{B}  {c_esq}{c_mid * W}{c_dir}{R}"


def _linha_simples(c_esq="╟", c_dir="╢", c_mid="─"):
    return f"{G3}  {c_esq}{c_mid * W}{c_dir}{R}"


def _linha_conteudo(texto_raw, texto_visivel):
    """Linha de conteúdo com bordas douradas. texto_visivel = versão sem escape para medir."""
    pad = W - len(texto_visivel)
    return f"{G1}{B}  ║{R} {texto_raw}{' ' * pad}{G1}{B}║{R}"


def aguardar_enter():
    print(f"\n  {GR}  ╰─{R} {D}{GR}Prima{R} {G3}Enter{R} {D}{GR}para continuar…{R}", end="")
    input()


# ══════════════════════════════════════════════════════════════════
#  CABEÇALHO
# ══════════════════════════════════════════════════════════════════

def imprimir_cabecalho(titulo, sub_titulo=None):
    limpar()
    print()
    print(_linha_dupla("╔", "╗"))

    # Linha decorativa interior
    naipe_line = f"  {G3}{B}║{R}{GD}{'─' * W}{G3}{B}║{R}"

    # Título
    t_vis = f"  {titulo}  "
    t_raw = f"  {G1}{B}{titulo}{R}  "
    print(_linha_conteudo(
        f"  {G1}{B}{titulo}{R}",
        f"  {titulo}"
    ))

    if sub_titulo:
        print(_linha_simples("╟", "╢"))
        print(_linha_conteudo(
            f"  {GR}{IT}{sub_titulo}{R}",
            f"  {sub_titulo}"
        ))

    print(_linha_dupla("╚", "╝"))
    print()


# ══════════════════════════════════════════════════════════════════
#  MENSAGENS DE FEEDBACK
# ══════════════════════════════════════════════════════════════════

def _caixa_msg(icone, msg, cor, delay=1.4):
    pad = W - len(msg) - 4
    pad = max(pad, 0)
    print()
    print(f"  {cor}{B}╭{'─' * (len(msg) + 6)}╮{R}")
    print(f"  {cor}{B}│{R}  {cor}{B}{icone}{R}  {cor}{msg}{R}{'  ' * (pad // 2 + 1)}{cor}{B}│{R}")
    print(f"  {cor}{B}╰{'─' * (len(msg) + 6)}╯{R}")
    time.sleep(delay)


def mensagem_erro(msg):
    _caixa_msg("✘", msg, VM)

def mensagem_sucesso(msg):
    _caixa_msg("✔", msg, VE)

def mensagem_info(msg):
    _caixa_msg("◈", msg, AZ, delay=1.2)

def mensagem_aviso(msg):
    _caixa_msg("⚑", msg, AM, delay=1.0)

def mensagem_confirmacao(msg):
    _caixa_msg("◆", msg, MG, delay=0)


# ══════════════════════════════════════════════════════════════════
#  CAIXAS DE CONTEÚDO
# ══════════════════════════════════════════════════════════════════

def mostrar_caixa_info(titulo, linhas):
    raw_linhas = [l for l in linhas]
    # Largura baseada no conteúdo (sem escape codes)
    import re
    ansi_escape = re.compile(r'\033\[[0-9;]*m')
    def clean(s): return ansi_escape.sub('', str(s))

    max_w = max(
        len(clean(titulo)) + 4,
        max((len(clean(str(l))) + 4) for l in linhas),
        30
    )
    max_w = min(max_w, 72)

    print(f"\n  {G1}{B}╭{'─' * max_w}╮{R}")
    titulo_clean = clean(titulo)
    pad_t = max_w - len(titulo_clean)
    e = pad_t // 2; d = pad_t - e
    print(f"  {G1}{B}│{R}{' ' * e}{G1}{B}{titulo}{R}{' ' * d}{G1}{B}│{R}")
    print(f"  {G3}├{'─' * max_w}┤{R}")

    for linha in linhas:
        l_str = str(linha)
        l_clean = clean(l_str)
        pad = max_w - len(l_clean) - 1
        print(f"  {G1}{B}│{R} {l_str}{' ' * pad}{G1}{B}│{R}")

    print(f"  {G1}{B}╰{'─' * max_w}╯{R}")


def mostrar_caixa_lista(titulo, itens):
    if not itens:
        mensagem_info("Nenhum item encontrado")
        return

    import re
    ansi_escape = re.compile(r'\033\[[0-9;]*m')
    def clean(s): return ansi_escape.sub('', str(s))

    entradas = []
    for id_item, info in itens.items():
        nome = info.get('nome', '')
        saldo_str = f"  {VE}€ {info['saldo']:,.2f}{R}" if 'saldo' in info else ''
        linha_raw = f"{G3}{B}{id_item}{R}  {CR}{nome}{R}{saldo_str}"
        linha_vis = f"{id_item}  {clean(nome)}" + (f"  € {info['saldo']:,.2f}" if 'saldo' in info else '')
        entradas.append((linha_raw, linha_vis))

    max_w = max(
        len(clean(titulo)) + 4,
        max(len(v) + 4 for _, v in entradas),
        30
    )
    max_w = min(max_w, 76)

    print(f"\n  {G1}{B}╭{'─' * max_w}╮{R}")
    t_clean = clean(titulo)
    pad_t = max_w - len(t_clean); e = pad_t // 2; d = pad_t - e
    print(f"  {G1}{B}│{R}{' ' * e}{G1}{B}{titulo}{R}{' ' * d}{G1}{B}│{R}")
    print(f"  {G3}├{'─' * max_w}┤{R}")

    for i, (raw, vis) in enumerate(entradas):
        sep = f"  {GD}│{R}" if i < len(entradas) - 1 else ""
        pad = max_w - len(vis) - 1
        print(f"  {G1}{B}│{R} {raw}{' ' * pad}{G1}{B}│{R}")

    print(f"  {G1}{B}╰{'─' * max_w}╯{R}")


def mostrar_caixa_detalhe(entidade, dados):
    linhas = []
    for chave, valor in dados.items():
        chave_fmt = chave.replace('_', ' ').title()
        if chave == 'saldo':
            linhas.append(f"{G3}  {chave_fmt.upper()}{R}   {VE}{B}€ {valor:,.2f}{R}")
        else:
            linhas.append(f"{GR}  {chave_fmt}{R}   {CR}{valor}{R}")
    mostrar_caixa_info(f"  DETALHES  ›  {entidade.upper()}  ", linhas)


def mostrar_caixa_menu(titulo, opcoes):
    import re
    ansi_escape = re.compile(r'\033\[[0-9;]*m')
    def clean(s): return ansi_escape.sub('', str(s))

    entradas = list(opcoes.items())
    max_w = max(
        len(titulo) + 4,
        max(len(f"  {k}   {v}  ") for k, v in entradas),
        34
    )
    max_w = min(max_w, 62)

    print(f"\n  {G1}{B}╭{'─' * max_w}╮{R}")
    pad_t = max_w - len(titulo); e = pad_t // 2; d = pad_t - e
    print(f"  {G1}{B}│{R}{' ' * e}{G3}{B}{titulo}{R}{' ' * d}{G1}{B}│{R}")
    print(f"  {G3}├{'─' * max_w}┤{R}")

    for cod, desc in entradas:
        # Separador antes do "0 - Voltar"
        if cod == "0":
            print(f"  {GD}│{'·' * max_w}│{R}")

        label = f"  {G1}{B}{cod}{R}  {C2}{desc}{R}"
        label_vis = f"  {cod}  {desc}"
        pad = max_w - len(label_vis)
        print(f"  {G1}{B}│{R}{label}{' ' * pad}{G1}{B}│{R}")

    print(f"  {G1}{B}╰{'─' * max_w}╯{R}")


# ══════════════════════════════════════════════════════════════════
#  PROMPT DE INPUT
# ══════════════════════════════════════════════════════════════════

def pedir(label):
    return input(f"  {G3}  ›{R} {C2}{label}:{R}  ")


def pedir_opcao(prompt="OPÇÃO"):
    return input(f"\n  {G1}{B}▸ {prompt}:{R}  ").strip()


# ══════════════════════════════════════════════════════════════════
#  SPLASH / MENU PRINCIPAL
# ══════════════════════════════════════════════════════════════════

def splash():
    """Ecrã de boas-vindas animado."""
    limpar()
    linhas = [
        "",
        f"  {G1}{B}    ╔══════════════════════════════════════════╗{R}",
        f"  {G1}{B}    ║{R}  {G2}♠  {G1}{B}R O Y A L   C A S I N O{R}  {G2}♠{R}  {G1}{B}   ║{R}",
        f"  {G1}{B}    ║{R}      {GR}{IT}Sistema de Gestão Integrado{R}         {G1}{B}║{R}",
        f"  {G1}{B}    ║{R}  {GD}{'─' * 42}{R}  {G1}{B}║{R}",
        f"  {G1}{B}    ║{R}   {G3}♣{R}              {G4}{D}v 2.0{R}              {G3}♦{R}   {G1}{B}║{R}",
        f"  {G1}{B}    ╚══════════════════════════════════════════╝{R}",
        "",
    ]
    for l in linhas:
        print(l)
        time.sleep(0.05)


def menu_principal():
    limpar()
    print()
    # Banner compacto inline
    print(f"  {G1}{B}╔{'═' * W}╗{R}")
    t = "♠  ROYAL CASINO  ♠"
    pad = W - len(t); e = pad // 2; d = pad - e
    print(f"  {G1}{B}║{R}{' ' * e}{G1}{B}{t}{R}{' ' * d}{G1}{B}║{R}")
    s = "Sistema de Gestão Integrado"
    pad = W - len(s); e = pad // 2; d = pad - e
    print(f"  {G1}{B}║{R}{' ' * e}{GR}{IT}{s}{R}{' ' * d}{G1}{B}║{R}")
    print(f"  {G1}{B}╚{'═' * W}╝{R}")

    opcoes = {
        "1": "👥  Gestão de Utilizadores",
        "2": "🏢  Gestão de Casinos",
        "3": "🎮  Gestão de Jogos",
        "4": "💰  Gestão de Transações",
        "0": "🚪  Sair do Sistema",
    }
    mostrar_caixa_menu("MENU PRINCIPAL", opcoes)
    return pedir_opcao()


# ══════════════════════════════════════════════════════════════════
#  GESTÃO DE UTILIZADORES
# ══════════════════════════════════════════════════════════════════

def gestao_utilizadores():
    while True:
        imprimir_cabecalho("👥  GESTÃO DE UTILIZADORES", "Operações CRUD")
        opcoes = {
            "1": "📝  Criar Utilizador",
            "2": "📋  Listar Utilizadores",
            "3": "🔍  Consultar Utilizador",
            "4": "✏️   Atualizar Utilizador",
            "5": "🗑️   Remover Utilizador",
            "0": "◀   Voltar",
        }
        mostrar_caixa_menu("UTILIZADORES", opcoes)
        op = pedir_opcao()

        if op == "1":
            print(); mensagem_info("Preencha os dados do novo utilizador"); print()
            nome        = pedir("Nome completo")
            email       = pedir("Email")
            tipo_conta  = pedir("Tipo de conta  [standard / vip / high roller]")
            data_nasc   = pedir("Data de nascimento  [DD-MM-AAAA]")
            nif         = pedir("NIF")
            iban        = pedir("IBAN")
            status, resultado = criar_utilizador_casino(nome, email, tipo_conta, data_nasc, nif, iban)
            mensagem_sucesso("Utilizador criado com sucesso!") if status == 201 else mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "2":
            status, dados = listar_utilizadores_casino()
            if status == 200: mostrar_caixa_lista("LISTA DE UTILIZADORES", dados)
            else: mensagem_info("Nenhum utilizador encontrado")
            aguardar_enter()

        elif op == "3":
            id_u = pedir("ID do utilizador")
            status, dados = consultar_utilizador_casino(id_u)
            if status == 200: mostrar_caixa_detalhe("UTILIZADOR", dados)
            else: mensagem_erro(str(dados))
            aguardar_enter()

        elif op == "4":
            id_u = pedir("ID do utilizador")
            mensagem_aviso("Deixe em branco para não alterar"); print()
            nome  = pedir("Novo nome")       or None
            email = pedir("Novo email")      or None
            tipo  = pedir("Novo tipo")       or None
            data  = pedir("Nova data nasc.") or None
            nif   = pedir("Novo NIF")        or None
            iban  = pedir("Novo IBAN")       or None
            status, resultado = atualizar_utilizador_casino(id_u, nome, email, tipo, data, nif, iban)
            mensagem_sucesso("Utilizador atualizado!") if status == 200 else mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "5":
            id_u = pedir("ID do utilizador")
            mensagem_confirmacao("ATENÇÃO: Esta ação é irreversível!")
            confirm = pedir("Confirmar remoção?  [s/n]").lower()
            if confirm == 's':
                status, resultado = remover_utilizador_casino(id_u)
                mensagem_sucesso("Utilizador removido!") if status == 200 else mensagem_erro(str(resultado))
            else:
                mensagem_info("Operação cancelada")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("Opção inválida — tente novamente")


# ══════════════════════════════════════════════════════════════════
#  GESTÃO DE CASINOS
# ══════════════════════════════════════════════════════════════════

def gestao_casinos():
    while True:
        imprimir_cabecalho("🏢  GESTÃO DE CASINOS", "Operações CRUD")
        opcoes = {
            "1": "📝  Criar Casino",
            "2": "📋  Listar Casinos",
            "3": "🔍  Consultar Casino",
            "4": "✏️   Atualizar Casino",
            "5": "🗑️   Remover Casino",
            "0": "◀   Voltar",
        }
        mostrar_caixa_menu("CASINOS", opcoes)
        op = pedir_opcao()

        if op == "1":
            print(); mensagem_info("Preencha os dados do novo casino"); print()
            nome       = pedir("Nome do Casino")
            localizacao= pedir("Localização  [cidade, país]")
            licenca    = pedir("Nº de Licença")
            data_inaug = pedir("Data de inauguração  [DD-MM-AAAA]")
            saldo      = pedir("Saldo inicial  [€]")
            status, resultado = criar_casino(nome, localizacao, licenca, data_inaug, saldo)
            if status == 201: mensagem_sucesso(f"Casino criado!  Saldo inicial: €{resultado['saldo']:,.2f}")
            else: mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "2":
            status, dados = listar_casinos()
            if status == 200: mostrar_caixa_lista("LISTA DE CASINOS", dados)
            else: mensagem_info("Nenhum casino encontrado")
            aguardar_enter()

        elif op == "3":
            id_c = pedir("ID do casino")
            status, dados = consultar_casino(id_c)
            if status == 200: mostrar_caixa_detalhe("CASINO", dados)
            else: mensagem_erro(str(dados))
            aguardar_enter()

        elif op == "4":
            id_c = pedir("ID do casino")
            mensagem_aviso("Deixe em branco para não alterar"); print()
            nome   = pedir("Novo nome")              or None
            local  = pedir("Nova localização")       or None
            licenca= pedir("Nova licença")           or None
            data   = pedir("Nova data inauguração")  or None
            saldo  = pedir("Novo saldo  [€]")        or None
            status, resultado = atualizar_casino(id_c, nome, local, licenca, data, saldo)
            mensagem_sucesso("Casino atualizado!") if status == 200 else mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "5":
            id_c = pedir("ID do casino")
            mensagem_confirmacao("ATENÇÃO: Esta ação é irreversível!")
            confirm = pedir("Confirmar remoção?  [s/n]").lower()
            if confirm == 's':
                status, resultado = remover_casino(id_c)
                mensagem_sucesso("Casino removido!") if status == 200 else mensagem_erro(str(resultado))
            else:
                mensagem_info("Operação cancelada")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("Opção inválida — tente novamente")


# ══════════════════════════════════════════════════════════════════
#  GESTÃO DE JOGOS
# ══════════════════════════════════════════════════════════════════

def gestao_jogos():
    while True:
        imprimir_cabecalho("🎮  GESTÃO DE JOGOS", "Operações CRUD")
        opcoes = {
            "1": "📝  Criar Jogo",
            "2": "📋  Listar Jogos",
            "3": "🔍  Consultar Jogo",
            "4": "🗑️   Remover Jogo",
            "0": "◀   Voltar",
        }
        mostrar_caixa_menu("JOGOS", opcoes)
        op = pedir_opcao()

        if op == "1":
            print(); mensagem_info("Preencha os dados do novo jogo"); print()
            nome      = pedir("Nome do jogo")
            tipo      = pedir("Tipo  [carta / roleta / slot]")
            aposta_min= pedir("Aposta mínima  [€]")
            aposta_max= pedir("Aposta máxima  [€]")
            status, resultado = criar_jogo(nome, tipo, aposta_min, aposta_max)
            mensagem_sucesso("Jogo criado com sucesso!") if status == 201 else mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "2":
            status, dados = listar_jogos()
            if status == 200:
                itens_fmt = {}
                for id_j, info in dados.items():
                    icone = "🃏" if info['tipo'] == 'carta' else "🎰" if info['tipo'] == 'slot' else "🎡"
                    itens_fmt[id_j] = {
                        'nome': f"{icone} {info['nome']}  [{info['tipo']}]  €{info['aposta_minima']}–€{info['aposta_maxima']}"
                    }
                mostrar_caixa_lista("LISTA DE JOGOS", itens_fmt)
            else:
                mensagem_info("Nenhum jogo encontrado")
            aguardar_enter()

        elif op == "3":
            id_j = pedir("ID do jogo")
            status, dados = consultar_jogo(id_j)
            if status == 200: mostrar_caixa_detalhe("JOGO", dados)
            else: mensagem_erro(str(dados))
            aguardar_enter()

        elif op == "4":
            id_j = pedir("ID do jogo")
            mensagem_confirmacao("ATENÇÃO: Esta ação é irreversível!")
            confirm = pedir("Confirmar remoção?  [s/n]").lower()
            if confirm == 's':
                status, resultado = remover_jogo(id_j)
                mensagem_sucesso("Jogo removido!") if status == 200 else mensagem_erro(str(resultado))
            else:
                mensagem_info("Operação cancelada")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("Opção inválida — tente novamente")


# ══════════════════════════════════════════════════════════════════
#  GESTÃO DE TRANSAÇÕES
# ══════════════════════════════════════════════════════════════════

def gestao_transacoes():
    while True:
        imprimir_cabecalho("💰  GESTÃO DE TRANSAÇÕES", "Operações CRUD")
        opcoes = {
            "1": "📝  Criar Transação",
            "2": "📋  Listar Transações",
            "3": "🔍  Consultar Transação",
            "4": "✏️   Atualizar Transação",
            "5": "🗑️   Remover Transação",
            "0": "◀   Voltar",
        }
        mostrar_caixa_menu("TRANSAÇÕES", opcoes)
        op = pedir_opcao()

        if op == "1":
            print(); mensagem_info("Preencha os dados da nova transação"); print()
            id_user = pedir("ID do utilizador")
            tipo    = pedir("Tipo  [deposito / levantamento]")
            valor   = pedir("Valor  [€]")
            data    = pedir("Data  [DD-MM-AAAA]")
            status, resultado = criar_transacao(id_user, tipo, valor, data)
            mensagem_sucesso("Transação criada com sucesso!") if status == 201 else mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "2":
            status, dados = listar_transacoes()
            if status == 200:
                itens_fmt = {}
                for id_t, info in dados.items():
                    sinal = "+" if info['tipo'] == 'deposito' else "−"
                    cor   = VE  if info['tipo'] == 'deposito' else VM
                    itens_fmt[id_t] = {
                        'nome': f"👤 {info['id_utilizador']}  ›  {info['tipo']}  ›  {sinal}€{info['valor']:.2f}  ›  {info['data']}"
                    }
                mostrar_caixa_lista("LISTA DE TRANSAÇÕES", itens_fmt)
            else:
                mensagem_info("Nenhuma transação encontrada")
            aguardar_enter()

        elif op == "3":
            id_t = pedir("ID da transação")
            status, dados = consultar_transacao(id_t)
            if status == 200: mostrar_caixa_detalhe("TRANSAÇÃO", dados)
            else: mensagem_erro(str(dados))
            aguardar_enter()

        elif op == "4":
            id_t = pedir("ID da transação")
            mensagem_aviso("Deixe em branco para não alterar"); print()
            tipo  = pedir("Novo tipo  [deposito / levantamento]") or None
            valor = pedir("Novo valor  [€]")                      or None
            data  = pedir("Nova data  [DD-MM-AAAA]")              or None
            kwargs = {}
            if tipo:  kwargs['tipo']  = tipo
            if valor: kwargs['valor'] = float(valor)
            if data:  kwargs['data']  = data
            status, resultado = atualizar_transacao(id_t, **kwargs)
            mensagem_sucesso("Transação atualizada!") if status == 200 else mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "5":
            id_t = pedir("ID da transação")
            mensagem_confirmacao("ATENÇÃO: Esta ação é irreversível!")
            confirm = pedir("Confirmar remoção?  [s/n]").lower()
            if confirm == 's':
                status, resultado = remover_transacao(id_t)
                mensagem_sucesso("Transação removida!") if status == 200 else mensagem_erro(str(resultado))
            else:
                mensagem_info("Operação cancelada")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("Opção inválida — tente novamente")


# ══════════════════════════════════════════════════════════════════
#  LOOP PRINCIPAL
# ══════════════════════════════════════════════════════════════════

def main():
    splash()
    time.sleep(0.6)

    while True:
        op = menu_principal()

        if   op == "1": gestao_utilizadores()
        elif op == "2": gestao_casinos()
        elif op == "3": gestao_jogos()
        elif op == "4": gestao_transacoes()
        elif op == "0":
            limpar()
            print()
            print(f"  {G1}{B}    ╔══════════════════════════════════════════╗{R}")
            print(f"  {G1}{B}    ║{R}  {G2}✦{R}  {CR}A encerrar o sistema…  Até breve!{R}  {G2}✦{R}  {G1}{B}║{R}")
            print(f"  {G1}{B}    ╚══════════════════════════════════════════╝{R}")
            print()
            break
        else:
            mensagem_erro("Opção inválida — tente novamente")


if __name__ == "__main__":
    main()
