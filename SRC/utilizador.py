# ==============================
# utilizador_casino.py
# CRUD simples para entidade Utilizador de Casino
# SEM utilização de classes
# armazenamento em dicionario
# validações feitas aqui (não no main)
# ==============================

from utils import (
    gerar_id_utilizador_casino,
    validar_nome,
    validar_email,
    validar_nif,
    validar_iban,
    validar_data_nascimento,
    validar_tipo_conta
)

utilizadores_casino = {}


# CREATE
def criar_utilizador_casino(nome, email, tipo_conta, data_nascimento, nif, iban):

    ok, res = validar_nome(nome)
    if not ok:
        return 500, res
    nome = res

    ok, res = validar_email(email)
    if not ok:
        return 500, res
    email = res

    ok, res = validar_tipo_conta(tipo_conta)
    if not ok:
        return 500, res
    tipo_conta = res

    ok, res = validar_data_nascimento(data_nascimento)
    if not ok:
        return 500, res

    ok, res = validar_nif(nif)
    if not ok:
        return 500, res
    nif = res

    ok, res = validar_iban(iban)
    if not ok:
        return 500, res
    iban = res

    id_utilizador_casino = gerar_id_utilizador_casino()
    utilizador_casino = {
        "nome": nome,
        "email": email,
        "tipo_conta": tipo_conta,
        "data_nascimento": data_nascimento,
        "nif": nif,
        "iban": iban
    }
    utilizadores_casino[id_utilizador_casino] = utilizador_casino
    return 201, utilizador_casino


# READ (listar todos)
def listar_utilizadores_casino():
    if not utilizadores_casino:
        return 404, "Não existem utilizadores de casino registados."
    return 200, utilizadores_casino


# READ (consultar individual)
def consultar_utilizador_casino(id_utilizador_casino):
    if id_utilizador_casino not in utilizadores_casino:
        return 404, "Utilizador de casino não encontrado."
    return 200, utilizadores_casino[id_utilizador_casino]


# UPDATE
def atualizar_utilizador_casino(id_utilizador_casino, nome=None, email=None, tipo_conta=None, data_nascimento=None, nif=None, iban=None):
    if id_utilizador_casino not in utilizadores_casino:
        return 404, "Utilizador de casino não encontrado."

    if nome is not None:
        ok, res = validar_nome(nome)
        if not ok:
            return 500, res
        utilizadores_casino[id_utilizador_casino]["nome"] = res

    if email is not None:
        ok, res = validar_email(email)
        if not ok:
            return 500, res
        utilizadores_casino[id_utilizador_casino]["email"] = res

    if tipo_conta is not None:
        ok, res = validar_tipo_conta(tipo_conta)
        if not ok:
            return 500, res
        utilizadores_casino[id_utilizador_casino]["tipo_conta"] = res

    if data_nascimento is not None:
        ok, res = validar_data_nascimento(data_nascimento)
        if not ok:
            return 500, res
        utilizadores_casino[id_utilizador_casino]["data_nascimento"] = data_nascimento

    if nif is not None:
        ok, res = validar_nif(nif)
        if not ok:
            return 500, res
        utilizadores_casino[id_utilizador_casino]["nif"] = res

    if iban is not None:
        ok, res = validar_iban(iban)
        if not ok:
            return 500, res
        utilizadores_casino[id_utilizador_casino]["iban"] = res

    return 200, utilizadores_casino[id_utilizador_casino]


# DELETE
def remover_utilizador_casino(id_utilizador_casino):
    if id_utilizador_casino not in utilizadores_casino:
        return 404, "Utilizador de casino não encontrado."
    del utilizadores_casino[id_utilizador_casino]
    return 200, id_utilizador_casino