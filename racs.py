import pygame
from szinek import Szinek

class Racs:
    def __init__(self) -> None:
        self._sorok_szama: int = 20
        self._oszlopok_szama: int = 10
        self._blokk_meret: int = 40
        self._eltolas_x: int = 150
        self._racs_matrix: list[list[int]] = [[0 for _ in range(self._oszlopok_szama)]
            for _ in range(self._sorok_szama)
        ]
        self._szinek: list[tuple[int, int, int]] = Szinek.cella_szinek_lekerese()

    def ertek_beallitasa(self, sor: int, oszlop: int, ertek: int) -> None:
        self._racs_matrix[sor][oszlop] = ertek

    def konzolra_iras(self) -> None:
        for sor in range(self._sorok_szama):
            for oszlop in range(self._oszlopok_szama):
                print(self._racs_matrix[sor][oszlop], end=" ")
            print()

    def bent_van(self, sor: int, oszlop: int) -> bool:
        if sor >= 0 and sor < self._sorok_szama and oszlop >= 0 and oszlop < self._oszlopok_szama:
            return True
        return False
    
    def tele_van_e_sor(self, sor: int) -> bool:
        for oszlop in range(self._oszlopok_szama):
            if self._racs_matrix[sor][oszlop] == 0:
                return False
        return True
    
    def sor_torlese(self, sor: int) -> None:
        for oszlop in range(self._oszlopok_szama):
            self._racs_matrix[sor][oszlop] = 0
            
    def sor_lemozgatasa(self, sor: int, sorok_szama: int) -> None:
        for oszlop in range(self._oszlopok_szama):
            self._racs_matrix[sor + sorok_szama][oszlop] = self._racs_matrix[sor][oszlop]
            self._racs_matrix[sor][oszlop] = 0
            
    def teljes_sor_torlese(self) -> int:
        befejezett: int = 0
        for sor in range(self._sorok_szama - 1, 0, -1):
            if self.tele_van_e_sor(sor):
                self.sor_torlese(sor)
                befejezett += 1
            elif befejezett > 0:
                self.sor_lemozgatasa(sor, befejezett)
        return befejezett
    
    def visszaallitas(self) -> None:
        for sor in range(self._sorok_szama):
            for oszlop in range(self._oszlopok_szama):
                self._racs_matrix[sor][oszlop] = 0
    
    def ures(self, sor: int, oszlop: int) -> bool:
        if self._racs_matrix[sor][oszlop] == 0:
            return True
        return False

    def rajzol(self, kepernyo: pygame.Surface) -> None:
        for sor in range(self._sorok_szama):
            for oszlop in range(self._oszlopok_szama):
                cella_erteke: int = self._racs_matrix[sor][oszlop]
                cella_negyzet: pygame.Rect = pygame.Rect(
                    (oszlop * self._blokk_meret) + 1 + self._eltolas_x,
                    (sor * self._blokk_meret) + 1,
                    self._blokk_meret - 1,
                    self._blokk_meret - 1,
                )
                pygame.draw.rect(kepernyo, self._szinek[cella_erteke], cella_negyzet)