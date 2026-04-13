class Pozicio:
    def __init__(self, sor: int, oszlop: int) -> None:
        self._sor: int = sor
        self._oszlop: int = oszlop

    @property
    def sor(self) -> int:
        return self._sor

    @property
    def oszlop(self) -> int:
        return self._oszlop
