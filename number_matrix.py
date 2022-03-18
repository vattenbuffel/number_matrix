from Cell import Cell
from Node import Node

PLUS = 1
MIN = 2
MUL = 3
DIV = 4

operands = (PLUS, MIN, MUL)
n = 10
numbers = (1, 2, 3)

def matrix_to_img(matrix):
    raise NotImplementedError

def matrices_to_surf(matrices):
    raise NotImplementedError

def print_calculation(Cell:Cell):
    raise NotImplementedError

def evaluate(start_num, operands, numbers):
    end_num = start_num
    for i in range(len(operands)):
        operand = operands[i]
        num = numbers[i]

        if operand == PLUS:
            end_num = end_num + num
        elif operand == MIN:
            end_num = end_num - num
        elif operand == MUL:
            end_num = end_num * num
        elif operand == DIV:
            end_num = end_num / num
        else:
            raise NotImplementedError

    return end_num
    

def run(cell:Cell, matrix):
    # print_cell(cell)

    if cell.end_num == cell.start_num:
        return False

    i = [0]
    
    def build_tree(parent:Node, max_depth, goal_val, matrix, i):
        i[0] += 1
        depth = parent.depth + 1
        if depth == max_depth:
            return None

        for operand in operands:
            for num in numbers:
                child = Node(parent.end_num, depth, parent, operand, num)
                parent.children.append(child)
                child.end_num = evaluate(child.start_num, [operand], [num])

                if child.end_num == goal_val:
                    return child

                if (child.start_num, goal_val) in matrix and matrix[(child.start_num, goal_val)].best_num_operations + depth < max_depth:
                    child.end_cell = matrix[(child.start_num, goal_val)]
                    return child
                
        
        for child in parent.children:
            best_child = build_tree(child, max_depth, goal_val, matrix, i)
            if best_child is not None:
                return best_child
        
        return None
    

    node = Node(cell.start_num, 0, None, None, None)
    node.end_num = cell.start_num
    best_child = build_tree(node, cell.best_num_operations, cell.end_num, matrix, i)

    if best_child is None:
        return False

    # get operand order
    operand_order = []
    number_order = []
    while best_child.parent is not None:
        operand_order.insert(0, best_child.operand)
        number_order.insert(0, best_child.num)
        best_child = best_child.parent

    # See if best child lead to another cell
    if best_child.end_cell is not None:
        operand_order.extend(best_child.end_cell.best_operation_order)
        number_order.extend(best_child.end_cell.best_number_order)
    
    cell.best_num_operations = len(operand_order)
    cell.best_number_order = number_order
    cell.best_operation_order = operand_order

    assert evaluate(cell.start_num, cell.best_operation_order, cell.best_number_order) == cell.end_num

    return True



    

def print_matrix(matrix):
    s = " | "
    s += "\t".join([f"{i}" for i in range(n)])
    print(s)

    s = " | " + "".join(["-"]*n*6)
    print(s)

    for row in range(n):
        s = f"{row}| "
        s += "\t".join([f"{matrix[(row, col)].best_num_operations}" for col in range(n)])
       
        print(s)

def operations_to_str(operations):
    s = []
    for operation in operations:
        if operation == PLUS:
            s.append("+")
        elif operation == MIN:
            s.append("-")
        elif operation == MUL:
            s.append("*")
        elif operation == DIV:
            s.append("/")
        else:
            raise NotImplementedError
    
    return s

def print_cell(cell:Cell):
    print(f"Start_num: {cell.start_num}, goal_num: {cell.end_num}, best num operations: {cell.best_num_operations}")
    print(f"operands: {operations_to_str(cell.best_operation_order)}")
    print(f"numbers: {cell.best_number_order}")

def init():
    # TODO: Make it possible to randomly init the best operation order
    matrix = {(row,col):Cell(row, col) for row in range(n) for col in range(n)}
    for key in matrix:
        cell = matrix[key]
        d = cell.end_num - cell.start_num
        if d > 0:
            operand = PLUS
        elif d < 0:
            operand = MIN
        else:
            cell.best_operation_order = []
            cell.best_number_order = []
            cell.best_num_operations = 0
            continue

        cell.best_operation_order = [operand]*abs(d)
        cell.best_number_order = [1]*abs(d)
        cell.best_num_operations = abs(d)

    return matrix



matrix = init()
print("Init matrix:")
print_matrix(matrix)


improved = True
while improved:
    improved = False
    
    for key in matrix:
        cell = matrix[key]
        improved |= run(cell, matrix)

    print_matrix(matrix)

print_matrix(matrix)
tehoa = 5

