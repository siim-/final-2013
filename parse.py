from util import node, inorder_traverse
from stack import stack
expr = "a+b+c"

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
            operands.push(node(operand))
            operand = ''
            if not operations.empty() and operations.peak() not in pars:
                if (ops[operations.peak()] > ops[char]) or (ops[operations.peak()]==ops[char]):
                    right_operand, left_operand = operands.pop(), operands.pop()
                    if not(left_operand.rbranch == None) and not(left_operand.rbranch.is_op):
                        left_operand.rbranch = node(operations.pop(),True,left_operand.rbranch,right_operand)
                        operands.push(left_operand)
                    else:
                        operands.push(node(operations.pop(),True,left_operand,right_operand))
            operations.push(char)
        if char in pars[0:3]:
            operations.push(char)
        if char in pars[3:len(pars)]:
            operands.push(node(operand))
            operand = ''
            while not operations.peak() in pars[0:3]:
                right_operand, left_operand = operands.pop(), operands.pop()
                operands.push(node(operations.pop(),True,left_operand,right_operand))
            operations.pop()

    if len(operand) > 0:
        operands.push(node(operand))

    while not operations.empty():
        right_operand, left_operand = operands.pop(), operands.pop()
        if not(left_operand.rbranch == None) and not(left_operand.rbranch.is_op):
            left_operand.rbranch = node(operations.pop(),True,left_operand.rbranch,right_operand)
            operands.push(left_operand)
        else:
            operands.push(node(operations.pop(),True,left_operand,right_operand))

    return operands.pop()
