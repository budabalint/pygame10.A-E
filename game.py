import sys
import pygame
from blocks import *
from grid import Grid
from colors import Colors
from tetris import Tetris


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.betűtípus = pygame.font.Font(None, 40)
        self.pont_felirat_területe = self.betűtípus.render("Pont", True, Colors._fehér)
        self.következő_felirat_területe = self.betűtípus.render("Next", True, Colors._fehér)
        self.game_over_felirat = self.betűtípus.render("GAME OVER", True, Colors._fehér)
        self.pontok_területe = pygame.Rect(595, 71, 340, 77)
        self.következő_területe = pygame.Rect(595, 277, 340, 232)
        self.ablak: pygame.Surface = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Tetris")

        self.óra = pygame.time.Clock()  # a játék sebességét adja meg
        self.rács: Grid = Grid()
        self.tetris = Tetris()

        
        self.rács.rács_kiíratása_consolra()

        self.GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.GAME_UPDATE, 200)

    def game_loop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if self.tetris.game_over == True:
                        self.tetris.game_over = False
                        self.tetris.reset()
                    if event.key == pygame.K_LEFT:
                        self.tetris.mozgás_balra()
                    if event.key == pygame.K_RIGHT:
                        self.tetris.mozgás_jobbra()
                    if event.key == pygame.K_DOWN:
                        self.tetris.mozgás_le()
                        self.tetris.pontszám_frissítése(0,1)
                    if event.key == pygame.K_UP:
                        self.tetris.rotate()
                if event.type == self.GAME_UPDATE:
                    if self.tetris.game_over == False:
                        self.tetris.mozgás_le()

            self.pont_érték_területe = self.betűtípus.render(str(self.tetris.pontszám), True, Colors._fehér)

            self.ablak.fill(Colors._sötétkék)
            self.ablak.blit(self.pont_felirat_területe, (730, 26, 100, 65))
            self.ablak.blit(self.következő_felirat_területe, (733, 232, 100, 65))
            if self.tetris.game_over == True:
                self.ablak.blit(self.game_over_felirat, (675, 581, 100, 65))    
            pygame.draw.rect(self.ablak, Colors._világoskék, self.pontok_területe, 0, 10)
            self.ablak.blit(self.pont_érték_területe, self.pont_érték_területe.get_rect(centerx = self.pontok_területe.centerx, centery = self.pontok_területe.centery))
            pygame.draw.rect(self.ablak, Colors._világoskék, self.következő_területe, 0, 10)
            self.rács.draw(self.ablak)
            self.tetris.draw(self.ablak)
            pygame.display.update()
            
            self.óra.tick(60)
            
