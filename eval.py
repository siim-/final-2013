"""
Avaldiste jooksutamine puude abil
"""
from util import node,inorder_traverse
from parse import parse
"""
Avaldise teisendamine puuks mida on võimalik läbi inorderis ning viia ellu soovitud operatsioonid
"""
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
             '/' : a/b,
             '^' : a**b }[node.data]

def main():
    print("Sisesta tehe:")
    #Peamine lõpmatu kordus
    while(True):
        expression = input(">> ")
        root = parse(expression)
        print(execute(root))
        del root
main()