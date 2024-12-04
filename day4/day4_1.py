directions = [
    (0,1), # right
    (0,-1), # left
    (1,0), # down
    (-1,0), # up
    (1,1), # diagonal down-right
    (-1,-1), # diagonal up-left
    (1,-1), # diagonal down-left
    (-1,1) # diagonal up-right
]

"""
Checks for the word starting at a point (row,col) in a direction (step_row,step_col)
"""
def search_word_in_a_direction(grid, row, col, step_row, step_col, word="XMAS") -> bool:
    rows, cols = len(grid), len(grid[0])
    for i in range(len(word)):
        current_row, current_col = row + i * step_row, col + i * step_col
        if current_row < 0 \
            or current_col < 0 \
            or current_row >= rows or \
            current_col >= cols or \
            grid[current_row][current_col] != word[i]:
            return False
    return True

with open("day4_1.txt", "r") as file:
    grid = [line for line in file.readlines()]
    print("The grid is", grid)
    def find_xmas(grid):
        rows, cols = len(grid), len(grid[0])
        total = 0
        for row in range(rows):
            for col in range(cols):
                for step_row, step_col in directions:
                    if search_word_in_a_direction(grid, row, col, step_row, step_col):
                        total+=1
        return total
    print(find_xmas(grid))
