# jogo.py
# CRUD simples para entidade Jogo
# ==============================

import random
import string
from utils import (
    validar_nome,
    validar_tipo_jogo,
    validar_aposta
)
from casino import casinos

jogos = {}


def gerar_id_jogo():
    """Gera ID no formato JG-XXXXXXXX"""
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=8))
    return f"JG-{codigo}"


# CREATE
def criar_jogo(nome, tipo, aposta_minima, aposta_maxima, id_casino):
    # Validar nome
    ok, res = validar_nome(nome)
    if not ok:
        return 500, res
    nome = res

    # Capitalizar nome automaticamente
    nome = nome.title()

    # Validar tipo
    ok, res = validar_tipo_jogo(tipo)
    if not ok:
        return 500, res
    tipo = res

    # Validar aposta mínima (>0)
    try:
        aposta_minima = float(aposta_minima)
        if aposta_minima <= 0:
            return 500, "Aposta mínima deve ser maior que 0."
    except (ValueError, TypeError):
        return 500, "Aposta mínima inválida."

    # Validar aposta máxima (> aposta_minima)
    try:
        aposta_maxima = float(aposta_maxima)
        if aposta_maxima <= aposta_minima:
            return 500, "Aposta máxima deve ser maior que a aposta mínima."
    except (ValueError, TypeError):
        return 500, "Aposta máxima inválida."

    # Validar se casino existe
    if id_casino not in casinos:
        return 500, f"Casino com ID {id_casino} não encontrado."

    # Criar jogo
    id_jogo = gerar_id_jogo()
    jogo = {
        "id_jogo": id_jogo,
        "nome": nome,
        "tipo": tipo,
        "aposta_minima": round(aposta_minima, 2),
        "aposta_maxima": round(aposta_maxima, 2),
        "id_casino": id_casino
    }
    jogos[id_jogo] = jogo
    return 201, jogo


# READ (listar todos)
def listar_jogos():
    if not jogos:
        return 404, "Sem jogos"
    return 200, jogos


# READ (consultar individual)
def consultar_jogo(id_jogo):
    if id_jogo not in jogos:
        return 404, "Jogo não encontrado"
    return 200, jogos[id_jogo]


# READ (listar jogos por casino)
def listar_jogos_por_casino(id_casino):
    if id_casino not in casinos:
        return 404, "Casino não encontrado"

    jogos_casino = {id_j: j for id_j, j in jogos.items() if j["id_casino"] == id_casino}

    if not jogos_casino:
        return 404, "Sem jogos para este casino"
    return 200, jogos_casino


# UPDATE
def atualizar_jogo(id_jogo, nome=None, tipo=None, aposta_minima=None, aposta_maxima=None, id_casino=None):
    if id_jogo not in jogos:
        return 404, "Jogo não encontrado"

    if nome is not None:
        ok, res = validar_nome(nome)
        if not ok:
            return 500, res
        jogos[id_jogo]["nome"] = res.title()

    if tipo is not None:
        ok, res = validar_tipo_jogo(tipo)
        if not ok:
            return 500, res
        jogos[id_jogo]["tipo"] = res

    if aposta_minima is not None:
        try:
            aposta_minima = float(aposta_minima)
            if aposta_minima <= 0:
                return 500, "Aposta mínima deve ser maior que 0."
            jogos[id_jogo]["aposta_minima"] = round(aposta_minima, 2)
        except (ValueError, TypeError):
            return 500, "Aposta mínima inválida."

        # Verificar se aposta_maxima ainda é > aposta_minima
        if jogos[id_jogo]["aposta_maxima"] <= jogos[id_jogo]["aposta_minima"]:
            return 500, "Aposta máxima deve ser maior que a aposta mínima."

    if aposta_maxima is not None:
        try:
            aposta_maxima = float(aposta_maxima)
            if aposta_maxima <= jogos[id_jogo]["aposta_minima"]:
                return 500, "Aposta máxima deve ser maior que a aposta mínima."
            jogos[id_jogo]["aposta_maxima"] = round(aposta_maxima, 2)
        except (ValueError, TypeError):
            return 500, "Aposta máxima inválida."

    if id_casino is not None:
        if id_casino not in casinos:
            return 500, f"Casino com ID {id_casino} não encontrado."
        jogos[id_jogo]["id_casino"] = id_casino

    return 200, jogos[id_jogo]


# DELETE
def remover_jogo(id_jogo):
    if id_jogo not in jogos:
        return 404, "Jogo não encontrado"
    del jogos[id_jogo]
    return 200, id_jogo
