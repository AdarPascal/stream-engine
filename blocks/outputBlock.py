from .block import Block

class OutputBlock(Block):

    def run(self, num):
        print(num)
        return num

