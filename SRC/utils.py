# ==============================
# utils.py
# Geração de ID e validações
# para utilizador de casino
# ==============================

import re, uuid
from datetime import datetime

BAN = [
    "pila", "puta", "merda", "foda-se", "caralho", "cona", "cabrão",
    "idiota", "imbecil", "estúpido", "burro", "vaca", "porra", "filho da puta",
    "viado", "cu", "prostituta", "fodasse", "besta", "treta", "lixo", "cretino",
    "mongol", "retardado", "palhaço", "chulo", "paneleiro"
]


# ══════════════════════════════════════════════════════════════════════════════
#  GERAÇÃO DE ID
# ══════════════════════════════════════════════════════════════════════════════

def gerar_id_utilizador_casino():
    return "UC-" + str(uuid.uuid4())[:8].upper()


# ══════════════════════════════════════════════════════════════════════════════
#  VALIDAÇÕES
# ══════════════════════════════════════════════════════════════════════════════

def ofensivo(t):
    return any(p in t.lower() for p in BAN)


def validar_nome(nome):
    valor = nome.strip()
    if not valor:
        return False, "Nome não pode estar vazio."
    if ofensivo(valor):
        return False, "Nome contém linguagem ofensiva."
    if not re.fullmatch(r"[A-Za-zÀ-ÿ]+(-[A-Za-zÀ-ÿ]+)*(\s[A-Za-zÀ-ÿ]+(-[A-Za-zÀ-ÿ]+)*)*", valor):
        return False, "Nome contém caracteres inválidos."
    valor = " ".join(
        "-".join(part.capitalize() for part in palavra.split("-"))
        for palavra in valor.split()
    )
    return True, valor


def validar_email(mail):
    mail = mail.strip().lower()
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", mail):
        return False, "Email inválido."
    return True, mail


def validar_nif(nif):
    nif = nif.strip()
    if not re.fullmatch(r"\d{9}", nif):
        return False, "NIF deve ter exatamente 9 dígitos."
    if nif[0] not in "123456789":
        return False, "NIF inválido (primeiro dígito não permitido)."
    soma = sum(int(nif[i]) * (9 - i) for i in range(8))
    resto = soma % 11
    controlo = 0 if resto < 2 else 11 - resto
    if int(nif[8]) != controlo:
        return False, "NIF inválido (dígito de controlo incorreto)."
    return True, nif


def validar_iban(iban):
    iban = iban.strip().replace(" ", "").upper()
    if not re.fullmatch(r"PT\d{23}", iban):
        return False, "IBAN deve estar no formato PT seguido de 23 dígitos."
    reordenado = iban[4:] + iban[:4]
    numerico = "".join(str(ord(c) - 55) if c.isalpha() else c for c in reordenado)
    if int(numerico) % 97 != 1:
        return False, "IBAN inválido (checksum incorreto)."
    return True, iban


def validar_data_nascimento(data_str):
    for fmt in ("%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y"):
        try:
            nasc = datetime.strptime(data_str.strip(), fmt)
            hoje = datetime.now()
            idade = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
            if nasc > hoje:
                return False, "Data de nascimento no futuro."
            if idade > 116:
                return False, f"Idade inválida: {idade} anos (máximo 116)."
            if idade < 18:
                return False, f"Idade insuficiente: {idade} anos (mínimo 18)."
            return True, idade
        except ValueError:
            continue
    return False, "Data inválida. Use DD-MM-AAAA, AAAA-MM-DD ou DD/MM/AAAA."


def validar_tipo_conta(tipo):
    tipos_validos = ["standard", "vip", "high roller"]
    tipo = tipo.strip().lower()
    if tipo not in tipos_validos:
        return False, f"Tipo de conta inválido. Escolha: {', '.join(tipos_validos)}."
    return True, tipo
    def gerar_id_casino():
    return "CA-" + str(uuid.uuid4())[:8].upper()

def validar_localizacao(loc):
    loc = loc.strip()
    if not loc:
        return False, "Localização não pode estar vazia."
    return True, loc.title()

def validar_licenca(lic):
    lic = lic.strip().upper()
    if not lic:
        return False, "Licença não pode estar vazia."
    return True, lic

def validar_data(data_str):
    for fmt in ("%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y"):
        try:
            datetime.strptime(data_str.strip(), fmt)
            return True, data_str.strip()
        except ValueError:
            continue
    return False, "Data inválida. Use DD-MM-AAAA, AAAA-MM-DD ou DD/MM/AAAA."
