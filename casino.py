import random
from colorama import Fore, Style, init
from utilizador import Utilizador

init(autoreset=True)

PATROCINIOS = {
    "Oreo": "Redonda como uma bola de futebol",
    "Monster": "Liberta a besta!!!",
}

PERGUNTAS_FUTEBOL = [
    {
        "pergunta": "Quantos títulos da Liga dos Campeões tem o Benfica?",
        "opcoes": ["1", "2", "3", "4"],
        "resposta": "2",
        "premio": 200,
        "multa": 100,
    },
    {
        "pergunta": "Qual clube português ganhou a Taça UEFA em 2003?",
        "opcoes": ["Benfica", "Sporting", "Porto", "Braga"],
        "resposta": "Porto",
        "premio": 300,
        "multa": 150,
    },
    {
        "pergunta": "Quem é o melhor marcador de sempre da Seleção Portuguesa?",
        "opcoes": ["Luís Figo", "Eusébio", "Cristiano Ronaldo", "Pauleta"],
        "resposta": "Cristiano Ronaldo",
        "premio": 150,
        "multa": 75,
    },
    {
        "pergunta": "Em que ano Portugal ganhou o Euro?",
        "opcoes": ["2012", "2016", "2018", "2020"],
        "resposta": "2016",
        "premio": 250,
        "multa": 125,
    },
]


def _input(prompt: str) -> str:
    return input(Fore.LIGHTYELLOW_EX + prompt + Style.RESET_ALL).strip()


def _ok(msg: str):
    print(Fore.LIGHTGREEN_EX + "  ✔ " + msg)


def _erro(msg: str):
    print(Fore.LIGHTRED_EX + "  ✘ " + msg)


def _linha():
    print(Fore.LIGHTBLUE_EX + "  ─────────────────────────────────────")


class Casino:
    def __init__(self):
        self.nome: str = "Casino Datson"
        self.online: bool = True
        self.plataforma: str = "Web / Mobile"
        self.pais: str = "Portugal"
        self.patrocinios: dict = PATROCINIOS
        self.data_registo: str = "19/07/2010"
        self.tipo_jogador: str = "Adulto (+18)"

    def apresentar(self):
        print(Fore.LIGHTBLUE_EX + "\n╔══════════════════════════════════════╗")
        print(Fore.LIGHTBLUE_EX + f"║        {self.nome:<30}║")
        print(Fore.LIGHTBLUE_EX + "╚══════════════════════════════════════╝")
        print(Fore.LIGHTWHITE_EX + f"  País           : {self.pais}")
        print(Fore.LIGHTWHITE_EX + f"  Online         : {'Sim' if self.online else 'Não'}")
        print(Fore.LIGHTWHITE_EX + f"  Plataforma     : {self.plataforma}")
        print(Fore.LIGHTWHITE_EX + f"  Registado em   : {self.data_registo}")
        print(Fore.LIGHTWHITE_EX + f"  Tipo de jogador: {self.tipo_jogador}")
        print(Fore.LIGHTWHITE_EX + "  Patrocínios    :")
        for marca, slogan in self.patrocinios.items():
            print(Fore.LIGHTCYAN_EX + f"    • {marca}: " + Fore.WHITE + slogan)

    # ──────────────────────────────────────────
    #  Jogo principal: Quiz de Futebol
    # ──────────────────────────────────────────

    def jogar_quiz(self, utilizador: Utilizador):
        print(Fore.LIGHTBLUE_EX + "\n╔══════════════════════════════════════╗")
        print(Fore.LIGHTBLUE_EX + "║         QUIZ DE FUTEBOL 🏆           ║")
        print(Fore.LIGHTBLUE_EX + "╚══════════════════════════════════════╝")
        print(Fore.LIGHTWHITE_EX + f"  Jogador: {utilizador.nome}")
        print(Fore.LIGHTWHITE_EX + f"  Saldo actual: {utilizador.saldo:.2f} €\n")

        perguntas = random.sample(PERGUNTAS_FUTEBOL, k=min(3, len(PERGUNTAS_FUTEBOL)))
        pontuacao = 0

        for i, q in enumerate(perguntas, 1):
            _linha()
            print(Fore.LIGHTCYAN_EX + f"  Pergunta {i}/{len(perguntas)}: {q['pergunta']}")
            for letra, opcao in zip("ABCD", q["opcoes"]):
                print(Fore.WHITE + f"    {letra}) {opcao}")

            # ── Aposta ────────────────────────
            while True:
                raw = _input(f"  Quanto quer apostar? (saldo: {utilizador.saldo:.2f} €): ")
                try:
                    aposta = float(raw.replace(",", "."))
                    if aposta <= 0:
                        raise ValueError
                    if aposta > utilizador.saldo:
                        _erro("Saldo insuficiente.")
                        continue
                    break
                except ValueError:
                    _erro("Valor inválido.")

            # ── Resposta ──────────────────────
            resp = _input("  A sua resposta (A/B/C/D ou texto): ").upper()

            # aceita letra ou texto directo
            if len(resp) == 1 and resp in "ABCD":
                idx = ord(resp) - ord("A")
                resp_texto = q["opcoes"][idx] if idx < len(q["opcoes"]) else resp
            else:
                resp_texto = resp.title()

            if resp_texto.lower() == q["resposta"].lower():
                ganho = aposta * (q["premio"] / 100)
                utilizador.saldo += ganho
                pontuacao += 1
                _ok(f"Correcto! +{ganho:.2f} € → saldo: {utilizador.saldo:.2f} €")
            else:
                perda = aposta * (q["multa"] / 100)
                utilizador.saldo -= perda
                _erro(f"Errado! A resposta era '{q['resposta']}'. -{perda:.2f} € → saldo: {utilizador.saldo:.2f} €")

                if utilizador.saldo <= 0:
                    utilizador.saldo = 0
                    _erro("Ficaste sem saldo! O jogo termina aqui.")
                    break

        _linha()
        print(Fore.LIGHTCYAN_EX + f"\n  Resultado final: {pontuacao}/{len(perguntas)} respostas correctas")
        print(Fore.LIGHTWHITE_EX + f"  Saldo final: {utilizador.saldo:.2f} €")

    # ──────────────────────────────────────────
    #  Jogo extra: Slots simples
    # ──────────────────────────────────────────

    def jogar_slots(self, utilizador: Utilizador):
        SIMBOLOS = ["🍒", "🍋", "🔔", "⭐", "7️⃣ "]

        print(Fore.LIGHTBLUE_EX + "\n╔══════════════════════════════════════╗")
        print(Fore.LIGHTBLUE_EX + "║              SLOT MACHINE              ║")
        print(Fore.LIGHTBLUE_EX + "╚══════════════════════════════════════╝")
        print(Fore.LIGHTWHITE_EX + f"  Jogador: {utilizador.nome}  |  Saldo: {utilizador.saldo:.2f} €\n")

        while True:
            if utilizador.saldo <= 0:
                _erro("Sem saldo. Não é possível continuar.")
                break

            raw = _input(f"  Aposta (saldo: {utilizador.saldo:.2f} €) ou 's' para sair: ")
            if raw.lower() == "s":
                break
            try:
                aposta = float(raw.replace(",", "."))
                if aposta <= 0 or aposta > utilizador.saldo:
                    raise ValueError
            except ValueError:
                _erro("Aposta inválida.")
                continue
            rodas = [random.choice(SIMBOLOS) for _ in range(3)]
            print(Fore.LIGHTCYAN_EX + "  [ " + "  |  ".join(rodas) + " ]")
            if rodas[0] == rodas[1] == rodas[2]:
                ganho = aposta * 3
                utilizador.saldo += ganho
                _ok(f"JACKPOT! +{ganho:.2f} € → {utilizador.saldo:.2f} €")
            elif rodas[0] == rodas[1] or rodas[1] == rodas[2]:
                ganho = aposta * 0.5
                utilizador.saldo += ganho
                _ok(f"Par! +{ganho:.2f} € → {utilizador.saldo:.2f} €")
            else:
                utilizador.saldo -= aposta
                _erro(f"Perdeste {aposta:.2f} € → {utilizador.saldo:.2f} €")

        print(Fore.LIGHTWHITE_EX + f"\n  Saldo ao sair das slots: {utilizador.saldo:.2f} €")