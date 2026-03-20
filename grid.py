import pygame

from colors import Colors


class Grid:
    _sorok_száma: int = 20
    _oszlopok_száma: int = 10
    _block_méret: int = 40
    _offset_x: int = 150

    def __init__(self) -> None:
        self.rács: list[list[int]] = [
            [0 for _ in range(self._oszlopok_száma)]
            for _ in range(
                self._sorok_száma
            )  # létrehozza a 0-kkal megtöltött listánkat
        ]
        self.színek = Colors.cella_színek_lekérése()

    def rács_kiíratása_consolra(self) -> None:
        for sor in range(self._sorok_száma):
            for oszlop in range(self._oszlopok_száma):
                print(self.rács[sor][oszlop], end=" ")
            print()

    def bent_van(self, sor: int, oszlop: int):
        if sor >= 0 and sor < self._sorok_száma and oszlop >= 0 and oszlop < self._oszlopok_száma:
            return True
        return False
    
    def tele_van_e_a_sor(self, sor: int) -> bool:
        for oszlop in range(self._oszlopok_száma):
            if self.rács[sor][oszlop] == 0:
                return False
        return True
    
    def sor_törlése(self, sor: int) -> None:
        for oszlop in range(self._oszlopok_száma):
            self.rács[sor][oszlop] = 0
            
    def sor_lemozgatása(self, sor: int, sorok_száma: int) -> None:
        for oszlop in range(self._oszlopok_száma):
            self.rács[sor+sorok_száma][oszlop] = self.rács[sor][oszlop]
            self.rács[sor][oszlop]
            
    def teljes_sor_törlése(self) -> int:
        completed: int = 0
        for sor in range(self._sorok_száma-1,0,-1):
            if self.tele_van_e_a_sor(sor):
                self.sor_törlése(sor)
                completed += 1
            elif completed > 0:
                self.sor_lemozgatása(sor, completed)
        return completed
    def üres(self, sor: int, oszlop: int):
        if self.rács[sor][oszlop] == 0:
            return True
        return False

    def draw(self, screen: pygame.Surface):
        for sor in range(self._sorok_száma):
            for oszlop in range(self._oszlopok_száma):
                cella_értéke: int = self.rács[sor][oszlop]
                cella_négyzet = pygame.Rect(
                    (oszlop) * self._block_méret + 1 + self._offset_x,
                    sor * self._block_méret + 1,
                    self._block_méret - 1,
                    self._block_méret - 1,
                )
                pygame.draw.rect(screen, self.színek[cella_értéke], cella_négyzet)
