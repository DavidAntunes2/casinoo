# transacao.py
# CRUD simples para entidade Transacao
# ==============================

import random
import string
from datetime import datetime
from utilizador import utilizadores
from casino import casinos

transacoes = {}


def gerar_id_transacao():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=8))
    return f"TR-{codigo}"


def validar_data_transacao(data_str):
    if not data_str or not isinstance(data_str, str):
        return False, "Data inválida."
    formatos = ['%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y']
    data_valida = None
    for formato in formatos:
        try:
            data_valida = datetime.strptime(data_str.strip(), formato)
            break
        except ValueError:
            continue
    if data_valida is None:
        return False, "Data inválida. Use DD-MM-AAAA, AAAA-MM-DD ou DD/MM/AAAA"
    if data_valida.date() > datetime.now().date():
        return False, "Data não pode ser futura"
    return True, data_valida.strftime('%d-%m-%Y')


def validar_tipo_transacao(tipo):
    if not tipo or not isinstance(tipo, str):
        return False, "Tipo de transação inválido."
    tipo = tipo.strip().lower()
    if tipo not in ['deposito', 'levantamento']:
        return False, "Tipo deve ser 'deposito' ou 'levantamento'."
    return True, tipo


def validar_valor_transacao(valor):
    try:
        valor = float(valor)  # aceita str ou float
        if valor <= 0:
            return False, "Valor da transação deve ser positivo."
        if valor > 1000000:
            return False, "Valor muito alto (máx: 1.000.000)."
        return True, round(valor, 2)
    except (ValueError, TypeError):
        return False, "Valor inválido."


# CREATE
def criar_transacao(id_utilizador, tipo, valor, data, id_casino):
    if id_utilizador not in utilizadores:
        return 500, f"Utilizador com ID {id_utilizador} não encontrado."
    if id_casino not in casinos:
        return 500, f"Casino com ID {id_casino} não encontrado."
    ok, res = validar_tipo_transacao(tipo)
    if not ok:
        return 500, res
    tipo = res
    ok, res = validar_valor_transacao(valor)
    if not ok:
        return 500, res
    valor = res
    ok, res = validar_data_transacao(data)
    if not ok:
        return 500, res
    data = res
    id_transacao = gerar_id_transacao()
    transacao = {
        "id_transacao": id_transacao,
        "id_utilizador": id_utilizador,
        "id_casino": id_casino,
        "tipo": tipo,
        "valor": valor,
        "data": data
    }
    transacoes[id_transacao] = transacao
    return 201, transacao


# READ
def listar_transacoes():
    if not transacoes:
        return 404, "Sem transações"
    return 200, transacoes


def consultar_transacao(id_transacao):
    if id_transacao not in transacoes:
        return 404, "Transação não encontrada"
    return 200, transacoes[id_transacao]


def listar_transacoes_por_utilizador(id_utilizador):
    if id_utilizador not in utilizadores:
        return 404, "Utilizador não encontrado"
    result = {id_t: t for id_t, t in transacoes.items() if t["id_utilizador"] == id_utilizador}
    if not result:
        return 404, "Sem transações para este utilizador"
    return 200, result


def listar_transacoes_por_casino(id_casino):
    if id_casino not in casinos:
        return 404, "Casino não encontrado"
    result = {id_t: t for id_t, t in transacoes.items() if t["id_casino"] == id_casino}
    if not result:
        return 404, "Sem transações para este casino"
    return 200, result


# UPDATE
def atualizar_transacao(id_transacao, tipo=None, valor=None, data=None, id_casino=None):
    if id_transacao not in transacoes:
        return 404, "Transação não encontrada"
    if tipo is not None:
        ok, res = validar_tipo_transacao(tipo)
        if not ok:
            return 500, res
        transacoes[id_transacao]["tipo"] = res
    if valor is not None:
        ok, res = validar_valor_transacao(valor)  # valida str ou float
        if not ok:
            return 500, res
        transacoes[id_transacao]["valor"] = res
    if data is not None:
        ok, res = validar_data_transacao(data)
        if not ok:
            return 500, res
        transacoes[id_transacao]["data"] = res
    if id_casino is not None:
        if id_casino not in casinos:
            return 500, f"Casino com ID {id_casino} não encontrado."
        transacoes[id_transacao]["id_casino"] = id_casino
    return 200, transacoes[id_transacao]


# DELETE
def remover_transacao(id_transacao):
    if id_transacao not in transacoes:
        return 404, "Transação não encontrada"
    del transacoes[id_transacao]
    return 200, id_transacao
