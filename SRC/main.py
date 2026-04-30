import os
import time
import re

from utilizador import *
from casino import *
from jogo import *
from transacao import *

# ══════════════════════ CORES ══════════════════════
R   = "\033[0m"
B   = "\033[1m"
IT  = "\033[3m"

OURO        = "\033[38;5;220m"
OURO2       = "\033[38;5;178m"
OURO_ESC    = "\033[38;5;136m"
CREME       = "\033[38;5;187m"
CREME_CLARO = "\033[38;5;230m"

VERMELHO = "\033[38;5;196m"
VERDE    = "\033[38;5;82m"
VERDE2   = "\033[38;5;48m"
AZUL     = "\033[38;5;39m"
AMARELO  = "\033[38;5;226m"
MAGENTA  = "\033[38;5;201m"

CINZA     = "\033[38;5;245m"
CINZA_ESC = "\033[38;5;238m"
BRANCO    = "\033[38;5;255m"

W = 54


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def _strip_ansi(t):
    return re.sub(r'\033\[[0-9;]*m', '', t)


def _centro(texto, largura):
    texto_raw = _strip_ansi(texto)
    pad = largura - len(texto_raw)
    l = pad // 2
    r = pad - l
    return ' ' * l + texto + ' ' * r


def _formatar_id(id_input):
    """Converte input de ID para formato com 3 dígitos (ex: '1' -> '001')"""
    s = str(id_input).strip()
    if s.isdigit():
        return s.zfill(3)
    return s


# ══════════════════════ CABEÇALHO ══════════════════════

def cabecalho(titulo, subtitulo=None):
    limpar()
    print()
    print(f"  {OURO}{B}+{'═' * W}+{R}")
    print(f"  {OURO}{B}║{R}{CREME_CLARO}{B}{_centro(titulo, W)}{R}{OURO}{B}║{R}")
    if subtitulo:
        print(f"  {OURO}{B}║{R}{CINZA}{IT}{_centro(subtitulo, W)}{R}{OURO}{B}║{R}")
    print(f"  {OURO}{B}+{'═' * W}+{R}")
    print()


# ══════════════════════ MENSAGENS ══════════════════════

def _msg(tag, cor, msg):
    interior = f"  {tag}   {msg}  "
    n = len(_strip_ansi(interior))
    borda = f"  {cor}{B}+{'─' * n}+{R}"
    print()
    print(borda)
    print(f"  {cor}{B}|{R}  {cor}{B}{tag}{R}   {BRANCO}{msg}{R}  {cor}{B}|{R}")
    print(borda)


def mensagem_erro(msg):
    _msg("✖  ERRO ", VERMELHO, msg)
    time.sleep(1.5)


def mensagem_sucesso(msg):
    _msg("✔  OK   ", VERDE2, msg)
    time.sleep(1.3)


def mensagem_info(msg):
    _msg("ℹ  INFO ", AZUL, msg)
    time.sleep(1.2)


def mensagem_aviso(msg):
    _msg("⚠  AVISO", AMARELO, msg)
    time.sleep(1.2)


def mensagem_confirmacao(msg):
    _msg("?  CONF ", MAGENTA, msg)


def aguardar_enter():
    print(f"\n  {CINZA_ESC}{'─' * 46}{R}")
    input(f"  {CINZA}  Prima Enter para continuar...{R}  ")


# ══════════════════════ CAIXAS ══════════════════════

def caixa_menu(titulo, opcoes):
    linhas_raw = [f"  [{k}]  {v}" for k, v in opcoes.items()]
    larg = max(len(_strip_ansi(titulo)) + 6,
               max(len(l) for l in linhas_raw) + 6)
    larg = min(larg, 58)

    sep  = f"  {OURO_ESC}+{'─' * larg}+{R}"
    print(sep)
    print(f"  {OURO_ESC}│{R}{OURO}{B}{_centro(titulo, larg)}{R}{OURO_ESC}│{R}")
    print(sep)
    for k, v in opcoes.items():
        interior = f"  [{k}]  {v}"
        pad = larg - len(interior) - 2
        if k == "0":
            print(f"  {OURO_ESC}│{R}  {CINZA}[{k}]  {v}{' ' * max(0, pad)}{R}  {OURO_ESC}│{R}")
        else:
            print(f"  {OURO_ESC}│{R}  {OURO2}{B}[{k}]{R}  {CREME}{v}{' ' * max(0, pad)}{R}  {OURO_ESC}│{R}")
    print(sep)


def caixa_info(titulo, linhas):
    raw_lens = [len(_strip_ansi(str(l))) for l in linhas]
    larg = max(len(_strip_ansi(titulo)) + 6,
               max(raw_lens) + 8, 36)
    larg = min(larg, 68)

    sep = f"  {OURO}+{'─' * larg}+{R}"
    print(f"\n{sep}")
    print(f"  {OURO}│{R}{CREME_CLARO}{B}{_centro(titulo, larg)}{R}{OURO}│{R}")
    print(sep)
    for linha in linhas:
        raw = _strip_ansi(str(linha))
        pad = larg - 4 - len(raw)
        print(f"  {OURO}│{R}  {linha}{' ' * max(0, pad)}  {OURO}│{R}")
    print(sep)


def caixa_lista(titulo, itens):
    if not itens:
        mensagem_info("Nenhum item encontrado.")
        return

    entradas = []
    for id_item, info in itens.items():
        nome = info.get('nome', '')
        saldo_txt = f"   EUR {info['saldo']:,.2f}" if 'saldo' in info else ""
        vis = f"  {OURO2}#{id_item}{R}  {CREME}{nome}{R}{VERDE}{saldo_txt}{R}"
        raw = f"  #{id_item}  {_strip_ansi(nome)}{saldo_txt}"
        entradas.append((vis, raw))

    larg = max(len(_strip_ansi(titulo)) + 6,
               max(len(r) for _, r in entradas) + 6)
    larg = min(larg, 78)

    sep = f"  {OURO}+{'─' * larg}+{R}"
    print(f"\n{sep}")
    print(f"  {OURO}│{R}{CREME_CLARO}{B}{_centro(titulo, larg)}{R}{OURO}│{R}")
    print(sep)
    for vis, raw in entradas:
        pad = larg - len(raw)
        print(f"  {OURO}│{R}{vis}{' ' * max(0, pad)}{OURO}│{R}")
    print(sep)


def caixa_detalhe(entidade, dados):
    """Exibe os detalhes de uma entidade numa caixa bem alinhada."""
    COL_CHAVE = 22

    linhas_vis  = []
    linhas_raw  = []

    for chave, valor in dados.items():
        chave_fmt = chave.replace('_', ' ').title()
        chave_pad = f"{chave_fmt}:".ljust(COL_CHAVE)

        if chave == 'saldo':
            valor_vis = f"{VERDE}{B}EUR {valor:,.2f}{R}"
            valor_raw = f"EUR {valor:,.2f}"
        else:
            valor_vis = f"{CREME}{valor}{R}"
            valor_raw = str(valor)

        linhas_vis.append(f"{OURO2}{chave_pad}{R} {valor_vis}")
        linhas_raw.append(f"{chave_pad} {valor_raw}")

    larg = max(
        len(_strip_ansi(entidade)) + 20,
        max(len(r) for r in linhas_raw) + 8,
        40
    )
    larg = min(larg, 70)

    titulo = f"DETALHES — {entidade.upper()}"
    sep = f"  {OURO}+{'─' * larg}+{R}"

    print(f"\n{sep}")
    print(f"  {OURO}│{R}{CREME_CLARO}{B}{_centro(titulo, larg)}{R}{OURO}│{R}")
    print(sep)
    for vis, raw in zip(linhas_vis, linhas_raw):
        pad = larg - 4 - len(raw)
        print(f"  {OURO}│{R}  {vis}{' ' * max(0, pad)}  {OURO}│{R}")
    print(sep)


# ══════════════════════ INPUTS ══════════════════════

def prompt_opcao():
    return input(f"\n  {OURO}{B}> Opção:{R} ").strip()


def prompt_campo(label, cor=CREME):
    return input(f"  {OURO2}  >{R}  {cor}{label}:{R} ").strip()


# ══════════════════════ MENU PRINCIPAL ══════════════════════

def menu_principal():
    cabecalho("[ ROYAL CASINO ]", "Sistema de Gestão Integrado  —  v2.0")
    opcoes = {
        "1": "Gestão de Utilizadores",
        "2": "Gestão de Casinos",
        "3": "Gestão de Jogos",
        "4": "Gestão de Transações",
        "0": "Sair do Sistema",
    }
    caixa_menu("MENU PRINCIPAL", opcoes)
    return prompt_opcao()


# ══════════════════════ UTILIZADORES ══════════════════════

def gestao_utilizadores():
    while True:
        cabecalho("GESTÃO DE UTILIZADORES", "Operações CRUD")
        opcoes = {
            "1": "Criar Utilizador",
            "2": "Listar Utilizadores",
            "3": "Consultar Utilizador",
            "4": "Atualizar Utilizador",
            "5": "Remover Utilizador",
            "0": "Voltar",
        }
        caixa_menu("SUB-MENU", opcoes)
        op = prompt_opcao()

        if op == "1":
            print()
            mensagem_info("Preencha os dados do novo utilizador")
            print()
            nome      = prompt_campo("Nome completo")
            email     = prompt_campo("Email")
            tipo      = prompt_campo("Tipo de conta  (standard / vip / high roller)")
            data_nasc = prompt_campo("Data de nascimento  (DD-MM-AAAA)")
            nif       = prompt_campo("NIF")
            iban      = prompt_campo("IBAN")

            status, resultado = criar_utilizador_casino(nome, email, tipo, data_nasc, nif, iban)
            if status == 201:
                mensagem_sucesso(f"Utilizador criado com ID: {resultado['id_utilizador']}!")
            else:
                mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "2":
            status, dados = listar_utilizadores_casino()
            if status == 200:
                caixa_lista("LISTA DE UTILIZADORES", dados)
            else:
                mensagem_info("Nenhum utilizador registado.")
            aguardar_enter()

        elif op == "3":
            id_u = _formatar_id(prompt_campo("ID do utilizador"))
            status, dados = consultar_utilizador_casino(id_u)
            if status == 200:
                caixa_detalhe("UTILIZADOR", dados)
            else:
                mensagem_erro(str(dados))
            aguardar_enter()

        elif op == "4":
            id_u = _formatar_id(prompt_campo("ID do utilizador"))
            mensagem_aviso("Deixe em branco para não alterar")
            print()
            nome  = prompt_campo("Novo nome")                              or None
            email = prompt_campo("Novo email")                             or None
            tipo  = prompt_campo("Novo tipo de conta")                     or None
            data  = prompt_campo("Nova data de nascimento (DD-MM-AAAA)")   or None
            nif   = prompt_campo("Novo NIF")                               or None
            iban  = prompt_campo("Novo IBAN")                              or None

            status, resultado = atualizar_utilizador_casino(id_u, nome, email, tipo, data, nif, iban)
            if status == 200:
                mensagem_sucesso("Utilizador atualizado com sucesso!")
            else:
                mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "5":
            id_u = _formatar_id(prompt_campo("ID do utilizador"))
            mensagem_confirmacao("Atenção: esta ação é irreversível!")
            confirm = prompt_campo("Confirmar remoção? (s/n)", VERMELHO).lower()
            if confirm == 's':
                status, resultado = remover_utilizador_casino(id_u)
                if status == 200:
                    mensagem_sucesso("Utilizador removido com sucesso!")
                else:
                    mensagem_erro(str(resultado))
            else:
                mensagem_info("Operação cancelada.")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("Opção inválida. Escolha uma opção do menu.")


# ══════════════════════ CASINOS ══════════════════════

def gestao_casinos():
    while True:
        cabecalho("GESTÃO DE CASINOS", "Operações CRUD")
        opcoes = {
            "1": "Criar Casino",
            "2": "Listar Casinos",
            "3": "Consultar Casino",
            "4": "Atualizar Casino",
            "5": "Remover Casino",
            "0": "Voltar",
        }
        caixa_menu("SUB-MENU", opcoes)
        op = prompt_opcao()

        if op == "1":
            print()
            mensagem_info("Preencha os dados do novo casino")
            print()
            nome       = prompt_campo("Nome do casino")
            local      = prompt_campo("Localização  (cidade, país)")
            licenca    = prompt_campo("Licença")
            data_inaug = prompt_campo("Data de inauguração  (DD-MM-AAAA)")
            saldo      = prompt_campo("Saldo inicial  (EUR)", VERDE)

            status, resultado = criar_casino(nome, local, licenca, data_inaug, saldo)
            if status == 201:
                mensagem_sucesso(f"Casino criado com ID: {resultado['id_casino']}!  Saldo: EUR {resultado['saldo']:,.2f}")
            else:
                mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "2":
            status, dados = listar_casinos()
            if status == 200:
                caixa_lista("LISTA DE CASINOS", dados)
            else:
                mensagem_info("Nenhum casino registado.")
            aguardar_enter()

        elif op == "3":
            id_c = _formatar_id(prompt_campo("ID do casino"))
            status, dados = consultar_casino(id_c)
            if status == 200:
                caixa_detalhe("CASINO", dados)
            else:
                mensagem_erro(str(dados))
            aguardar_enter()

        elif op == "4":
            id_c = _formatar_id(prompt_campo("ID do casino"))
            mensagem_aviso("Deixe em branco para não alterar")
            print()
            nome    = prompt_campo("Novo nome")                          or None
            local   = prompt_campo("Nova localização")                   or None
            licenca = prompt_campo("Nova licença")                       or None
            data    = prompt_campo("Nova data de inauguração (DD-MM-AAAA)") or None
            saldo   = prompt_campo("Novo saldo  (EUR)", VERDE)           or None

            status, resultado = atualizar_casino(id_c, nome, local, licenca, data, saldo)
            if status == 200:
                mensagem_sucesso("Casino atualizado com sucesso!")
            else:
                mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "5":
            id_c = _formatar_id(prompt_campo("ID do casino"))
            mensagem_confirmacao("Atenção: esta ação é irreversível!")
            confirm = prompt_campo("Confirmar remoção? (s/n)", VERMELHO).lower()
            if confirm == 's':
                status, resultado = remover_casino(id_c)
                if status == 200:
                    mensagem_sucesso("Casino removido com sucesso!")
                else:
                    mensagem_erro(str(resultado))
            else:
                mensagem_info("Operação cancelada.")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("Opção inválida. Escolha uma opção do menu.")


# ══════════════════════ JOGOS ══════════════════════

def gestao_jogos():
    while True:
        cabecalho("GESTÃO DE JOGOS", "Operações CRUD")
        opcoes = {
            "1": "Criar Jogo",
            "2": "Listar Jogos",
            "3": "Consultar Jogo",
            "4": "Atualizar Jogo",
            "5": "Remover Jogo",
            "0": "Voltar",
        }
        caixa_menu("SUB-MENU", opcoes)
        op = prompt_opcao()

        if op == "1":
            print()
            mensagem_info("Preencha os dados do novo jogo")
            print()
            nome       = prompt_campo("Nome do jogo")
            tipo       = prompt_campo("Tipo  (carta / roleta / slot)")
            aposta_min = prompt_campo("Aposta mínima  (EUR)")
            aposta_max = prompt_campo("Aposta máxima  (EUR)")
            id_casino  = _formatar_id(prompt_campo("ID do casino"))

            status, resultado = criar_jogo(nome, tipo, aposta_min, aposta_max, id_casino)
            if status == 201:
                mensagem_sucesso(f"Jogo criado com ID: {resultado['id_jogo']}!")
            else:
                mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "2":
            status, dados = listar_jogos()
            if status == 200:
                itens_fmt = {}
                for id_j, info in dados.items():
                    itens_fmt[id_j] = {
                        'nome': f"{info['nome']}  [{info['tipo']}]  EUR {info['aposta_minima']:.2f} – {info['aposta_maxima']:.2f}"
                    }
                caixa_lista("LISTA DE JOGOS", itens_fmt)
            else:
                mensagem_info("Nenhum jogo registado.")
            aguardar_enter()

        elif op == "3":
            id_j = prompt_campo("ID do jogo")
            status, dados = consultar_jogo(id_j)
            if status == 200:
                caixa_detalhe("JOGO", dados)
            else:
                mensagem_erro(str(dados))
            aguardar_enter()

        elif op == "4":
            id_j = prompt_campo("ID do jogo")
            mensagem_aviso("Deixe em branco para não alterar")
            print()
            nome       = prompt_campo("Novo nome")                      or None
            tipo       = prompt_campo("Novo tipo (carta/roleta/slot)")   or None
            aposta_min = prompt_campo("Nova aposta mínima  (EUR)")       or None
            aposta_max = prompt_campo("Nova aposta máxima  (EUR)")       or None
            id_casino  = prompt_campo("Novo ID do casino")               or None

            if id_casino:
                id_casino = _formatar_id(id_casino)

            status, resultado = atualizar_jogo(id_j, nome, tipo, aposta_min, aposta_max, id_casino)
            if status == 200:
                mensagem_sucesso("Jogo atualizado com sucesso!")
            else:
                mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "5":
            id_j = prompt_campo("ID do jogo")
            mensagem_confirmacao("Atenção: esta ação é irreversível!")
            confirm = prompt_campo("Confirmar remoção? (s/n)", VERMELHO).lower()
            if confirm == 's':
                status, resultado = remover_jogo(id_j)
                if status == 200:
                    mensagem_sucesso("Jogo removido com sucesso!")
                else:
                    mensagem_erro(str(resultado))
            else:
                mensagem_info("Operação cancelada.")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("Opção inválida. Escolha uma opção do menu.")


# ══════════════════════ TRANSAÇÕES ══════════════════════

def gestao_transacoes():
    while True:
        cabecalho("GESTÃO DE TRANSAÇÕES", "Operações CRUD")
        opcoes = {
            "1": "Criar Transação",
            "2": "Listar Transações",
            "3": "Consultar Transação",
            "4": "Atualizar Transação",
            "5": "Remover Transação",
            "0": "Voltar",
        }
        caixa_menu("SUB-MENU", opcoes)
        op = prompt_opcao()

        if op == "1":
            print()
            mensagem_info("Preencha os dados da nova transação")
            print()
            id_user   = _formatar_id(prompt_campo("ID do utilizador"))
            tipo      = prompt_campo("Tipo  (deposito / levantamento)")
            valor     = prompt_campo("Valor  (EUR)")
            data      = prompt_campo("Data  (DD-MM-AAAA)")
            id_casino = _formatar_id(prompt_campo("ID do casino"))

            status, resultado = criar_transacao(id_user, tipo, valor, data, id_casino)
            if status == 201:
                mensagem_sucesso(f"Transação criada com ID: {resultado['id_transacao']}!")
            else:
                mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "2":
            status, dados = listar_transacoes()
            if status == 200:
                itens_fmt = {}
                for id_t, info in dados.items():
                    sinal = "+" if info['tipo'] == 'deposito' else "-"
                    itens_fmt[id_t] = {
                        'nome': f"{info['tipo']:<14}  utilizador:{info['id_utilizador']}  {sinal}EUR {info['valor']:.2f}  {info['data']}"
                    }
                caixa_lista("LISTA DE TRANSAÇÕES", itens_fmt)
            else:
                mensagem_info("Nenhuma transação registada.")
            aguardar_enter()

        elif op == "3":
            id_t = prompt_campo("ID da transação")
            status, dados = consultar_transacao(id_t)
            if status == 200:
                caixa_detalhe("TRANSAÇÃO", dados)
            else:
                mensagem_erro(str(dados))
            aguardar_enter()

        elif op == "4":
            id_t = prompt_campo("ID da transação")
            mensagem_aviso("Deixe em branco para não alterar")
            print()
            tipo  = prompt_campo("Novo tipo  (deposito / levantamento)") or None
            valor = prompt_campo("Novo valor  (EUR)")                     or None
            data  = prompt_campo("Nova data  (DD-MM-AAAA)")              or None

            kwargs = {}
            if tipo:  kwargs['tipo']  = tipo
            if valor:
                try:
                    kwargs['valor'] = float(valor)
                except ValueError:
                    mensagem_erro("Valor inválido.")
                    aguardar_enter()
                    continue
            if data:  kwargs['data'] = data

            status, resultado = atualizar_transacao(id_t, **kwargs)
            if status == 200:
                mensagem_sucesso("Transação atualizada com sucesso!")
            else:
                mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "5":
            id_t = prompt_campo("ID da transação")
            mensagem_confirmacao("Atenção: esta ação é irreversível!")
            confirm = prompt_campo("Confirmar remoção? (s/n)", VERMELHO).lower()
            if confirm == 's':
                status, resultado = remover_transacao(id_t)
                if status == 200:
                    mensagem_sucesso("Transação removida com sucesso!")
                else:
                    mensagem_erro(str(resultado))
            else:
                mensagem_info("Operação cancelada.")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("Opção inválida. Escolha uma opção do menu.")


# ══════════════════════ ECRÃ DE SAÍDA ══════════════════════

def ecra_saida():
    limpar()
    linhas = [
        "Obrigado por utilizar o Royal Casino.",
        "Até à próxima!",
    ]
    larg = max(len(l) for l in linhas) + 10
    print()
    print(f"  {VERDE}{B}+{'═' * larg}+{R}")
    print(f"  {VERDE}{B}║{' ' * larg}║{R}")
    for l in linhas:
        pad = larg - len(l)
        esq = pad // 2
        dir = pad - esq
        print(f"  {VERDE}{B}║{R}{BRANCO}{B}{' ' * esq}{l}{' ' * dir}{R}{VERDE}{B}║{R}")
    print(f"  {VERDE}{B}║{' ' * larg}║{R}")
    print(f"  {VERDE}{B}+{'═' * larg}+{R}")
    print()
    time.sleep(1.0)


# ══════════════════════ MAIN ══════════════════════

def main():
    while True:
        op = menu_principal()
        if op == "1":
            gestao_utilizadores()
        elif op == "2":
            gestao_casinos()
        elif op == "3":
            gestao_jogos()
        elif op == "4":
            gestao_transacoes()
        elif op == "0":
            ecra_saida()
            break
        else:
            mensagem_erro("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()
