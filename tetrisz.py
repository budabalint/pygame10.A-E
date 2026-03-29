from racs import Racs
from blokkok import IBlokk, JBlokk, LBlokk, OBlokk, SBlokk, TBlokk, ZBlokk, KisIBlokk, NagyOBlokk, Blokk
from pozicio import Pozicio
import random
import pygame

class Tetrisz:
    def __init__(self) -> None:
        self._racs: Racs = Racs()
        self._blokkok: list[Blokk] =[IBlokk(), JBlokk(), LBlokk(), OBlokk(), SBlokk(), TBlokk(), ZBlokk(), KisIBlokk(), NagyOBlokk()]
        self._aktualis_blokk: Blokk = self.veletlen_blokk_lekerese()
        self._kovetkezo_blokk: Blokk = self.veletlen_blokk_lekerese()
        self._jatek_vege: bool = False
        self._pontszam: int = 0
        
    @property
    def racs(self) -> Racs:
        return self._racs

    @property
    def pontszam(self) -> int:
        return self._pontszam

    @property
    def jatek_vege(self) -> bool:
        return self._jatek_vege

    @jatek_vege.setter
    def jatek_vege(self, ertek: bool) -> None:
        self._jatek_vege = ertek
        
    def pontszam_frissitese(self, torolt_sorok: int, pontok_csokkentese: int) -> None:
        if torolt_sorok == 1:
            self._pontszam += 100
        elif torolt_sorok == 2:
            self._pontszam += 300
        elif torolt_sorok == 3:
            self._pontszam += 500
        self._pontszam += pontok_csokkentese

    def veletlen_blokk_lekerese(self) -> Blokk:
        if len(self._blokkok) == 0:
            self._blokkok =[IBlokk(), JBlokk(), LBlokk(), OBlokk(), SBlokk(), TBlokk(), ZBlokk(), KisIBlokk(), NagyOBlokk()]
        blokk: Blokk = random.choice(self._blokkok)
        self._blokkok.remove(blokk)
        return blokk
    
    def mozgas_balra(self) -> None:
        self._aktualis_blokk.mozgat(0, -1)
        if self.bent_van_a_blokk() == False:
            self._aktualis_blokk.mozgat(0, 1)

    def mozgas_jobbra(self) -> None:
        self._aktualis_blokk.mozgat(0, 1)        
        if self.bent_van_a_blokk() == False:
            self._aktualis_blokk.mozgat(0, -1)

    def mozgas_le(self) -> None:
        self._aktualis_blokk.mozgat(1, 0)
        if self.bent_van_a_blokk() == False or self.blokk_belefer() == False:
            self._aktualis_blokk.mozgat(-1, 0)
            self.blokk_rogzitese()

    def blokk_rogzitese(self) -> None:
        lapok: list[Pozicio] = self._aktualis_blokk.cella_poziciok_lekerese()
        for pozicio in lapok:
            self._racs.ertek_beallitasa(pozicio.sor, pozicio.oszlop, self._aktualis_blokk.azonosito)
        self._aktualis_blokk = self._kovetkezo_blokk
        self._kovetkezo_blokk = self.veletlen_blokk_lekerese()
        
        torolt_sorok: int = self._racs.teljes_sor_torlese()
        self.pontszam_frissitese(torolt_sorok, 0)
        if self.blokk_belefer() == False:
            self._jatek_vege = True

    def blokk_belefer(self) -> bool:
        lapok: list[Pozicio] = self._aktualis_blokk.cella_poziciok_lekerese()
        for lap in lapok:
            if self._racs.ures(lap.sor, lap.oszlop) == False:
                return False
        return True

    def forgat(self) -> None:
        self._aktualis_blokk.forgat()
        if self.bent_van_a_blokk() == False or self.blokk_belefer() == False:
            self._aktualis_blokk.forgatas_visszavonasa()

    def bent_van_a_blokk(self) -> bool:
        lapok: list[Pozicio] = self._aktualis_blokk.cella_poziciok_lekerese()
        for lap in lapok:
            if self._racs.bent_van(lap.sor, lap.oszlop) == False:
                return False
        return True
    
    def visszaallitas(self) -> None:
        self._racs.visszaallitas()
        self._blokkok =[
            IBlokk(),
            JBlokk(),
            LBlokk(),
            OBlokk(),
            SBlokk(),
            TBlokk(),
            ZBlokk(),
            KisIBlokk(),
            NagyOBlokk(),
        ]
        self._aktualis_blokk = self.veletlen_blokk_lekerese()
        self._kovetkezo_blokk = self.veletlen_blokk_lekerese()
        self._pontszam = 0
    
    def rajzol(self, kepernyo: pygame.Surface) -> None:
        self._racs.rajzol(kepernyo)
        self._aktualis_blokk.rajzol(kepernyo)
        
        if self._kovetkezo_blokk.azonosito == 3:
            self._kovetkezo_blokk.rajzol(kepernyo, 418, 372)
        elif self._kovetkezo_blokk.azonosito == 4:
            self._kovetkezo_blokk.rajzol(kepernyo, 418, 352)
        else:
            self._kovetkezo_blokk.rajzol(kepernyo, 430, 348)