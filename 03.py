# This didn't work, don't know why.
# Maybe missing returning -1 for `mines` equal to None or empty?
def minefield(mines):
    i = -1
    steps = 0
    len_mines = len(mines)
    while i < len_mines - 1:
        if (i + 2 > len_mines - 1) or (i + 2 < len_mines and mines[i + 2] != 1):
            i += 2
        elif (i + 1 > len_mines - 1) or (i + 1 < len_mines and mines[i + 1] != 1):
            i += 1
        else:
            return -1
        steps += 1
    return steps
