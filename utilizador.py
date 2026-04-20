from utils import *

carregar_dados()


# ══════════════════════════════════════════════════════════════════════════════
#  LÓGICA DE NEGÓCIO  —  sem prints, só retorna (codigo, mensagem/dados)
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


def obter_resumo():
    """Devolve dict com estatísticas gerais para a main imprimir."""
    total   = len(jogadores)
    saldo_t = sum(v['saldo'] for v in jogadores.values())
    hr      = sum(1 for v in jogadores.values() if "HIGH ROLLER" in v['rank'])
    return {
        "total":   total,
        "saldo_t": saldo_t,
        "hr":      hr,
        "vip":     total - hr,
    }
