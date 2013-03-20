#Mingisugune stack
#2013 01
class element:
    def __init__(self,info,prev_node):
        self.info = info
        self.prev = prev_node

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
            ##print("Empty stack!")
            return None
        return self.current.info

    def pop(self):
        if(self.current == None):
            print("Empty stack! Can't pop")
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
        


