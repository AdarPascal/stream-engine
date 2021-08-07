from .block import Block

class FixedWindowBlock(Block):

    def __init__(self, maxSize):
        self.window = []
        self.maxSize = maxSize


    def run(self, num):
        if len(self.window) < self.maxSize:
            self.window.append(num)
            if len(self.window) == self.maxSize:
                copy = self.window
                self.window = []
                return copy

