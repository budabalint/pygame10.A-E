from colors import Colors

class Block:
    def __init__(self, id: int) -> None:
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = Colors.cella_színek_lekérése()