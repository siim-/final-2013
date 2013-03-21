#Puu nn. leht või oks
class node:
    def __init__(self, data, is_op=False,lbranch=None,rbranch=None):
        self.data = data #andmed
        self.rbranch = rbranch #Parem oks
        self.lbranch = lbranch #Vasak oks
        self.is_op = is_op #operaatori või operandi märge
#Magasiniga seonduv elemendi class
class element:
    def __init__(self,info,prev_node):
        self.info = info
        self.prev = prev_node

#Puu inorder läbimine alates etteantud sõlmest
def inorder_traverse(node):
    if node == None: return None
    inorder_traverse(node.lbranch)
    print(node.data,end='')
    inorder_traverse(node.rbranch)

#Programmis kasutatav magasini class
class stack:
    def __init__(self):
        self.current = None
        self.size = 0

    def push(self,string):
        n = element(string,self.current)
        self.current = n
        self.size += 1

    def peak(self):
        if(self.current == None):
            return None
        return self.current.info

    def pop(self):
        if(self.current == None):
            return None

        temp = self.current
        self.current = temp.prev
        r_value = temp.info
        del temp
        self.size -=1
        return r_value

    def print_stack(self):
        item = self.current
        i=0
        while item is not None:
            print("{1}: {0}".format(repr(item.info),i),end='\n')
            i+=1
            item = item.prev

    def empty(self):
        return True if self.current == None else False

def make_operand(right_operand,left_operand,operations):
    if not(left_operand.rbranch == None) and not(left_operand.rbranch.is_op) and left_operand.data not in ['*','/','^'] and operations.peak() not in ['*','/','^']:
        left_operand.rbranch = node(operations.pop(),True,left_operand.rbranch,right_operand)
        return left_operand
    else:
        return node(operations.pop(),True,left_operand,right_operand)