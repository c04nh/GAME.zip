import pygame
import sys
import random
from time import sleep

padwWidth = 480  # 게임화면의 가로크기
padHeight = 640  # 게임화면의 세로 크기
rockImage = ['Shooting/rock01.png', 'Shooting/rock02.png', 'Shooting/rock03.png', 'Shooting/rock04.png', 'Shooting/rock05.png', \
             'Shooting/rock06.png', 'Shooting/rock07.png', 'Shooting/rock08.png', 'Shooting/rock09.png', 'Shooting/rock10.png', \
             'Shooting/rock11.png', 'Shooting/rock12.png', 'Shooting/rock13.png', 'Shooting/rock14.png', 'Shooting/rock15.png', \
             'Shooting/rock16.png', 'Shooting/rock17.png', 'Shooting/rock18.png', 'Shooting/rock19.png', 'Shooting/rock20.png', \
             'Shooting/rock21.png', 'Shooting/rock22.png', 'Shooting/rock23.png', 'Shooting/rock24.png', 'Shooting/rock25.png', \
             'Shooting/rock26.png', 'Shooting/rock27.png', 'Shooting/rock28.png', 'Shooting/rock29.png', 'Shooting/rock30.png']
explosionSound = ['Shooting/explosion01.wav', 'Shooting/explosion02.wav', 'Shooting/explosion03.wav', 'Shooting/explosion04.wav']


# 운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
    font = pygame.font.Font('Shooting/NanumGothic.ttf', 20)
    text = font.render('파괴한 운석 수: ' + str(count), True, (255, 255, 255))
    gamePad.blit(text, (10, 0))


# 운석이 화면 아래로 동과한 개수
def writePassed(count):
    global gamePad
    font = pygame.font.Font('Shooting/NanumGothic.ttf', 20)
    text = font.render('놓친 운석 수: ' + str(count), True, (255, 0, 0))
    gamePad.blit(text, (340, 0))


# 게임 메시지 출력
def writeMessage(text):
    global gamePad, gameOverSound
    textfont = pygame.font.Font('Shooting/NanumGothic.ttf', 80)
    text = textfont.render(text, True, (255, 0, 0))
    textpos = text.get_rect()
    textpos.center = (padwWidth / 2, padHeight / 2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()  # 배경 음악 정지
    gameOverSound.play()  # 게임 오버 사운드 재생
    sleep(2)
    pygame.mixer.music.play(-1)  # 배경 음악 재생
    runGame()


# 전투기가 운석과 충돌했을 때 메시지 출력
def crash():
    global gamePad
    writeMessage('전투기 파괴!')


# 게임 오버 메시지 보이기
def gameOver():
    global gamePad
    writeMessage('게임 오버!')


# 게임에 등장하는 객체를 드로잉
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))


def initGame():
    global gamePad, clock, background, fighter, missile, explosion, missileSound, gameOverSound
    pygame.init()
    gamePad = pygame.display.set_mode((padwWidth, padHeight))
    pygame.display.set_caption('PyShooting')  # 게임 이름
    background = pygame.image.load('Shooting/background.png')  # 배경 그림
    fighter = pygame.image.load('Shooting/fighter.png')  # 전투기 그림
    missile = pygame.image.load('Shooting/missile.png')  # 미사일 그림
    explosion = pygame.image.load('Shooting/explosion.png')  # 폭발 그림
    pygame.mixer.music.load('Shooting/music.wav')  # 배경 음악
    pygame.mixer.music.play(-1)  # 배경 음악 재생
    missileSound = pygame.mixer.Sound('Shooting/missile.wav')  # 미사일 사운드
    gameOverSound = pygame.mixer.Sound('Shooting/gameover.wav')  # 게임 오버 사운드
    clock = pygame.time.Clock()


def runGame():
    global gamepad, clock, background, fighter, missile, explosion, missileSound

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
    destroySound = pygame.mixer.Sound(random.choice(explosionSound))

    # 운석 초기 위치 설정
    rockX = random.randrange(0, padwWidth - rockWidth)
    rockY = 0
    rockSpeed = 2

    # 전투기 미사일에 운석이 맞았을 경우 True
    isShot = False
    shotCount = 0
    rockPassed = 0

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
                    missileSound.play()  # 미사일 사운드 재생
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
                crash()

        drawObject(fighter, x, y)  # 비행기를 게임 화면의 (x, y) 좌표에 그림

        if rockPassed == 7:  # 운석 7개 놓치면 게임 오버
            gameOver()

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
            destroySound.play()                  # 운석 폭발 사운드 재생

            # 새로운 운석 (랜덤)
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padwWidth - rockWidth)
            rockY = 0
            destroySound = pygame.mixer.Sound(random.choice(explosionSound))
            isShot = False

            # 운석 맞추면 속도 증가
            rockSpeed += 0.2
            if rockSpeed >= 10:
                rockSpeed = 10

        drawObject(rock, rockX, rockY)

        pygame.display.update()  # 게임화면을 다시그림

        clock.tick(60)  # 게임화면의 초당 프레임수를 60으로 설정

    pygame.quit()  # pygame 종료


