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



#Paddles {Paddle 1 : CPU, Paddle 2 : User}
paddle_width = 20
paddle_height = 175
paddle_speed_1 = 9
paddle_speed_2 = 9
paddle_score_1 = 0
paddle_score_2 = 0

paddle_surface_1 = pygame.Surface((paddle_width,paddle_height))
paddle_surface_2 = pygame.Surface((paddle_width,paddle_height))

paddle_rect_1 = paddle_surface_1.get_rect(center = (30,HEIGHT//2))
paddle_rect_2 = paddle_surface_2.get_rect(center = (WIDTH-30,HEIGHT//2))

#Ball
ball_width = 20
ball_height  = 20
ball_speed_x = 10
ball_speed_y = 10

ball_surface = pygame.Surface((ball_width,ball_height))
ball_rect = ball_surface.get_rect(center = (WIDTH//2, HEIGHT//2))


#font
def display_score():
    retro_font = pygame.font.Font('retrofont.ttf',45)
    score_surface = retro_font.render(f"{paddle_score_1} : {paddle_score_2}",True,black_color)
    score_rect = score_surface.get_rect(center = (WIDTH//2,50))
    screen.blit(score_surface,score_rect)

# GAME LOOP STARTS
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
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
  
    #ball movement
    ball_rect.x += ball_speed_x
    
    #if ball hits the paddle 
    if ball_rect.colliderect(paddle_rect_1):
        ball_speed_x *= -1
    if ball_rect.colliderect(paddle_rect_2):
        ball_speed_x *= -1
        

    #if ball goes to either wall, then increase the score respectively
    if ball_rect.x > WIDTH :
        paddle_score_1 += 1
        ball_rect.center = (WIDTH//2,random.randrange(100,HEIGHT-100))
    if ball_rect.x < 0:
        paddle_score_2 += 1
        ball_rect.center = (WIDTH//2, random.randrange(100,HEIGHT-100))

    
    screen.fill("white")
    screen.blit(paddle_surface_1,paddle_rect_1) #bliting paddle 1
    screen.blit(paddle_surface_2,paddle_rect_2) #bliting paddl 2
    display_score()
    screen.blit(ball_surface,ball_rect)
    pygame.display.update()
    clock.tick(60)

#GAME LOOP ENDS
pygame.quit()
