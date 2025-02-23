import copy

class TetrisBeast:
    def __init__(self, boardLength):
        self.height = 20
        self.length = boardLength # 10
        self.board = None
        self.block1 = None
        self.block2 = None

        self.bestScore = None
        self.bestRotation = None
        self.bestOffset = None

        self.weights = [0.39357083734159515, -1.8961941343266449, -5.107694873375318, -3.6314963941589093, -2.9262681134021786, -2.146136640641482, -7.204192964669836, -3.476853402227247, -6.813002842291903, 4.152001386170861, -21.131715861293525, -10.181622180279133, -5.351108175564556, -2.6888972099986956, -2.684925769670947, -4.504495386829769, -7.4527302422826, -6.3489634714511505, -4.701455626343827, -10.502314845278828, 0.6969259450910086, -4.483319180395864, -2.471375907554622, -6.245643268054767, -1.899364785170105, -5.3416512085013395, -4.072687054171711, -5.936652569831475, -2.3140398163110643, -4.842883337741306, 17.677262456993276, -4.42668539845469, -6.8954976464473585, 4.481308299774875]
    
    def PrintBoard(self):
        # prints game board
        for i in range(self.height):
            for j in range(self.length):
                print(self.board[i][j], end=" ")
            print("\n")
        print("\n")

    def ColHeight(self, col):
        for i in range(self.height): # find height of column
            if self.board[i][col] != 0: # found height
                return self.height - i
        return 0

    def Heuristics(self):
        heights = [] # get current height of blocks on board 
        for j in range(self.length): # for each column
            heights.append(self.ColHeight(j))

        heightSum = sum(heights) # aggregate height

        # find number of holes
        holes = []
        for j in range(self.length): # for each column
            holeCount = 0 # hole count for each column
            for i in range(self.height): # find height of column
                if self.board[i][j] == 0 and (self.height - i < heights[j]): # if there is a hole in column
                    holeCount += 1
            holes.append(holeCount) 

        # find bumpiness of board
        bumps = []
        for i in range(len(heights)-1): # for each column height
            bumps.append(abs(heights[i] - heights[i+1])) # find differences in height

        # check if lines are completed
        lines = 0
        for i in range(self.height):
            if 0 not in self.board[i]:
                lines += 1

        maxHeight = max(heights)
        minHeight = min(heights)
        maxDepth = maxHeight - minHeight

        # calculate heuristic
        result = heights + [heightSum] + holes + bumps + [lines, maxDepth, maxHeight, minHeight]
        return result

    def ScorePosition(self, block, xOffset, rotation):
        blockLen = block[-1][1] + 1
        blockHeight = block[-1][0] + 1

        if xOffset + blockLen > self.length or xOffset < 0:  # block doesn't fit in board
            return
        
        # add x offset to block
        for coord in block: 
            coord[1] += xOffset 
        
        # find y offset
        yOffset = self.height - blockHeight 
        for coord in block: # find how far block can drop
            for y in range(self.height): # look through cell column
                if self.board[y][coord[1]] != 0 and y < yOffset: # find lowest point block can drop
                    yOffset = y

        # add y offset to block
        for coord in block:
            coord[0] += yOffset 

        # put block in temp board
        for i in range(len(block)): 
            x = block[i][0]
            y = block[i][1]
            self.board[x][y] = 8

        # score position based on board holes, bumpiness, lines cleared 
        score = sum([a*b for a,b in zip(self.Heuristics(), self.weights)])

        # update best score if necessary
        if self.bestScore == None or self.bestScore < score:
            self.bestScore = score
            self.bestOffset = xOffset
            self.bestRotation = rotation

        # undo grid for next test
        for i in range(len(block)): 
            x = block[i][0]
            y = block[i][1]
            self.board[x][y] = 0


    def RunAI(self, board, block1, block2, centre):
        moves = [] # store moves
        self.board = copy.deepcopy(board) # copy game board
        self.block1 = block1 # current block
        self.block2 = block2 # next block

        for rotation in range(len(self.block1)): # for each block rotation 
            for offset in range(self.length): # for the length of the board
                self.ScorePosition(self.block1[rotation], offset, rotation) # score each rotation of block in each grid position

        offset = self.bestOffset - centre # minus board centre

        # find moves that get block in best position
        for _ in range(1, self.bestRotation):
            moves.append("up")
        for _ in range(0, abs(offset)):
            if offset > 0:
                moves.append("right")
            else:
                moves.append("left")
        return moves
