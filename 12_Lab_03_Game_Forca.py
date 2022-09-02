# PROJETO HANGMAN
# Importando Biblioteca
import random
from re import A

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


# Buscar Palavra
with open('Arquivos/palavras.txt', "r") as arquivo:
    lista = arquivo.read().split('\n')

palavra = random.choice(lista)


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
        if letra in self.palavra:
            self.letra_correta.append(letra)
                        
        elif letra not in self.palavra:
            self.letra_errada.append(letra)
        else:
            return False
            
    # Status
    def game_status (self):
        print(board[len(self.letra_errada)])
        print(f'\nPalavra: {self.palavra_oculta()}')
        print(f'\nLetras Corretas: {self.letra_correta}')
        print(f'Letras Erradas: {self.letra_errada}')

    def player_status(self):
        if len(self.letra_correta) == len(self.palavra):
            print('Parabens. Voce Ganhou!')
        elif len(self.letra_errada) == 6:
            print('Infelizmente não foi dessa vez, tente novamente!')
        else:
            return False

# Main
# Chamar Classe
game = Hangman(palavra)
game.letra_errada.clear()
game.letra_correta.clear()
while len(game.letra_correta) < len(game.palavra) and len(game.letra_errada) < 6:
    game.game_status()
    game.letra(input('Insira uma Letra: '))
else:
    game.game_status()
    game.player_status()

