from util import node, inorder_traverse, stack, make_operand
"""
Avaldise teisendamine AST'ks modifitseeritud Dijkstra Shunting-Yard algoritmi abil
"""

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

    return operands.pop()