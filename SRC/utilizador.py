# utilizador.py
# CRUD simples para entidade Utilizador
# ==============================

from utils import (
    gerar_id_utilizador,
    validar_nome,
    validar_email,
    validar_tipo_conta,
    validar_data,
    validar_nif,
    validar_iban
)

utilizadores = {}


# CREATE
def criar_utilizador_casino(nome, email, tipo_conta, data_nascimento, nif, iban):
    # Validar nome
    ok, res = validar_nome(nome)
    if not ok:
        return 500, res
    nome = res

    # Validar email
    ok, res = validar_email(email)
    if not ok:
        return 500, res
    email = res

    # Validar tipo conta
    ok, res = validar_tipo_conta(tipo_conta)
    if not ok:
        return 500, res
    tipo_conta = res

    # Validar data nascimento - CORRIGIDO
    ok, res = validar_data(data_nascimento)
    if not ok:
        return 500, res
    data_nascimento = res  # <--- LINHA CORRIGIDA

    # Validar NIF
    ok, res = validar_nif(nif)
    if not ok:
        return 500, res
    nif = res

    # Validar IBAN
    ok, res = validar_iban(iban)
    if not ok:
        return 500, res
    iban = res

    # Criar utilizador
    id_utilizador = gerar_id_utilizador()
    utilizador = {
        "nome": nome,
        "email": email,
        "tipo_conta": tipo_conta,
        "data_nascimento": data_nascimento,
        "nif": nif,
        "iban": iban
    }
    utilizadores[id_utilizador] = utilizador
    return 201, utilizador


# READ (listar todos)
def listar_utilizadores_casino():
    if not utilizadores:
        return 404, "Não existem utilizadores registados."
    return 200, utilizadores


# READ (consultar individual) - CORRIGIDO para aceitar nome ou ID
def consultar_utilizador_casino(id_utilizador):
    # Se for número (ou string numérica), procura por ID
    if str(id_utilizador).isdigit():
        id_formatado = str(int(id_utilizador)).zfill(3)
        if id_formatado in utilizadores:
            return 200, utilizadores[id_formatado]
    
    # Se não encontrou por ID, procura por nome (case insensitive)
    for uid, dados in utilizadores.items():
        if dados['nome'].lower() == str(id_utilizador).lower():
            return 200, dados
    
    return 404, "Utilizador não encontrado."


# UPDATE
def atualizar_utilizador_casino(id_utilizador, nome=None, email=None, tipo_conta=None,
                                 data_nascimento=None, nif=None, iban=None):
    # Converter ID para formato correto
    id_utilizador = str(id_utilizador).zfill(3)
    
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
        utilizadores[id_utilizador]["data_nascimento"] = res  # CORRIGIDO

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

    return 200, utilizadores[id_utilizador]


# DELETE
def remover_utilizador_casino(id_utilizador):
    id_utilizador = str(id_utilizador).zfill(3)
    
    if id_utilizador not in utilizadores:
        return 404, "Utilizador não encontrado."
    del utilizadores[id_utilizador]
    return 200, id_utilizador
