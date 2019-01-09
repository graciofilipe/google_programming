from random import uniform

def make_mine_locations(n_mines, dim):
    mine_locations = set()
    while len(mine_locations) < n_mines:
        (row, col) = int(uniform(a=0, b=dim)), int(uniform(a=0, b=dim))
        mine_locations.add((row, col))
    print('mine_locations', mine_locations)
    return mine_locations

def place_mines(mine_locations, init_matrix):
    for mine in mine_locations:
        row, col = mine
        for row_diff in [-1, 0, 1]:
            for col_diff in [-1, 0, 1]:
                if row_diff == 0 and col_diff ==0:
                    pass
                else:
                    try:
                        init_matrix[row+row_diff][col+col_diff] += 1
                    except:
                        print(row+row_diff, col+col_diff)
                        pass
    for mine in mine_locations:
        row, col = mine
        init_matrix[row][col]=9

    return init_matrix

def build_board(n_mines, dim):
    mine_locations = make_mine_locations(n_mines, dim)
    init_matrix = [[0 for _ in range(dim)] for _ in range(dim)]
    board_ready = place_mines(mine_locations, init_matrix)
    return board_ready


m = build_board(n_mines=5, dim=5)
for r in m:
    print(r)