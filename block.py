from colors import Colors
import pygame

from position import Position


class Block:
    _eltérés_x: int = 400

    
    def __init__(self, id: int) -> None:
        self.id = id
        self.cells: dict[int, list[Position]] = {}
        self.cell_size = 40
        self.rotation_state = 0
        self._sor_eltérés: int = 0
        self._oszlop_eltérés: int = 0
        self.colors = Colors.cella_színek_lekérése()
        
    def move(self, sorok: int, oszlopok: int):
        self._sor_eltérés += sorok
        self._oszlop_eltérés += oszlopok

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles: list[Position] = []
        for position in tiles:
            position = Position(position.sor + self._sor_eltérés, position.oszlop + self._oszlop_eltérés)
            moved_tiles.append(position)
        return moved_tiles

    def draw(self, screen: pygame.surface.Surface, sor_eltérés: int = 0, oszlop_eltérés: int = 0):
        tiles: list[Position] = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(
                (tile.oszlop + oszlop_eltérés) * self.cell_size + self._eltérés_x,
                +(sor_eltérés+tile.sor) * self.cell_size,
                self.cell_size - 1,
                self.cell_size - 1,
            )
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
