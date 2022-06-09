"""
hw-7
스택 계산기 gui 모듈

추가된 기능
키보드 입력
이전 계산값 불러오기
괄호

예정
삼각함수
에러 처리

2021440099 이주형
2022 / 06 / 03
"""

import calc
from tkinter import *

window = Tk()
window.title("PostfixCalc")
window.geometry("500x200")

button_list = [
    '7', '8', '9', '+', '-', 'sin',
    '4', '5', '6', '*', '/', 'cos',
    '1', '2', '3', '(', ')', 'tan',
    '0', '.', '=', 'C', 'MR', '']

key_map = {'Return': '=', 'plus': '+', 'minus': '-', 'asterisk': '*', 'slash': '/',
           'equal': '=', 'parenright': ')', 'parenleft': '(', 'period': '.'}

expr = calc.StackCalc()
s = 0
keyInp = 0

def keyB(event):
    global keyInp
    if event.keysym in button_list:
        click(event.keysym)
    elif event.keysym in key_map.keys():
        click(key_map.get(event.keysym))

def raiseError(e):
    display.delete(0, END)
    display.insert(END, e)
    print(e)
    expr.clear()

def click(key):
    global s
    try:
        if key == "=":
            result = expr.calc()
            print(result)
            s = str(result)
            display.insert(END, "=" + s)
        elif key == 'C':
            display.delete(0, END)
            expr.clear()
        elif key == 'MR':
            # 이전의 결과를 불러옴
            display.insert(END, s)
            expr.append(s)
        elif key in ['sin', 'cos', 'tan']:
            display.insert(END, key+'(')
        else:
            if calc.isConVal(expr, key):
                expr.expr[-1] += key
            else:
                expr.append(key)
            print(expr.getExpr())
            display.insert(END, key)
    except ZeroDivisionError:
        print('영으로 나누기 오류')
    except Exception as e:
        display.delete(0, END)
        display.insert(END, e)
        print(e)
        expr.clear()


display = Entry(window, width=50, bg="yellow")
display.grid(row=0, column=0, columnspan=5)
window.bind('<Key>', keyB)

row_index = 1
col_index = 0
for button_text in button_list:
    Button(window, text=button_text, width=8, height=2,
           command=lambda t=button_text: click(t)).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 5:
        row_index += 1
        col_index = 0

window.mainloop()
