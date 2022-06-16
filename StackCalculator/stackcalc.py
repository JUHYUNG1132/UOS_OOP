from Stackbycompo import *
from math import *

if int(input("0 = Composition // 1 = Inheritance = ")):    # composition과 inherit 중 선택
    from StackbyInherit import *
else:
    from Stackbycompo import *

def evalPostfix(expr):
    """
    후위 식 연산
    :param expr: 계산할 식(후위), 리스트
    :return: 계산 결과, 값
    """
    s = Stack()
    for token in expr:
        if token in "()":
            pass
        elif token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if token == '+':
                s.push(val1 + val2)
            elif token == '-':
                s.push(val1 - val2)
            elif token == '*':
                s.push(val1 * val2)
            elif token == '/':
                s.push(val1 / val2)
        ##########################################
        elif token == 'sin':                        # 삼각함수 수정
            s.push(sin(radians(s.pop())))
        elif token == 'cos':
            s.push(cos(radians(s.pop())))
        elif token == 'tan':
            s.push(tan(radians(s.pop())))
        ##########################################
        else:
            s.push(float(token))

    return s.pop()

if __name__ == '__main__':
    expr1 = ['8', '2', '/', '3', '-', '(', '3', '2', '*', '+']
    expr2 = ['1', '2', '/', '4', '*', '1', '4', '/', '*']
    print(expr1, ' --> ', evalPostfix(expr1))
    print(expr2, ' --> ', evalPostfix(expr2))


# ----------------------------------------------------------------------

def precedence(op):
    """
    연산자 우선순위 판별
    :param op: 판별할 요소
    :return: -1 / 0 / 1 / 2 우선순위 값
    (클수록 우선순위 높음)
    """
    if op == '(' or op == ')':
        return 0
    ###########################################################
    elif op == '+' or op == '-' or op in ['sin', 'cos', 'tan']: # 삼각함수 수정
        return 1
    ###########################################################
    elif op == '*' or op == '/':
        return 2
    else:
        return -1


def Infix2Postfix(expr):
    """
    중위식을 후위식으로 변환 \n
    :param expr: 중위 수식, 리스트 \n
    :return: 후위 수식으로 변환 결과, 리스트
    """
    s = Stack()     # 연산자 저장용
    output = []
    for term in expr:
        if term in '(':
            s.push(term)

        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)

        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if precedence(term) <= precedence(op):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)
###########################################
        elif term in ['sin', 'cos', 'tan']:     #삼각함수 수정
            s.push(term)
###########################################
        else:
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    print(output)
    return output

if __name__ == '__main__':
    infix1 = ['8', '/', '2', '-', '(', '3', '+', '3', '*', '2', ')']
    infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']
    postfix1 = Infix2Postfix(infix1)
    postfix2 = Infix2Postfix(infix2)
    # Infix2Postfix()
    result1 = evalPostfix(postfix1)
    result2 = evalPostfix(postfix2)
    print('  중위표기: ', infix1)    # ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
    print('  후위표기: ', postfix1)  # ['8', '2', '/', '3', '-', '3', '2', '*', '+']
    print('  계산결과: ', result1, end='\n\n')
    print('  중위표기: ', infix2)
    print('  후위표기: ', postfix2)
    print('  계산결과: ', result2)
