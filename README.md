♜ Royal Casino VIP
Sistema de gestão de membros VIP para terminal, desenvolvido em Python.

Estrutura do Projeto
SRC/
├── main.py          # Ponto de entrada — todos os ecrãs e interação com o utilizador
├── utilizador.py    # Lógica de negócio — registo e consulta de clientes
└── utils.py         # Utilitários visuais, validações e persistência de dados

Funcionalidades

Registar novos clientes VIP com validação completa de dados
Listar todos os clientes com ficha detalhada e estatísticas gerais
Atribuição automática de rank (VIP ou HIGH ROLLER) com base no depósito
Persistência de dados em ficheiro JSON local
Interface visual rica no terminal com cores ANSI


Validações
CampoRegrasNomeSó letras e hífens, primeira letra maiúscula automáticaEmailFormato x@x.x, normalizado para minúsculasNIF9 dígitos, primeiro dígito válido, dígito de controlo (mod-11)IBANFormato PT + 23 dígitos, checksum mod-97IdadeEntre 18 e 116 anos, múltiplos formatos de data aceitesDepósitoNúmero positivo, vírgula ou ponto como separador decimalConteúdoFiltro de linguagem ofensiva em nomes e emails

Ranks
RankCondição♠ VIPDepósito inicial abaixo de 5000 €♛ HIGH ROLLERDepósito inicial igual ou superior a 5000 €

Formatos de Data Aceites
DD-MM-AAAA    →  15-06-1990
AAAA-MM-DD    →  1990-06-15
DD/MM/AAAA    →  15/06/1990

Como Executar
Requisitos: Python 3.8+
bashpython main.py

O terminal deve suportar cores ANSI. No Windows, o PowerShell e o terminal do PyCharm suportam nativamente.


Dados Guardados
Os clientes são guardados em jogadores.json na mesma pasta do projeto. O ficheiro é criado automaticamente no primeiro registo.
Exemplo de entrada:
json{
  "VIP-533J": {
    "nome": "João Silva",
    "idade": 34,
    "nif": "500963533",
    "iban": "PT50000201231234567890154",
    "saldo": 1500.0,
    "rank": "♠ VIP",
    "mail": "joao@mail.com"
  }
}
