# ♠ Royal Casino — Sistema de Gestão

Sistema de gestão de casino em Python com interface de terminal interativa,
validações completas e armazenamento em memória.

---

## 📁 Estrutura do Projeto
SRC/
├── main.py          # Interface de terminal e navegação
├── utilizador.py    # CRUD da entidade Utilizador
├── casino.py        # CRUD da entidade Casino
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
└── [0] Sair

---

## 📦 Entidades

### 👤 Utilizador
```python
{
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
    "nome":             "Royal Lisboa",
    "localizacao":      "Lisboa, Portugal",
    "licenca":          "PT-2024-001",
    "data_inauguracao": "01-01-2024",
    "saldo":            1000000.00
}
```

| Função | Descrição | Códigos |
|---|---|---|
| `criar_casino()` | Regista um novo casino | 201 / 500 |
| `listar_casinos()` | Lista todos os casinos | 200 / 404 |
| `consultar_casino()` | Consulta um casino pelo ID | 200 / 404 |
| `atualizar_casino()` | Atualiza campos de um casino | 200 / 404 / 500 |
| `remover_casino()` | Remove um casino | 200 / 404 |

---

## ✅ Validações

### Utilizador
| Campo | Regras |
|---|---|
| `nome` | Apenas letras e hífens, sem palavrões, capitalização automática |
| `email` | Formato válido `x@x.x` |
| `tipo_conta` | `standard`, `vip` ou `high roller` |
| `data_nascimento` | Formatos DD-MM-AAAA, AAAA-MM-DD ou DD/MM/AAAA — mínimo 18 anos |
| `nif` | 9 dígitos com verificação do dígito de controlo |
| `iban` | Formato PT + 23 dígitos com checksum mod 97 |

### Casino
| Campo | Regras |
|---|---|
| `nome` | Apenas letras e hífens, sem palavrões, capitalização automática |
| `localizacao` | Mínimo 3 caracteres, máximo 200 |
| `licenca` | Mínimo 5 caracteres, máximo 50 |
| `data_inauguracao` | Formatos DD-MM-AAAA, AAAA-MM-DD ou DD/MM/AAAA |
| `saldo` | Número ≥ 0, máximo 1 000 000 000, arredondado a 2 casas decimais |

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

---

## 🎨 Cores no Terminal

| Cor | Utilização |
|---|---|
| 🟡 Dourado | Menus principais e bordas |
| 🟢 Verde | Sucesso e saldos positivos |
| 🔴 Vermelho | Erros e remoções |
| 🔵 Azul | Gestão de casinos |
| 🟣 Roxo | Emails e licenças |
| ⚪ Cinza | Informações secundárias |

---

## 🐍 Dependências

Python 3.8+ — apenas módulos da biblioteca padrão: `os` `time` `re` `uuid` `datetime`

---

## 📄 Licença

Uso académico / educacional.
