# utils.py
# Funções utilitárias para validação e geração de IDs
# ==============================

import re
import random
import string
import json
import os
from datetime import datetime


# ══════════════════════ JSON ══════════════════════

def carregar_dados(ficheiro):
    if not os.path.exists(ficheiro):
        return {}
    try:
        with open(ficheiro, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def guardar_dados(ficheiro, dados):
    try:
        with open(ficheiro, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"Erro ao guardar ficheiro {ficheiro}: {e}")


# ══════════════════════ FICHEIROS ══════════════════════

FICHEIRO_UTILIZADORES = "utilizadores.json"
FICHEIRO_CASINOS      = "casinos.json"
FICHEIRO_JOGOS        = "jogos.json"
FICHEIRO_TRANSACOES   = "transacoes.json"


# ══════════════════════ GERAÇÃO DE IDs ══════════════════════

def gerar_id_utilizador():
    dados = carregar_dados(FICHEIRO_UTILIZADORES)
    contador = len(dados) + 1
    ids_existentes = set(dados.keys())
    while str(contador).zfill(3) in ids_existentes:
        contador += 1
    return str(contador).zfill(3)


def gerar_id_casino():
    dados = carregar_dados(FICHEIRO_CASINOS)
    contador = len(dados) + 1
    ids_existentes = set(dados.keys())
    while str(contador).zfill(3) in ids_existentes:
        contador += 1
    return str(contador).zfill(3)


def gerar_id_jogo():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=8))
    return f"JG-{codigo}"


def gerar_id_transacao():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=8))
    return f"TR-{codigo}"


# ══════════════════════ VALIDAÇÕES GERAIS ══════════════════════

def validar_nome(nome):
    if not nome or not isinstance(nome, str):
        return False, "Nome inválido."
    nome = nome.strip()
    if len(nome) < 2:
        return False, "Nome deve ter pelo menos 2 caracteres."
    if len(nome) > 100:
        return False, "Nome deve ter no máximo 100 caracteres."
    return True, nome


def validar_email(email):
    if not email or not isinstance(email, str):
        return False, "Email inválido."
    email = email.strip()
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(padrao, email):
        return False, "Email inválido."
    return True, email


def validar_tipo_conta(tipo_conta):
    if not tipo_conta or not isinstance(tipo_conta, str):
        return False, "Tipo de conta inválido."
    tipo_conta = tipo_conta.strip().lower()
    if tipo_conta not in ['standard', 'vip', 'high roller']:
        return False, "Tipo de conta deve ser standard, vip ou high roller."
    return True, tipo_conta


def validar_data(data_str):
    if not data_str or not isinstance(data_str, str):
        return False, "Data inválida."
    formatos = ['%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y']
    for fmt in formatos:
        try:
            data_valida = datetime.strptime(data_str.strip(), fmt)
            return True, data_valida.strftime('%d-%m-%Y')
        except ValueError:
            continue
    return False, "Data inválida. Use DD-MM-AAAA, AAAA-MM-DD ou DD/MM/AAAA."


def validar_nif(nif):
    if not nif or not isinstance(nif, str):
        return False, "NIF inválido."
    nif = nif.strip()
    if not nif.isdigit() or len(nif) != 9:
        return False, "NIF deve ter 9 dígitos."
    return True, nif


def validar_iban(iban):
    if not iban or not isinstance(iban, str):
        return False, "IBAN inválido."
    iban = iban.strip().upper()
    if len(iban) < 15 or len(iban) > 34:
        return False, "IBAN inválido."
    return True, iban


# ══════════════════════ VALIDAÇÕES DE CASINO ══════════════════════

def validar_localizacao(localizacao):
    if not localizacao or not isinstance(localizacao, str):
        return False, "Localização inválida."
    localizacao = localizacao.strip()
    if len(localizacao) < 3:
        return False, "Localização deve ter pelo menos 3 caracteres."
    if len(localizacao) > 200:
        return False, "Localização deve ter no máximo 200 caracteres."
    return True, localizacao


def validar_licenca(licenca):
    if not licenca or not isinstance(licenca, str):
        return False, "Licença inválida."
    licenca = licenca.strip()
    if len(licenca) < 5:
        return False, "Licença deve ter pelo menos 5 caracteres."
    if len(licenca) > 50:
        return False, "Licença deve ter no máximo 50 caracteres."
    return True, licenca


def validar_saldo(saldo):
    try:
        saldo = float(saldo)
        if saldo < 0:
            return False, "Saldo não pode ser negativo."
        if saldo > 1000000000:
            return False, "Saldo muito alto (máx: 1.000.000.000)."
        return True, round(saldo, 2)
    except (ValueError, TypeError):
        return False, "Saldo inválido. Deve ser um número."


# ══════════════════════ VALIDAÇÕES DE JOGO ══════════════════════

def validar_tipo_jogo(tipo):
    if not tipo or not isinstance(tipo, str):
        return False, "Tipo de jogo inválido."
    tipo = tipo.strip().lower()
    if tipo not in ['carta', 'roleta', 'slot']:
        return False, "Tipo de jogo deve ser carta, roleta ou slot."
    return True, tipo


def validar_aposta_minima(aposta):
    try:
        aposta = float(aposta)
        if aposta <= 0:
            return False, "Aposta mínima deve ser maior que 0."
        if aposta > 1000000:
            return False, "Aposta mínima muito alta (máx: 1.000.000)."
        return True, round(aposta, 2)
    except (ValueError, TypeError):
        return False, "Aposta mínima inválida."


def validar_aposta_maxima(aposta_maxima, aposta_minima):
    try:
        aposta_maxima = float(aposta_maxima)
        if aposta_maxima <= aposta_minima:
            return False, "Aposta máxima deve ser maior que a aposta mínima."
        if aposta_maxima > 1000000:
            return False, "Aposta máxima muito alta (máx: 1.000.000)."
        return True, round(aposta_maxima, 2)
    except (ValueError, TypeError):
        return False, "Aposta máxima inválida."


# ══════════════════════ VALIDAÇÕES DE TRANSAÇÃO ══════════════════════

def validar_tipo_transacao(tipo):
    if not tipo or not isinstance(tipo, str):
        return False, "Tipo de transação inválido."
    tipo = tipo.strip().lower()
    if tipo not in ['deposito', 'levantamento']:
        return False, "Tipo deve ser 'deposito' ou 'levantamento'."
    return True, tipo


def validar_valor_transacao(valor):
    try:
        valor = float(valor)
        if valor <= 0:
            return False, "Valor da transação deve ser positivo."
        if valor > 1000000:
            return False, "Valor muito alto (máx: 1.000.000)."
        return True, round(valor, 2)
    except (ValueError, TypeError):
        return False, "Valor inválido."


def validar_data_transacao(data_str):
    if not data_str or not isinstance(data_str, str):
        return False, "Data inválida."
    formatos = ['%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y']
    for fmt in formatos:
        try:
            data_valida = datetime.strptime(data_str.strip(), fmt)
            if data_valida.date() > datetime.now().date():
                return False, "Data não pode ser futura."
            return True, data_valida.strftime('%d-%m-%Y')
        except ValueError:
            continue
    return False, "Data inválida. Use DD-MM-AAAA, AAAA-MM-DD ou DD/MM/AAAA."
