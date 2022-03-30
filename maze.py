from ast import Index
from ctypes import sizeof
from dataclasses import dataclass
import operator
import sys


class Maze(object):
    """on défini le labyrinthe"""

    def init(self):
        self.data = []

    def readFile(self, path):
        """On lit le fichier texte et on retourne une liste à deux dimensions. """
        maze = []
        with open(path) as ouvrir:
            for line in ouvrir.read().splitlines():
                maze.append(list(line))
        self.data = maze

    def writeFile(self, path):
    
        with open(path, 'w') as ouvrir:
            for x, line in enumerate(self.data):
                ouvrir.write('%s\n' % ''.join(line))

    def find(self, symbol):
        """on cherche le symbol."""
        for x, line in enumerate(self.data):
            try:
                return x, line.index('1')
            except ValueError:
                pass

    def get(self, where):
        """On retourne le symbol dans la cellule ou on l'a trouvé """
        x, c = where
        return self.data[x][c]

    def set(self, where, symbol):
        """Stock le symbol."""
        x, c = where
        self.data[x][c] = symbol



    def __str__(self):
        """On joint le tout"""
        return '\n'.join(''.join(x) for x in self.data)


def solutionMaze(maze, where=None, direction=None):
    """-On cherche le chemin à travers le labyrinthe.On commence par where et si where n'est pas fourni une cellule marquée 'S'et vise versa.
       -À chaque cellule, les quatre directions sont essayées dans l'ordre suivant
            Gauche, Haut, Droite, Bas.
       
       -Un symbole de direction nous indiques ou nous sommes.

       -si retour en arriére obligatoire le symbole ('.') est écrit."""
    SigneDebut = '1'
    SigneFin = '2'
    SigneVide = ' '
    SigneRetour = '.'
    directions = (1,0), (0, 1), (-1, 0), (0,-1)
    SigneDirection = '<', '^' , '>', 'v'

    where = where or maze.find(SigneDebut)
    if not where:
      
        return
    if maze.get(where) == SigneFin:
      
        return where
    if maze.get(where) not in (SigneVide, SigneDebut):
      
        return

    for direction in directions:
        try:
        
            suivant = list(map(operator.add, where, direction))
           
            marker = SigneDirection[directions.index(direction)]
            if maze.get(where) != SigneDebut:
                maze.set(where, marker)
            solve = solutionMaze(maze, suivant, direction)
            if solve:
               
                return solve
           
            maze.set(where, SigneRetour)
        except:
            print(" ")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print ('Arguments: input file output file')
        sys.exit(1)
    input_file, outputFile = sys.argv[1:3]

    maze = Maze()
    maze.readFile(input_file)

    solution = solutionMaze(maze)
    if solution:
        print ('Trouvé  %s' % solution)
        
    else:
        print ('pas trouvé')
    print (maze)
    maze.writeFile(outputFile)