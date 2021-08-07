from .block import Block
import statistics

class MedianBlock(Block):

    def run(self, fixedWindow):
        return statistics.median(fixedWindow)

