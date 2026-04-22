# ♠ Royal Casino — Sistema de Gestão

Sistema de gestão de um casino em Python, com menu de terminal interativo, validações e armazenamento em dicionário.

---

## 📁 Estrutura do Projeto

```
SRC/
├── main.py          # Menu terminal e interface com o utilizador
├── utilizador.py    # CRUD da entidade Utilizador de Casino
├── casino.py        # CRUD da entidade Casino
└── utils.py         # Geração de IDs e validações
```

---

## ▶️ Como Correr

```bash
python main.py
```

> Requer Python 3.8+. Não tem dependências externas.

---

## 🗺️ Navegação

```
Menu Principal
├── [1] Gestão de Utilizadores
│     ├── [1] Criar utilizador
│     ├── [2] Listar utilizadores
│     ├── [3] Consultar utilizador
│     ├── [4] Atualizar utilizador
│     ├── [5] Remover utilizador
│     └── [0] Voltar
├── [2] Gestão de Casinos
│     ├── [1] Criar casino
│     ├── [2] Listar casinos
│     ├── [3] Consultar casino
│     ├── [4] Atualizar casino
│     ├── [5] Remover casino
│     └── [0] Voltar
└── [0] Sair
```

---

## 👤 Utilizador de Casino (`utilizador.py`)

### Campos

```python
{
    "nome":             "João Silva",
    "email":            "joao@email.com",
    "tipo_conta":       "vip",            # standard | vip | high roller
    "data_nascimento":  "01-01-1990",
    "nif":              "123456789",
    "iban":             "PT50000201231234567890154"
}
```

### Funções

| Função                         | Descrição                         |
|--------------------------------|-----------------------------------|
| `criar_utilizador_casino()`    | Regista um novo membro            |
| `listar_utilizadores_casino()` | Lista todos os membros            |
| `consultar_utilizador_casino()`| Consulta um membro pelo ID        |
| `atualizar_utilizador_casino()`| Atualiza campos de um membro      |
| `remover_utilizador_casino()`  | Remove um membro                  |

---

## 🏛️ Casino (`casino.py`)

### Campos

```python
{
    "nome":             "Royal Lisboa",
    "localizacao":      "Lisboa",
    "licenca":          "PT-2024-001",
    "data_inauguracao": "01-01-2024"
}
```

### Funções

| Função               | Descrição                        |
|----------------------|----------------------------------|
| `criar_casino()`     | Regista um novo casino           |
| `listar_casinos()`   | Lista todos os casinos           |
| `consultar_casino()` | Consulta um casino pelo ID       |
| `atualizar_casino()` | Atualiza campos de um casino     |
| `remover_casino()`   | Remove um casino                 |

---

## ✅ Validações (`utils.py`)

### Utilizador

| Campo              | Regras                                                                |
|--------------------|-----------------------------------------------------------------------|
| `nome`             | Apenas letras e hífens, sem palavrões, capitalização automática       |
| `email`            | Formato `x@x.x`                                                       |
| `tipo_conta`       | Apenas `standard`, `vip` ou `high roller`                             |
| `data_nascimento`  | Formatos `DD-MM-AAAA`, `AAAA-MM-DD` ou `DD/MM/AAAA` — mínimo 18 anos |
| `nif`              | 9 dígitos com verificação do dígito de controlo                       |
| `iban`             | Formato `PT` + 23 dígitos com checksum mod 97                         |

### Casino

| Campo              | Regras                                                                |
|--------------------|-----------------------------------------------------------------------|
| `nome`             | Apenas letras e hífens, sem palavrões, capitalização automática       |
| `localizacao`      | Não pode estar vazio                                                  |
| `licenca`          | Não pode estar vazio, convertido para maiúsculas                      |
| `data_inauguracao` | Formatos `DD-MM-AAAA`, `AAAA-MM-DD` ou `DD/MM/AAAA`                  |

---

## 🔁 Códigos de Resposta

Todas as funções devolvem um tuplo `(código, resultado)`:

| Código | Significado            |
|--------|------------------------|
| `201`  | Criado com sucesso     |
| `200`  | Operação bem-sucedida  |
| `404`  | Registo não encontrado |
| `500`  | Erro de validação      |

---

## 🔑 Formato dos IDs

| Entidade   | Formato       | Exemplo       |
|------------|---------------|---------------|
| Utilizador | `UC-XXXXXXXX` | `UC-3F2A1B9C` |
| Casino     | `CA-XXXXXXXX` | `CA-7D4E2F1A` |
