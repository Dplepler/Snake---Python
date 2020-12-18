import pygame
import sys
import random

#|-------------------------------------------------------------------------------------|
#|First game I ever made, sorry for no documantation (didn't know it existed back then)|
#|-------------------------------------------------------------------------------------|

def pause(screen, white, pink, height, width, clock):
    paused = True
    paused_text = "Paused"
    paused_text_2 = "Press SPACE to continue"
    font = pygame.font.SysFont("comicsansms", 80)
    font_2 = pygame.font.SysFont("comicsansms", 40)
    while paused:
        screen.fill(white)
        pause_label = font.render(paused_text, 1, pink)
        pause_label2 = font_2.render(paused_text_2, 1, pink)
        screen.blit(pause_label, (width // 3, height // 3))
        screen.blit(pause_label2, (width // 4, height // 3 + 80))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
        pygame.display.update()
        clock.tick(10)


def new_food(screen, pink):
    location_food_x = random.randint(1, 79) * 10
    location_food_y = random.randint(1, 59) * 10
    pygame.draw.rect(screen, pink, (location_food_x, location_food_y, 10, 10))
    return location_food_x, location_food_y


def grow(tail, direction, player_size):
    pp = []

    x = tail[len(tail) - 1][0]
    y = tail[len(tail) - 1][1]

    if direction == 'up':
        pp = [x, y - player_size]
    elif direction == 'down':
        pp = [x, y + player_size]
    elif direction == "right":
        pp = [x + player_size, y]
    elif direction == "left":
        pp = [x - player_size, y]
    tail.append(pp)


def food_function(screen, pink, location_food_x, location_food_y):
    pygame.draw.rect(screen, pink, (location_food_x, location_food_y, 10, 10))


def check_food(tail, location_food_x, location_food_y):
    if tail[len(tail) - 1][0] == location_food_x and tail[len(tail) - 1][1] == location_food_y:
        return True

    return False


def fail_check(tail, width, height):
    i = 0
    if tail[- 1][1] <= 0 or tail[-1][1] >= height or tail[-1][0] <= 0 or tail[- 1][0] >= width:
        return True
    while i < len(tail)-3:
        if tail[len(tail) - 1][0] == tail[i][0] and tail[len(tail) - 1][1] == tail[i][1]:
            return True
        else:
            i += 1

    return False


def update(tail, direction, player_size, screen, white):

    tail = tail[1:]

    x = tail[len(tail) - 1][0]
    y = tail[len(tail) - 1][1]

    if direction == "up":
        pp1 = [x, y - player_size]
    elif direction == "down":
        pp1 = [x, y + player_size]
    elif direction == "right":
        pp1 = [x + player_size, y]
    elif direction == "left":
        pp1 = [x - player_size, y]

    tail.append(pp1)

    for i in range(len(tail)):
        pygame.draw.rect(screen, white, (tail[i][0], tail[i][1], player_size, player_size))
        
    return tail


def main():
    pygame.init()
    width = 800
    height = 600
    background = [105, 105, 105]
    white = [255, 255, 255]
    screen = pygame.display.set_mode((width, height))
    screen.fill(background)
    game_over = False
    clock = pygame.time.Clock()
    player_size = 10
    direction = "right"
    pink = [206, 40, 81]
    x = width // 2
    y = height // 2
    location_food_x = random.randint(1, 79) * 10
    location_food_y = random.randint(1, 59) * 10
    speed = 1
    score = 0
    text = "Score: " + str(score)
    yellow = 255, 255, 0
    myfont = pygame.font.SysFont("monospace", 35)
    tail = [[x - 3 * player_size, y], [x - 2 * player_size, y], [x - player_size, y], [x, y]]
    while not game_over:
        label = myfont.render(text, 1, yellow)
        screen.blit(label, (width - 200, height - 40))
        food_function(screen, pink, location_food_x, location_food_y)
        tail = update(tail, direction, player_size, screen, white)
        if fail_check(tail, width, height):
            sys.exit()
        if check_food(tail, location_food_x, location_food_y):
            location_food_x, location_food_y = new_food(screen, pink)
            grow(tail, direction, player_size)
            score += 10
            text = "Score: " + str(score)
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key_pressed = event.key
                if key_pressed == pygame.K_w:
                    if direction != "down":
                        direction = "up"

                elif key_pressed == pygame.K_s:
                    if direction != "up":
                        direction = "down"

                elif key_pressed == pygame.K_d:
                    if direction != "left":
                        direction = "right"

                elif key_pressed == pygame.K_a:
                    if direction != "right":
                        direction = "left"
                elif event.key == pygame.K_p:
                    pause(screen, white, pink, height, width, clock)
                    
        pygame.display.update()
        clock.tick(20)
        screen.fill(background)

if __name__ == "__main__":
    main()