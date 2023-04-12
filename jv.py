combinacoesVitoriosas = [
  [ 0, 1, 2 ], [3, 4, 5], [6, 7, 8], # Linhas 
  [ 0, 3, 6 ], [1, 4, 7], [2, 5, 8], # Colunas
  [ 0, 4, 8 ], [ 2, 4, 6 ] # Diagonais
]

jogadores = {
  1: [],
  2: []
}

jogadorAtual = 1

jogo = [
  "0️⃣", "1️⃣", "2️⃣",
  "3️⃣", "4️⃣", "5️⃣",
  "6️⃣", "7️⃣", "8️⃣"
]

def verificarVitoria(jogador):
  for combinacao in combinacoesVitoriosas:
    if all(jogada in jogadores[jogador] for jogada in combinacao):
      return True
  return False

def verificarEmpate():
  if len(jogadores[1]) + len(jogadores[2]) == 9:
    return True
  return False

def verificarJogada(jogada):
  while not jogada in range(0, 9):
    return True
  for jogador in jogadores:
    if jogada in jogadores[jogador]:
      return True
  return False

def imprimirJogo():
  i = 0;
  while i < len(jogo):
    print(jogo[i], jogo[i+1], jogo[i+2])
    i += 3

def atualizarJogo():
  jogo[jogada] = "❌" if jogadorAtual == 1 else "⭕"
  jogadores[jogadorAtual].append(jogada)

while True:
  imprimirJogo()

  jogada = int(input(f"Jogador {jogadorAtual} por favor faça sua jogada: "))
  while verificarJogada(jogada):
    jogada = int(input(f"Jogador {jogadorAtual} por favor faça uma jogada válida: "))

  atualizarJogo()

  if verificarVitoria(jogadorAtual):
    print()
    imprimirJogo()
    print(f"Parabéns jogador {jogadorAtual}, você venceu! 🎉🎉🎉")
    break;

  if verificarEmpate():
    print()
    imprimirJogo()
    print(f"Deu velha! Uma batalha feroz, até mesmo deu empate.")
    break;

  jogadorAtual = (3 - jogadorAtual)
  print()