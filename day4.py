import collections


class Board:
    def __init__(self):
        self.rows = []

    def feed_line(self, line_string):
        self.rows += [[int(x.strip()) for x in line_string.split()]]

    def check_moves(self, plays):
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        diag_down = 0
        diag_up = 0

        hit = collections.defaultdict(bool)

        try:
            for turn, play in enumerate(plays):
                for row, row_items in enumerate(self.rows):
                    for col, col_item in enumerate(row_items):
                        if col_item == play:
                            rows[row] += 1
                            cols[col] += 1
                            if row == col:
                                diag_down += 1
                            elif row == (len(row_items) - (col + 1)):
                                diag_up += 1
                            hit[(row, col)] = True

                            if rows[row] == len(row_items):
                                raise ValueError("ROW:", row, hit)
                            elif cols[col] == len(row_items):
                                raise ValueError("COL:", col, hit)
                            elif diag_down == len(row_items) or diag_up == len(
                                row_items
                            ):
                                raise ValueError("DIAG:", hit)
        except ValueError:
            um_sum = 0
            for row, row_items in enumerate(self.rows):
                for col, col_item in enumerate(row_items):
                    #print(f'{col_item:*>3}' if hit[(row, col)] else f"{col_item:>3}", end=' ')
                    if not hit[(row, col)]:
                        um_sum += col_item
                #print("| T", turn, um_sum, um_sum * play)
            #print()
            return (turn, um_sum * play, um_sum, play)


with open("day4.txt") as in_handle:
    item_iter = iter(in_handle)
    plays = [int(i.strip()) for i in next(item_iter).strip().split(",")]
    next(item_iter)

    current_board = Board()

    wins = []

    for line in item_iter:
        ls = line.strip()
        if ls:
            current_board.feed_line(ls)
        else:
            i = current_board.check_moves(plays)
            if i is not None:
                wins.append(i)
            current_board = Board()

    i = current_board.check_moves(plays)
    if i is not None:
        wins.append(i)

    w = list(sorted(wins))
    print(w[0][1], w[-1][1])