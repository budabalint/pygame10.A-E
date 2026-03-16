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
        
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block: Block = r.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def draw(self, screen: pygame.Surface):
        self.grid.draw(screen)
        self.current_block.draw(screen)