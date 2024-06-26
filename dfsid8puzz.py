import copy

def findzero(A):
    for i in range(3):
        for j in range(3):
            if A[i][j] == 0:
                return i, j

def moveleft(A, i, j, l):
    new = copy.deepcopy(A)
    if j != 0:
        new[i][j], new[i][j - 1] = new[i][j - 1], new[i][j]
        l.append(new)

def moveright(A, i, j, l):
    new = copy.deepcopy(A)
    if j != 2:
        new[i][j], new[i][j + 1] = new[i][j + 1], new[i][j]
        l.append(new)

def moveup(A, i, j, l):
    new = copy.deepcopy(A)
    if i != 0:
        new[i][j], new[i - 1][j] = new[i - 1][j], new[i][j]
        l.append(new)

def movedown(A, i, j, l):
    new = copy.deepcopy(A)
    if i != 2:
        new[i][j], new[i + 1][j] = new[i + 1][j], new[i][j]
        l.append(new)

def movegen(A, l):
    i, j = findzero(A)
    moveleft(A, i, j, l)
    moveright(A, i, j, l)
    moveup(A, i, j, l)
    movedown(A, i, j, l)

def dfsid_search(s1, g):
    open = [s1]
    closed = []
    i = 0
    while (1):
        i += 1
        for state in open:
            l = []
            movegen(state, l)
            for each in l:
                if each not in open and each not in closed:
                    open.append(each)
            closed.append(state)
            if state == g:
                print("Found at depth", i)
                return
        for state in open:
            if state not in closed:
                open.append(state)
        # open = [state for state in open if state not in closed]
    print("Not found")

s = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
g = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
dfsid_search(s, g)
