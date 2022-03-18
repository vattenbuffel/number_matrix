class Cell:
    def __init__(self, start_num, end_num):
        self.start_num = start_num
        self.end_num = end_num

        self.best_operation_order = None
        self.best_number_order = None
        self.best_num_operations = None
