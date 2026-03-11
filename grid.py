import pygame

from colors import Colors


class Grid:
    _sorok_száma: int = 20
    _oszlopok_száma: int = 10
    _block_méret: int = 40

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

    def draw(self, screen: pygame.Surface):
        for sor in range(self._sorok_száma):
            for oszlop in range(self._oszlopok_száma):
                cella_értéke: int = self.rács[sor][oszlop]
                cella_négyzet = pygame.Rect(
                    (oszlop+10) * self._block_méret +1,
                    sor * self._block_méret+1,
                    self._block_méret-1,
                    self._block_méret-1,
                )
                pygame.draw.rect(screen, self.színek[cella_értéke], cella_négyzet)
