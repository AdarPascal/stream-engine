from .block import Block

class SumBlock(Block):

    def run(self, fixedWindow):
        return sum(fixedWindow)

