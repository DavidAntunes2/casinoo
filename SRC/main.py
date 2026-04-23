import os
import time

# --- Módulos ---
from utilizador import *
from casino import *
from jogo import *
from transacao import *

# ══════════════════════ CORES E ESTILO ══════════════════════
R = "\033[0m"  # Reset
B = "\033[1m"  # Bold
D = "\033[2m"  # Dim

# Cores principais
OURO = "\033[38;5;220m"
OURO2 = "\033[38;5;178m"
CREME = "\033[38;5;187m"
CREME_CLARO = "\033[38;5;230m"

# Cores de status
VERMELHO = "\033[38;5;196m"
VERDE = "\033[38;5;82m"
AZUL = "\033[38;5;39m"
AMARELO = "\033[38;5;226m"
CIANO = "\033[38;5;51m"
MAGENTA = "\033[38;5;201m"

# Cores neutras
CINZA = "\033[38;5;245m"
CINZA_ESCURO = "\033[38;5;240m"
BRANCO = "\033[38;5;255m"

W = 54  # Largura da caixa


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def imprimir_cabecalho(titulo, sub_titulo=None):
    limpar()
    print(f"\n{OURO}{B}  ╔{'═' * W}╗{R}")

    espaco_titulo = W - len(titulo)
    esquerda = espaco_titulo // 2
    direita = espaco_titulo - esquerda
    print(f"{OURO}{B}  ║{R}{CREME_CLARO}{B}{' ' * esquerda}{titulo}{' ' * direita}{R}{OURO}{B}║{R}")

    if sub_titulo:
        espaco_sub = W - len(sub_titulo)
        esquerda_sub = espaco_sub // 2
        direita_sub = espaco_sub - esquerda_sub
        print(f"{OURO}{B}  ║{R}{CINZA}{' ' * esquerda_sub}{sub_titulo}{' ' * direita_sub}{R}{OURO}{B}║{R}")
        print(f"{OURO}{B}  ╠{'═' * W}╣{R}")

    print(f"{OURO}{B}  ╚{'═' * W}╝{R}\n")


def imprimir_menu_item(num, texto, cor_num=OURO2, cor_texto=CREME):
    print(f"  {cor_num}{B}[{num}]{R} {cor_texto}{texto}{R}")


def mensagem_erro(msg):
    """Mensagem de erro com caixa bonita"""
    print()
    print(f"  {VERMELHO}{B}┌{'─' * (len(msg) + 6)}┐{R}")
    print(f"  {VERMELHO}{B}│{R}  {VERMELHO}{B}✘{R} {VERMELHO}{msg}{R}  {VERMELHO}{B}│{R}")
    print(f"  {VERMELHO}{B}└{'─' * (len(msg) + 6)}┘{R}")
    time.sleep(1.5)


def mensagem_sucesso(msg):
    """Mensagem de sucesso com caixa bonita"""
    print()
    print(f"  {VERDE}{B}┌{'─' * (len(msg) + 6)}┐{R}")
    print(f"  {VERDE}{B}│{R}  {VERDE}{B}✔{R} {VERDE}{msg}{R}  {VERDE}{B}│{R}")
    print(f"  {VERDE}{B}└{'─' * (len(msg) + 6)}┘{R}")
    time.sleep(1.5)


def mensagem_info(msg):
    """Mensagem informativa com caixa bonita"""
    print()
    print(f"  {AZUL}{B}┌{'─' * (len(msg) + 6)}┐{R}")
    print(f"  {AZUL}{B}│{R}  {AZUL}{B}ℹ{R} {AZUL}{msg}{R}  {AZUL}{B}│{R}")
    print(f"  {AZUL}{B}└{'─' * (len(msg) + 6)}┘{R}")
    time.sleep(1.5)


def mensagem_aviso(msg):
    """Mensagem de aviso com caixa bonita"""
    print()
    print(f"  {AMARELO}{B}┌{'─' * (len(msg) + 6)}┐{R}")
    print(f"  {AMARELO}{B}│{R}  {AMARELO}{B}⚠{R} {AMARELO}{msg}{R}  {AMARELO}{B}│{R}")
    print(f"  {AMARELO}{B}└{'─' * (len(msg) + 6)}┘{R}")
    time.sleep(1.5)


def mensagem_confirmacao(msg):
    """Mensagem de confirmação com caixa bonita"""
    print()
    print(f"  {MAGENTA}{B}┌{'─' * (len(msg) + 6)}┐{R}")
    print(f"  {MAGENTA}{B}│{R}  {MAGENTA}{B}?{R} {MAGENTA}{msg}{R}  {MAGENTA}{B}│{R}")
    print(f"  {MAGENTA}{B}└{'─' * (len(msg) + 6)}┘{R}")


def aguardar_enter():
    input(f"\n  {CINZA}{B}└─{R} {CINZA}Prima Enter para continuar...{R}")


def mostrar_caixa_info(titulo, linhas):
    """Mostra informações dentro de uma caixa bonita"""
    max_len = max(len(titulo) + 4, max(len(str(l)) for l in linhas) + 4)
    max_len = min(max_len, 60)

    print(f"\n  {OURO}{B}┌{'─' * (max_len)}┐{R}")
    print(f"  {OURO}{B}│{R} {CREME_CLARO}{B}{titulo.center(max_len - 2)}{R} {OURO}{B}│{R}")
    print(f"  {OURO}{B}├{'─' * (max_len)}┤{R}")

    for linha in linhas:
        linha_str = str(linha)
        print(f"  {OURO}{B}│{R} {CREME}{linha_str.ljust(max_len - 2)}{R} {OURO}{B}│{R}")

    print(f"  {OURO}{B}└{'─' * (max_len)}┘{R}")


def mostrar_caixa_lista(titulo, itens):
    """Mostra uma lista dentro de uma caixa bonita"""
    if not itens:
        mensagem_info("Nenhum item encontrado")
        return

    max_len = max(len(titulo) + 4, max(len(f"ID: {k} - {v.get('nome', '')}") for k, v in itens.items()) + 4)
    max_len = min(max_len, 70)

    print(f"\n  {OURO}{B}┌{'─' * (max_len)}┐{R}")
    print(f"  {OURO}{B}│{R} {CREME_CLARO}{B}{titulo.center(max_len - 2)}{R} {OURO}{B}│{R}")
    print(f"  {OURO}{B}├{'─' * (max_len)}┤{R}")

    for id_item, info in itens.items():
        linha = f"{OURO}{B}ID:{R} {id_item}  {CREME}{info.get('nome', '')}{R}"
        if 'saldo' in info:
            linha += f"  {VERDE}💰 €{info['saldo']:,.2f}{R}"
        print(f"  {OURO}{B}│{R} {linha.ljust(max_len - 2)} {OURO}{B}│{R}")

    print(f"  {OURO}{B}└{'─' * (max_len)}┘{R}")


def mostrar_caixa_detalhe(entidade, dados):
    """Mostra detalhes de uma entidade numa caixa bonita"""
    linhas = []
    for chave, valor in dados.items():
        if chave == 'saldo':
            linhas.append(f"{VERDE}💰 {chave.upper()}:{R} €{valor:,.2f}")
        else:
            chave_formatada = chave.replace('_', ' ').title()
            linhas.append(f"{CREME}{chave_formatada}:{R} {valor}")

    mostrar_caixa_info(f"📋 DETALHES DO {entidade.upper()}", linhas)


def mostrar_caixa_menu(titulo, opcoes):
    """Mostra um menu dentro de uma caixa bonita"""
    max_len = max(len(titulo) + 4, max(len(f"[{k}] {v}") for k, v in opcoes.items()) + 4)
    max_len = min(max_len, 60)

    print(f"\n  {OURO}{B}┌{'─' * (max_len)}┐{R}")
    print(f"  {OURO}{B}│{R} {CREME_CLARO}{B}{titulo.center(max_len - 2)}{R} {OURO}{B}│{R}")
    print(f"  {OURO}{B}├{'─' * (max_len)}┤{R}")

    for codigo, descricao in opcoes.items():
        print(f"  {OURO}{B}│{R}   {OURO2}{B}[{codigo}]{R} {CREME}{descricao.ljust(max_len - 8)}{R} {OURO}{B}│{R}")

    print(f"  {OURO}{B}└{'─' * (max_len)}┘{R}")


# ══════════════════════ MENU PRINCIPAL ══════════════════════

def menu_principal():
    imprimir_cabecalho("♠ ROYAL CASINO ♠", "Sistema de Gestão Integrado")

    opcoes = {
        "1": "👥 Gestão de Utilizadores",
        "2": "🏢 Gestão de Casinos",
        "3": "🎮 Gestão de Jogos",
        "4": "💰 Gestão de Transações",
        "0": "🚪 Sair do Sistema"
    }

    mostrar_caixa_menu("MENU PRINCIPAL", opcoes)

    print(f"\n  {OURO}{B}▶{R} {CREME_CLARO}ESCOLHA UMA OPÇÃO:{R} ", end="")
    return input().strip()


# ══════════════════════ GESTÃO DE UTILIZADORES ══════════════════════

def gestao_utilizadores():
    while True:
        imprimir_cabecalho("👥 GESTÃO DE UTILIZADORES", "Operações CRUD")

        opcoes = {
            "1": "📝 Criar Utilizador",
            "2": "📋 Listar Utilizadores",
            "3": "🔍 Consultar Utilizador",
            "4": "✏️ Atualizar Utilizador",
            "5": "🗑️ Remover Utilizador",
            "0": "◀ Voltar ao Menu Principal"
        }

        mostrar_caixa_menu("SUB-MENU", opcoes)

        op = input(f"\n  {OURO}{B}▶ OPÇÃO:{R} ").strip()

        if op == "1":
            print()
            mensagem_info("Preencha os dados do novo utilizador")
            print()
            nome = input(f"  {CREME}{B}➤{R} {CREME}Nome completo:{R} ")
            email = input(f"  {CREME}{B}➤{R} {CREME}Email:{R} ")
            tipo_conta = input(f"  {CREME}{B}➤{R} {CREME}Tipo conta (standard/vip/high roller):{R} ")
            data_nasc = input(f"  {CREME}{B}➤{R} {CREME}Data nascimento (DD-MM-AAAA):{R} ")
            nif = input(f"  {CREME}{B}➤{R} {CREME}NIF:{R} ")
            iban = input(f"  {CREME}{B}➤{R} {CREME}IBAN:{R} ")

            status, resultado = criar_utilizador_casino(nome, email, tipo_conta, data_nasc, nif, iban)
            if status == 201:
                mensagem_sucesso(f"✅ Utilizador criado com sucesso!")
            else:
                mensagem_erro(f"❌ {resultado}")
            aguardar_enter()

        elif op == "2":
            status, dados = listar_utilizadores_casino()
            if status == 200:
                mostrar_caixa_lista("📋 LISTA DE UTILIZADORES", dados)
            else:
                mensagem_info("📭 Nenhum utilizador encontrado")
            aguardar_enter()

        elif op == "3":
            id_u = input(f"\n  {CREME}{B}➤{R} {CREME}ID do utilizador:{R} ")
            status, dados = consultar_utilizador_casino(id_u)
            if status == 200:
                mostrar_caixa_detalhe("UTILIZADOR", dados)
            else:
                mensagem_erro(f"❌ {dados}")
            aguardar_enter()

        elif op == "4":
            id_u = input(f"\n  {CREME}{B}➤{R} {CREME}ID do utilizador:{R} ")
            mensagem_aviso("Deixe em branco para não alterar")
            print()
            nome = input(f"  {CREME}{B}➤{R} {CREME}Novo nome:{R} ") or None
            email = input(f"  {CREME}{B}➤{R} {CREME}Novo email:{R} ") or None
            tipo = input(f"  {CREME}{B}➤{R} {CREME}Novo tipo:{R} ") or None
            data = input(f"  {CREME}{B}➤{R} {CREME}Nova data nasc:{R} ") or None
            nif = input(f"  {CREME}{B}➤{R} {CREME}Novo NIF:{R} ") or None
            iban = input(f"  {CREME}{B}➤{R} {CREME}Novo IBAN:{R} ") or None

            status, resultado = atualizar_utilizador_casino(id_u, nome, email, tipo, data, nif, iban)
            if status == 200:
                mensagem_sucesso("✅ Utilizador atualizado com sucesso!")
            else:
                mensagem_erro(f"❌ {resultado}")
            aguardar_enter()

        elif op == "5":
            id_u = input(f"\n  {CREME}{B}➤{R} {CREME}ID do utilizador:{R} ")
            mensagem_confirmacao("⚠️ ATENÇÃO: Esta ação é irreversível!")
            confirm = input(f"\n  {VERMELHO}{B}➤{R} {VERMELHO}Confirmar remoção? (s/n):{R} ").lower()
            if confirm == 's':
                status, resultado = remover_utilizador_casino(id_u)
                if status == 200:
                    mensagem_sucesso("✅ Utilizador removido com sucesso!")
                else:
                    mensagem_erro(f"❌ {resultado}")
            else:
                mensagem_info("Operação cancelada")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("❌ Opção inválida! Tente novamente.")


# ══════════════════════ GESTÃO DE CASINOS ══════════════════════

def gestao_casinos():
    while True:
        imprimir_cabecalho("🏢 GESTÃO DE CASINOS", "Operações CRUD")

        opcoes = {
            "1": "📝 Criar Casino",
            "2": "📋 Listar Casinos",
            "3": "🔍 Consultar Casino",
            "4": "✏️ Atualizar Casino",
            "5": "🗑️ Remover Casino",
            "0": "◀ Voltar ao Menu Principal"
        }

        mostrar_caixa_menu("SUB-MENU", opcoes)

        op = input(f"\n  {OURO}{B}▶ OPÇÃO:{R} ").strip()

        if op == "1":
            print()
            mensagem_info("Preencha os dados do novo casino")
            print()
            nome = input(f"  {CREME}{B}➤{R} {CREME}Nome do Casino:{R} ")
            localizacao = input(f"  {CREME}{B}➤{R} {CREME}Localização (cidade, país):{R} ")
            licenca = input(f"  {CREME}{B}➤{R} {CREME}Nº Licença:{R} ")
            data_inaug = input(f"  {CREME}{B}➤{R} {CREME}Data inauguração (DD-MM-AAAA):{R} ")
            saldo = input(f"  {VERDE}{B}➤{R} {VERDE}Saldo inicial do Casino (€):{R} ")

            status, resultado = criar_casino(nome, localizacao, licenca, data_inaug, saldo)
            if status == 201:
                mensagem_sucesso(f"✅ Casino criado com sucesso! Saldo inicial: €{resultado['saldo']:,.2f}")
            else:
                mensagem_erro(f"❌ {resultado}")
            aguardar_enter()

        elif op == "2":
            status, dados = listar_casinos()
            if status == 200:
                mostrar_caixa_lista("📋 LISTA DE CASINOS", dados)
            else:
                mensagem_info("📭 Nenhum casino encontrado")
            aguardar_enter()

        elif op == "3":
            id_c = input(f"\n  {CREME}{B}➤{R} {CREME}ID do casino:{R} ")
            status, dados = consultar_casino(id_c)
            if status == 200:
                mostrar_caixa_detalhe("CASINO", dados)
            else:
                mensagem_erro(f"❌ {dados}")
            aguardar_enter()

        elif op == "4":
            id_c = input(f"\n  {CREME}{B}➤{R} {CREME}ID do casino:{R} ")
            mensagem_aviso("Deixe em branco para não alterar")
            print()
            nome = input(f"  {CREME}{B}➤{R} {CREME}Novo nome:{R} ") or None
            local = input(f"  {CREME}{B}➤{R} {CREME}Nova localização:{R} ") or None
            licenca = input(f"  {CREME}{B}➤{R} {CREME}Nova licença:{R} ") or None
            data = input(f"  {CREME}{B}➤{R} {CREME}Nova data inauguração:{R} ") or None
            saldo = input(f"  {VERDE}{B}➤{R} {VERDE}Novo saldo (€):{R} ") or None

            status, resultado = atualizar_casino(id_c, nome, local, licenca, data, saldo)
            if status == 200:
                mensagem_sucesso("✅ Casino atualizado com sucesso!")
            else:
                mensagem_erro(f"❌ {resultado}")
            aguardar_enter()

        elif op == "5":
            id_c = input(f"\n  {CREME}{B}➤{R} {CREME}ID do casino:{R} ")
            mensagem_confirmacao("⚠️ ATENÇÃO: Esta ação é irreversível!")
            confirm = input(f"\n  {VERMELHO}{B}➤{R} {VERMELHO}Confirmar remoção? (s/n):{R} ").lower()
            if confirm == 's':
                status, resultado = remover_casino(id_c)
                if status == 200:
                    mensagem_sucesso("✅ Casino removido com sucesso!")
                else:
                    mensagem_erro(f"❌ {resultado}")
            else:
                mensagem_info("Operação cancelada")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("❌ Opção inválida! Tente novamente.")


# ══════════════════════ GESTÃO DE JOGOS ══════════════════════

def gestao_jogos():
    while True:
        imprimir_cabecalho("🎮 GESTÃO DE JOGOS", "Operações CRUD")

        opcoes = {
            "1": "📝 Criar Jogo",
            "2": "📋 Listar Jogos",
            "3": "🔍 Consultar Jogo",
            "4": "🗑️ Remover Jogo",
            "0": "◀ Voltar ao Menu Principal"
        }

        mostrar_caixa_menu("SUB-MENU", opcoes)

        op = input(f"\n  {OURO}{B}▶ OPÇÃO:{R} ").strip()

        if op == "1":
            print()
            mensagem_info("Preencha os dados do novo jogo")
            print()
            nome = input(f"  {CREME}{B}➤{R} {CREME}Nome do jogo:{R} ")
            tipo = input(f"  {CREME}{B}➤{R} {CREME}Tipo (carta/roleta/slot):{R} ")
            aposta_min = input(f"  {CREME}{B}➤{R} {CREME}Aposta mínima (€):{R} ")
            aposta_max = input(f"  {CREME}{B}➤{R} {CREME}Aposta máxima (€):{R} ")

            status, resultado = criar_jogo(nome, tipo, aposta_min, aposta_max)
            if status == 201:
                mensagem_sucesso("✅ Jogo criado com sucesso!")
            else:
                mensagem_erro(f"❌ {resultado}")
            aguardar_enter()

        elif op == "2":
            status, dados = listar_jogos()
            if status == 200:
                # Formatação especial para jogos
                itens_formatados = {}
                for id_j, info in dados.items():
                    icone = "🃏" if info['tipo'] == 'carta' else "🎰" if info['tipo'] == 'slot' else "🎡"
                    itens_formatados[id_j] = {
                        'nome': f"{icone} {info['nome']} ({info['tipo']}) - €{info['aposta_minima']}-€{info['aposta_maxima']}"
                    }
                mostrar_caixa_lista("📋 LISTA DE JOGOS", itens_formatados)
            else:
                mensagem_info("📭 Nenhum jogo encontrado")
            aguardar_enter()

        elif op == "3":
            id_j = input(f"\n  {CREME}{B}➤{R} {CREME}ID do jogo:{R} ")
            status, dados = consultar_jogo(id_j)
            if status == 200:
                mostrar_caixa_detalhe("JOGO", dados)
            else:
                mensagem_erro(f"❌ {dados}")
            aguardar_enter()

        elif op == "4":
            id_j = input(f"\n  {CREME}{B}➤{R} {CREME}ID do jogo:{R} ")
            mensagem_confirmacao("⚠️ ATENÇÃO: Esta ação é irreversível!")
            confirm = input(f"\n  {VERMELHO}{B}➤{R} {VERMELHO}Confirmar remoção? (s/n):{R} ").lower()
            if confirm == 's':
                status, resultado = remover_jogo(id_j)
                if status == 200:
                    mensagem_sucesso("✅ Jogo removido com sucesso!")
                else:
                    mensagem_erro(f"❌ {resultado}")
            else:
                mensagem_info("Operação cancelada")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("❌ Opção inválida! Tente novamente.")


# ══════════════════════ GESTÃO DE TRANSAÇÕES ══════════════════════

def gestao_transacoes():
    while True:
        imprimir_cabecalho("💰 GESTÃO DE TRANSAÇÕES", "Operações CRUD")

        opcoes = {
            "1": "📝 Criar Transação",
            "2": "📋 Listar Transações",
            "3": "🔍 Consultar Transação",
            "4": "✏️ Atualizar Transação",
            "5": "🗑️ Remover Transação",
            "0": "◀ Voltar ao Menu Principal"
        }

        mostrar_caixa_menu("SUB-MENU", opcoes)

        op = input(f"\n  {OURO}{B}▶ OPÇÃO:{R} ").strip()

        if op == "1":
            print()
            mensagem_info("Preencha os dados da nova transação")
            print()
            id_user = input(f"  {CREME}{B}➤{R} {CREME}ID do utilizador:{R} ")
            tipo = input(f"  {CREME}{B}➤{R} {CREME}Tipo (deposito/levantamento):{R} ")
            valor = input(f"  {CREME}{B}➤{R} {CREME}Valor (€):{R} ")
            data = input(f"  {CREME}{B}➤{R} {CREME}Data (DD-MM-AAAA):{R} ")

            status, resultado = criar_transacao(id_user, tipo, valor, data)
            if status == 201:
                mensagem_sucesso("✅ Transação criada com sucesso!")
            else:
                mensagem_erro(f"❌ {resultado}")
            aguardar_enter()

        elif op == "2":
            status, dados = listar_transacoes()
            if status == 200:
                # Formatação especial para transações
                itens_formatados = {}
                for id_t, info in dados.items():
                    sinal = "+" if info['tipo'] == 'deposito' else "-"
                    cor = VERDE if info['tipo'] == 'deposito' else VERMELHO
                    itens_formatados[id_t] = {
                        'nome': f"👤 {info['id_utilizador']} | {info['tipo']} | {cor}{sinal}€{info['valor']:.2f}{R} | 📅 {info['data']}"
                    }
                mostrar_caixa_lista("📋 LISTA DE TRANSAÇÕES", itens_formatados)
            else:
                mensagem_info("📭 Nenhuma transação encontrada")
            aguardar_enter()

        elif op == "3":
            id_t = input(f"\n  {CREME}{B}➤{R} {CREME}ID da transação:{R} ")
            status, dados = consultar_transacao(id_t)
            if status == 200:
                mostrar_caixa_detalhe("TRANSAÇÃO", dados)
            else:
                mensagem_erro(f"❌ {dados}")
            aguardar_enter()

        elif op == "4":
            id_t = input(f"\n  {CREME}{B}➤{R} {CREME}ID da transação:{R} ")
            mensagem_aviso("Deixe em branco para não alterar")
            print()
            tipo = input(f"  {CREME}{B}➤{R} {CREME}Novo tipo (deposito/levantamento):{R} ") or None
            valor = input(f"  {CREME}{B}➤{R} {CREME}Novo valor (€):{R} ") or None
            data = input(f"  {CREME}{B}➤{R} {CREME}Nova data (DD-MM-AAAA):{R} ") or None

            kwargs = {}
            if tipo:
                kwargs['tipo'] = tipo
            if valor:
                kwargs['valor'] = float(valor)
            if data:
                kwargs['data'] = data

            status, resultado = atualizar_transacao(id_t, **kwargs)
            if status == 200:
                mensagem_sucesso("✅ Transação atualizada com sucesso!")
            else:
                mensagem_erro(f"❌ {resultado}")
            aguardar_enter()

        elif op == "5":
            id_t = input(f"\n  {CREME}{B}➤{R} {CREME}ID da transação:{R} ")
            mensagem_confirmacao("⚠️ ATENÇÃO: Esta ação é irreversível!")
            confirm = input(f"\n  {VERMELHO}{B}➤{R} {VERMELHO}Confirmar remoção? (s/n):{R} ").lower()
            if confirm == 's':
                status, resultado = remover_transacao(id_t)
                if status == 200:
                    mensagem_sucesso("✅ Transação removida com sucesso!")
                else:
                    mensagem_erro(f"❌ {resultado}")
            else:
                mensagem_info("Operação cancelada")
            aguardar_enter()

        elif op == "0":
            break
        else:
            mensagem_erro("❌ Opção inválida! Tente novamente.")


# ══════════════════════ LOOP PRINCIPAL ══════════════════════

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
            limpar()
            print(f"\n  {VERDE}{B}╔{'═' * 45}╗{R}")
            print(f"  {VERDE}{B}║{R}   {VERDE}{B}✨{R} {B}A encerrar o sistema... Até breve!{R}   {VERDE}{B}║{R}")
            print(f"  {VERDE}{B}╚{'═' * 45}╝{R}\n")
            break
        else:
            mensagem_erro("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
