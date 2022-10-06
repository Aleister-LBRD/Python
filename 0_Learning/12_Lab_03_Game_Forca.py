# PROJETO HANGMAN
# Importando Biblioteca
import random

# Desenhando Board
board = [
'''
>>>>>>> HANGMAN <<<<<<<

 +---+
 |   |
 |   
 |   
 |   
========
''',
'''
>>>>>>> HANGMAN <<<<<<<

 +---+
 |   |
 |   O
 |  
 |   
========
''',
'''
>>>>>>> HANGMAN <<<<<<<

 +---+
 |   |
 |   O
 |   | 
 |   
========
''',
'''
>>>>>>> HANGMAN <<<<<<<

 +---+
 |   |
 |   O
 |  /| 
 |   
========
''',
'''
>>>>>>> HANGMAN <<<<<<<

 +---+
 |   |
 |   O
 |  /|\ 
 |   
========
''',
'''
>>>>>>> HANGMAN <<<<<<<

 +---+
 |   |
 |   O
 |  /|\ 
 |  /  
========
''',
'''
>>>>>>> HANGMAN <<<<<<<

 +---+
 |   |
 |   O
 |  /|\ 
 |  / \ 
========
''']


# Classe
class Hangman():

    # Construtor
    def __init__(self,palavra):
        self.palavra = palavra
        self.letra_correta = []
        self.letra_errada = []

    # Ocultar Palavra
    def palavra_oculta(self):
        oculto = ''
        for i in self.palavra:
            if i in self.letra_correta:
                oculto += i + " "
            else:
                oculto += '_ '
        return oculto

    # Letra
    def letra (self, letra):
        if letra in self.palavra and letra not in self.letra_correta:
            self.letra_correta.append(letra)
        elif letra not in self.palavra and letra not in self.letra_errada:
            self.letra_errada.append(letra)
        else:
            return False
            
    # Status do Game
    def game_status (self):
        print(board[len(self.letra_errada)])
        print(f'\nPalavra: {self.palavra_oculta()}')
        print(f'\nLetras Corretas: {self.letra_correta}')
        print(f'Letras Erradas: {self.letra_errada}')

    # Status do Player
    def player_status(self):
        if len(self.letra_correta) == len(self.palavra):
            print('\nParabens. Voce Ganhou!')
        elif len(self.letra_errada) == 6:
            print('\nInfelizmente não foi dessa vez, tente novamente!')
            print(f'\nA palavra era: "{self.palavra}"')
        else:
            return False

# Buscar Palavra
with open('Arquivos/palavras.txt', "r") as arquivo:
    lista = arquivo.read().split('\n')

palavra = random.choice(lista)

# Main - Compilacao das funcoes
def main():
# Chamar Classe
    game = Hangman(palavra)
# Funcao Principal
    while len(game.letra_correta) < len(game.palavra) and len(game.letra_errada) < 6:
        game.game_status()
        game.letra(input('Insira uma Letra: '))
    else:
        game.game_status()
        game.player_status()

# Executa o Programa
if __name__ == '__main__':
    main()