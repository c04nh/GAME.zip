from tkinter import *
import operator

def shooting():
    label2 = Label(root, text='운석 깨기', font=('Shooting/NanumGothic.ttf', 22), fg='white', bg='black')  # 글씨 생성
    label2.place(x=0, y=100, relx=0.5, anchor="s", width = 200)  # 글씨 배치
    f = open("shooting.txt", 'r', encoding='utf-8')
    rank = {}
    top5 = []
    cnt = 0
    while True:
        line = f.readline()
        if not line: break
        arr = line.split("\t")
        rank[f'{arr[0]}'] = int(arr[1])
    ranking = sorted(rank.items(), key=operator.itemgetter(1), reverse=True)
    for key in ranking:
        top5.append(key)
        cnt += 1
        if cnt == 5: break
    rank0 = Label(root, text='등수', font=('Shooting/NanumGothic.ttf', 15), fg='white', bg='black')  # 글씨 생성
    rank0_time = Label(root, text='날짜, 시간', font=('Shooting/NanumGothic.ttf', 15), fg='white', bg='black')  # 글씨 생성
    rank0_score = Label(root, text='점수', font=('Shooting/NanumGothic.ttf', 15), fg='white', bg='black')  # 글씨 생성
    rank0.place(x=50, y=150, anchor="s")  # 글씨 배치
    rank0_time.place(x=240, y=150, anchor="s")  # 글씨 배치
    rank0_score.place(x=430, y=150, anchor="s")  # 글씨 배치
    rank1 = Label(root, text='1', font=('Shooting/NanumGothic.ttf', 15), fg='white', bg='black')  # 글씨 생성
    rank1_time = Label(root, text=f'{top5[0][0]}', font=('Shooting/NanumGothic.ttf', 15), fg='white', bg='black')  # 글씨 생성
    rank1_score = Label(root, text=f'{top5[0][1]}', font=('Shooting/NanumGothic.ttf', 15), fg='white', bg='black')  # 글씨 생성
    rank1.place(x=50, y=200, anchor="s")  # 글씨 배치
    rank1_time.place(x=240, y=200, anchor="s")  # 글씨 배치
    rank1_score.place(x=430, y=200, anchor="s")  # 글씨 배치
    rank2 = Label(root, text='2', font=('Shooting/NanumGothic.ttf', 15), fg='white', bg='black')  # 글씨 생성
    rank2_time = Label(root, text=f'{top5[1][0]}', font=('Shooting/NanumGothic.ttf', 15), fg='white', bg='black')  # 글씨 생성
    rank2_score = Label(root, text=f'{top5[1][1]}', font=('Shooting/NanumGothic.ttf', 15), fg='white', bg='black')  # 글씨 생성
    rank2.place(x=50, y=250, anchor="s")  # 글씨 배치
    rank2_time.place(x=240, y=250, anchor="s")  # 글씨 배치
    rank2_score.place(x=430, y=250, anchor="s")  # 글씨 배치
    f.close()

def bug():
    label2 = Label(root, text='벌레 잡기', font=('Shooting/NanumGothic.ttf', 22), fg='white', bg='black')  # 글씨 생성
    label2.place(x=0, y=100, relx=0.5, anchor="s", width = 200)  # 글씨 배치

def snakeGame():
    label2 = Label(root, text='스네이크 게임', font=('Shooting/NanumGothic.ttf', 22), fg='white', bg='black')  # 글씨 생성
    label2.place(x=0, y=100, relx=0.5, anchor="s", width = 200)  # 글씨 배치

def tetris():
    label2 = Label(root, text='테트리스', font=('Shooting/NanumGothic.ttf', 22), fg='white', bg='black')  # 글씨 생성
    label2.place(x=0, y=100, relx=0.5, anchor="s", width = 200)  # 글씨 배치

def exit():
    root.destroy()

def main():
    global root
    root = Tk()
    root.title("GAME.zip")  # 타이틀 지정
    root.resizable(False, False)  # 창 크기 조절 불가

    w = 480  # 창 가로
    h = 640  # 창 세로

    ws = root.winfo_screenwidth()  # 모니터 가로
    hs = root.winfo_screenheight()  # 모니터 세로

    # 모니터 가운데에 위치
    x = (ws / 2) - (w / 2) - 8  # x좌표
    y = (hs / 2) - (h / 2) - 31  # y좌표

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))  # 창 크기, 위치 지정
    root.configure(background='black')  # 배경색 지정

    btn1 = Button(root, text='운석 깨기', font=('Shooting/NanumGothic.ttf', 13), fg='red', command=shooting)  # 버튼 생성
    btn2 = Button(root, text='벌레 잡기', font=('Shooting/NanumGothic.ttf', 13), fg='red', command=bug)  # 버튼 생성
    btn3 = Button(root, text='테트리스', font=('Shooting/NanumGothic.ttf', 13), fg='red', command=tetris)  # 버튼 생성
    btn4 = Button(root, text='스네이크 게임', font=('Shooting/NanumGothic.ttf', 13), fg='red', command=snakeGame)  # 버튼 생성
    btn5 = Button(root, text='홈으로', font=('Shooting/NanumGothic.ttf', 16), fg='red', command=exit)  # 버튼 생성
    btn1.place(x=0, y=1, width=120, height=50)  # 버튼 배치
    btn2.place(x=120, y=1, width=120, height=50)  # 버튼 배치
    btn3.place(x=240, y=1, width=120, height=50)  # 버튼 배치
    btn4.place(x=360, y=1, width=120, height=50)  # 버튼 배치
    btn5.place(x=140, y=570, width=200, height=50)  # 버튼 배치