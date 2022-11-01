import random
class NQueens:
    def __init__(self,n):
        self.board, self.qPosit  = self.getNewBoard(n)
        self.n = n

    def getNewBoard(self,n):
    # queens are represented as ones in 2d list of all zeros
    # Since it's a 2d list, each element is a row of zeros except for the queen
        board = []
        qPos = []
        for x in range(n): # makes n x n board of zeros
            board.append([0]*n)

        for x in range(n): # sets a random value of each row to be 1, denoting the queen
            ranIx = random.randint(0,n-1)
            board[x][ranIx] = 1
            qPos.append( (x,ranIx) )

        return (board,qPos)

    def allQueensSafe(self): # returns true if problem is solved and all queens safe, false otherwise
        for pos in self.qPosit:
            if(self.UnderAttack(pos)):
                return False
        return True

    def attackViaCol(self,pos):
        for queen in self.qPosit:
            if(pos[1] == queen[1] and queen != pos): # last inqueality checks to make sure you arent comparing the same queen
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

    def specificQueenConflicts(self,pos): # returns number of pieces attacking queen at position pos
        assert pos in self.qPosit # checks to make sure given position is a queen
        count = 0
        for queen in self.qPosit:
            if (abs(queen[0] - pos[0]) == abs(queen[1] - pos[1]) and queen != pos):
                count += 1

            if (pos[0] == queen[0] and queen != pos):
                count += 1

            if (pos[1] == queen[1] and queen != pos):
                count += 1

        return count

    def pickRandomQueen(self): # returns position of random queen
        newIndex = random.randint(0,self.n - 1)
        return self.qPosit[newIndex]

    def printBoard(self): # prints out all positions of queens
        for queen in self.qPosit:
            print(queen)


    def moveQueen(self,startPos,endPos): # moves queen from startpos to endpos
        assert self.board[startPos[0]][startPos[1]] == 1
        # above assert will fail if the start position does not have a queen
        self.board[startPos[0]][startPos[1]] = 0
        self.board[endPos[0]][endPos[1]] = 1
        self.qPosit.remove(startPos)
        self.qPosit.append(endPos)

    def availablePositions(self,pos):
        # returns list of tuples with all positions queen can go
        availablePos = []
        for x in range(self.n):
            availablePos.append( (pos[0],x) )

        return availablePos

n = 8
pro = NQueens(n)
timer = 0
while(not pro.allQueensSafe()):
    minAttacks = n + 1 # n + 1 is greater than any possibility of attacks so this is guaranteed to get minimized
    pickedQueen = pro.pickRandomQueen() 

    positions = pro.availablePositions(pickedQueen)
    minConflictPosition = (-1,-1)
    for pos in positions: # iterate through all positions of pickedQueen and move to position of minimum conflict
        pro.moveQueen(pickedQueen,pos)
        newNumberOfConflicts = pro.specificQueenConflicts(pos)
        if(newNumberOfConflicts < minAttacks ):
            minConflictPosition = pos
            minAttacks = newNumberOfConflicts
        pro.moveQueen(pos,pickedQueen) # move queen back

    pro.moveQueen(pickedQueen,minConflictPosition)# move queen to least conflict spot

print(pro.printBoard())