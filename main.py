from blocks.inputBlock import InputBlock
from blocks.filterBlock import FilterBlock
from blocks.fixedWindowBlock import FixedWindowBlock
from blocks.sumBlock import SumBlock
from blocks.medianBlock import MedianBlock
from blocks.outputBlock import OutputBlock

def run_block(Block, args):
    return Block.run(args)


def run_pipeline(pipeline):
    next = None
    blocksAmount = len(pipeline)
    blockInProccess = 0

    while blockInProccess < blocksAmount:
        result = run_block(pipeline[blockInProccess], next)
        if result:
            next = result
            blockInProccess += 1
        else:
            next = None
            blockInProccess = 0

def main():
    pipeline = [InputBlock(), FilterBlock(lambda i: i > 0), FixedWindowBlock(2), SumBlock(), FixedWindowBlock(3), MedianBlock(), OutputBlock()]
    run_pipeline(pipeline)

if __name__ == "__main__":
    main()