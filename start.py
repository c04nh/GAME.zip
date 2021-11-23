from tkinter import *
import pygame
import PyShooting
import catchBug
import snake
import tetrisGame

pygame.init()

def shooting():
    PyShooting.initGame()
    PyShooting.runGame()

def bug():
    catchBug.initGame()
    catchBug.runGame()

def snack():
    snake.initGame()
    snake.runGame()

def tetris():
    tetrisGame.main()

root = Tk()
root.title("GAME.zip")  # 타이틀 지정
root.resizable(False, False)    # 창 크기 조절 불가

w = 480     # 창 가로
h = 640     # 창 세로

ws = root.winfo_screenwidth()   # 모니터 가로
hs = root.winfo_screenheight()  # 모니터 세로

# 모니터 가운데에 위치
x = (ws/2) - (w/2)  # x좌표
y = (hs/2) - (h/2)  # y좌효

root.geometry('%dx%d+%d+%d' % (w, h, x, y))     # 창 크기, 위치 지정
root.configure(background='black')  # 배경색 지정

label1 = Label(root, text='GAME.zip', font=('Arial', 65, 'bold'), fg='blue', bg='black')    # 글씨 생성
label1.place(x=0, y=200, relx=0.5, anchor="s")  # 글씨 배치
label2 = Label(root, text='게임을 선택하세요', font=('돋움', 22), fg='white', bg='black')  # 글씨 생성
label2.place(x=0, y=280, relx=0.5, anchor="s")   # 글씨 배치

btn1 = Button(root, text='운석 깨기', font=('돋움', 18), fg='red', command=shooting)     # 버튼 생성
btn2 = Button(root, text='벌레 잡기', font=('돋움', 18), fg='red', command=bug)     # 버튼 생성
btn3 = Button(root, text='테트리스', font=('돋움', 18), fg='red', command=tetris)     # 버튼 생성
btn4 = Button(root, text='스네이크 게임', font=('돋움', 18), fg='red', command=snack)     # 버튼 생성
btn1.place(x=0, y=360, relx=0.5, anchor="s", width=200, height=50)  # 버튼 배치
btn2.place(x=0, y=430, relx=0.5, anchor="s", width=200, height=50)  # 버튼 배치
btn3.place(x=0, y=500, relx=0.5, anchor="s", width=200, height=50)  # 버튼 배치
btn4.place(x=0, y=570, relx=0.5, anchor="s", width=200, height=50)  # 버튼 배치
label3 = Label(root, text='made by eunwon and nahyun', font=('Arial', 15), fg='white', bg='black')  # 글씨 생성
label3.pack(side="bottom", anchor="e", pady=15, padx=10)    # 글씨 배치



root.mainloop()