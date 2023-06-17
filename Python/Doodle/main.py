import pygame
import random
pygame.init()

#game contents
white = (255, 255, 255)
black = (0 , 0, 0)
gray = (128, 128, 128)
WIDTH = 400
HEIGHT = 500
background = white

player = pygame.transform.scale(pygame.image.load('C:\\Users\\dhanu\\Desktop\\Tutorials\\Python\\Doodle\\doodle.jpg'), (90,70))
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

score = 0
high_score = 0
game_over = False

#game variables
player_x = 170
player_y = 400
platforms = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
jump = False
y_change = 0
x_change = 0
player_speed = 3
#display

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Doodle Jumper')

#update_player
def update_player(y_pos):
    global jump
    global y_change
    jump_height = 10
    gravity = .4
    if jump:
        y_change = -jump_height
        jump = False
    y_pos += y_change
    y_change += gravity
    return y_pos

def check_collision(rect_list, j):
    global player_x
    global player_y
    global y_change
    for i in range (len(rect_list)):
        if rect_list[i].colliderect([player_x + 30, player_y + 60, 35, 5]) and jump == False and y_change > 0:
            j = True
    return j

def update_platforms(list, y_pos, change):
    global score
    if y_pos < 250 and y_change < 0:
        for i in range(len(list)):
            list[i][1] -= change
    else:
        pass
    for item in range(len(list)):
        if list[item][1] > 500:
            list[item] = [random.randint(10, 320),random.randint(-50, -10), 70, 10]
            score += 1
    return list
                

#game loop

running = True
while running == True:
    timer.tick(fps)
    screen.fill(background)

    screen.blit(player,(player_x, player_y))
    blocks = []
    score_text = font.render('Score: ' + str(score), True, black, background)
    screen.blit(score_text, (320, 0))
    high_score_text = font.render('HighScore: ' + str(high_score), True, black, background)
    screen.blit(high_score_text, (0, 0))
    if game_over:
        game_over_text = font.render('Game Over! Hit Spacebar to restart', True, black, background)
        screen.blit(game_over_text, (65, 70))

    for i in range(len(platforms)):
        block = pygame.draw.rect(screen, black, platforms[i], 3,2)
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                score = 0
                player_x = 170
                player_y = 400
                background = white
                platforms = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]

            if event.key == pygame.K_a:
                x_change = -player_speed
            if event.key == pygame.K_d:
                x_change =  player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_change = 0
            if event.key == pygame.K_d:
                x_change = 0
            
    
    
    
    jump = check_collision(blocks, jump)
    player_x += x_change 

    if player_y < 440:
        player_y = update_player(player_y)
    else:
        game_over = True
        y_change = 0
        x_change = 0


    platforms = update_platforms(platforms, player_y, y_change)

    if x_change > 0:
        player = pygame.transform.scale(pygame.image.load('C:\\Users\\dhanu\\Desktop\\Tutorials\\Python\\Doodle\\doodle.jpg'), (90,70))
    elif x_change < 0:
        player = pygame.transform.flip(player, 1, 0)

    if score > high_score:
        high_score = score

    pygame.display.flip()
pygame.QUIT
