import os

import pygame
import sys
import random
import time

padwWidth = 480  # 게임화면의 가로크기
padHeight = 640  # 게임화면의 세로 크기
rockImage = ['Shooting/rock01.png', 'Shooting/rock02.png', 'Shooting/rock03.png', 'Shooting/rock04.png', 'Shooting/rock05.png', \
             'Shooting/rock06.png', 'Shooting/rock07.png', 'Shooting/rock08.png', 'Shooting/rock09.png', 'Shooting/rock10.png', \
             'Shooting/rock01.png', 'Shooting/rock02.png', 'Shooting/rock03.png', 'Shooting/rock04.png', 'Shooting/rock05.png', \
             'Shooting/rock06.png', 'Shooting/rock07.png', 'Shooting/rock08.png', 'Shooting/rock09.png', 'Shooting/rock10.png', \
             'Shooting/rock01.png', 'Shooting/rock02.png', 'Shooting/rock03.png', 'Shooting/rock04.png', 'Shooting/rock05.png', \
             'Shooting/rock06.png', 'Shooting/rock07.png', 'Shooting/rock08.png', 'Shooting/rock09.png', 'Shooting/rock10.png']


# 운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
    font = pygame.font.Font('Shooting/NanumGothic.ttf', 20)
    text = font.render('Point ' + str(count), True, (255, 255, 0))
    gamePad.blit(text, (10, 0))


# 운석이 화면 아래로 동과한 개수
def writePassed(count):
    global gamePad
    font = pygame.font.Font('Shooting/NanumGothic.ttf', 20)
    text = font.render('놓친 운석 수 ' + str(count), True, (255, 255, 0))
    gamePad.blit(text, (340, 0))


# 게임 메시지 출력
def writeMessage(text, count):
    global gamePad
    textfont = pygame.font.Font('Shooting/NanumGothic.ttf', 60)
    text = textfont.render(text, True, (255, 0, 0))
    count = textfont.render(f'{count}점', True, (255, 0, 0))
    textpos = text.get_rect()
    countpos = count.get_rect()
    textpos.center = (padwWidth / 2, padHeight / 2 - 100)
    countpos.center = (padwWidth / 2, padHeight / 2)
    gamePad.blit(text, textpos)
    gamePad.blit(count, countpos)
    pygame.display.update()
    os.system("pause")



# 전투기가 운석과 충돌했을 때 메시지 출력
def crash(count):
    global gamePad
    writeMessage('GAME OVER', count)


# 게임 오버 메시지 보이기
def gameOver(count):
    global gamePad
    writeMessage('GAME OVER', count)


# 게임에 등장하는 객체를 드로잉
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))


def initGame():
    global gamePad, clock, background, fighter, missile, explosion
    pygame.init()
    gamePad = pygame.display.set_mode((padwWidth, padHeight))
    pygame.display.set_caption('운석 깨기')  # 게임 이름
    background = pygame.image.load('Shooting/background.png')  # 배경 그림
    fighter = pygame.image.load('Shooting/fighter.png')  # 전투기 그림
    fighter = pygame.transform.scale(fighter, (140, 141))
    missile = pygame.image.load('Shooting/missile.png')  # 미사일 그림
    missile = pygame.transform.scale(missile, (20, 70))
    explosion = pygame.image.load('Shooting/explosion.png')  # 폭발 그림
    clock = pygame.time.Clock()


def runGame():
    global gamepad, clock, background, fighter, missile, explosion

    # 전투기 크기
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    # 전투기 초기 위치 (x, y)
    x = padwWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0

    # 무기 좌표 리스트
    missileXY = []

    # 운석 랜덤 생성
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size  # 운석 크기
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]

    # 운석 초기 위치 설정
    rockX = random.randrange(0, padwWidth - rockWidth)
    rockY = 0
    rockSpeed = 2

    # 전투기 미사일에 운석이 맞았을 경우 True
    isShot = False
    shotCount = 0
    rockPassed = 0

    f = open('shooting.txt', 'a', encoding='utf-8')
    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:  # 게임 프로그램 종료
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:  # 전투기를 왼쪽으로 이동
                    fighterX -= 5

                elif event.key == pygame.K_RIGHT:  # 전투기를 오른쪽으로 이동
                    fighterX += 5

                elif event.key == pygame.K_SPACE:  # 미사일 발사
                    missileX = x + fighterWidth / 2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0

        drawObject(background, 0, 0)  # 배경 화면 다시 그리기

        # 전투기 위치 재조정
        x += fighterX
        if x < 0:
            x = 0
        elif x > padwWidth - fighterWidth:
            x = padwWidth - fighterWidth

        # 전투기가 운석과 충돌했는지 체크
        if y < rockY + rockHeight:
            if (rockX > x and rockX < x + fighterWidth) or \
                    (rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth):
                now = time.localtime()
                save_time = "%04d년 %02d월 %02d일 %02d시 %02d분" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
                f.write(f'{save_time}\t{shotCount}\n')
                f.close()
                gameOver(shotCount)
                crash(shotCount)

        drawObject(fighter, x, y)  # 비행기를 게임 화면의 (x, y) 좌표에 그림

        if rockPassed == 3:  # 운석 3개 놓치면 게임 오버
            now = time.localtime()
            save_time = "%04d년 %02d월 %02d일 %02d시 %02d분" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            f.write(f'{save_time}\t{shotCount}\n')
            f.close()
            gameOver(shotCount)

        # 미사일 발사 화면에 그리기
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):  # 미사일 요소에대해 반복함
                bxy[1] -= 10  # 총알의 y좌표 - 10 (위로 이동)
                missileXY[i][1] = bxy[1]

                # 미사일이 운석을 맞추었을 경우
                if bxy[1] < rockY:
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1

                if bxy[1] <= 0:  # 미사일이 화면 밖을 벗어나면
                    try:
                        missileXY.remove(bxy)  # 미사일 제거
                    except:
                        pass

        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        # 운석 맞춘 점수 표시
        writeScore(shotCount)

        rockY += rockSpeed  # 운석 아래로 움직임

        # 운석이 지구로 떨어진 경우
        if rockY > padHeight:
            # 새로운 운석 (랜덤)
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padwWidth - rockWidth)
            rockY = 0
            rockPassed += 1

        # 놓친 운석 수 표시
        writePassed(rockPassed)

        # 운석을 맞춘 경우
        if isShot:
            # 운석 폭발
            drawObject(explosion, rockX, rockY)  # 운석 폭발 그리기

            # 새로운 운석 (랜덤)
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padwWidth - rockWidth)
            rockY = 0
            isShot = False

            # 운석 맞추면 속도 증가
            rockSpeed += 0.2
            if rockSpeed >= 10:
                rockSpeed = 10

        drawObject(rock, rockX, rockY)

        pygame.display.update()  # 게임화면을 다시그림

        clock.tick(60)  # 게임화면의 초당 프레임수를 60으로 설정

    pygame.quit()  # pygame 종료