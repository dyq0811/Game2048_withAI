#2048 ai tester
#Yingqi Ding

#call testAI() or testRandom() to see list of scores,
# maximum score, and average score.
#They are a little bit slow. Some patience is needed.

##############
#Test Results#
##############
#random
#average: around 1000 points

#ai
#average: 3000-3100 points
#highest: more than 10000 points

from random import *

#totally random player        
def random():
    grid = addTwo(startGame())
    totalScore = 0
    while gameState(grid) == "Game continues...":
        moveList = ["w","s","a","d"]
        i = randint(0,3)
        move = moveList[i]
        grid,addScore = makeMove(grid,move)
        totalScore += addScore
        grid = addTwo(grid)
    return totalScore

def testRandom():
    scores = []
    maxScore = 0
    total = 0
    for i in range(200):
        scores.append(random())
        total += random()
        if random() > maxScore:
            maxScore = random()
    average = total/200
    print(scores)
    print(maxScore)
    print(average)


def testAI():
    scores = []
    maxScore = 0
    total = 0
    for i in range(200):
        scores.append(ai())
        total += ai()
        if ai() > maxScore:
            maxScore = ai()
    average = total/200
    print(scores)
    print(maxScore)
    print(average)

#kind of an artificial intelligence
def ai():
    grid = addTwo(startGame())
    totalScore = 0
    while gameState(grid) == "Game continues...":
        moveList = ["w","s","a","d"]
        maxScore = 0
        i = randint(0,1)
        bestList = ["w","d"]
        bestMove = bestList[i]
        for move in moveList:
            gridCopy = []
            rowCopy = []
            for r in grid:
                for c in r:
                    rowCopy.append(c)
                gridCopy.append(rowCopy)
                rowCopy = []
            gridCopy,addScore = makeMove(gridCopy,move)
            if addScore > maxScore:
                maxScore = addScore
                bestMove = move
        grid,addScore = makeMove(grid,bestMove)
        totalScore += addScore
        grid = addTwo(grid)
    return totalScore




#------------------------------------------------------------------------------

def startGame():
    grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    return grid


def gameState(grid):
    size = len(grid)
    state = ["Game continues...", "Win!", "Game over."]
    # ----------------------------------------------------
    # Check 2048 and 0.
    for r in range(size):
        for c in range(size):
            if grid[r][c] == 2048:
                return state[1]
            if grid[r][c] == 0:
                return state[0]
    # ----------------------------------------------------
    # Check grids on the right or below.
    for r in range(size-1):
        for c in range(size-1):
            if grid[r][c] == grid[r][c+1] or grid[r][c] == grid[r+1][c]:
                return state[0]
    # ----------------------------------------------------
    # Check last row.
    for c in range(size-1):
        if grid[size-1][c] == grid[size-1][c+1]:
            return state[0]
    # Chek last column.
    for r in range(size-1):
        if grid[r][size-1] == grid[r+1][size-1]:
            return state[0]
    # ----------------------------------------------------
    # If all the tests above fail, game over.
    return state[2]

def full(grid):
    for i in grid:
        for j in i:
            if j == 0:
                return False
    return True

def addTwo(grid):
    r, c = randint(0,3), randint(0,3)
    while grid[r][c] != 0 and not full(grid):
        r, c = randint(0,3), randint(0,3)
    grid[r][c] = 2
    return grid

def left(grid):
    score = 0
    #first, move the grid towards one direction.
    #for example,[2,0,0,2] will become[2,2,0,0]
    for i in range(2):
        for r in range(4):
            for c in range(4):
                if grid[r][c] == 0:
                    del grid[r][c]
                    grid[r].append(0)
                    
    #then, combine grids with the same number.
    #for example, [2,2,0,0] will become [4,0,0,0]
    for r in range(4):
        for c in range(3):
            if grid[r][c] != 0 and grid[r][c+1] == grid[r][c]:
                grid[r][c] = (grid[r][c])*2
                score += grid[r][c]
                del grid[r][c+1]
                grid[r].append(0)
    return grid,score

def right(grid):
    score = 0
    for i in range(2):
        for r in range(4):
            for c in range(3,-1,-1):
                if grid[r][c] == 0:
                    del grid[r][c]
                    grid[r]=[0]+grid[r]
                    
    for r in range(4):
        for c in range(2,-1,-1):
            if grid[r][c] != 0 and grid[r][c+1] == grid[r][c]:
                grid[r][c+1] = grid[r][c+1]*2
                score += grid[r][c+1]
                del grid[r][c]
                grid[r]=[0]+grid[r]
    return grid,score
    

def shift(grid):
    newRow = []
    shiftGrid = []
    i = 0
    while i < 4:
        for r in grid:
            newRow.append(r[i])
        shiftGrid.append(newRow)
        newRow = []
        i += 1
    return shiftGrid

def up(grid):
    shiftGrid = shift(grid)
    newGrid,score = left(shiftGrid)
    grid = shift(newGrid)
    return grid, score

def down(grid):
    shiftGrid = shift(grid)
    newGrid,score = right(shiftGrid)
    grid = shift(newGrid)
    return grid,score

def printGrid(grid):
    for r in grid:
        for c in r:
            print(c, end = " ")
        print()

def testLegal(move):
    if move not in ["w","s","a","d"]:
        return False
    return True

def makeMove(grid,move):
    if move == "w":
        return up(grid)
    if move == "s":
        return down(grid)
    if move == "a":
        return left(grid)
    if move == "d":
        return right(grid)


def randomPlayer():
    print("Random player is playing 2048!")
    grid = addTwo(startGame())
    totalScore = 0
    printGrid(grid)
    print("The current score is:",totalScore)
    while gameState(grid) == "Game continues...":
        moveList = ["w","s","a","d"]
        i = randint(0,3)
        move = moveList[i]
        grid,addScore = makeMove(grid,move)
        totalScore += addScore
        grid = addTwo(grid)
        printGrid(grid)
        print("The current score is:",totalScore)
    print(gameState(grid))


def aiPlayer():
    print("AI player is playing 2048!")
    grid = addTwo(startGame())
    totalScore = 0
    printGrid(grid)
    print("The current score is:",totalScore)
    while gameState(grid) == "Game continues...":
        moveList = ["w","s","a","d"]
        maxScore = 0
        bestMove = "w"
        for move in moveList:
            gridCopy = []
            rowCopy = []
            for r in grid:
                for c in r:
                    rowCopy.append(c)
                gridCopy.append(rowCopy)
                rowCopy = []
            gridCopy,addScore = makeMove(gridCopy,move)
            if addScore > maxScore:
                maxScore = addScore
                bestMove = move
##        while not testLegal(move):
##            i = randint(0,3)
##            move = moveList[i]
        grid,addScore = makeMove(grid,bestMove)
        totalScore += addScore
        grid = addTwo(grid)
        printGrid(grid)
        print("The current score is:",totalScore)
    print(gameState(grid))
