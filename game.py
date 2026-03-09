import pygame


class Game:
    def __init__(self) -> None:
        pygame.init()
        ablak: pygame.Surface = pygame.display.set_mode((1200, 600))
        print(ablak)
