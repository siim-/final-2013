"""
Avaldiste jooksutamine puude abil
"""
from util import node,find_pivot,inorder_traverse
from parse import parse
"""
Avaldise teisendamine puuks mida on võimalik läbi inorderis ning viia ellu soovitud operatsioonid
"""
# def build_tree(expr):
#     operators = ['+','-','*','/',')','(']
#     ops = []
#     pos = 0
#     for char in expr:
#         if char in operators and char not in [')','(']:
#             ops.append([pos, char]) #Leiame kõik sooritatavad tehted
#         pos += 1
#     if(len(ops)>0):
#         pivot = find_pivot(ops) #Leiame potentsiaalse juurtehte millest asume puud ehitama
#         temp = node(ops[pivot][1],is_op=True)
#         #Rekursiivne puu ehitamine
#         temp.lbranch = build_tree(expr[0:ops[pivot][0]])
#         temp.rbranch = build_tree(expr[ops[pivot][0]+1:len(expr)])      
#         return temp
#     else: return node(expr) #Juhul kui puuduvad operaatorid siis lihtsalt loome uue sõlme arvuga
def execute(node):
    if not(node.is_op):
        try:
            #Juhul kui tegemist pole operaatoriga siis on tegemist operandiga või muutujaga
            return int(node.data)
        except ValueError:
            #Programm küsib kasutajalt puudu oleva muutuja
            return int(input("Muutuja {0}= ".format(node.data)))
    #Väärtuste saamine või rekursiivselt okste väärtuste arvutamine
    a = execute(node.lbranch)
    b = execute(node.rbranch)
    #Võimalikud operatsioonid
    return { '+' : a+b,
             '-' : a-b,
             '*' : a*b,
             '/' : a/b,}[node.data]

def main():
    print("Sisesta tehe:")
    #Peamine lõpmatu kordus
    while(True):
        expression = input(">> ")
        root = parse(expression)
        print(execute(root))
        del root
main()