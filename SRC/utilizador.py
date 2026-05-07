# utilizador.py
# CRUD da entidade Utilizador
# ==============================

from utils import (
    FICHEIRO_UTILIZADORES,
    carregar_dados,
    guardar_dados,
    gerar_id_utilizador,
    validar_nome,
    validar_email,
    validar_tipo_conta,
    validar_data,
    validar_nif,
    validar_iban
)


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

    ok, res = validar_data(data_nascimento)
    if not ok:
        return 500, res
    data_nascimento = res

    ok, res = validar_nif(nif)
    if not ok:
        return 500, res
    nif = res

    ok, res = validar_iban(iban)
    if not ok:
        return 500, res
    iban = res

    utilizadores = carregar_dados(FICHEIRO_UTILIZADORES)
    id_utilizador = gerar_id_utilizador()
    utilizador = {
        "id_utilizador":   id_utilizador,
        "nome":            nome,
        "email":           email,
        "tipo_conta":      tipo_conta,
        "data_nascimento": data_nascimento,
        "nif":             nif,
        "iban":            iban
    }
    utilizadores[id_utilizador] = utilizador
    guardar_dados(FICHEIRO_UTILIZADORES, utilizadores)
    return 201, utilizador


# READ (listar todos)
def listar_utilizadores_casino():
    utilizadores = carregar_dados(FICHEIRO_UTILIZADORES)
    if not utilizadores:
        return 404, "Não existem utilizadores registados."
    return 200, utilizadores


# READ (consultar individual)
def consultar_utilizador_casino(identificador):
    utilizadores = carregar_dados(FICHEIRO_UTILIZADORES)
    identificador = str(identificador).strip()

    if identificador.isdigit():
        id_formatado = identificador.zfill(3)
        if id_formatado in utilizadores:
            return 200, utilizadores[id_formatado]

    if identificador in utilizadores:
        return 200, utilizadores[identificador]

    for uid, dados in utilizadores.items():
        if dados['nome'].lower() == identificador.lower():
            return 200, dados

    return 404, "Utilizador não encontrado."


# UPDATE
def atualizar_utilizador_casino(id_utilizador, nome=None, email=None, tipo_conta=None,
                                data_nascimento=None, nif=None, iban=None):
    utilizadores = carregar_dados(FICHEIRO_UTILIZADORES)
    id_utilizador = str(id_utilizador).strip().zfill(3)

    if id_utilizador not in utilizadores:
        return 404, "Utilizador não encontrado."

    if nome is not None:
        ok, res = validar_nome(nome)
        if not ok:
            return 500, res
        utilizadores[id_utilizador]["nome"] = res

    if email is not None:
        ok, res = validar_email(email)
        if not ok:
            return 500, res
        utilizadores[id_utilizador]["email"] = res

    if tipo_conta is not None:
        ok, res = validar_tipo_conta(tipo_conta)
        if not ok:
            return 500, res
        utilizadores[id_utilizador]["tipo_conta"] = res

    if data_nascimento is not None:
        ok, res = validar_data(data_nascimento)
        if not ok:
            return 500, res
        utilizadores[id_utilizador]["data_nascimento"] = res

    if nif is not None:
        ok, res = validar_nif(nif)
        if not ok:
            return 500, res
        utilizadores[id_utilizador]["nif"] = res

    if iban is not None:
        ok, res = validar_iban(iban)
        if not ok:
            return 500, res
        utilizadores[id_utilizador]["iban"] = res

    guardar_dados(FICHEIRO_UTILIZADORES, utilizadores)
    return 200, utilizadores[id_utilizador]


# DELETE
def remover_utilizador_casino(id_utilizador):
    utilizadores = carregar_dados(FICHEIRO_UTILIZADORES)
    id_utilizador = str(id_utilizador).strip().zfill(3)

    if id_utilizador not in utilizadores:
        return 404, "Utilizador não encontrado."

    del utilizadores[id_utilizador]
    guardar_dados(FICHEIRO_UTILIZADORES, utilizadores)
    return 200, id_utilizador
