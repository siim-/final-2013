class node:
    def __init__(self, data, parent=None, is_op=False):
        self.data = data
        self.rbranch = None
        self.lbranch = None
        self.is_op = False
        self.parent = parent

class tree:
    def __init__(self):
        self.root = None