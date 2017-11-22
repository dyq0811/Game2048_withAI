#Game2048
#Yingqi Halley Ding and Yiwen Starr Wang

from random import *
from graphics import *

def startGame(cellSize):
    grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    return grid

def gameState(grid):
    #check each positionin the grid 
    for row in range(4):
        for column in range(4):
            #if there is "2014", the player wins.
            if grid[row][column]==2048:
                return "You win!!"

            #if there is "0", the game continues.
            if grid[row][column]==0:
                return "Game continues..."

            #if the position has the same number with nearby position, the game continues.
            else:
                if row < 3:
                    if grid[row][column]==grid[row+1][column]:
                        return "Game continues..."
                if column < 3:
                    if grid[row][column]==grid[row][column+1]:
                        return "Game continues..."                       
                if row >= 1 :
                    if grid[row][column]==grid[row-1][column]:
                        return "Game continues..."
                if column >= 1:
                    if grid[row][column]==grid[row][column-1]:
                        return "Game continues..."

    #if all the tests above fails, the player lose the game
    return "You lose..."


def full(grid):
    for i in grid:
        for j in i:
            if j == 0:
                return False
    return True

def addTwo(grid):
    #generate a new "2"
    if full(grid):
        return grid
    else:
        r, c = randint(0,3), randint(0,3)
        while grid[r][c] != 0:
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
    
#convert columns into rows and reuse left/right algorithms above.
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

def drawAllGrids(grid,cellSize,win):           
    #write the text
    welcome= Text(Point(cellSize*2,cellSize *4.2),"Welcome to 2048! ")
    welcome.draw(win)
    listnumber=[]
    
    #draw the 4*4 matrix and the number
    for x in range(0,4*cellSize,cellSize):
        for y in range(0,4*cellSize,cellSize):
            number = grid[y//cellSize][x//cellSize]
            polygon = Rectangle(Point(x,y),Point(x+cellSize, y+cellSize))
            polygon.draw(win)
            
            if number!= 0:
                drawnumber = Text(Point(x+cellSize/2,y+cellSize/2),number)
                drawnumber.setSize(20)
                drawnumber.draw(win)
                listnumber.append(drawnumber)               
            if number == 0:
                color = color_rgb(255,255,255)
                polygon.setFill(color)
            if number == 2:
                color = color_rgb(255,252,139)
                polygon.setFill(color)
    return listnumber

def updateGrid(grid,cellSize,win,listnumber):
    for i in listnumber:
        i.undraw()
    listnumber = []
    for x in range(0,4*cellSize,cellSize):
        for y in range(0,4*cellSize,cellSize):
            polygon = Rectangle(Point(x,y),Point(x+cellSize, y+cellSize))
            polygon.draw(win)
            number = grid[y//cellSize][x//cellSize]

            if number!= 0:
                drawnumber = Text(Point(x+cellSize/2,y+cellSize/2),number)
                drawnumber.setSize(20)
                drawnumber.draw(win)
                listnumber.append(drawnumber)
            if number == 0:
                color = color_rgb(255,255,255)
                polygon.setFill(color)
            if number == 2:
                color = color_rgb(255,252,139)
                polygon.setFill(color)
            if number == 4:
                color = color_rgb(224,236,55)
                polygon.setFill(color)
            if number == 8:
                color = color_rgb(178,219,83)
                polygon.setFill(color)               
            if number == 16:
                color = color_rgb(88,188,73)
                polygon.setFill(color)                
            if number == 32:
                color = color_rgb(91,225,207)
                polygon.setFill(color)
            if number == 64:
                color = color_rgb(118,242,217)
                polygon.setFill(color)          
            if number == 128:
                color = color_rgb(149,220,225)
                polygon.setFill(color)
            if number == 256:
                color = color_rgb(101,191,236)
                polygon.setFill(color)
            if number == 512:
                color = color_rgb(139,172,238)
                polygon.setFill(color)
            if number == 1024:
                color = color_rgb(139,139,238)
                polygon.setFill(color)
            if number == 2048:
                color = color_rgb(197,152,225)
                polygon.setFill(color)
    return listnumber

def drawScore(score,win,cellSize):
    showscore = Text(Point(cellSize*2,cellSize *4.6),"Your current score is "+str(score))
    showscore.draw(win)
    return showscore

def updateScore(score,win,cellSize,showscore):
    showscore.undraw()
    showscore = Text(Point(cellSize*2,cellSize *4.6),"Your current score is "+str(score))
    showscore.draw(win)
    return showscore

def drawMakeAMove(win,cellSize):
    status = Text(Point(cellSize*2,cellSize *4.4),
                  "Please make your move(up/down/left/right) by entering w/s/a/d ")
    status.draw(win)
    showillegal = Text(Point(cellSize*2,cellSize *4.9),"")
    showillegal.draw(win)
    return status, showillegal

def drawIllegalMove(win,cellSize,status,showillegal):
    status.undraw()
    showillegal.undraw()   
    showillegal = Text(Point(cellSize*2,cellSize *4.4),"Please make a legal move.")
    showillegal.draw(win)
    return showillegal

def updateMakeMove(win,cellSize,status,showillegal):
    status.undraw()
    showillegal.undraw()
    status = Text(Point(cellSize*2,cellSize *4.4),
                  "Please make your move(up/down/left/right) by entering w/s/a/d ")
    status.draw(win)
    return status

def drawGameState(state,win,cellSize):
    showstate = Text(Point(cellSize*2,cellSize *4.8),state)
    showstate.draw(win)
    return showstate
    

def humanPlayer():
    cellSize = 100
    print("Welcome to 2048!")
    print("Please make your move(up/down/left/right) by entering w/s/a/d: ")
    grid = startGame(cellSize)
    grid = addTwo(grid)
    totalScore = 0
    printGrid(grid)
    
    win = GraphWin("2048",4*cellSize,5*cellSize) #create the window
    listnumber = drawAllGrids(grid,cellSize,win)  #draw the grid in the window
    showscore = drawScore(totalScore,win,cellSize) #draw the score in the window
    status,showillegal = drawMakeAMove(win,cellSize) #draw the making move command
    state = gameState(grid)
    showstate = drawGameState(state,win,cellSize)  #draw the game state

    while state == "Game continues...":
        move = input("Please enter your move: ")
        
        while not testLegal(move):
            showillegal = drawIllegalMove(win,cellSize,status,showillegal)
            move = input("Please make a legal move: ")

        status = updateMakeMove(win,cellSize,status,showillegal)
        grid,addScore = makeMove(grid,move)
        totalScore += addScore
        grid = addTwo(grid)
        printGrid(grid)

        listnumber = updateGrid(grid,cellSize,win,listnumber)              
        showscore = updateScore(totalScore,win,cellSize,showscore)   #show the score
        
        print("Your current score is:",totalScore)

    print(state)
    showstate.undraw()
    drawGameState(state,win,cellSize)


def AIisPlaying(win,cellSize):
    status = Text(Point(cellSize*2,cellSize *4.4),
                  "Artificial intelligence is playing the game!")
    status.draw(win)
    return status
    

def aiPlayer():
    cellSize = 100
    print("AI player is playing 2048!")
    grid = startGame(cellSize)
    grid = addTwo(grid)
    totalScore = 0
    printGrid(grid)
    print("The current score is:",totalScore)
    print()

    win = GraphWin("2048",4*cellSize,5*cellSize) #create the window
    listnumber = drawAllGrids(grid,cellSize,win)  #draw the grid in the window
    showscore = drawScore(totalScore,win,cellSize) #draw the score in the window
    AIisPlaying(win,cellSize) #draw "AI is playing the game!"
    state = gameState(grid)
    drawstate = drawGameState(state,win,cellSize) #draw the state of the game

    while state == "Game continues...":
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
        printGrid(grid)

        listnumber = updateGrid(grid,cellSize,win,listnumber)              
        showscore = updateScore(totalScore,win,cellSize,showscore) #draw the score in window

        state = gameState(grid)
       
        print("The current score is:",totalScore)
        print()
    print(state)
    drawstate.undraw()
    drawGameState(state,win,cellSize)

def main():
    player = input("human or AI?")
    if player == "human":
        humanPlayer()
    if player == "AI":
        aiPlayer()
main()
