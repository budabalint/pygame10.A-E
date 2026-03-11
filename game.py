import sys
import pygame
from grid import Grid


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.ablak: pygame.Surface = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Tetris")
        self.sötétkék: tuple[int ,int ,int] = (50, 50, 130)

        self.óra = pygame.time.Clock()  # a játék sebességét adja meg
        self.rács: Grid = Grid()
        self.rács.rács_kiíratása_consolra()

    def game_loop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.ablak.fill(self.sötétkék)
            self.rács.draw(self.ablak)
            pygame.display.update()
            self.óra.tick(60)
