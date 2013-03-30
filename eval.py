from util import node,inorder_traverse,stack,make_operand
from parse import parse
import graphics as g
"""
Avaldise teisendamine AST'ks Dijkstra Shunting-Yard algoritmi abil
"""
# sisse:
# expr - avaldis millest ehitada puu
# välja - puu juur
def parse(expr):
    ops = { '+' : 1, '-' : 1,
            '*' : 2, '/' : 2,
            '^' : 3
          }
    pars = ['{','[','(','}',']',')']
    operations, operands = stack(), stack()
    operand = ''

    for char in expr:
        if (char not in ops) and (char not in pars):
            operand += char
        if char in ops:
            if not(operand == ''):
                operands.push(node(operand))
            operand = ''
            if not operations.empty() and operations.peak() not in pars:
                if (ops[operations.peak()] > ops[char]) or (ops[operations.peak()]==ops[char]):
                    operands.push(make_operand(operands.pop(),operands.pop(),operations))
            operations.push(char)
        if char in pars[0:3]:
            operations.push(char)
        if char in pars[3:len(pars)]:
            if not(operand == ''):
                operands.push(node(operand))
            operand = ''
            while operations.peak() not in pars[0:3]:
                operands.push(make_operand(operands.pop(),operands.pop(),operations))
            operations.pop()
    if len(operand) > 0:
        operands.push(node(operand))

    while not operations.empty():
        operands.push(make_operand(operands.pop(),operands.pop(),operations))

    return operands.pop() #Puu juure element on ainuke operandide magasinis olev element

def execute(node):
    if not(node.is_op):
        try:
            #Juhul kui tegemist pole operaatoriga siis on tegemist operandiga või muutujaga
            return int(node.data)
        #Juhul kui eelpoolne int() tõstatab ValueErrori
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

#Inorder läbimine AST joonistamiseks
def traverse_and_draw(window,element,posx,posy):
    if element == None: return None
    if(element.rbranch is not None):
        if element.rbranch.is_op:
            traverse_and_draw(window,element.lbranch,posx-40,posy+30)
        else:
            traverse_and_draw(window,element.lbranch,posx-20,posy+30)
    else:
        traverse_and_draw(window,element.lbranch,posx-20,posy+30)
    #Joonistamine
    draw_element(window,element.data,posx,posy)
    if(element.rbranch is not None):
        if element.rbranch.is_op:
            traverse_and_draw(window,element.rbranch,posx+40,posy+30)
        else:
            traverse_and_draw(window,element.rbranch,posx+20,posy+30)
    else:
        traverse_and_draw(window,element.rbranch,posx+20,posy+30)
    return True

def draw_element(window,data,posx,posy):
    global ON_SCREEN
    c=g.Circle(g.Point(posx,posy),10)
    c.draw(window)
    ON_SCREEN.push(c)
    c = g.Text(g.Point(posx,posy),data)
    c.draw(window)
    ON_SCREEN.push(c)

#Graafilise ekraani puhastamine
def clear_screen(window):
    while not ON_SCREEN.empty():
        ON_SCREEN.pop().undraw()

#Magasin hoidmaks ekraanil olevaid graafilisi elemente
ON_SCREEN = stack()
def main():
    graphics_switch = input("Graafilised puud? (Y/n): ")
    if(graphics_switch == "Y" or graphics_switch == "y"):
        win = g.GraphWin("Avaldise puud",400,300)
        draw_tree = True
    else:
        draw_tree = False
    print("Sisesta tehe / q lõpetamiseks")
    #Peamine lõpmatu kordus
    while(True):
        expression = input(">> ")
        if(expression == "q" or expression == "Q"):
            break
        if ON_SCREEN.size > 0:
            clear_screen(win)
        root = parse(expression)
        print(execute(root))
        if draw_tree:
            #Joonistame juur elemendi ning seejärel rekursiivselt ülejaanud puu
            draw_element(win,root.data,win.getWidth()//2,12)
            traverse_and_draw(win,root.lbranch,win.getWidth()//2-50,42)
            traverse_and_draw(win,root.rbranch,win.getWidth()//2+50,42)
        del root
    if draw_tree:
        win.close()
main()