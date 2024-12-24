def check(x, y, puzzle):
    out = set()
    for i in range(9):
        if (puzzle[i][y] != 0 and i != x): out.add(puzzle[i][y])
    for i in range(9):
        if (puzzle[x][i] != 0 and i != y): out.add(puzzle[x][i])
    
    for i in range((x // 3) * 3, (x // 3 + 1) * 3):
        for j in range((y // 3) * 3, (y // 3 + 1) * 3):
            if (puzzle[i][j] != 0 and i != x and j != y): out.add(puzzle[i][j])
    
    
    return out

def solve(puzzle):
    pos = {}

    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0: pos[(i, j)] = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
            else: pos[(i, j)] = set([puzzle[i][j]])

    a, b = 0, 0
    prio = {}
    for i in range(9):
        for j in range(9):
            pos[(i, j)] = pos[(i, j)] - check(i, j, puzzle)
        
            if prio.get(len(pos[(i, j)])) is not None: prio[len(pos[(i, j)])].add((i, j))
            else: prio[len(pos[(i, j)])] = {(i, j)}


    # for i in range(9): print(i, len(prio.get(i)), prio.get(i)) if prio.get(i) is not None else print(i, "NO VALUES")
    
    ones = prio.get(1)
    
    for a in ones:
        x, y = a[0], a[1]
        if puzzle[x][y] == 0:
            # print(x, y, list(pos[(x, y)])[-1])
            puzzle[x][y] = list(pos[(x, y)])[-1]
    

    print("=================")
    for l in puzzle: print(*l)
    
    flag = True
    for i in range(9):
        for j in range(9):
            flag = puzzle_nyt[i][j] != 0 and flag
    
    if flag: return
    solve(puzzle)

puzzle_hard = [
[0, 0, 0, 4, 0, 0, 0, 0, 0],
[7, 2, 3, 0, 0, 9, 4, 0, 0],
[0, 0, 1, 0, 0, 0, 9, 0, 0],
[2, 0, 0, 8, 0, 3, 0, 5, 4],
[0, 0, 0, 2, 6, 0, 0, 0, 0],
[0, 0, 0, 0, 5, 0, 0, 0, 9],
[3, 0, 0, 0, 0, 0, 0, 0, 0],
[8, 7, 0, 0, 0, 6, 0, 0, 0],
[5, 0, 0, 3, 0, 8, 0, 7, 2]]

puzzle = [
[0, 7, 0, 5, 8, 3, 0, 2, 0],
[0, 5, 9, 2, 0, 0, 3, 0, 0],
[3, 4, 0, 0, 0, 6, 5, 0, 7],
[7, 9, 5, 0, 0, 0, 6, 3, 2],
[0, 0, 3, 6, 9, 7, 1, 0, 0],
[6, 8, 0, 0, 0, 2, 7, 0, 9],
[9, 1, 4, 8, 3, 5, 0, 7, 6],
[0, 3, 0, 7, 0, 1, 4, 9, 5],
[5, 6, 7, 4, 2, 9, 0, 1, 3]]

puzzle_nyt = [
[0, 0, 0, 2, 7, 3, 9, 0, 5],
[5, 0, 0, 0, 0, 9, 0, 3, 7],
[7, 9, 0, 4, 0, 0, 0, 0, 2],
[0, 8, 0, 5, 2, 6, 4, 0, 0],
[1, 6, 5, 8, 0, 0, 0, 0, 0],
[0, 0, 2, 0, 9, 0, 5, 0, 6],
[0, 0, 1, 0, 0, 5, 3, 6, 0],
[9, 3, 8, 0, 6, 2, 0, 0, 0],
[0, 0, 0, 9, 3, 0, 0, 2, 0]]

solve(puzzle_nyt)
print("=================")

