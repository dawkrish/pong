import pygame
import random
pygame.init()

# VARIABLES
WIDTH, HEIGHT = 800,600
black_color = (0,0,0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()  # will be used for FPS & Stuff
running = True

#menu
menu_screen = True
game_screen = False
game_mode = ""

#Paddles 
paddle_width = 15
paddle_height = 175
paddle_speed_1 = 9
paddle_speed_2 = 9
paddle_score_1 = 0
paddle_score_2 = 0

paddle_surface_1 = pygame.Surface((paddle_width,paddle_height))
paddle_surface_2 = pygame.Surface((paddle_width,paddle_height))

paddle_rect_1 = paddle_surface_1.get_rect(center = (10,HEIGHT//2))
paddle_rect_2 = paddle_surface_2.get_rect(center = (WIDTH-10,HEIGHT//2))

#Ball
ball_width = 20
ball_height  = 20
ball_speed_x = 7
ball_speed_y = 7

ball_surface = pygame.Surface((ball_width,ball_height))
ball_rect = ball_surface.get_rect(center = (WIDTH//2, HEIGHT//2))


#font
def display_score():
    retro_font = pygame.font.Font('retrofont.ttf',45)
    score_surface = retro_font.render(f"{paddle_score_1} : {paddle_score_2}",True,black_color)
    score_rect = score_surface.get_rect(center = (WIDTH//2,50))
    screen.blit(score_surface,score_rect)

def display_menu_text():
    retro_font = pygame.font.Font('retrofont.ttf',30)
    menu_text_1_surface = retro_font.render(f"Press SPACE for Single Player",True,black_color)
    menu_text_2_surface = retro_font.render(f"Press ENTER for Multi Player",True,black_color)
    menu_text_1_rect = menu_text_1_surface.get_rect(center = (WIDTH//2, 200))
    menu_text_2_rect = menu_text_2_surface.get_rect(center = (WIDTH//2, 300))
    screen.blit(menu_text_1_surface,menu_text_1_rect)
    screen.blit(menu_text_2_surface,menu_text_2_rect)

#ball reset to center
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball_rect.center = (WIDTH//2, random.randrange(100,HEIGHT-100))
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))


# GAME LOOP STARTS
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if menu_screen:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_mode = "single"
            menu_screen = False
            game_screen = True
        if keys[pygame.K_RETURN]:
            game_mode = "multiplayer"
            menu_screen = False
            game_screen = True

        screen.fill("white")
        display_menu_text()
        
    elif game_screen:
        if game_mode == "single" : 
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                paddle_rect_2.y += paddle_speed_2
            if keys[pygame.K_UP]:
                paddle_rect_2.y -= paddle_speed_2
            
            #top boundary
            if paddle_rect_2.y <= 0:
                paddle_rect_2.y = 0
            #bottom boundary
            if paddle_rect_2.y + paddle_height >= HEIGHT:
                paddle_rect_2.y = HEIGHT - paddle_height
            
            #paddle 1 automatic movement...
            paddle_rect_1.y += paddle_speed_1
            if paddle_rect_1.y <= 0 or paddle_rect_1.y + paddle_height >= HEIGHT:
                paddle_speed_1 *= -1

        if game_mode == "multiplayer":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                paddle_rect_1.y -= paddle_speed_1
            if keys[pygame.K_s]:
                paddle_rect_1.y += paddle_speed_1
            if keys[pygame.K_UP]:
                paddle_rect_2.y -= paddle_speed_2
            if keys[pygame.K_DOWN]:
                paddle_rect_2.y += paddle_speed_2
            
            #top boundary
            if paddle_rect_1.y <= 0:
                paddle_rect_1.y = 0
            if paddle_rect_2.y <= 0:
                paddle_rect_2.y = 0
            #bottom boundary
            if paddle_rect_1.y + paddle_height >= HEIGHT:
                paddle_rect_1.y = HEIGHT - paddle_height
            if paddle_rect_2.y + paddle_height >= HEIGHT:
                paddle_rect_2.y = HEIGHT - paddle_height
    
        #ball movement
        ball_rect.x += ball_speed_x
        ball_rect.y += ball_speed_y
        
        #if ball hits the paddle 
        if ball_rect.colliderect(paddle_rect_1):
            ball_speed_x *= -1
            ball_speed_y*= random.choice((1,-1))
        if ball_rect.colliderect(paddle_rect_2):
            ball_speed_x *= -1
            ball_speed_y*= random.choice((1,-1))

        #if ball goes to either left or Right wall, then increase the score respectively
        if ball_rect.x > WIDTH :
            paddle_score_1 += 1
            ball_restart()
        if ball_rect.x < 0:
            paddle_score_2 += 1
            ball_restart()
        #if ball hits bottom or top wall, reverse the direction
        if ball_rect.y <= 0 or ball_rect.y + ball_height >= HEIGHT:
            # ball_speed_x *= -1
            ball_speed_y *= -1
        
        screen.fill("white")
        screen.blit(paddle_surface_1,paddle_rect_1) #bliting paddle 1
        screen.blit(paddle_surface_2,paddle_rect_2) #bliting paddl 2
        display_score()
        screen.blit(ball_surface,ball_rect)

    pygame.display.update()
    clock.tick(60)

#GAME LOOP ENDS
pygame.quit()
