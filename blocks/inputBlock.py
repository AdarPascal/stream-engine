from .block import Block

class InputBlock(Block):
    
    def run(self, arguments = None):
        try:
            inputVal = input()
            print(f'> {inputVal}')
            return int(inputVal)
        except ValueError:
            print(f'Error: Input is not valid')

