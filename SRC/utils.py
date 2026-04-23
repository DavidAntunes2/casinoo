# utils.py
# Funções utilitárias para validação e geração de IDs
# ==============================

import re
from datetime import datetime

# NOTA: Os IDs agora são gerados com formato específico nas suas entidades
# JG-XXXXXXXX para Jogos
# TR-XXXXXXXX para Transações
# Os contadores abaixo são mantidos para compatibilidade com código existente

id_casino_counter = 1
id_utilizador_counter = 1


# ========== GERADORES DE ID ==========
def gerar_id_casino():
    global id_casino_counter
    id_atual = id_casino_counter
    id_casino_counter += 1
    return str(id_atual).zfill(3)


def gerar_id_utilizador():
    global id_utilizador_counter
    id_atual = id_utilizador_counter
    id_utilizador_counter += 1
    return str(id_atual).zfill(3)


# ========== VALIDAÇÕES ==========
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
    try:
        datetime.strptime(data_str, '%d-%m-%Y')
        return True, data_str
    except ValueError:
        return False, "Data inválida. Use o formato DD-MM-AAAA."


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
    """Valida o saldo do casino"""
    try:
        saldo = float(saldo)
        if saldo < 0:
            return False, "Saldo não pode ser negativo."
        if saldo > 1000000000:
            return False, "Saldo muito alto (máx: 1.000.000.000)."
        return True, round(saldo, 2)
    except (ValueError, TypeError):
        return False, "Saldo inválido. Deve ser um número."


def validar_tipo_jogo(tipo):
    if not tipo or not isinstance(tipo, str):
        return False, "Tipo de jogo inválido."
    tipo = tipo.strip().lower()
    if tipo not in ['carta', 'roleta', 'slot']:
        return False, "Tipo de jogo deve ser carta, roleta ou slot."
    return True, tipo


def validar_aposta(aposta, min_val=0, max_val=1000000):
    try:
        aposta = float(aposta)
        if aposta < min_val:
            return False, f"Aposta não pode ser menor que {min_val}."
        if aposta > max_val:
            return False, f"Aposta não pode ser maior que {max_val}."
        return True, round(aposta, 2)
    except (ValueError, TypeError):
        return False, "Valor de aposta inválido."


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
