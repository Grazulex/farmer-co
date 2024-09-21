import pygame
import sys
from pygame.locals import *
from config import *
from game import Game

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()

# Initialisation de la fenêtre du jeu avant de charger des images
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

# Charger la musique de fond
pygame.mixer.music.load(MUSIC)
pygame.mixer.music.play(-1)

def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()

pygame.quit()
sys.exit()
