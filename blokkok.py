from blokk import Blokk
from pozicio import Pozicio


class LBlokk(Blokk):
    def __init__(self) -> None:
        super().__init__(azonosito=1)
        self._cellak = {
            0: [Pozicio(0, 2), Pozicio(1, 0), Pozicio(1, 1), Pozicio(1, 2)],
            1: [Pozicio(0, 1), Pozicio(1, 1), Pozicio(2, 1), Pozicio(2, 2)],
            2: [Pozicio(1, 0), Pozicio(1, 1), Pozicio(1, 2), Pozicio(2, 0)],
            3: [Pozicio(0, 0), Pozicio(0, 1), Pozicio(1, 1), Pozicio(2, 1)],
        }
        self.mozgat(0, 3)


class JBlokk(Blokk):
    def __init__(self) -> None:
        super().__init__(azonosito=2)
        self._cellak = {
            0: [Pozicio(0, 0), Pozicio(1, 0), Pozicio(1, 1), Pozicio(1, 2)],
            1: [Pozicio(0, 1), Pozicio(0, 2), Pozicio(1, 1), Pozicio(2, 1)],
            2: [Pozicio(1, 0), Pozicio(1, 1), Pozicio(1, 2), Pozicio(2, 2)],
            3: [Pozicio(0, 1), Pozicio(1, 1), Pozicio(2, 0), Pozicio(2, 1)],
        }
        self.mozgat(0, 3)


class IBlokk(Blokk):
    def __init__(self) -> None:
        super().__init__(azonosito=3)
        self._cellak = {
            0: [Pozicio(1, 0), Pozicio(1, 1), Pozicio(1, 2), Pozicio(1, 3)],
            1: [Pozicio(0, 2), Pozicio(1, 2), Pozicio(2, 2), Pozicio(3, 2)],
            2: [Pozicio(2, 0), Pozicio(2, 1), Pozicio(2, 2), Pozicio(2, 3)],
            3: [Pozicio(0, 1), Pozicio(1, 1), Pozicio(2, 1), Pozicio(3, 1)],
        }
        self.mozgat(-1, 3)


class OBlokk(Blokk):
    def __init__(self) -> None:
        super().__init__(azonosito=4)
        self._cellak = {0: [Pozicio(0, 0), Pozicio(0, 1), Pozicio(1, 0), Pozicio(1, 1)]}
        self.mozgat(0, 4)


class SBlokk(Blokk):
    def __init__(self) -> None:
        super().__init__(azonosito=5)
        self._cellak = {
            0: [Pozicio(0, 1), Pozicio(0, 2), Pozicio(1, 0), Pozicio(1, 1)],
            1: [Pozicio(0, 1), Pozicio(1, 1), Pozicio(1, 2), Pozicio(2, 2)],
            2: [Pozicio(1, 1), Pozicio(1, 2), Pozicio(2, 0), Pozicio(2, 1)],
            3: [Pozicio(0, 0), Pozicio(1, 0), Pozicio(1, 1), Pozicio(2, 1)],
        }
        self.mozgat(0, 3)


class TBlokk(Blokk):
    def __init__(self) -> None:
        super().__init__(azonosito=6)
        self._cellak = {
            0: [Pozicio(0, 1), Pozicio(1, 0), Pozicio(1, 1), Pozicio(1, 2)],
            1: [Pozicio(0, 1), Pozicio(1, 1), Pozicio(1, 2), Pozicio(2, 1)],
            2: [Pozicio(1, 0), Pozicio(1, 1), Pozicio(1, 2), Pozicio(2, 1)],
            3: [Pozicio(0, 1), Pozicio(1, 0), Pozicio(1, 1), Pozicio(2, 1)],
        }
        self.mozgat(0, 3)


class ZBlokk(Blokk):
    def __init__(self) -> None:
        super().__init__(azonosito=7)
        self._cellak = {
            0: [Pozicio(0, 0), Pozicio(0, 1), Pozicio(1, 1), Pozicio(1, 2)],
            1: [Pozicio(0, 2), Pozicio(1, 1), Pozicio(1, 2), Pozicio(2, 1)],
            2: [Pozicio(1, 0), Pozicio(1, 1), Pozicio(2, 1), Pozicio(2, 2)],
            3: [Pozicio(0, 1), Pozicio(1, 0), Pozicio(1, 1), Pozicio(2, 0)],
        }
        self.mozgat(0, 3)


class KisIBlokk(Blokk):
    def __init__(self) -> None:
        super().__init__(azonosito=8)
        self._cellak = {
            0: [Pozicio(1, 0), Pozicio(1, 1), Pozicio(1, 2)],
            1: [Pozicio(0, 1), Pozicio(1, 1), Pozicio(2, 1)],
            2: [Pozicio(1, 0), Pozicio(1, 1), Pozicio(1, 2)],
            3: [Pozicio(0, 1), Pozicio(1, 1), Pozicio(2, 1)],
        }
        self.mozgat(-1, 3)


class NagyOBlokk(Blokk):
    def __init__(self) -> None:
        super().__init__(azonosito=9)
        self._cellak = {
            0: [
                Pozicio(0, 0),
                Pozicio(0, 1),
                Pozicio(0, 2),
                Pozicio(1, 0),
                Pozicio(1, 1),
                Pozicio(1, 2),
                Pozicio(2, 0),
                Pozicio(2, 1),
                Pozicio(2, 2),
            ],
        }
        self.mozgat(0, 3)
