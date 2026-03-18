from grid import Grid
from blocks import *
import random as r
import pygame
class Tetris:
    def  __init__(self) -> None:
        self.grid = Grid()
        self.blocks: list[Block] = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block: Block = self.get_random_block()
        self.next_block: Block = self.get_random_block()
        self.game_over = False
        
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block: Block = r.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def mozgás_balra(self):
        self.current_block.move(0, -1)
        if self.bent_van_a_block() == False:
            self.current_block.move(0, 1)

    def mozgás_jobbra(self):
        self.current_block.move(0, 1)        
        if self.bent_van_a_block() == False:
            self.current_block.move(0, -1)

    def mozgás_le(self):
        self.current_block.move(1, 0)
        if self.bent_van_a_block() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        lapok = self.current_block.get_cell_positions()
        for position in lapok:
            self.grid.rács[position.sor][position.oszlop] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        self.grid.teljes_sor_törlése()
        if self.block_fits() == False:
            self.game_over = True

    def block_fits(self):
        lapok = self.current_block.get_cell_positions()
        for lap in lapok:
            if self.grid.üres(lap.sor, lap.oszlop) == False:
                return False
        return True


    def rotate(self):
        self.current_block.rotate()
        if self.bent_van_a_block() == False or self.block_fits() == False:
            self.current_block.undo_rotation()

    def bent_van_a_block(self):
        lapok = self.current_block.get_cell_positions()
        for lap in lapok:
            if self.grid.bent_van(lap.sor, lap.oszlop) == False:
                return False
        return True

    
    def draw(self, screen: pygame.Surface):
        self.grid.draw(screen)
        self.current_block.draw(screen)