class Strategy:
    def __init__(self, rows: int, cols: int, ships_dict: dict[int, int]):
        self.rows = rows
        self.cols = cols
        self.ships_dict = ships_dict
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        
        # Tady vytvoříme 2D seznam otazníků '?', znamenající "neznámé pole"
        self.enemy_board = [['?' for _ in range(cols)] for _ in range(rows)]

    def get_next_attack(self) -> tuple[int, int]:
        for y in range(self.rows):
            for x in range(self.cols):
                if self.enemy_board[y][x] == '?':
                    return x, y
        raise ValueError("No target found.")

    def register_attack(self, x: int, y: int, is_hit: bool, is_sunk: bool) -> None:
        self.enemy_board[y][x] = 'H' if is_hit else 'M'
        if is_sunk:
            for ship_id in self.ships_dict:
                if self.ships_dict[ship_id] > 0:
                    self.ships_dict[ship_id] -= 1 # Odebere loď pokud byla zasáhnuta
                    break

    def get_enemy_board(self) -> list[list[str]]:
        return self.enemy_board

    def get_remaining_ships(self) -> dict[int, int]:
        return self.ships_dict

    def all_ships_sunk(self) -> bool:
        return all(count == 0 for count in self.ships_dict.values())
