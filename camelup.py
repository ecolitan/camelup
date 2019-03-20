import random

class Board():
    def __init__(self):
        self.moveNumber = 0
        self.boardSquares = [
            ["y", "b", "r", "g", "w"], [], [], [],
            [], [], [], [],
            [], [], [], [],
            [], [], [], [],
            [], [], [],
        ]
        self.dice = ["y", "b", "r", "g", "w"]
        random.shuffle(self.dice)

    def rollDice(self):
        try:
            camel = self.dice.pop()
        except IndexError:
            self.resetDice()
            camel = self.dice.pop()
        steps = random.shuffle([1,2,3]).pop()

        return (camel, steps)

    def resetDice(self):
        self.dice = ["y", "b", "r", "g", "w"]
        random.shuffle(self.dice)

    def takeTurn(self):
        camel, steps = self.rollDice()
        self.updateBoard(camel, steps)

    def updateBoard(self, camel, steps):

        # find camel square
        for square in self.boardSquares:
            if camel in square:
                camelsquare = self.boardSquares.index(square)

        # find camel place on square
        camelplace = self.boardSquares[camelsquare].index(camel)

        # what camels are moving
        movingcamels = self.boardSquares[camelsquare][camelplace::]

        # remove moving camels from last square
        for _ in range(len(movingcamels)):
            self.boardSquares[camelsquare].pop()

        # add moving camels to new square
        camelsquare += steps
        self.boardSquares[camelsquare].extend(movingcamels)

    def checkWin(self):
        for square in self.boardSquares[-3::]:
            if square:
                return True
        return False
