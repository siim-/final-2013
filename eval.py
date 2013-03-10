"""
Avaldiste jooksutamine puude abil
"""

expression = 'a+b+c+d'

def parse_expression(expr):
    operators = ['+','-','*','/']
    operations = []
    pos = 0
    for char in expr:
        if char == ' ':
            continue
        if char in operators:
            operations.append([pos,char])
        pos += 1
    return operations

ops = parse_expression(expression)
print(ops[round(len(ops)/2)-1])