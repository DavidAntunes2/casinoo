# casino.py
# CRUD simples para entidade Casino
# SEM utilização de classes
# armazenamento em dicionario
# validações feitas aqui (não no main)
# ==============================

import uuid
from utils import (
    validar_nome,
    validar_localizacao,
    validar_licenca,
    validar_data,
    validar_saldo
)

casinos = {}


def gerar_id_casino():
    """Gera ID no formato CA-XXXXXXXX"""
    return "CA-" + str(uuid.uuid4())[:8].upper()


# CREATE
def criar_casino(nome, localizacao, licenca, data_inauguracao, saldo):
    # Validar nome
    ok, res = validar_nome(nome)
    if not ok:
        return 500, res
    nome = res

    # Validar localização
    ok, res = validar_localizacao(localizacao)
    if not ok:
        return 500, res
    localizacao = res

    # Validar licença
    ok, res = validar_licenca(licenca)
    if not ok:
        return 500, res
    licenca = res

    # Validar data
    ok, res = validar_data(data_inauguracao)
    if not ok:
        return 500, res

    # Validar saldo
    ok, res = validar_saldo(saldo)
    if not ok:
        return 500, res
    saldo = res

    # Criar casino
    id_casino = gerar_id_casino()
    casino = {
        "nome": nome,
        "localizacao": localizacao,
        "licenca": licenca,
        "data_inauguracao": data_inauguracao,
        "saldo": saldo
    }
    casinos[id_casino] = casino
    return 201, casino


# READ (listar todos)
def listar_casinos():
    if not casinos:
        return 404, "Não existem casinos registados."
    return 200, casinos


# READ (consultar individual)
def consultar_casino(id_casino):
    if id_casino not in casinos:
        return 404, "Casino não encontrado."
    return 200, casinos[id_casino]


# UPDATE
def atualizar_casino(id_casino, nome=None, localizacao=None, licenca=None,
                     data_inauguracao=None, saldo=None):
    if id_casino not in casinos:
        return 404, "Casino não encontrado."

    if nome is not None:
        ok, res = validar_nome(nome)
        if not ok:
            return 500, res
        casinos[id_casino]["nome"] = res

    if localizacao is not None:
        ok, res = validar_localizacao(localizacao)
        if not ok:
            return 500, res
        casinos[id_casino]["localizacao"] = res

    if licenca is not None:
        ok, res = validar_licenca(licenca)
        if not ok:
            return 500, res
        casinos[id_casino]["licenca"] = res

    if data_inauguracao is not None:
        ok, res = validar_data(data_inauguracao)
        if not ok:
            return 500, res
        casinos[id_casino]["data_inauguracao"] = data_inauguracao

    if saldo is not None:
        ok, res = validar_saldo(saldo)
        if not ok:
            return 500, res
        casinos[id_casino]["saldo"] = res

    return 200, casinos[id_casino]


# DELETE
def remover_casino(id_casino):
    if id_casino not in casinos:
        return 404, "Casino não encontrado."
    del casinos[id_casino]
    return 200, id_casino
