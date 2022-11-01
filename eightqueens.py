# To run and interpret output -- 
# To use typical command line prompts for python to run the file ex. Windows "python eightqueens.py" and Mac "python3.x eightqueens.py" x being the version of python you have on your mac
# From there if the output is taking too long terminate the run time and run again. Continue until the runtime is less than 2 seconds
# To interpret the output all queens are in tuple positions x pos is the row and the y is the column. If it doesnt get the correct output it will return (none)
# This solution will run a majority of the time

import random
class NQueens:
    def __init__(self,n):
        self.board, self.qPosit  = self.getNewBoard(n)
        self.n = n

    def getNewBoard(self,n):
        board = []
        qPos = []
        for x in range(n):
            board.append([0]*n)

        for x in range(n):
            ranIx = random.randint(0,n-1)
            board[x][ranIx] = 1
            qPos.append( (x,ranIx) )

        return (board,qPos)

    def allQueensSafe(self):
        for pos in self.qPosit:
            if(self.UnderAttack(pos)):
                return False
        return True

    def attackViaCol(self,pos):
        for queen in self.qPosit:
            if(pos[1] == queen[1] and queen != pos):
                return True
        return False

    def attackViaRow(self,pos):
        for queen in self.qPosit:
            if(pos[0] == queen[0] and queen != pos):
                return True
        return False

    def attackViaDiagonal(self,pos):
        for queen in self.qPosit:
            if (abs(queen[0] - pos[0]) == abs(queen[1] - pos[1]) and queen != pos):
                return True
        return False

    def UnderAttack(self,position):
        if(self.attackViaDiagonal(position)):
            return True

        if(self.attackViaRow(position)):
            return True

        if(self.attackViaCol(position)):
            return True

        return False

    def specificQueenConflicts(self,pos):
        assert pos in self.qPosit
        count = 0
        for queen in self.qPosit:
            if (abs(queen[0] - pos[0]) == abs(queen[1] - pos[1]) and queen != pos):
                count += 1

            if (pos[0] == queen[0] and queen != pos):
                count += 1

            if (pos[1] == queen[1] and queen != pos):
                count += 1

        return count

    def pickRandomQueen(self):
        newIndex = random.randint(0,self.n - 1)
        return self.qPosit[newIndex]

    def printBoard(self):
        for queen in self.qPosit:
            print(queen)


    def moveQueen(self,startPos,endPos):
        assert self.board[startPos[0]][startPos[1]] == 1
        self.board[startPos[0]][startPos[1]] = 0
        self.board[endPos[0]][endPos[1]] = 1
        self.qPosit.remove(startPos)
        self.qPosit.append(endPos)

    def availablePositions(self,pos):
        availablePos = []
        for x in range(self.n):
            availablePos.append( (pos[0],x) )

        return availablePos

n = 8
pro = NQueens(n)
while(not pro.allQueensSafe()):
    minAttacks = n + 1
    pickedQueen = pro.pickRandomQueen() 

    positions = pro.availablePositions(pickedQueen)
    minConflictPosition = (-1,-1)
    for pos in positions:
        pro.moveQueen(pickedQueen,pos)
        newNumberOfConflicts = pro.specificQueenConflicts(pos)
        if(newNumberOfConflicts < minAttacks ):
            minConflictPosition = pos
            minAttacks = newNumberOfConflicts
        pro.moveQueen(pos,pickedQueen)

    pro.moveQueen(pickedQueen,minConflictPosition)

print(pro.printBoard())   
    
