class Colors:
    sötétszürke: tuple[int, int, int] = (26, 31, 40)
    zöld: tuple[int, int, int] = (47, 230, 23)
    piros: tuple[int, int, int] = (232, 18, 18)
    narancssárga: tuple[int, int, int] = (226, 116, 17)
    sárga: tuple[int, int, int] = (237, 234, 4)
    lila: tuple[int, int, int] = (166, 0, 247)
    cián: tuple[int, int, int] = (21, 204, 209)
    kék: tuple[int, int, int] = (13, 64, 216)
    fehér: tuple[int, int, int] = (255, 255, 255)
    sötétkék: tuple[int, int, int] = (44, 44, 127)
    világoskék: tuple[int, int, int] = (59, 85, 162)

    @classmethod
    def cella_színek_lekérése(cls):
        return [
            cls.sötétszürke,
            cls.zöld,
            cls.piros,
            cls.narancssárga,
            cls.sárga,
            cls.lila,
            cls.cián,
            cls.kék,
        ]
