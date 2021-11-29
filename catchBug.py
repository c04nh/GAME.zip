import pygame
import random
import time

def writeScore(count):
    global screen
    font = pygame.font.Font('Shooting/NanumGothic.ttf', 20)
    text = font.render('Point ' + str(count), True, (255, 255, 0))
    screen.blit(text, (10, 10))


def writeMessage(text, count):
    global screen
    textfont = pygame.font.Font('Shooting/NanumGothic.ttf', 60)
    text = textfont.render(text, True, (255, 0, 0))
    count = textfont.render(f'{count}점', True, (255, 0, 0))
    textpos = text.get_rect()
    countpos = count.get_rect()
    textpos.center = (480 / 2, 640 / 2 - 100)
    countpos.center = (480 / 2, 640 / 2)
    screen.blit(text, textpos)
    screen.blit(count, countpos)
    pygame.display.update()

def initGame():
    global BLACK, RED, YELLOW, WHITE, screen_width, screen_height, screen, done, clock
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    screen_width = 480
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("벌레 잡기")
    done = False
    clock = pygame.time.Clock()

def runGame():
    global BLACK, RED, YELLOW, WHITE, screen_width, screen_height, screen, done, clock
    pygame.init()
    small_font = pygame.font.Font('Shooting/NanumGothic.ttf', 20)
    score = 0
    start_time = int(time.time())
    remain_time = 0
    game_over = 0

    bug_image = pygame.image.load('bug.png')
    bug_image = pygame.transform.scale(bug_image, (70, 60))
    bugs = []
    for i in range(3):
        bug = pygame.Rect(bug_image.get_rect())
        bug.left = random.randint(0, screen_width)
        bug.top = random.randint(0, screen_height)
        dx = random.randint(-9, 9)
        dy = random.randint(-9, 9)
        bugs.append((bug, dx, dy))

    f = open('catchBug.txt', 'a', encoding='utf-8')
    while not done: 
        clock.tick(30)
        screen.fill(BLACK) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # [X] 종료키가 누르면, 게임 종료
                done=True
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over == 0:
                for (bug, dx, dy) in bugs:
                    if bug.collidepoint(event.pos):
                        bugs.remove((bug, dx, dy))
                        bug = pygame.Rect(bug_image.get_rect())
                        bug.left = random.randint(0, screen_width)
                        bug.top = random.randint(0, screen_height)
                        dx = random.randint(-9, 9)
                        dy = random.randint(-9, 9)
                        bugs.append((bug, dx, dy))
                        score += 1

        if game_over == 0:
            for (bug, dx, dy) in bugs:
                bug.left += dx
                bug.top += dy

            remain_time = 30 - (int(time.time()) - start_time)

            if remain_time <= 0:
                game_over = 1

        for (bug, dx, dy) in bugs:
            screen.blit(bug_image, bug)

        for (bug, dx, dy) in bugs:
            if not bug.colliderect(screen.get_rect()):
                bugs.remove((bug, dx, dy))
                bug = pygame.Rect(bug_image.get_rect())
                bug.left = random.randint(0, screen_width)
                bug.top = random.randint(0, screen_height)
                dx = random.randint(-9, 9)
                dy = random.randint(-9, 9)
                bugs.append((bug, dx, dy))

        writeScore(score)

        remain_time_image = small_font.render('Time {}'.format(remain_time), True, YELLOW)
        screen.blit(remain_time_image, (screen_width - 10 - remain_time_image.get_width(), 10))

        if game_over == 1:
            done = True
            now = time.localtime()
            save_time = "%04d년 %02d월 %02d일 %02d시 %02d분" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            f.write(f'{save_time}\t{score}\n')
            f.close()
            writeMessage('GAME OVER', score)
            time.sleep(3)

        pygame.display.update()

    pygame.quit()


