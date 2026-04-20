import os, re, json, time
from datetime import datetime

FICHEIRO = "jogadores.json"

BAN = [
    "pila", "puta", "merda", "foda-se", "caralho", "cona", "cabrão",
    "idiota", "imbecil", "estúpido", "burro", "vaca", "porra", "filho da puta",
    "viado", "cu", "prostituta", "fodasse", "besta", "treta", "lixo", "cretino",
    "mongol", "retardado", "palhaço", "chulo", "paneleiro"
]

jogadores = {}

# ══════════════════════════════════════════════════════════════════════════════
#  CORES  (ANSI)
# ══════════════════════════════════════════════════════════════════════════════

class C:
    RESET    = "\033[0m"
    BOLD     = "\033[1m"
    DIM      = "\033[2m"

    OURO     = "\033[38;5;220m"
    OURO2    = "\033[38;5;178m"
    CREME    = "\033[38;5;230m"
    VERDE    = "\033[38;5;40m"
    VERMELHO = "\033[38;5;160m"
    CINZA    = "\033[38;5;244m"
    CINZA2   = "\033[38;5;238m"
    ROXO     = "\033[38;5;135m"

    BG_VERDE    = "\033[48;5;22m"
    BG_VERMELHO = "\033[48;5;88m"
    BG_OURO     = "\033[48;5;136m"

    @staticmethod
    def pintar(texto, *estilos):
        return "".join(estilos) + texto + C.RESET


# ══════════════════════════════════════════════════════════════════════════════
#  UTILITÁRIOS DE TERMINAL
# ══════════════════════════════════════════════════════════════════════════════

W = 70

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def _strip_ansi(t):
    return re.sub(r'\033\[[^m]*m', '', t)

def _centro(texto, largura=W):
    pad = max(0, (largura - len(_strip_ansi(texto))) // 2)
    return " " * pad + texto

def linha_dupla(cor=C.OURO):
    print(C.pintar("═" * W, cor))

def linha_simples(cor=C.OURO2):
    print(C.pintar("─" * W, cor))

def linha_pontilhada(cor=C.CINZA2):
    print(C.pintar("· " * (W // 2), cor))

def espaco():
    print()


# ══════════════════════════════════════════════════════════════════════════════
#  COMPONENTES VISUAIS
# ══════════════════════════════════════════════════════════════════════════════

def cabecalho():
    limpar()
    espaco()
    linha_dupla()

    naipes = (C.pintar("  ♠  ", C.BOLD, C.CINZA) +
              C.pintar("♥  ", C.BOLD, C.VERMELHO) +
              C.pintar("♦  ", C.BOLD, C.VERMELHO) +
              C.pintar("♣  ", C.BOLD, C.CINZA))
    print(_centro(naipes))

    print(_centro(C.pintar("♜  ROYAL CASINO VIP  ♜", C.BOLD, C.OURO)))
    print(_centro(C.pintar("━━━━  Membros Exclusivos  ━━━━", C.OURO2)))
    print(_centro(naipes))

    linha_dupla()
    espaco()


def moldura(texto, cor_borda=C.OURO, cor_texto=C.CREME):
    inner = W - 2
    print(C.pintar("╔" + "═" * inner + "╗", cor_borda))
    visivel = texto.upper()
    pad_total = inner - len(visivel)
    pad_esq = pad_total // 2
    pad_dir = pad_total - pad_esq
    print(C.pintar("║", cor_borda) +
          " " * pad_esq +
          C.pintar(visivel, C.BOLD, cor_texto) +
          " " * pad_dir +
          C.pintar("║", cor_borda))
    print(C.pintar("╚" + "═" * inner + "╝", cor_borda))


def badge_rank(rank):
    if "HIGH ROLLER" in rank:
        return C.pintar(" ♛ HIGH ROLLER ", C.BOLD, C.BG_OURO, C.CREME)
    return C.pintar(" ♠ VIP ", C.BOLD, C.BG_VERDE, C.CREME)


def sucesso(msg):
    prefixo = C.pintar(" ✔ ", C.BOLD, C.BG_VERDE, C.CREME)
    print(prefixo + C.pintar(f" {msg}", C.BOLD, C.VERDE))

def erro(msg):
    prefixo = C.pintar(" ✖ ", C.BOLD, C.BG_VERMELHO, C.CREME)
    print(prefixo + C.pintar(f" {msg}", C.BOLD, C.VERMELHO))


def info(rotulo, valor, cor_val=C.CREME):
    """Linha:  Rótulo ············ Valor"""
    dots = W - len(rotulo) - len(_strip_ansi(valor)) - 6
    dots = max(3, dots)
    print(C.pintar(f"  {rotulo} ", C.CINZA) +
          C.pintar("·" * dots, C.CINZA2) +
          C.pintar(f" {valor}", C.BOLD, cor_val))


def animacao_loading(msg="A processar", duracao=0.8, passos=10):
    frames = ["◐", "◓", "◑", "◒"]
    for i in range(passos):
        frame = frames[i % len(frames)]
        print(C.pintar(f"\r  {frame}  {msg}...", C.OURO), end="", flush=True)
        time.sleep(duracao / passos)
    print("\r" + " " * (len(msg) + 14) + "\r", end="")


def tabela_cliente(id_vip, dados):
    espaco()
    linha_simples(C.CINZA2)
    print(C.pintar(f"  ◆ {id_vip}", C.BOLD, C.OURO))
    linha_pontilhada()
    info("Nome",   dados['nome'],             C.CREME)
    info("Idade",  f"{dados['idade']} anos",  C.CREME)
    info("Saldo",  f"{dados['saldo']:.2f} €", C.VERDE if dados['saldo'] >= 0 else C.VERMELHO)
    info("NIF",    dados['nif'],              C.CINZA)
    info("IBAN",   dados['iban'],             C.CINZA)
    info("Email",  dados['mail'],             C.ROXO)
    print(C.pintar("  Rank  ", C.CINZA) + "  " + badge_rank(dados['rank']))
    linha_simples(C.CINZA2)


def menu_opcao(num, texto):
    print(C.pintar(f"  [{num}]", C.BOLD, C.OURO) +
          C.pintar(f"  {texto}", C.OURO2))

def prompt(texto):
    return input(C.pintar(f"  ▶  {texto}: ", C.BOLD, C.OURO2))


# ══════════════════════════════════════════════════════════════════════════════
#  VALIDAÇÕES
# ══════════════════════════════════════════════════════════════════════════════

def ofensivo(t):
    return any(p in t.lower() for p in BAN)

def validar_nome_parte(valor, campo):
    valor = valor.strip()
    if not valor:
        return False, f"{campo} não pode estar vazio."
    if not re.fullmatch(r"[A-Za-zÀ-ÿ]+(-[A-Za-zÀ-ÿ]+)*", valor):
        return False, f"{campo} contém caracteres inválidos."
    valor = "-".join(part.capitalize() for part in valor.split("-"))
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

def validar_idade(data_str):
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


# ══════════════════════════════════════════════════════════════════════════════
#  PERSISTÊNCIA
# ══════════════════════════════════════════════════════════════════════════════

def guardar_dados():
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(jogadores, f, ensure_ascii=False, indent=2)

def carregar_dados():
    global jogadores
    if os.path.exists(FICHEIRO):
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            jogadores = json.load(f)
