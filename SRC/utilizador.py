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

    # Validar data nascimento
    ok, res = validar_data(data_nascimento)
    if not ok:
        return 500, res
    data_nascimento = res  # CORRIGIDO: usar a variável correta

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
        "id": id_utilizador,  # ADICIONADO: incluir ID no dicionário
        "nome": nome,
        "email": email,
        "tipo_conta": tipo_conta,
        "data_nascimento": data_nascimento,
        "nif": nif,
        "iban": iban
    }
    utilizadores[id_utilizador] = utilizador
    return 201, utilizador


# READ (listar todos) - CORRIGIDO para formato consistente
def listar_utilizadores_casino():
    if not utilizadores:
        return 404, "Não existem utilizadores registados."

    # Retornar no formato esperado pelo main.py {id: dados}
    dados_formatados = {}
    for id_user, dados in utilizadores.items():
        dados_formatados[id_user] = {
            'nome': dados['nome'],
            'saldo': 0  # Saldo padrão, ajuste conforme necessário
        }
    return 200, dados_formatados


# READ (consultar individual)
def consultar_utilizador_casino(id_utilizador):
    # Converter para string se necessário (os IDs são strings tipo "001")
    id_utilizador = str(id_utilizador).zfill(3)

    if id_utilizador not in utilizadores:
        return 404, "Utilizador não encontrado."

    # Retornar cópia para não modificar o original
    dados = utilizadores[id_utilizador].copy()
    return 200, dados


# UPDATE
def atualizar_utilizador_casino(id_utilizador, nome=None, email=None, tipo_conta=None,
                                data_nascimento=None, nif=None, iban=None):
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
