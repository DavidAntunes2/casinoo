# casino
utilizador.py — O coração dos dados
É aqui que o jogador "existe". A classe Utilizador é um contentor de dados — guarda nome, NIF, saldo, contactos, etc., tudo em memória RAM enquanto o programa corre. A propriedade idade é calculada automaticamente a partir da data_nascimento sempre que é acedida, sem ser guardada. A função registar_utilizador() é o único sítio onde um Utilizador é criado — valida cada campo antes de o aceitar e recusa o registo se o utilizador for menor de 18 anos.

casino.py — A lógica dos jogos
A classe Casino guarda apenas informação estática sobre o próprio casino (nome, país, patrocínios). Os jogos jogar_quiz e jogar_slots não guardam nada — recebem o objeto Utilizador e mexem diretamente no utilizador.saldo, somando ganhos e subtraindo perdas em tempo real. As perguntas do quiz estão definidas numa lista de dicionários PERGUNTAS_FUTEBOL no topo do ficheiro — cada pergunta tem opções, resposta certa, prémio e multa em percentagem.

utilizador.py (segunda versão / atualizada) — Igual mas com mensagem de erro melhorada
É a versão mais recente do mesmo ficheiro, com uma pequena diferença na mensagem de erro do saldo inicial — mais descritiva para o utilizador. O funcionamento é idêntico.

main.py — O maestro
Não guarda nem processa dados — apenas orquestra tudo. Cria o Casino, chama o registo, recebe o Utilizador devolvido e passa-o para o menu_jogos. O menu é um loop infinito que só termina quando o jogador escolhe sair. O fluxo é sempre linear:
Apresentar Casino
       ↓
Registar Utilizador  ──(menor de idade)──► Termina
       ↓
Menu de Jogos
  ├── Quiz      → altera saldo
  ├── Slots     → altera saldo
  ├── Ver dados → só leitura
  └── Sair      → termina
O único objeto que "viaja" por todo o programa é o Utilizador — nasce no utilizador.py, é entregue ao main.py, e é emprestado ao casino.py sempre que há um jogo.
