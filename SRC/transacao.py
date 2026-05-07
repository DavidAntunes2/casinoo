# transacao.py
# CRUD da entidade Transação
# ==============================

from utilizador import utilizadores
from casino import casinos
from utils import (
    gerar_id_transacao,
    validar_tipo_transacao,
    validar_valor_transacao,
    validar_data_transacao
)

transacoes = {}


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
        "id_transacao":  id_transacao,
        "id_utilizador": id_utilizador,
        "id_casino":     id_casino,
        "tipo":          tipo,
        "valor":         valor,
        "data":          data
    }
    transacoes[id_transacao] = transacao
    return 201, transacao


# READ (listar todos)
def listar_transacoes():
    if not transacoes:
        return 404, "Sem transações registadas."
    return 200, transacoes


# READ (consultar individual)
def consultar_transacao(id_transacao):
    if id_transacao not in transacoes:
        return 404, "Transação não encontrada."
    return 200, transacoes[id_transacao]


# READ (listar por utilizador)
def listar_transacoes_por_utilizador(id_utilizador):
    if id_utilizador not in utilizadores:
        return 404, "Utilizador não encontrado."
    resultado = {id_t: t for id_t, t in transacoes.items()
                 if t["id_utilizador"] == id_utilizador}
    if not resultado:
        return 404, "Sem transações para este utilizador."
    return 200, resultado


# READ (listar por casino)
def listar_transacoes_por_casino(id_casino):
    if id_casino not in casinos:
        return 404, "Casino não encontrado."
    resultado = {id_t: t for id_t, t in transacoes.items()
                 if t["id_casino"] == id_casino}
    if not resultado:
        return 404, "Sem transações para este casino."
    return 200, resultado


# UPDATE
def atualizar_transacao(id_transacao, tipo=None, valor=None, data=None, id_casino=None):
    if id_transacao not in transacoes:
        return 404, "Transação não encontrada."

    if tipo is not None:
        ok, res = validar_tipo_transacao(tipo)
        if not ok:
            return 500, res
        transacoes[id_transacao]["tipo"] = res

    if valor is not None:
        ok, res = validar_valor_transacao(valor)
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
        return 404, "Transação não encontrada."
    del transacoes[id_transacao]
    return 200, id_transacao
