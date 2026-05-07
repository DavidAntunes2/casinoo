# ♠ Royal Casino — Sistema de Gestão

Sistema de gestão de casino em Python com interface de terminal interativa,
validações completas e armazenamento em memória.

---

## 📁 Estrutura do Projeto
SRC/
├── main.py          # Interface de terminal e navegação
├── utilizador.py    # CRUD da entidade Utilizador
├── casino.py        # CRUD da entidade Casino
├── jogo.py          # CRUD da entidade Jogo
├── transacao.py     # CRUD da entidade Transação
└── utils.py         # Validações e geração de IDs

---

## ▶️ Como Correr

```bash
python main.py
```

> Requer Python 3.8+. Sem dependências externas.

---

## 🗺️ Navegação
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
│     ├── [4] Atualizar jogo
│     ├── [5] Remover jogo
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

---

## 📦 Entidades

### 👤 Utilizador
```python
{
    "id_utilizador":   "UC-3F2A1B9C",
    "nome":            "João Silva",
    "email":           "joao@email.com",
    "tipo_conta":      "vip",           # standard | vip | high roller
    "data_nascimento": "01-01-1990",
    "nif":             "123456789",
    "iban":            "PT50000201231234567890154"
}
```

| Função | Descrição | Códigos |
|---|---|---|
| `criar_utilizador_casino()` | Regista um novo membro | 201 / 500 |
| `listar_utilizadores_casino()` | Lista todos os membros | 200 / 404 |
| `consultar_utilizador_casino()` | Consulta um membro pelo ID | 200 / 404 |
| `atualizar_utilizador_casino()` | Atualiza campos de um membro | 200 / 404 / 500 |
| `remover_utilizador_casino()` | Remove um membro | 200 / 404 |

### 🏛️ Casino
```python
{
    "id_casino":        "CA-7D4E2F1A",
    "nome":             "Royal Lisboa",
    "localizacao":      "Lisboa, Portugal",
    "licenca":          "PT-2024-001",
    "data_inauguracao": "01-01-2024",
    "saldo":            1000000.00
}
```

### 🎮 Jogo
```python
{
    "id_jogo":       "JG-8A3B5C7D",
    "nome":          "Blackjack Vip",
    "tipo":          "carta",          # carta | roleta | slot
    "aposta_minima": 10.00,
    "aposta_maxima": 5000.00,
    "id_casino":     "CA-7D4E2F1A"
}
```

### 💰 Transação
```python
{
    "id_transacao":  "TR-2E4F6A8C",
    "id_utilizador": "UC-3F2A1B9C",
    "id_casino":     "CA-7D4E2F1A",
    "tipo":          "deposito",       # deposito | levantamento
    "valor":         500.00,
    "data":          "15-04-2025"
}
```

---

## ✅ Validações

### Utilizador
| Campo | Regras |
|---|---|
| `nome` | Mínimo 2 caracteres, máximo 100 |
| `email` | Formato válido `x@x.x` |
| `tipo_conta` | `standard`, `vip` ou `high roller` |
| `data_nascimento` | Formato DD-MM-AAAA — mínimo 18 anos |
| `nif` | Exatamente 9 dígitos |
| `iban` | Formato PT + 23 dígitos |

### Casino
| Campo | Regras |
|---|---|
| `nome` | Mínimo 2 caracteres, máximo 100 |
| `localizacao` | Mínimo 3 caracteres, máximo 200 |
| `licenca` | Mínimo 5 caracteres, máximo 50 |
| `data_inauguracao` | Formato DD-MM-AAAA |
| `saldo` | Número ≥ 0, máximo 1 000 000 000 |

### Jogo
| Campo | Regras |
|---|---|
| `nome` | Mínimo 2 caracteres, capitalizado automaticamente |
| `tipo` | `carta`, `roleta` ou `slot` |
| `aposta_minima` | Maior que 0 |
| `aposta_maxima` | Maior que `aposta_minima` |
| `id_casino` | Deve existir no sistema |

### Transação
| Campo | Regras |
|---|---|
| `id_utilizador` | Deve existir no sistema |
| `id_casino` | Deve existir no sistema |
| `tipo` | `deposito` ou `levantamento` |
| `valor` | Maior que 0, máximo 1 000 000 |
| `data` | Formato DD-MM-AAAA, não pode ser futura |

---

## 🔁 Códigos de Resposta

Todas as funções devolvem um tuplo `(código, resultado)`:

| Código | Significado |
|---|---|
| `201` | Criado com sucesso |
| `200` | Operação bem-sucedida |
| `404` | Registo não encontrado |
| `500` | Erro de validação |

---

## 🔑 Formato dos IDs

| Entidade | Formato | Exemplo |
|---|---|---|
| Utilizador | `UC-XXXXXXXX` | `UC-3F2A1B9C` |
| Casino | `CA-XXXXXXXX` | `CA-7D4E2F1A` |
| Jogo | `JG-XXXXXXXX` | `JG-8A3B5C7D` |
| Transação | `TR-XXXXXXXX` | `TR-2E4F6A8C` |

---

## 📊 Exemplos de Uso

```python
# Criar um casino
criar_casino("Royal Lisboa", "Lisboa, Portugal", "PT-2024-001", "01-01-2024", 1000000)
# → (201, {"id_casino": "CA-7D4E2F1A", "nome": "Royal Lisboa", ...})

# Criar um jogo
criar_jogo("Blackjack VIP", "carta", 10.0, 5000.0, "CA-7D4E2F1A")
# → (201, {"id_jogo": "JG-3F2A1B9C", "nome": "Blackjack Vip", ...})

# Criar uma transação
criar_transacao("UC-3F2A1B9C", "deposito", 500.0, "15-04-2025", "CA-7D4E2F1A")
# → (201, {"id_transacao": "TR-7D4E2F1A", "tipo": "deposito", "valor": 500.0, ...})
```

---

## 🐍 Dependências

Python 3.8+ — apenas módulos da biblioteca padrão: `os` `time` `re` `datetime` `random` `string`

---

## 📄 Licença

Uso académico / educacional.
