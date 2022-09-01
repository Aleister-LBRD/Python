# HANGMAN

# Criando Board
print('>>>>>>>HANGMAN<<<<<<<')
board = [" +---+ \n |   | \n |     \n |      \n |      \n======= ", " +---+ \n |   | \n |   O \n |      \n |      \n======= ", " +---+ \n |   | \n |   O \n |   |  \n |      \n======= ", " +---+ \n |   | \n |   O \n |  /|  \n |      \n======= ", " +---+ \n |   | \n |   O \n |  /|\ \n |      \n======= ", " +---+ \n |   | \n |   O \n |  /|\ \n |  /   \n======= ", " +---+ \n |   | \n |   O \n |  /|\ \n |  / \ \n======= "]

import random

# Class
class Hangman:

    # Metodo Construtor
    def __init__(self,word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []

    # Metodo para adivinhar a letra
    def guess(self, letter):



    # Metodo para verificar se o jogo terminou
    def hangman_over(self):


    # Metodos para verificar se o jogador venceu
    def hangman_won(self):


    # Metodo para nao mostrar a letra no board
    def hide_word(self):


    # Metodo para checar o status do game e imprimir o board na tela
    def game_satus(self):


# Funcao para ler uma palavra de forma aleatoria no banco de palavras
def rand_word():
    with open("Arquivos/palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()

# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman (rand_word())

    #Enquanto o jogo nao terminar, print do status, solicita uma letra e faz a leitura do carcter
    #verifica o status do jogo
    game.game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print ('\nParabens, voce venceu!')
    else:
        print('\nGame Over, voce perdeu!')
        print('A palavra era ' + game.word)
    print ('\nFoi bom jogar com voce!')

# Executa o programa
if __game__== "__main__":
    main()

