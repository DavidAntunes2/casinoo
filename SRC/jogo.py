# jogo.py
# CRUD da entidade Jogo
# ==============================

from utils import (
    FICHEIRO_JOGOS,
    FICHEIRO_CASINOS,
    carregar_dados,
    guardar_dados,
    gerar_id_jogo,
    validar_nome,
    validar_tipo_jogo,
    validar_aposta_minima,
    validar_aposta_maxima
)


# CREATE
def criar_jogo(nome, tipo, aposta_minima, aposta_maxima, id_casino):
    ok, res = validar_nome(nome)
    if not ok:
        return 500, res
    nome = res.title()

    ok, res = validar_tipo_jogo(tipo)
    if not ok:
        return 500, res
    tipo = res

    ok, res = validar_aposta_minima(aposta_minima)
    if not ok:
        return 500, res
    aposta_minima = res

    ok, res = validar_aposta_maxima(aposta_maxima, aposta_minima)
    if not ok:
        return 500, res
    aposta_maxima = res

    casinos = carregar_dados(FICHEIRO_CASINOS)
    if id_casino not in casinos:
        return 500, f"Casino com ID {id_casino} não encontrado."

    jogos = carregar_dados(FICHEIRO_JOGOS)
    id_jogo = gerar_id_jogo()
    jogo = {
        "id_jogo":       id_jogo,
        "nome":          nome,
        "tipo":          tipo,
        "aposta_minima": aposta_minima,
        "aposta_maxima": aposta_maxima,
        "id_casino":     id_casino
    }
    jogos[id_jogo] = jogo
    guardar_dados(FICHEIRO_JOGOS, jogos)
    return 201, jogo


# READ (listar todos)
def listar_jogos():
    jogos = carregar_dados(FICHEIRO_JOGOS)
    if not jogos:
        return 404, "Sem jogos registados."
    return 200, jogos


# READ (consultar individual)
def consultar_jogo(id_jogo):
    jogos = carregar_dados(FICHEIRO_JOGOS)
    if id_jogo not in jogos:
        return 404, "Jogo não encontrado."
    return 200, jogos[id_jogo]


# READ (listar por casino)
def listar_jogos_por_casino(id_casino):
    casinos = carregar_dados(FICHEIRO_CASINOS)
    if id_casino not in casinos:
        return 404, "Casino não encontrado."
    jogos = carregar_dados(FICHEIRO_JOGOS)
    resultado = {id_j: j for id_j, j in jogos.items()
                 if j["id_casino"] == id_casino}
    if not resultado:
        return 404, "Sem jogos para este casino."
    return 200, resultado


# UPDATE
def atualizar_jogo(id_jogo, nome=None, tipo=None,
                   aposta_minima=None, aposta_maxima=None, id_casino=None):
    jogos = carregar_dados(FICHEIRO_JOGOS)

    if id_jogo not in jogos:
        return 404, "Jogo não encontrado."

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
        ok, res = validar_aposta_minima(aposta_minima)
        if not ok:
            return 500, res
        if res >= jogos[id_jogo]["aposta_maxima"]:
            return 500, "Aposta mínima deve ser menor que a aposta máxima atual."
        jogos[id_jogo]["aposta_minima"] = res

    if aposta_maxima is not None:
        ok, res = validar_aposta_maxima(aposta_maxima, jogos[id_jogo]["aposta_minima"])
        if not ok:
            return 500, res
        jogos[id_jogo]["aposta_maxima"] = res

    if id_casino is not None:
        casinos = carregar_dados(FICHEIRO_CASINOS)
        if id_casino not in casinos:
            return 500, f"Casino com ID {id_casino} não encontrado."
        jogos[id_jogo]["id_casino"] = id_casino

    guardar_dados(FICHEIRO_JOGOS, jogos)
    return 200, jogos[id_jogo]


# DELETE
def remover_jogo(id_jogo):
    jogos = carregar_dados(FICHEIRO_JOGOS)

    if id_jogo not in jogos:
        return 404, "Jogo não encontrado."

    del jogos[id_jogo]
    guardar_dados(FICHEIRO_JOGOS, jogos)
    return 200, id_jogo
