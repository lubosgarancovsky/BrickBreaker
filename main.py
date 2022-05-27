#!/usr/bin/env python
import pygame
import object
import main_menu
import sound
import texts

pygame.font.init()

lost_game = False
FPS = 60
(BLACK) = (0,0,0)
(WIDTH, HEIGHT) = (900, 600)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")
gameIcon = pygame.image.load("Assets/brick.png")
pygame.display.set_icon(gameIcon)

brick_img = pygame.image.load("Assets/brick.png").convert_alpha()
game_BG = pygame.image.load("Assets/gameBG.png").convert_alpha()

sound_player = sound.Sound()
text_display = texts.Texts()

pad = object.Pad(WIDTH, HEIGHT)
ball = object.Ball(WIDTH,HEIGHT)
bricks = []


LOST_TEXT = text_display.endgame_font.render("You Lost", False, (200, 10, 10))
WON_TEXT = text_display.endgame_font.render("You Won", False, (10, 200, 10))

menu = main_menu.Menu()

# 5 17
def create_bricks():
    for y in range(5):
        for x in range(17):
            bricks.append(object.Brick(x, 2*y))

def delete_bricks(bricks):
    bricks.clear()


def draw_bricks(bricks):
    i = 0
    if len(bricks) > 0:
        for brick in bricks:
            bricks[i].draw(screen)
            screen.blit(brick_img, (bricks[i].brick.x, bricks[i].brick.y))
            i+=1
    else:
        won()



def check_collisions():
    global lost_game

    ball_top = ball.ball.y
    ball_bottom = ball.ball.y + ball.size
    ball_left = ball.ball.x
    ball_right= ball.ball.x + ball.size

    pad_top = pad.pad.y
    pad_bottom = pad.pad.y + pad.pad.height
    pad_left = pad.pad.x
    pad_right = pad.pad.x + pad.pad.width

    #ball and walls
    if ball_top <= 0:
        ball.y_dir *= -1
        sound_player.play_wall_bounce()
    if ball_bottom >= HEIGHT:
        lost_game = True
    if ball_left <= 0 or ball_right >= WIDTH:
        ball.x_dir *= -1
        sound_player.play_wall_bounce()

    #ball and pad
    collision_tollerance = 10
    if pad.pad.colliderect(ball.ball):
        if abs(pad_top - ball_bottom) < collision_tollerance:
            ball.y_dir *= -1
        if abs(pad_bottom - ball_top) < collision_tollerance:
            ball.y_dir *= -1
        if abs(pad_left - ball_right) < collision_tollerance:
            ball.x_dir *= -1
        if abs(pad_right - ball_left) < collision_tollerance:
            ball.x_dir *= -1
        sound_player.play_pad_bounce()

    i = 0
    for brick in bricks:
        if ball.ball.colliderect(brick.brick):
            brick_top = brick.brick.y
            brick_bottom = brick.brick.y + brick.brick.height
            brick_left = brick.brick.x
            brick_right = brick.brick.x + brick.brick.width

            #brick collision
            if abs(ball_top - brick_bottom) < collision_tollerance:
                ball.y_dir *= -1
            if abs(ball_bottom - brick_top) < collision_tollerance:
                ball.y_dir *= -1
            if abs(ball_left - brick_right) < collision_tollerance:
                ball.x_dir *= -1
            if abs(ball_right - brick_left) < collision_tollerance:
                ball.x_dir *= -1
  
            sound_player.play_brick_bounce()
            bricks.remove(brick)
            i += 1



def reset_game():
    delete_bricks(bricks)
    create_bricks()
    ball.reset()
    pad.reset()


def lost():
    global lost_game
    screen.blit(LOST_TEXT, (300, HEIGHT//2))
    pygame.display.update()
    sound_player.play_lost_round()
    pygame.time.wait(3000)
    lost_game = False
    menu.inMenu = True
    reset_game()

def won():
    print("Game Won")
    screen.blit(WON_TEXT, (300, HEIGHT//2))
    pygame.display.update()
    pygame.time.wait(4000)
    menu.inMenu = True
    reset_game()

def main():
    create_bricks()
    sound_player.play_game_song()
    run = True
    clock = pygame.time.Clock()
    while run:
        screen.fill(BLACK)
        clock.tick(FPS)
        if menu.inMenu:
            menu.draw(screen, BLACK, 60)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_ESCAPE]:
                menu.inMenu = True

            if not lost_game:
                if not menu.inMenu:
                    screen.blit(game_BG, (0, 0))
                    
                    pad.draw(screen)
                    pad.move(keys_pressed)

                    ball.draw(screen)
                    ball.move()

                    draw_bricks(bricks)
                    check_collisions()
                    pygame.display.update()
            else:
                lost()
                

if __name__ == "__main__":
    main()