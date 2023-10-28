import pygame

pygame.init()

p1color = [255, 0, 0]
screen = pygame.display.set_mode([1024, 500])

isBar1MovingUp = False
isBar1MovingDown = False

isBar2MovingDown = False
isBar2MovingUp = False

bar1_y = 30
bar2_y = 30

ball_x = 512
ball_y = 250




ball_speedX = 0
ball_speedY = 0

while True:

    screen.fill([0,0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                isBar1MovingUp = True
            elif event.key == pygame.K_s:
                isBar1MovingDown = True

            if event.key == pygame.K_UP:
                isBar2MovingUp = True
            elif event.key == pygame.K_DOWN:
                isBar2MovingDown = True


            if event.key == pygame.K_SPACE:
                ball_x = 512
                ball_y = 250

                ball_speedX = 0.2
                ball_speedY = 0.2

            

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                isBar1MovingUp = False
            elif event.key == pygame.K_s:
                isBar1MovingDown = False


            if event.key == pygame.K_UP:
                isBar2MovingUp = False
            elif event.key == pygame.K_DOWN:
                isBar2MovingDown = False






    






    if isBar1MovingUp:
        bar1_y -= 0.3

    elif isBar1MovingDown:
        bar1_y += 0.3

    if isBar2MovingUp:
        bar2_y -= 0.3

    elif isBar2MovingDown:
        bar2_y += 0.3



    
        #elif event.key == pygame.K_UP:
                
    ball_x += ball_speedX
    ball_y += ball_speedY
    
    
    ball_rect = pygame.draw.circle( screen, [45, 255, 255], [ball_x, ball_y], 25 )
    bar1_rect = pygame.draw.rect(screen, p1color, pygame.Rect(50, bar1_y, 40, 120))
    bar2_rect = pygame.draw.rect(screen, [0,0, 255], pygame.Rect(910, bar2_y, 40, 120)) #position x y then width height

    if pygame.Rect.colliderect(ball_rect, bar2_rect):
        ball_speedX = -0.45

    if pygame.Rect.colliderect(ball_rect, bar1_rect):
        ball_speedX = 0.45

    if ball_x >= 1024:
        print("Player 1 wins")
        ball_x = 512
        ball_y = 250
        ball_speedX = 0
        ball_speedY = 0

    elif ball_x <= 0:
        print("PLayer 2 wins")
        ball_x = 512
        ball_y = 250
        ball_speedY = 0
        ball_speedX = 0





    if ball_y <= 0 or ball_y >= 475:
        ball_speedY = -ball_speedY




        

    pygame.display.flip()
