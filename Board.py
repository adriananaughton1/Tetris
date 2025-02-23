import pygame



class GameBoard:

    def __init__(self, boardWidth):  # updated cols to 10
        # Board dimensions
        self.cols = boardWidth
        self.rows = 20  # initialise rows to 20
        self.cellSize = 30
        self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]

    def GetBoard(self):
        return self.grid

    def setField(self):
        from ConfigurePage import ConfigurePage
        configurePage = ConfigurePage()
        self.cols = configurePage.getField()

    def PrintBoard(self):
        # Display the game board in the console
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.grid[i][j], end=" ")
            print("\n")

    def Colours(self):
        # Tetris block colors
        # 0 index is for empty cells
        return [
            (25, 30, 40),  # Dark grey (for empty cells)
            (21, 204, 209),  # Light blue
            (13, 64, 216),  # Blue
            (226, 116, 17),  # Orange
            (166, 0, 247),  # Purple
            (237, 234, 4),  # Yellow
            (47, 230, 23),  # Green
            (232, 18, 18)  # Red
        ]

    def DrawBoard(self, gamePage):
        # Render the board
        for i in range(self.rows):
            for j in range(self.cols):
                cellColour = self.grid[i][j]
                pygame.draw.rect(gamePage, self.Colours()[cellColour], (
                    j * self.cellSize + 50, i * self.cellSize + 100,
                    self.cellSize - 1, self.cellSize - 1))

    def PlaceBlock(self, blockCells):
        # Determine initial position for a new block
        blockPosition = []
        center = self.cols // 2 - 2
        for cell in blockCells:

            blockPosition.append([cell[0], cell[1] + center])
        return blockPosition

    def IsValidPosition(self, cells):
        # Check if cells are within board boundaries and not colliding with other blocks
        for cell in cells:
            if cell[0] < 0 or cell[0] >= self.rows or cell[1] < 0 or cell[1] >= self.cols:
                return False
            if self.grid[cell[0]][cell[1]] != 0:
                return False
        return True

    def LockBlock(self, cells, blockID):
        # Assign the block cells to the grid and remove full rows if any
        for cell in cells:
            self.grid[cell[0]][cell[1]] = blockID
        removed_lines = self.RemoveFullRows()

        return removed_lines

    def RemoveFullRows(self):
        # Check and remove full rows
        rows_to_remove = []
        for i in range(self.rows):
            if all(self.grid[i][j] != 0 for j in range(self.cols)):
                rows_to_remove.append(i)

        # If any full rows found, remove and shift above rows down
        lines_removed = len(rows_to_remove)  # Count of removed rows for scoring
        for row in reversed(rows_to_remove):
            del self.grid[row]
            self.grid.insert(0, [0 for _ in range(self.cols)])

        return lines_removed