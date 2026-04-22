♠ Royal Casino — Gestão de Membros
Sistema de gestão de utilizadores de casino em Python, com menu de terminal interativo, validações e armazenamento em dicionário.

📁 Estrutura do Projeto
SRC/
├── main.py          # Menu terminal e interface com o utilizador
├── utilizador.py    # CRUD da entidade Utilizador de Casino
└── utils.py         # Geração de IDs e validações

▶️ Como Correr
bashpython main.py

Requer Python 3.8+. Não tem dependências externas.


⚙️ Funcionalidades
OpçãoOperaçãoDescrição1Criar utilizadorRegista um novo membro com validações2Listar utilizadoresMostra todos os membros registados3Consultar utilizadorPesquisa um membro pelo ID4Atualizar utilizadorEdita campos de um membro existente5Remover utilizadorElimina um membro (pede confirmação)0SairEncerra o programa

🗂️ Estrutura de um Utilizador
python{
    "nome":             "João Silva",
    "email":            "joao@email.com",
    "tipo_conta":       "vip",           # standard | vip | high roller
    "data_nascimento":  "01-01-1990",
    "nif":              "123456789",
    "iban":             "PT50000201231234567890154"
}

✅ Validações
Todas as validações estão em utils.py e são chamadas antes de qualquer escrita no dicionário.
CampoRegrasnomeApenas letras e hífens, sem palavrões, capitalização automáticaemailFormato x@x.xtipo_contaApenas standard, vip ou high rollerdata_nascimentoFormatos DD-MM-AAAA, AAAA-MM-DD ou DD/MM/AAAA — mínimo 18 anosnif9 dígitos com verificação do dígito de controloibanFormato PT + 23 dígitos com checksum mod 97

🔁 Códigos de Resposta
Todas as funções de utilizador.py devolvem um tuplo (código, resultado):
CódigoSignificado201Criado com sucesso200Operação bem-sucedida404Utilizador não encontrado500Erro de validação

📋 Exemplo de Uso
===== MENU UTILIZADOR CASINO =====
[1]  Criar utilizador
[2]  Listar utilizadores
[3]  Consultar utilizador
[4]  Atualizar utilizador
[5]  Remover utilizador
[0]  Sair

▶  Opção: 1

▶  Nome completo: João Silva
▶  Email: joao@email.com
▶  Tipo de conta: vip
▶  Data nascimento: 01-01-1990
▶  NIF: 123456789
▶  IBAN: PT50000201231234567890154

 ✔  Membro registado com sucesso!
