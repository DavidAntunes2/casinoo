# ♠ Royal Casino — Sistema de Gestão (Completo)

Sistema de gestão completo de um casino em Python, com menu de terminal interativo, validações, armazenamento em dicionário e suporte a **Jogos** e **Transações**.

---

## 📁 Estrutura do Projeto
SRC/
├── main.py # Menu terminal e interface com o utilizador
├── utilizador.py # CRUD da entidade Utilizador de Casino
├── casino.py # CRUD da entidade Casino
├── jogo.py # CRUD da entidade Jogo
├── transacao.py # CRUD da entidade Transação
└── utils.py # Geração de IDs e validações

text

---

## ▶️ Como Correr

```bash
python main.py
Requer Python 3.8+. Não tem dependências externas.

🗺️ Navegação
text
Menu Principal
├── [1] Gestão de Utilizadores
│     ├── [1] Criar utilizador
│     ├── [2] Listar utilizadores
│     ├── [3] Consultar utilizador
│     ├── [4] Atualizar utilizador
│     ├── [5] Remover utilizador
│     └── [0] Voltar
│
├── [2] Gestão de Casinos
│     ├── [1] Criar casino
│     ├── [2] Listar casinos
│     ├── [3] Consultar casino
│     ├── [4] Atualizar casino
│     ├── [5] Remover casino
│     └── [0] Voltar
│
├── [3] Gestão de Jogos
│     ├── [1] Criar jogo
│     ├── [2] Listar jogos
│     ├── [3] Consultar jogo
│     ├── [4] Remover jogo
│     └── [0] Voltar
│
├── [4] Gestão de Transações
│     ├── [1] Criar transação
│     ├── [2] Listar transações
│     ├── [3] Consultar transação
│     ├── [4] Atualizar transação
│     ├── [5] Remover transação
│     └── [0] Voltar
│
└── [0] Sair
👤 Utilizador de Casino (utilizador.py)
Campos
python
{
    "nome":             "João Silva",
    "email":            "joao@email.com",
    "tipo_conta":       "vip",            # standard | vip | high roller
    "data_nascimento":  "01-01-1990",
    "nif":              "123456789",
    "iban":             "PT50000201231234567890154"
}
Funções
Função	Descrição	Códigos
criar_utilizador_casino()	Regista um novo membro	201 / 500
listar_utilizadores_casino()	Lista todos os membros	200 / 404
consultar_utilizador_casino()	Consulta um membro pelo ID	200 / 404
atualizar_utilizador_casino()	Atualiza campos de um membro	200 / 404/500
remover_utilizador_casino()	Remove um membro	200 / 404
🏛️ Casino (casino.py)
Campos
python
{
    "nome":             "Royal Lisboa",
    "localizacao":      "Lisboa",
    "licenca":          "PT-2024-001",
    "data_inauguracao": "01-01-2024",
    "saldo":            1000000.00
}
Funções
Função	Descrição	Códigos
criar_casino()	Regista um novo casino	201 / 500
listar_casinos()	Lista todos os casinos	200 / 404
consultar_casino()	Consulta um casino pelo ID	200 / 404
atualizar_casino()	Atualiza campos de um casino	200 / 404/500
remover_casino()	Remove um casino	200 / 404
🎮 Jogo (jogo.py)
Campos
python
{
    "id_jogo":          "JG-3F2A1B9C",
    "nome":             "Blackjack Vip",
    "tipo":             "carta",          # carta | roleta | slot
    "aposta_minima":    10.00,
    "aposta_maxima":    5000.00,
    "id_casino":        "CA-7D4E2F1A"
}
Funções
Função	Descrição	Códigos
criar_jogo()	Regista um novo jogo num casino	201 / 500
listar_jogos()	Lista todos os jogos	200 / 404
consultar_jogo()	Consulta um jogo pelo ID	200 / 404
atualizar_jogo()	Atualiza campos de um jogo	200 / 404/500
remover_jogo()	Remove um jogo	200 / 404
listar_jogos_por_casino()	Lista jogos de um casino específico	200 / 404
💰 Transação (transacao.py)
Campos
python
{
    "id_transacao":     "TR-2E4F6A8C",
    "id_utilizador":    "UC-3F2A1B9C",
    "id_casino":        "CA-7D4E2F1A",
    "tipo":             "deposito",       # deposito | levantamento
    "valor":            500.00,
    "data":             "15-04-2025"
}
Funções
Função	Descrição	Códigos
criar_transacao()	Regista um depósito ou levantamento	201 / 500
listar_transacoes()	Lista todas as transações	200 / 404
consultar_transacao()	Consulta uma transação pelo ID	200 / 404
atualizar_transacao()	Atualiza campos de uma transação	200 / 404/500
remover_transacao()	Remove uma transação	200 / 404
listar_transacoes_por_utilizador()	Lista transações de um utilizador	200 / 404
listar_transacoes_por_casino()	Lista transações de um casino	200 / 404
✅ Validações (utils.py)
Utilizador
Campo	Regras
nome	Apenas letras e hífens, sem palavrões, capitalização automática
email	Formato x@x.x
tipo_conta	Apenas standard, vip ou high roller
data_nascimento	Formatos DD-MM-AAAA, AAAA-MM-DD ou DD/MM/AAAA — mínimo 18 anos
nif	9 dígitos com verificação do dígito de controlo
iban	Formato PT + 23 dígitos com checksum mod 97
Casino
Campo	Regras
nome	Apenas letras e hífens, sem palavrões, capitalização automática
localizacao	Não pode estar vazio, mínimo 3 caracteres, máximo 200
licenca	Não pode estar vazio, mínimo 5 caracteres, máximo 50
data_inauguracao	Formatos DD-MM-AAAA, AAAA-MM-DD ou DD/MM/AAAA
saldo	Número ≥ 0, máximo 1.000.000.000, arredondado a 2 casas decimais
Jogo
Campo	Regras
nome	Capitalizado automaticamente, mínimo 2 caracteres
tipo	Apenas carta, roleta ou slot
aposta_minima	> 0
aposta_maxima	> aposta_minima
id_casino	Deve existir no sistema
Transação
Campo	Regras
id_utilizador	Deve existir no sistema
id_casino	Deve existir no sistema
tipo	Apenas deposito ou levantamento
valor	> 0, máximo 1.000.000
data	Formatos DD-MM-AAAA, AAAA-MM-DD ou DD/MM/AAAA — não pode ser futura
🔁 Códigos de Resposta
Todas as funções devolvem um tuplo (código, resultado):

Código	Significado
201	Criado com sucesso
200	Operação bem-sucedida
404	Registo não encontrado
500	Erro de validação
🔑 Formato dos IDs
Entidade	Formato	Exemplo
Utilizador	UC-XXXXXXXX	UC-3F2A1B9C
Casino	CA-XXXXXXXX	CA-7D4E2F1A
Jogo	JG-XXXXXXXX	JG-8A3B5C7D
Transação	TR-XXXXXXXX	TR-2E4F6A8C
🎨 Cores no Terminal
Cor	Utilização
🟡 Dourado	Menus principais e bordas
🟢 Verde	Sucesso, depósitos e saldos
🔴 Vermelho	Erros, remoções e levantamentos
🔵 Azul	Gestão de casinos
🟣 Roxo	Emails e licenças
🟠 Laranja	Menus secundários
⚪ Cinza	Informações secundárias
📊 Exemplos de Uso
Criar um Jogo
python
criar_jogo("Blackjack VIP", "carta", 10.0, 5000.0, "CA-7D4E2F1A")
# (201, {
#   "id_jogo": "JG-3F2A1B9C",
#   "nome": "Blackjack Vip",
#   "tipo": "carta",
#   "aposta_minima": 10.0,
#   "aposta_maxima": 5000.0,
#   "id_casino": "CA-7D4E2F1A"
# })
Criar uma Transação
python
criar_transacao("UC-3F2A1B9C", "deposito", 500.0, "15-04-2025", "CA-7D4E2F1A")
# (201, {
#   "id_transacao": "TR-7D4E2F1A",
#   "id_utilizador": "UC-3F2A1B9C",
#   "id_casino": "CA-7D4E2F1A",
#   "tipo": "deposito",
#   "valor": 500.0,
#   "data": "15-04-2025"
# })
📦 Dependências
Python 3.8+ standard library

Módulos: os, time, re, uuid, datetime, random, string

👨‍💻 Autor
Sistema completo desenvolvido para gestão de casinos, membros, jogos e transações financeiras.

📄 Licença
Uso académico / educacional.

text

---

## 📊 **Resumo dos Dois READMEs**

| Característica | README Base | README Completo |
|----------------|-------------|-----------------|
| **Entidades** | Utilizador, Casino | Utilizador, Casino, Jogo, Transação |
| **Ficheiros** | 4 ficheiros | 6 ficheiros |
| **Campo saldo** | ✅ Sim | ✅ Sim |
| **Relação com Casino** | ❌ Não | ✅ Sim (Jogo e Transação têm id_casino) |
| **Formato IDs** | UC-XXX, CA-XXX | UC-XXX, CA-XXX, JG-XXX, TR-XXX |
| **Opções menu** | 2 principais + submenus | 4 principais + submenus |
| **Validações** | 10 regras | 16 regras |
| **Funções totais** | 10 | 20+ |
| **Exemplos de código** | ❌ | ✅ Sim |
| **Listagens por relação** | ❌ | ✅ Sim |

Agora estão **completamente separados** e fáceis de distinguir! 🚀
