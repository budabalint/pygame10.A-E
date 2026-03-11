class Colors:
    _sötétszürke: tuple[int, int, int] = (26, 31, 40)
    _zöld: tuple[int, int, int] = (47, 230, 23)
    _piros: tuple[int, int, int] = (232, 18, 18)
    _narancssárga: tuple[int, int, int] = (226, 116, 17)
    _sárga: tuple[int, int, int] = (237, 234, 4)
    _lila: tuple[int, int, int] = (166, 0, 247)
    _cián: tuple[int, int, int] = (21, 204, 209)
    _kék: tuple[int, int, int] = (13, 64, 216)
    _fehér: tuple[int, int, int] = (255, 255, 255)
    _sötétkék: tuple[int, int, int] = (44, 44, 127)
    _világoskék: tuple[int, int, int] = (59, 85, 162)

    @classmethod
    def cella_színek_lekérése(cls):
        return [
            cls._sötétszürke,
            cls._zöld,
            cls._piros,
            cls._narancssárga,
            cls._sárga,
            cls._lila,
            cls._cián,
            cls._kék,
        ]
