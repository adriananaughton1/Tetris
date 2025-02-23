from Board import GameBoard
import pygame


class BlockFactory:
    # Choose random black
    @staticmethod
    def CreateBlock(blockType):
        if blockType == "I":
            return I()
        elif blockType == "J":
            return J()
        elif blockType == "L":
            return L()
        elif blockType == "O":
            return O()
        elif blockType == "S":
            return S()
        elif blockType == "T":
            return T()
        elif blockType == "Z":
            return Z()
        elif blockType == "Ex_I":
            return Ex_I()
        elif blockType == "Ex_J":
            return Ex_J()


class Blocks:
    # parent class for all blocks
    def __init__(self, blockID):
        self.cellSize = 30  # size of grid cells
        self.block = blockID  # block ID number
        self.rotation = 0  # defines current rotation of block
        self.x = 0  # tracks current block's x axis location
        self.y = 0  # tracks current block's y axis location

    def GetBlockPos(self):
        return self.rotations[self.rotation]

    def GetBlockID(self):
        return self.block

    # pass in block colour
    def DrawBlock(self, gamePage, colour, x, y):
        # Colour active rotation cells in block grid
        for cell in self.rotations[self.rotation]:
            i, j = cell
            pygame.draw.rect(gamePage, colour, (j * self.cellSize + (self.x + x),
                                                i * self.cellSize + (self.y + y), self.cellSize - 1, self.cellSize - 1))

    def DropBlock(self):  # drop block down y axis by 1 cell
        self.y += self.cellSize


    def MoveLeft(self):  # move block left across x axis by 1 cell
        self.x -= self.cellSize

    def MoveRight(self):  # move block right across x axis by 1 cell
        self.x += self.cellSize

    def RotateBlock(self):  # rotate block
        old_rotation = self.rotation
        self.rotation = (self.rotation + 1) % len(self.rotations)
        newPosition = []
        # compare difference between positions
        for i in range(len(self.rotations[self.rotation])):
            new = []
            for j in range(len(self.rotations[self.rotation][i])):
                new.append(self.rotations[self.rotation][i][j] - self.rotations[old_rotation][i][j])
            newPosition.append(new)
        return newPosition

    def UndoRotation(self):
        self.rotation = (self.rotation - 1) % len(self.rotations)

    def GetBlockPos(self):
        return self.rotations[self.rotation]

    def GetRotations(self):
        return self.rotations

# Child classes for each block type
class I(Blocks):  # light blue
    def __init__(self):
        super().__init__(blockID=1)  # block number 1
        # defines the grid position of block for each rotation
        self.rotations = {
            0: [[0, 1], [1, 1], [2, 1], [3, 1]],
            1: [[1, 0], [1, 1], [1, 2], [1, 3]],
            2: [[0, 2], [1, 2], [2, 2], [3, 2]],
            3: [[2, 0], [2, 1], [2, 2], [2, 3]]

        }


class J(Blocks):  # blue
    def __init__(self):
        super().__init__(blockID=2)  # block number 2
        self.rotations = {
            0: [[0, 0], [1, 0], [1, 1], [1, 2]],
            1: [[0, 1], [0, 2], [1, 1], [2, 1]],
            2: [[1, 0], [1, 1], [1, 2], [2, 2]],
            3: [[0, 1], [1, 1], [2, 0], [2, 1]]
        }


class L(Blocks):  # orange
    def __init__(self):
        super().__init__(blockID=3)  # block number 3
        self.rotations = {
            0: [[0, 1], [1, 1], [2, 1], [2, 2]],
            1: [[1, 0], [1, 1], [1, 2], [2, 0]],
            2: [[0, 0], [0, 1], [1, 1], [2, 1]],
            3: [[0, 2], [1, 0], [1, 1], [1, 2]]
        }


class T(Blocks):  # purple
    def __init__(self):
        super().__init__(blockID=4)  # block number 4
        self.rotations = {
            0: [[0, 1], [1, 0], [1, 1], [1, 2]],
            1: [[0, 1], [1, 1], [1, 2], [2, 1]],
            2: [[1, 0], [1, 1], [1, 2], [2, 1]],
            3: [[0, 1], [1, 0], [1, 1], [2, 1]]
        }


class O(Blocks):  # yellow
    def __init__(self):
        super().__init__(blockID=5)  # block number 5
        self.rotations = {
            0: [[0, 0], [0, 1], [1, 0], [1, 1]]
        }


class S(Blocks):  # green
    def __init__(self):
        super().__init__(blockID=6)  # block number 6
        self.rotations = {
            0: [[0, 1], [0, 2], [1, 0], [1, 1]],
            1: [[0, 0], [1, 0], [1, 1], [2, 1]]
        }


class Z(Blocks):  # red
    def __init__(self):
        super().__init__(blockID=7)  # block number 7
        self.rotations = {
            0: [[0, 0], [0, 1], [1, 1], [1, 2]],
            1: [[0, 2], [1, 1], [1, 2], [2, 1]],
        }


class Ex_I(Blocks):  # light blue
    def __init__(self):
        super().__init__(blockID=1)  # block number 1
        # defines the grid position of block for each rotation
        self.rotations = {
            0: [[0, 1], [1, 1], [2, 1]],
            1: [[1, 0], [1, 1], [1, 2]]
        }


class Ex_J(Blocks):  # blue
    def __init__(self):
        super().__init__(blockID=2)  # block number 2
        self.rotations = {
            0: [[0, 0], [1, 0], [1, 1]],
            1: [[0, 0], [0, 1], [1, 0]],
            2: [[0, 0], [0, 1], [1, 1]],
            3: [[0, 1], [1, 0], [1, 1]]
        }