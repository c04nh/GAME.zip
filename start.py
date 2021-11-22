from tkinter import *

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
label1.pack(pady='70')  # 글씨 배치 (y좌표 외부 패딩 70)
label1 = Label(root, text='게임을 선택하세요', font=('Arial', 20), fg='white', bg='black')  # 글씨 생성
label1.pack()   # 글씨 배치

root.mainloop()