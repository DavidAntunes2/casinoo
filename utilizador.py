from colorama import Fore, Style, init
from datetime import date
init(autoreset=True)
def calcular_idade(data_nascimento: date) -> int:
    hoje = date.today()
    return hoje.year - data_nascimento.year - (
            (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
    )
class Utilizador:
    def __init__(self):
        self.nome: str = ""
        self.data_nascimento: date = None
        self.nif: str = ""
        self.saldo: float = 0.0
        self.profissao: str = ""
        self.nacionalidade: str = ""
        self.contactos: list[str] = []
        self.email: str = ""
        self.conta: str = ""
    @property
    def idade(self) -> int:
        if self.data_nascimento:
            return calcular_idade(self.data_nascimento)
        return 0
    @property
    def maior_de_idade(self) -> bool:
        return self.idade >= 18
    def to_dict(self) -> dict:
        return {
            "Nome": self.nome,
            "Data de Nascimento": self.data_nascimento.strftime("%d/%m/%Y") if self.data_nascimento else "—",
            "Idade": self.idade,
            "NIF": self.nif,
            "Conta": self.conta,
            "Saldo": f"{self.saldo:.2f} €",
            "Profissão": self.profissao,
            "Nacionalidade": self.nacionalidade,
            "Contactos": self.contactos,
            "Email": self.email,
        }
    def mostrar(self):
        print(Fore.LIGHTBLUE_EX + "\n╔══════════════════════════════════════╗")
        print(Fore.LIGHTBLUE_EX + "║         DADOS DO UTILIZADOR          ║")
        print(Fore.LIGHTBLUE_EX + "╚══════════════════════════════════════╝")
        for chave, valor in self.to_dict().items():
            print(Fore.LIGHTWHITE_EX + f"  {chave}: " + Fore.LIGHTYELLOW_EX + f"{valor}")
    def __str__(self):
        return f"Utilizador({self.nome}, {self.idade} anos)"
def _input(prompt: str) -> str:
    return input(Fore.LIGHTYELLOW_EX + prompt + Style.RESET_ALL).strip()
def _ok(msg: str):
    print(Fore.LIGHTGREEN_EX + "  ✔ " + msg)
def _erro(msg: str):
    print(Fore.LIGHTRED_EX + "  ✘ " + msg)
def registar_utilizador() -> "Utilizador | None":
    """Fluxo interativo de registo. Devolve Utilizador ou None se menor de idade."""
    print(Fore.LIGHTBLUE_EX + "\n╔══════════════════════════════════════╗")
    print(Fore.LIGHTBLUE_EX + "║              REGISTO                 ║")
    print(Fore.LIGHTBLUE_EX + "╚══════════════════════════════════════╝\n")
    u = Utilizador()
    while True:
        nome = _input("Nome completo: ")
        if len(nome) >= 2:
            u.nome = nome
            _ok(f"Nome registado: {nome}")
            break
        _erro("O nome deve ter pelo menos 2 caracteres.")
    while True:
        raw = _input("Data de nascimento (DD/MM/AAAA): ")
        try:
            partes = raw.split("/")
            u.data_nascimento = date(int(partes[2]), int(partes[1]), int(partes[0]))
            break
        except (ValueError, IndexError):
            _erro("Formato inválido. Use DD/MM/AAAA.")
    if u.idade < 18:
        _erro(f"Tens {u.idade} anos — não podes registar-te (mínimo 18 anos).")
        _erro("Registo cancelado — és menor de idade.")
        return None
    if u.idade > 160:
        _erro(f"Tens {u.idade} anos — não podes registar-te (idade impossível).")
        _erro("Registo cancelado — idade inválida.")
        return None
    _ok(f"Tens {u.idade} anos — podes prosseguir.")
    while True:
        nif = _input("NIF (9 dígitos): ")
        if nif.isdigit() and len(nif) == 9:
            u.nif = nif
            _ok("NIF registado.")
            break
        _erro("NIF inválido — deve ter exactamente 9 dígitos numéricos.")
    u.conta = _input("Número de conta bancária (IBAN ou outro): ")
    _ok("Conta registada.")
    while True:
        raw = _input("Saldo inicial para depositar (€) sem € na tua resposta: ")
        try:
            saldo = float(raw.replace(",", "."))
            if saldo < 0:
                raise ValueError
            u.saldo = saldo
            _ok(f"Saldo: {saldo:.2f} €")
            break
        except ValueError:
            _erro(Fore.LIGHTRED_EX+"Insire um valor númerico sem € no final (o programa depois quando mostrar faz isso).")
    u.profissao = _input("Profissão: ")
    u.nacionalidade = _input("Nacionalidade: ")
    print(Fore.LIGHTCYAN_EX + "  Contactos (separa por espaço, ou deixa em branco):")
    raw = _input("  Contactos: ")
    u.contactos = raw.split() if raw else []
    while True:
        email = _input("Email: ")
        if "@" in email and "." in email:
            u.email = email
            _ok("Email registado.")
            break
        _erro("Email inválido.")
    u.mostrar()
    return u
