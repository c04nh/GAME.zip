import pygame
import random
import time

pygame.init()

def initGame():
    global BLACK, RED, YELLOW, WHITE, large_font, small_font, screen_width, screen_height, screen, done, clock
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    large_font = pygame.font.SysFont('malgungothic', 36)
    small_font = pygame.font.SysFont('malgungothic', 25)
    screen_width = 480
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))

    done = False
    clock = pygame.time.Clock()

def runGame():
    global BLACK, RED, YELLOW, WHITE, large_font, small_font, screen_width, screen_height, screen, done, clock
    pygame.init()
    score = 0
    start_time = int(time.time())
    remain_time = 0
    game_over = 0

    bug_image = pygame.image.load('bug.png')
    bug_image = pygame.transform.scale(bug_image, (60, 80))
    bugs = []
    for i in range(3):
        bug = pygame.Rect(bug_image.get_rect())
        bug.left = random.randint(0, screen_width)
        bug.top = random.randint(0, screen_height)
        dx = random.randint(-9, 9)
        dy = random.randint(-9, 9)
        bugs.append((bug, dx, dy))

    f = open('catchBug.txt', 'a')
    while not done: 
        clock.tick(30)
        screen.fill(BLACK) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # [X] 종료키가 누르면, 게임 종료
                done=True
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over == 0:
                print(event.pos[0], event.pos[1])
                for (bug, dx, dy) in bugs:
                    if bug.collidepoint(event.pos):
                        print(bug)
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

            remain_time = 60 - (int(time.time()) - start_time)

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

        score_image = small_font.render('Point {}'.format(score), True, YELLOW)
        screen.blit(score_image, (10, 10))

        remain_time_image = small_font.render('Time {}'.format(remain_time), True, YELLOW)
        screen.blit(remain_time_image, (screen_width - 10 - remain_time_image.get_width(), 10))

        if game_over == 1:
            game_over_image = large_font.render('GameOver', True, RED)
            total_score = large_font.render('{}점'.format(score), True, RED)
            save_score_image = small_font.render('점수 저장', True, WHITE)
            screen.blit(game_over_image, (screen_width // 2 - game_over_image.get_width() // 2, screen_height // 2 - game_over_image.get_height() // 2 - 100))
            screen.blit(total_score, (screen_width // 2 - total_score.get_width() // 2, screen_height // 2 - total_score.get_height() // 2 - 50))
            screen.blit(save_score_image, (screen_width // 2 - save_score_image.get_width() // 2, screen_height // 2 - save_score_image.get_height() // 2 - 10))

            f.write(f'{score}\n')
            f.close()

        pygame.display.update()





# initGame()
# runGame()
# pygame.quit()


