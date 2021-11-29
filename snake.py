import pygame # 1. pygame 선언
import random
from datetime import datetime
from datetime import timedelta
import time
 
pygame.init() # 2. pygame 초기화

def initGame():
    global BLACK, RED, GREEN, size, screen, done, clock, last_moved_time, KEY_DIRECTION, large_font, small_font
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    size = [480,640]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("스네이크 게임")
    large_font = pygame.font.Font('Shooting/NanumGothic.ttf', 60)
    small_font = pygame.font.Font('Shooting/NanumGothic.ttf', 20)
    done= False
    clock= pygame.time.Clock()
    last_moved_time = datetime.now()

    KEY_DIRECTION = {
        pygame.K_UP: 'N',
        pygame.K_DOWN: 'S',
        pygame.K_LEFT: 'W',
        pygame.K_RIGHT: 'E',
    }
 
def draw_block(screen, color, position):
    block = pygame.Rect((position[1] * 20, position[0] * 20),
                        (20, 20))
    pygame.draw.rect(screen, color, block)
 
class Snake:
    def __init__(self):
        self.positions = [(0,2),(0,1),(0,0)]  # 뱀의 위치
        self.direction = ''
 
    def draw(self):
        for position in self.positions: 
            draw_block(screen, GREEN, position)
 
    def move(self):
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'N':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'S':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'W':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'E':
            self.positions = [(y, x + 1)] + self.positions[:-1]
 
    def grow(self):
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'N':
            self.positions.append((y - 1, x))
        elif self.direction == 'S':
            self.positions.append((y + 1, x))
        elif self.direction == 'W':
            self.positions.append((y, x - 1))
        elif self.direction == 'C':
            self.positions.append((y, x + 1))    
 
 
class Apple:
    def __init__(self, position=(5, 5)):
        self.position = position
 
    def draw(self):
        draw_block(screen, RED, self.position)
 
# 4. pygame 무한루프
def runGame():
    global BLACK, RED, GREEN, size, screen, done, clock, last_moved_time, KEY_DIRECTION
    #게임 시작 시, 뱀과 사과를 초기화
    snake = Snake() 
    apple = Apple()

    count = 0

    f = open('snake.txt', 'a', encoding='utf-8')
    while not done:
        clock.tick(10)
        screen.fill(BLACK)

        snake.draw()
        apple.draw()
        # score_str = str(count).zfill(6)
        # score_image = large_font.render(score_str,True, (0, 255, 0))
        # screen.blit(score_image, (350, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_DIRECTION:
                    snake.direction = KEY_DIRECTION[event.key]

        score_image = small_font.render('Point {}'.format(count), True, (255, 255, 0))
        screen.blit(score_image, (10, 10))
 
        if timedelta(seconds=0.1) <= datetime.now() - last_moved_time:
            snake.move()
            last_moved_time = datetime.now()
 
        if snake.positions[0] == apple.position:
            snake.grow()
            count += 1
            apple.position = (random.randint(0, 19), random.randint(0, 19))
        
        if snake.positions[0] in snake.positions[1:]:
            done = True
            game_over_image = large_font.render('GAME OVER', True, RED)
            total_score = large_font.render('{}점'.format(count), True, RED)
            screen.blit(game_over_image, (480 // 2 - game_over_image.get_width() // 2, 640 // 2 - game_over_image.get_height() // 2 - 100))
            screen.blit(total_score, (480 // 2 - total_score.get_width() // 2, 640 // 2 - total_score.get_height() // 2))

            now = time.localtime()
            save_time = "%04d년 %02d월 %02d일 %02d시 %02d분" % (
            now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            f.write(f'{save_time}\t{count}\n')
            f.close()

        pygame.display.update()

# initGame()
# runGame()
pygame.quit()
