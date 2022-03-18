from Cell import Cell

class Node:
    def __init__(self, val, depth, parent, operand, num):
        self.start_num = val
        self.depth = depth
        self.parent = parent
        self.operand = operand
        self.num = num
        
        self.end_num = None
        self.children = []
        self.end_cell:Cell = None