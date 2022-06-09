"""
hw-8
스택 계산기 gui 모듈

====추가된 기능====
    키보드 입력
    이전 계산값 불러오기
    괄호
    OOP 적용
    삼각함수            (단, 삼각함수 뒤에 * / 가 있을 경우 오작동)
    에러 처리

2021440099 이주형
2022 / 06 / 09
"""

import calc
from tkinter import *
import math


class MyCalc:
    button_list = [
        '7', '8', '9', '+', '-', 'sin',
        '4', '5', '6', '*', '/', 'cos',
        '1', '2', '3', '(', ')', 'tan',
        '0', '.', '=', 'C', 'MR', '']

    key_map = {'Return': '=', 'plus': '+', 'minus': '-', 'asterisk': '*', 'slash': '/',
               'equal': '=', 'parenright': ')', 'parenleft': '(', 'period': '.',
               's': 'sin', 'c': 'cos', 't': 'tan'}

    def __init__(self):
        self.window = Tk()
        self.window.title("MyCalc")
        self.window.geometry('450x200')
        self.expr = calc.StackCalc()            # 계산기 모듈 클래스
        self.s = 0                              # 직전 계산 결과 저장 변수
        self.display = Entry(self.window, width=50, bg='white', state=DISABLED)
        self.display.grid(row=0, column=0, columnspan=5)
        self.window.bind('<Key>', self.keyB)    # 키보드 입력 Callback 함수와 연결
        self.parant_integrity = 0               # 소괄호 오류 확인용 변수

    def myEntry(self, text='', op=0):
        """
        엔트리 키보드 중복입력 버그 방지용\n
        이 함수를 통해 엔트리의 텍스트 접근
        :param text: 삽입할 텍스트
        :param op: 0=> insert, 1=> clear
        """
        self.display.configure(state=NORMAL)
        if not op:
            self.display.insert(END, text)
        else:
            self.display.delete(0, END)
        self.display.configure(state=DISABLED)


    def initGUI(self):
        row_index = 1
        col_index = 0
        for buttonText in MyCalc.button_list:
            Button(self.window, text=buttonText, width=8, height=2, bg='white',
                   command=(lambda t=buttonText: self.click(t))).grid(row=row_index, column=col_index)
            col_index += 1
            if col_index > 5:
                row_index += 1
                col_index = 0
        self.window.mainloop()

    def keyB(self, event):
        """
        키보드입력 콜백 함수\n
        :param event: 키보드 이벤트
        :return: X
        """
        if event.keysym in MyCalc.button_list:
            self.click(event.keysym)
        elif event.keysym in MyCalc.key_map.keys():
            self.click(MyCalc.key_map.get(event.keysym))

    def raiseError(self, e):
        """
        에러 핸들러
        :param e: 에러 명
        :return: X
        """
        self.myEntry(op=1)
        self.myEntry(e)
        print(e)
        self.expr.clear()

    def click(self, key):
        try:
            if key == '=':                      # '=' 처리
                if not self.parant_integrity:   # 괄호 오류 없을경우 결과 계산하고 저장 후 display
                    result = self.expr.calc()
                    print(result)
                    self.s = str(result)
                    # self.display.insert(END, "=" + self.s)
                    self.myEntry('='+self.s)
                else:                           # 소괄호 오류가 있을 경우
                    print(self.parant_integrity)
                    raise Exception('소괄호 오류!')
            elif key == 'C':                    # 'Clear' 처리
                # self.display.delete(0, END)   # 결과값 s 제외 모두 초기화
                self.myEntry(op=1)
                self.expr.clear()
                self.parant_integrity = 0
            elif key == 'MR':                   # 'Memory Recall' 처리
                # self.display.insert(END, self.s)
                self.myEntry(self.s)
                self.expr.append(self.s)
            elif key in ['sin', 'cos', 'tan']:  # 삼각함수 처리, 괄호까지 추가됨
                self.expr.append(key)
                self.expr.append('(')
                # self.display.insert(END, key + '(')
                self.myEntry(key+'(')
                self.parant_integrity += 1
            else:                               # 숫자와 괄호 처리(연속된 숫자인지 판별)
                if calc.isConVal(self.expr, key):
                    self.expr.expr[-1] += key
                else:
                    if key == '(':
                        self.parant_integrity += 1
                    elif key == ')':
                        self.parant_integrity -= 1
                    self.expr.append(key)
                print(self.expr.getExpr())
                # self.display.insert(END, key)
                self.myEntry(key)

        except ZeroDivisionError:

            self.raiseError('영으로 나누기 오류!')

        except Exception as e:
            self.raiseError(e)


calcOBJ = MyCalc()
calcOBJ.initGUI()
