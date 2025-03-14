import random

class BoardSetup:
    def __init__(self, rows: int, cols: int, ships_dict: dict[int, int]):
        self.rows = rows
        self.cols = cols
        self.ships_dict = ships_dict
        
        self.board = [[0 for _ in range(cols)] for _ in range(rows)] # Hrací plocha, seznam všech míst

    def get_board(self) -> list[list[int]]:
        return self.board

    def get_tile(self, x: int, y: int) -> int:
        if 0 <= x < self.cols and 0 <= y < self.rows:
            return self.board[y][x]
        raise IndexError("Out of bounds.") # Chyba pokud je vybraná pozice mimo board

    def place_ships(self) -> None:
        for ship_id, count in self.ships_dict.items():
            for _ in range(count):
                placed = False
                while not placed:
                    x, y = random.randint(0, self.cols - 1), random.randint(0, self.rows - 1)
                    if self.board[y][x] == 0:
                        self.board[y][x] = ship_id # Přidá loď pokud vybraná pozice nemá
                        placed = True

    def reset_board(self) -> None:
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def board_stats(self) -> dict:
        empty_spaces = sum(row.count(0) for row in self.board)
        occupied_spaces = self.rows * self.cols - empty_spaces
        return {"empty_spaces": empty_spaces, "occupied_spaces": occupied_spaces}
