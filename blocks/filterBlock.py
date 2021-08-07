from .block import Block

class FilterBlock(Block):
    
    def __init__(self, predicate):
        self.predicate = predicate


    def run(self, num):
        if self.predicate(num):
            return num

