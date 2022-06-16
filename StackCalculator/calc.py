"""
스택 계산기 계산 모듈

2021440099 이주형
2022 / 06 / 17
"""

import stackcalc as sc

class StackCalc:
    def __init__(self):
        self.expr = list()

    def clear(self):
        self.expr = []

    def append(self, elem):
        self.expr.append(elem)

    def getExpr(self):
        return self.expr

    def isEmpty(self):
        return len(self.expr) == 0

    def calc(self):
        return round(sc.evalPostfix(sc.Infix2Postfix(self.expr)), 10)

operator = ['+', '-', '*', '/']

def isConVal(exprs, key):
    """
    Is_Continued_Value\n
    두자리 이상의 숫자와 소수점을 판별하는 함수 \n
    :param exprs: 중위 표현식 리스트
    :param key: 연속되는지 확인할 값
    :return: True / False
    """
    if not exprs.isEmpty():
        if exprs.expr[-1] in operator and key in operator:
            raise Exception('연산자 오류!')              # 이 함수에서 연산자 연속 오류까지 확인함
        return exprs.expr[-1].replace('.', '').isnumeric() and key.isnumeric() or key == '.'
    else:
        return False

if __name__ == "__main__":
    expr = ['8', '/', '2', '-', '(', '3', '+', '3', '*', '2', ')']
    expr1 = StackCalc()
    for i in expr:
        expr1.append(i)
    print(expr1.getExpr())
    print(expr1.calc())
