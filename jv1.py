# Definição da matriz e mostruário de inicio de jogo
jogodavelha = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(033[1mJogo da Velha)
print(jogodavelha[0])
print(jogodavelha[1])
print(jogodavelha[2])
print()

# Jogadas
jogada1 = int(input(Jogador 1nQual posição você vai jogar))

# Jogador 1
for linha in range(len(jogodavelha))
    for coluna in range(len(jogodavelha[linha]))
      if jogodavelha[linha][coluna] == jogada1
        jogodavelha[linha][coluna] = str('X')
        print(jogodavelha[0])
        print(jogodavelha[1])
        print(jogodavelha[2])
        break