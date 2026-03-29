class SzinKezelo:
    def __init__(self) -> None:
        self._sotetszurke: tuple[int, int, int] = (26, 31, 40)
        self._zold: tuple[int, int, int] = (47, 230, 23)
        self._piros: tuple[int, int, int] = (232, 18, 18)
        self._narancssarga: tuple[int, int, int] = (226, 116, 17)
        self._sarga: tuple[int, int, int] = (237, 234, 4)
        self._lila: tuple[int, int, int] = (166, 0, 247)
        self._cian: tuple[int, int, int] = (21, 204, 209)
        self._kek: tuple[int, int, int] = (13, 64, 216)
        self._feher: tuple[int, int, int] = (255, 255, 255)
        self._sotetkek: tuple[int, int, int] = (44, 44, 127)
        self._vilagoskek: tuple[int, int, int] = (59, 85, 162)
        self._barna: tuple[int, int, int] = (139, 69, 19)
        self._sotetlila: tuple[int, int, int] = (75, 0, 130)

    @property
    def sotetszurke(self) -> tuple[int, int, int]:
        return self._sotetszurke

    @property
    def zold(self) -> tuple[int, int, int]:
        return self._zold

    @property
    def piros(self) -> tuple[int, int, int]:
        return self._piros

    @property
    def narancssarga(self) -> tuple[int, int, int]:
        return self._narancssarga

    @property
    def sarga(self) -> tuple[int, int, int]:
        return self._sarga

    @property
    def lila(self) -> tuple[int, int, int]:
        return self._lila

    @property
    def cian(self) -> tuple[int, int, int]:
        return self._cian

    @property
    def kek(self) -> tuple[int, int, int]:
        return self._kek

    @property
    def feher(self) -> tuple[int, int, int]:
        return self._feher

    @property
    def sotetkek(self) -> tuple[int, int, int]:
        return self._sotetkek

    @property
    def vilagoskek(self) -> tuple[int, int, int]:
        return self._vilagoskek

    @property
    def barna(self) -> tuple[int, int, int]:
        return self._barna

    @property
    def sotetlila(self) -> tuple[int, int, int]:
        return self._sotetlila

    def cella_szinek_lekerese(self) -> list[tuple[int, int, int]]:
        return[
            self._sotetszurke,
            self._zold,
            self._piros,
            self._narancssarga,
            self._sarga,
            self._lila,
            self._cian,
            self._kek,
            self._sotetlila,
            self._barna
        ]

Szinek: SzinKezelo = SzinKezelo()