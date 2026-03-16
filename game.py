import sys
import pygame
from blocks import *
from grid import Grid
from tetris import Tetris


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.ablak: pygame.Surface = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Tetris")
        self.sötétkék: tuple[int ,int ,int] = (50, 50, 130)

        self.óra = pygame.time.Clock()  # a játék sebességét adja meg
        self.rács: Grid = Grid()
        self.tetris = Tetris()

        
        self.rács.rács_kiíratása_consolra()

    def game_loop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.tetris.mozgás_balra()
                    if event.key == pygame.K_RIGHT:
                        self.tetris.mozgás_jobbra()
                    if event.key == pygame.K_DOWN:
                        self.tetris.mozgás_le()




            self.ablak.fill(self.sötétkék)
            self.rács.draw(self.ablak)
            self.tetris.draw(self.ablak)
            pygame.display.update()
            
            self.óra.tick(60)
            
