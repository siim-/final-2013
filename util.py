
class node:
    def __init__(self, data, is_op=False,lbranch=None,rbranch=None):
        self.data = data #andmed
        self.rbranch = rbranch #Parem oks
        self.lbranch = lbranch #Vasak oks
        self.is_op = is_op #operaatori või operandi märge

#Puu inorder läbimine alates etteantud sõlmest
def inorder_traverse(node):
    if node == None: return None
    inorder_traverse(node.lbranch)
    print(node.data,end='')
    inorder_traverse(node.rbranch)

#Funktsioon leidmaks nn. juur operatsiooni
def find_pivot(ops):
    pivot = len(ops)//2
    if(ops[pivot][1] in ['*','/']):
        for i in range(0,len(ops)):
            if ops[i][1] in ['+','-']: return i
    return pivot