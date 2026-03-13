from colors import Colors
import pygame

from position import Position
class Block:
    _offset_x: int = 400
    def __init__(self, id: int) -> None:
        self.id = id
        self.cells: dict[int, list[Position]] = {}
        self.cell_size = 40
        self.rotation_state = 0
        self.colors = Colors.cella_színek_lekérése()
    
    def draw(self, screen: pygame.surface.Surface):
        tiles: list[Position] = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.oszlop * self.cell_size + self._offset_x, 
				+ tile.sor * self.cell_size, self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)