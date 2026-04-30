import os
import time
import re

from utilizador import *
from casino import *
from jogo import *
from transacao import *

# ══════════════════════ CORES ══════════════════════
R  = "\033[0m"
B  = "\033[1m"
IT = "\033[3m"

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

W = 52


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def _strip_ansi(t):
    return re.sub(r'\033\[[0-9;]*m', '', t)


def _centro(texto, largura):
    pad = largura - len(texto)
    l = pad // 2
    r = pad - l
    return ' ' * l + texto + ' ' * r


# ══════════════════════ CABECALHO ══════════════════════

def cabecalho(titulo, subtitulo=None):
    limpar()
    print()
    print(f"  {OURO}{B}+{'=' * W}+{R}")
    print(f"  {OURO}{B}|{R}{CREME_CLARO}{B}{_centro(titulo, W)}{R}{OURO}{B}|{R}")
    if subtitulo:
        print(f"  {OURO}{B}|{R}{CINZA}{IT}{_centro(subtitulo, W)}{R}{OURO}{B}|{R}")
    print(f"  {OURO}{B}+{'=' * W}+{R}")
    print()


# ══════════════════════ MENSAGENS ══════════════════════

def _msg(tag, cor, msg):
    conteudo = f"  {tag}  {msg}  "
    n = len(conteudo)
    print()
    print(f"  {cor}{B}+{'-' * n}+{R}")
    print(f"  {cor}{B}|{R}{cor}{B}  {tag}{R}  {BRANCO}{msg}{R}  {cor}{B}|{R}")
    print(f"  {cor}{B}+{'-' * n}+{R}")


def mensagem_erro(msg):
    _msg("ERRO ", VERMELHO, msg)
    time.sleep(1.5)


def mensagem_sucesso(msg):
    _msg(" OK  ", VERDE2, msg)
    time.sleep(1.3)


def mensagem_info(msg):
    _msg("INFO ", AZUL, msg)
    time.sleep(1.2)


def mensagem_aviso(msg):
    _msg("AVISO", AMARELO, msg)
    time.sleep(1.2)


def mensagem_confirmacao(msg):
    _msg(" ??? ", MAGENTA, msg)


def aguardar_enter():
    print(f"\n  {CINZA_ESC}{'─' * 42}{R}")
    input(f"  {CINZA}  Prima Enter para continuar...{R}  ")


# ══════════════════════ CAIXAS ══════════════════════

def caixa_menu(titulo, opcoes):
    linhas_raw = [f"  [{k}]  {v}" for k, v in opcoes.items()]
    larg = max(len(titulo) + 4, max(len(l) for l in linhas_raw) + 4)
    larg = min(larg, 58)

    print(f"  {OURO_ESC}+{'-' * larg}+{R}")
    print(f"  {OURO_ESC}|{R}{OURO}{B}{_centro(titulo, larg)}{R}{OURO_ESC}|{R}")
    print(f"  {OURO_ESC}+{'-' * larg}+{R}")

    for k, v in opcoes.items():
        interior = f"  [{k}]  {v}"
        pad = larg - len(interior) - 2
        if k == "0":
            print(f"  {OURO_ESC}|{R}  {CINZA}[{k}]  {v}{' ' * max(0, pad)}{R}  {OURO_ESC}|{R}")
        else:
            print(f"  {OURO_ESC}|{R}  {OURO2}{B}[{k}]{R}  {CREME}{v}{' ' * max(0, pad)}{R}  {OURO_ESC}|{R}")

    print(f"  {OURO_ESC}+{'-' * larg}+{R}")


def caixa_info(titulo, linhas):
    raw_lens = [len(_strip_ansi(str(l))) for l in linhas]
    larg = max(len(titulo) + 4, max(raw_lens) + 6, 30)
    larg = min(larg, 64)

    print(f"\n  {OURO}+{'-' * larg}+{R}")
    print(f"  {OURO}|{R}{CREME_CLARO}{B}{_centro(titulo, larg)}{R}{OURO}|{R}")
    print(f"  {OURO}+{'-' * larg}+{R}")
    for linha in linhas:
        raw = _strip_ansi(str(linha))
        pad = larg - 2 - len(raw)
        print(f"  {OURO}|{R}  {linha}{' ' * max(0, pad)} {OURO}|{R}")
    print(f"  {OURO}+{'-' * larg}+{R}")


def caixa_lista(titulo, itens):
    if not itens:
        mensagem_info("Nenhum item encontrado.")
        return

    entradas = []
    for id_item, info in itens.items():
        nome = info.get('nome', '')
        saldo_txt = f"  EUR {info['saldo']:,.2f}" if 'saldo' in info else ""
        vis = f"  {OURO2}#{id_item}{R}  {CREME}{nome}{R}{VERDE}{saldo_txt}{R}"
        raw = f"  #{id_item}  {_strip_ansi(nome)}{saldo_txt}"
        entradas.append((vis, raw))

    larg = max(len(titulo) + 4, max(len(r) for _, r in entradas) + 4)
    larg = min(larg, 74)

    print(f"\n  {OURO}+{'-' * larg}+{R}")
    print(f"  {OURO}|{R}{CREME_CLARO}{B}{_centro(titulo, larg)}{R}{OURO}|{R}")
    print(f"  {OURO}+{'-' * larg}+{R}")
    for vis, raw in entradas:
        pad = larg - len(raw)
        print(f"  {OURO}|{R}{vis}{' ' * max(0, pad)}{OURO}|{R}")
    print(f"  {OURO}+{'-' * larg}+{R}")


def caixa_detalhe(entidade, dados):
    linhas = []
    for chave, valor in dados.items():
        chave_fmt = chave.replace('_', ' ').title()
        if chave == 'saldo':
            linhas.append(f"{VERDE}{chave_fmt}:{R} {VERDE}{B}EUR {valor:,.2f}{R}")
        else:
            linhas.append(f"{OURO2}{chave_fmt}:{R} {CREME}{valor}{R}")
    caixa_info(f"DETALHES -- {entidade.upper()}", linhas)


# ══════════════════════ INPUTS ══════════════════════

def prompt_opcao():
    return input(f"\n  {OURO}{B}> Opcao:{R} ").strip()


def prompt_campo(label, cor=CREME):
    return input(f"  {OURO2}  >{R}  {cor}{label}:{R} ")


# ══════════════════════ MENU PRINCIPAL ══════════════════════

def menu_principal():
    cabecalho("[ ROYAL CASINO ]", "Sistema de Gestao Integrado  --  v2.0")
    opcoes = {
        "1": "Gestao de Utilizadores",
        "2": "Gestao de Casinos",
        "3": "Gestao de Jogos",
        "4": "Gestao de Transacoes",
        "0": "Sair do Sistema",
    }
    caixa_menu("MENU PRINCIPAL", opcoes)
    return prompt_opcao()


# ══════════════════════ UTILIZADORES ══════════════════════

def gestao_utilizadores():
    while True:
        cabecalho("GESTAO DE UTILIZADORES", "Operacoes CRUD")
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
            mensagem_sucesso("Utilizador criado!") if status == 201 else mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "2":
            status, dados = listar_utilizadores_casino()
            caixa_lista("LISTA DE UTILIZADORES", dados) if status == 200 else mensagem_info("Nenhum utilizador encontrado.")
            aguardar_enter()

        elif op == "3":
            id_u = prompt_campo("ID do utilizador")
            status, dados = consultar_utilizador_casino(id_u)
            caixa_detalhe("UTILIZADOR", dados) if status == 200 else mensagem_erro(str(dados))
            aguardar_enter()

        elif op == "4":
            id_u = prompt_campo("ID do utilizador")
            mensagem_aviso("Deixe em branco para nao alterar")
            print()
            nome  = prompt_campo("Novo nome")            or None
            email = prompt_campo("Novo email")           or None
            tipo  = prompt_campo("Novo tipo")            or None
            data  = prompt_campo("Nova data nascimento") or None
            nif   = prompt_campo("Novo NIF")             or None
            iban  = prompt_campo("Novo IBAN")            or None
            status, resultado = atualizar_utilizador_casino(id_u, nome, email, tipo, data, nif, iban)
            mensagem_sucesso("Utilizador atualizado!") if status == 200 else mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "5":
            id_u = prompt_campo("ID do utilizador")
            mensagem_confirmacao("ATENCAO: Esta acao e irreversivel!")
            confirm = prompt_campo("Confirmar remocao? (s/n)", VERMELHO).lower()
            if confirm == 's':
                status, resultado = remover_utilizador_casino(id_u)
                mensagem_sucesso("Utilizador removido!") if status == 200 else mensagem_erro(str(resultado))
            else:
                mensagem_info("Operacao cancelada.")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("Opcao invalida.")


# ══════════════════════ CASINOS ══════════════════════

def gestao_casinos():
    while True:
        cabecalho("GESTAO DE CASINOS", "Operacoes CRUD")
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
            nome       = prompt_campo("Nome do Casino")
            local      = prompt_campo("Localizacao  (cidade, pais)")
            licenca    = prompt_campo("Licenca")
            data_inaug = prompt_campo("Data de inauguracao  (DD-MM-AAAA)")
            saldo      = prompt_campo("Saldo inicial  (EUR)", VERDE)
            status, resultado = criar_casino(nome, local, licenca, data_inaug, saldo)
            mensagem_sucesso(f"Casino criado!  Saldo: EUR {resultado['saldo']:,.2f}") if status == 201 else mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "2":
            status, dados = listar_casinos()
            caixa_lista("LISTA DE CASINOS", dados) if status == 200 else mensagem_info("Nenhum casino encontrado.")
            aguardar_enter()

        elif op == "3":
            id_c = prompt_campo("ID do casino")
            status, dados = consultar_casino(id_c)
            caixa_detalhe("CASINO", dados) if status == 200 else mensagem_erro(str(dados))
            aguardar_enter()

        elif op == "4":
            id_c = prompt_campo("ID do casino")
            mensagem_aviso("Deixe em branco para nao alterar")
            print()
            nome    = prompt_campo("Novo nome")                  or None
            local   = prompt_campo("Nova localizacao")           or None
            licenca = prompt_campo("Nova licenca")               or None
            data    = prompt_campo("Nova data de inauguracao")   or None
            saldo   = prompt_campo("Novo saldo  (EUR)", VERDE)   or None
            status, resultado = atualizar_casino(id_c, nome, local, licenca, data, saldo)
            mensagem_sucesso("Casino atualizado!") if status == 200 else mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "5":
            id_c = prompt_campo("ID do casino")
            mensagem_confirmacao("ATENCAO: Esta acao e irreversivel!")
            confirm = prompt_campo("Confirmar remocao? (s/n)", VERMELHO).lower()
            if confirm == 's':
                status, resultado = remover_casino(id_c)
                mensagem_sucesso("Casino removido!") if status == 200 else mensagem_erro(str(resultado))
            else:
                mensagem_info("Operacao cancelada.")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("Opcao invalida.")


# ══════════════════════ JOGOS ══════════════════════

def gestao_jogos():
    while True:
        cabecalho("GESTAO DE JOGOS", "Operacoes CRUD")
        opcoes = {
            "1": "Criar Jogo",
            "2": "Listar Jogos",
            "3": "Consultar Jogo",
            "4": "Remover Jogo",
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
            aposta_min = prompt_campo("Aposta minima  (EUR)")
            aposta_max = prompt_campo("Aposta maxima  (EUR)")
            id_casino  = prompt_campo("ID do casino")
            status, resultado = criar_jogo(nome, tipo, aposta_min, aposta_max, id_casino)
            mensagem_sucesso("Jogo criado!") if status == 201 else mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "2":
            status, dados = listar_jogos()
            if status == 200:
                itens_fmt = {}
                for id_j, info in dados.items():
                    itens_fmt[id_j] = {
                        'nome': f"{info['nome']}  [{info['tipo']}]  EUR {info['aposta_minima']} - {info['aposta_maxima']}"
                    }
                caixa_lista("LISTA DE JOGOS", itens_fmt)
            else:
                mensagem_info("Nenhum jogo encontrado.")
            aguardar_enter()

        elif op == "3":
            id_j = prompt_campo("ID do jogo")
            status, dados = consultar_jogo(id_j)
            caixa_detalhe("JOGO", dados) if status == 200 else mensagem_erro(str(dados))
            aguardar_enter()

        elif op == "4":
            id_j = prompt_campo("ID do jogo")
            mensagem_confirmacao("ATENCAO: Esta acao e irreversivel!")
            confirm = prompt_campo("Confirmar remocao? (s/n)", VERMELHO).lower()
            if confirm == 's':
                status, resultado = remover_jogo(id_j)
                mensagem_sucesso("Jogo removido!") if status == 200 else mensagem_erro(str(resultado))
            else:
                mensagem_info("Operacao cancelada.")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("Opcao invalida.")


# ══════════════════════ TRANSACOES ══════════════════════

def gestao_transacoes():
    while True:
        cabecalho("GESTAO DE TRANSACOES", "Operacoes CRUD")
        opcoes = {
            "1": "Criar Transacao",
            "2": "Listar Transacoes",
            "3": "Consultar Transacao",
            "4": "Atualizar Transacao",
            "5": "Remover Transacao",
            "0": "Voltar",
        }
        caixa_menu("SUB-MENU", opcoes)
        op = prompt_opcao()

        if op == "1":
            print()
            mensagem_info("Preencha os dados da nova transacao")
            print()
            id_user   = prompt_campo("ID do utilizador")
            tipo      = prompt_campo("Tipo  (deposito / levantamento)")
            valor     = prompt_campo("Valor  (EUR)")
            data      = prompt_campo("Data  (DD-MM-AAAA)")
            id_casino = prompt_campo("ID do casino")
            status, resultado = criar_transacao(id_user, tipo, valor, data, id_casino)
            mensagem_sucesso("Transacao criada!") if status == 201 else mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "2":
            status, dados = listar_transacoes()
            if status == 200:
                itens_fmt = {}
                for id_t, info in dados.items():
                    sinal = "+" if info['tipo'] == 'deposito' else "-"
                    itens_fmt[id_t] = {
                        'nome': f"{info['tipo']:14}  user:{info['id_utilizador']}  {sinal}EUR {info['valor']:.2f}  {info['data']}"
                    }
                caixa_lista("LISTA DE TRANSACOES", itens_fmt)
            else:
                mensagem_info("Nenhuma transacao encontrada.")
            aguardar_enter()

        elif op == "3":
            id_t = prompt_campo("ID da transacao")
            status, dados = consultar_transacao(id_t)
            caixa_detalhe("TRANSACAO", dados) if status == 200 else mensagem_erro(str(dados))
            aguardar_enter()

        elif op == "4":
            id_t = prompt_campo("ID da transacao")
            mensagem_aviso("Deixe em branco para nao alterar")
            print()
            tipo  = prompt_campo("Novo tipo  (deposito / levantamento)") or None
            valor = prompt_campo("Novo valor  (EUR)")                     or None
            data  = prompt_campo("Nova data  (DD-MM-AAAA)")              or None
            kwargs = {}
            if tipo:  kwargs['tipo']  = tipo
            if valor: kwargs['valor'] = float(valor)
            if data:  kwargs['data']  = data
            status, resultado = atualizar_transacao(id_t, **kwargs)
            mensagem_sucesso("Transacao atualizada!") if status == 200 else mensagem_erro(str(resultado))
            aguardar_enter()

        elif op == "5":
            id_t = prompt_campo("ID da transacao")
            mensagem_confirmacao("ATENCAO: Esta acao e irreversivel!")
            confirm = prompt_campo("Confirmar remocao? (s/n)", VERMELHO).lower()
            if confirm == 's':
                status, resultado = remover_transacao(id_t)
                mensagem_sucesso("Transacao removida!") if status == 200 else mensagem_erro(str(resultado))
            else:
                mensagem_info("Operacao cancelada.")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("Opcao invalida.")


# ══════════════════════ SAIDA ══════════════════════

def ecra_saida():
    limpar()
    print()
    msg = "  A encerrar o sistema...  Ate logo!  "
    n = len(msg) + 2
    print(f"  {VERDE}{B}+{'=' * n}+{R}")
    print(f"  {VERDE}{B}|{' ' * n}|{R}")
    print(f"  {VERDE}{B}|{R}  {BRANCO}{B}{msg}{R}  {VERDE}{B}|{R}")
    print(f"  {VERDE}{B}|{' ' * n}|{R}")
    print(f"  {VERDE}{B}+{'=' * n}+{R}")
    print()
    time.sleep(0.8)


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
            mensagem_erro("Opcao invalida.")


if __name__ == "__main__":
    main()
