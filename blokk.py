import pygame
from szinek import Szinek
from pozicio import Pozicio

class Blokk:
    def __init__(self, azonosito: int) -> None:
        self._azonosito: int = azonosito
        self._cellak: dict[int, list[Pozicio]] = {}
        self._cella_meret: int = 40
        self._forgatasi_allapot: int = 0
        self._sor_elteres: int = 0
        self._oszlop_elteres: int = 0
        self._szinek: list[tuple[int, int, int]] = Szinek.cella_szinek_lekerese()
        self._eltolas_x: int = 150

    @property
    def azonosito(self) -> int:
        return self._azonosito

    def mozgat(self, sorok: int, oszlopok: int) -> None:
        self._sor_elteres += sorok
        self._oszlop_elteres += oszlopok

    def cella_poziciok_lekerese(self) -> list[Pozicio]:
        lapok: list[Pozicio] = self._cellak[self._forgatasi_allapot]
        mozgatott_lapok: list[Pozicio] =[]
        for pozicio in lapok:
            uj_pozicio: Pozicio = Pozicio(pozicio.sor + self._sor_elteres, pozicio.oszlop + self._oszlop_elteres)
            mozgatott_lapok.append(uj_pozicio)
        return mozgatott_lapok
    
    def forgat(self) -> None:
        self._forgatasi_allapot += 1
        if self._forgatasi_allapot == len(self._cellak):
            self._forgatasi_allapot = 0

    def forgatas_visszavonasa(self) -> None:
        self._forgatasi_allapot -= 1
        if self._forgatasi_allapot == -1:
            self._forgatasi_allapot = len(self._cellak) - 1

    def rajzol(self, kepernyo: pygame.Surface, pixel_x: int = 0, pixel_y: int = 0) -> None:
        lapok: list[Pozicio] = self.cella_poziciok_lekerese()
        for lap in lapok:
            lap_teglalap: pygame.Rect = pygame.Rect(
                (lap.oszlop * self._cella_meret) + self._eltolas_x + pixel_x,
                (lap.sor * self._cella_meret) + pixel_y,
                self._cella_meret - 1,
                self._cella_meret - 1,
            )
            pygame.draw.rect(kepernyo, self._szinek[self._azonosito], lap_teglalap)