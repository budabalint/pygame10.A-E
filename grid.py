class Grid:
    def __init__(self) -> None:
        self.sorok_száma: int = 20
        self.oszlopok_száma: int = 10
        self.block_méret: int = 40  # pixelben megadja egy négyzet méretét
        self.rács: list[list[int]] = [
            [0 for _ in range(self.oszlopok_száma)] for _ in range(self.sorok_száma)
        ]  # létrehozza a 0-kkal megtöltött listánkat

    def rács_kiíratása_consolra(self) -> None:
        for sor in range(self.sorok_száma):
            for oszlop in range(self.oszlopok_száma):
                print(self.rács[sor][oszlop], end=" ")
            print()
