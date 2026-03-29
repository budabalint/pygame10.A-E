import sys
import pygame
from szinek import Szinek
from tetrisz import Tetrisz

class Jatek:
    def __init__(self) -> None:
        pygame.init()
        self._betutipus: pygame.font.Font = pygame.font.Font(None, 40)
        self._pont_felirat_terulete: pygame.Surface = self._betutipus.render("Pont", True, Szinek.feher)
        self._kovetkezo_felirat_terulete: pygame.Surface = self._betutipus.render("Következő", True, Szinek.feher)
        self._jatek_vege_felirat: pygame.Surface = self._betutipus.render("JATEK VEGE", True, Szinek.feher)
        self._pontok_terulete: pygame.Rect = pygame.Rect(595, 71, 340, 77)
        self._kovetkezo_terulete: pygame.Rect = pygame.Rect(595, 277, 340, 232)
        self._ablak: pygame.Surface = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Tetrisz")

        self._ora: pygame.time.Clock = pygame.time.Clock()
        self._tetrisz: Tetrisz = Tetrisz()
        
        self._tetrisz.racs.konzolra_iras()

        self._jatek_frissites: int = pygame.USEREVENT
        pygame.time.set_timer(self._jatek_frissites, 200)

    def frissit(self) -> None:
        for esemeny in pygame.event.get():
            if esemeny.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if esemeny.type == pygame.KEYDOWN:
                if self._tetrisz.jatek_vege == True:
                    self._tetrisz.jatek_vege = False
                    self._tetrisz.visszaallitas()
                if esemeny.key == pygame.K_LEFT:
                    self._tetrisz.mozgas_balra()
                if esemeny.key == pygame.K_RIGHT:
                    self._tetrisz.mozgas_jobbra()
                if esemeny.key == pygame.K_DOWN:
                    self._tetrisz.mozgas_le()
                    self._tetrisz.pontszam_frissitese(0, 1)
                if esemeny.key == pygame.K_UP:
                    self._tetrisz.forgat()
            if esemeny.type == self._jatek_frissites:
                if self._tetrisz.jatek_vege == False:
                    self._tetrisz.mozgas_le()

    def rajzol(self) -> None:
        pont_ertek_terulete: pygame.Surface = self._betutipus.render(str(self._tetrisz.pontszam), True, Szinek.feher)

        self._ablak.fill(Szinek.sotetkek)
        self._ablak.blit(self._pont_felirat_terulete, (730, 26, 100, 65))
        self._ablak.blit(self._kovetkezo_felirat_terulete, (692, 232, 100, 65))
        
        if self._tetrisz.jatek_vege == True:
            self._ablak.blit(self._jatek_vege_felirat, (675, 581, 100, 65))    
            
        pygame.draw.rect(self._ablak, Szinek.vilagoskek, self._pontok_terulete, 0, 10)
        self._ablak.blit(pont_ertek_terulete, pont_ertek_terulete.get_rect(centerx = self._pontok_terulete.centerx, centery = self._pontok_terulete.centery))
        pygame.draw.rect(self._ablak, Szinek.vilagoskek, self._kovetkezo_terulete, 0, 10)
        
        self._tetrisz.racs.rajzol(self._ablak)
        self._tetrisz.rajzol(self._ablak)
        pygame.display.update()
        
        self._ora.tick(60)