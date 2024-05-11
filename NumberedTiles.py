import pygame
import random
import datetime

pygame.init()
screen = pygame.display.set_mode( [450, 768] )
num_font = pygame.font.SysFont("Catamaran", 200)
big_font = pygame.font.SysFont("Catamaran", 250)
time_font = pygame.font.SysFont("Catamaran", 150)

f = pygame.image.load("1.png")

clock = pygame.image.load("wall-clock.png")
clock = pygame.transform.scale(clock, [75, 75])

f = pygame.transform.scale(f, [70, 100])

Tiles = [1, 2, 3,
         4, 5, 6,
         7, 8, 0]

selected_tile = 1
random.shuffle(Tiles)

startTime = datetime.datetime.now()

def swap( tiles, fromTile, toTile ):
    if tiles[toTile] == 0: #check if tile has a value of 0
        #   swap
        if  fromTile == 3 and toTile == 2 or fromTile == 2 and toTile == 3 or fromTile == 5 and toTile == 6 or fromTile == 6 and toTile == 5:
            return
        
        tmp = Tiles[fromTile]
        tiles[fromTile] = tiles[toTile]
        tiles[toTile] = tmp

while True:
    screen.fill([0, 150, 255])

    currentTime = datetime.datetime.now()
    second = (currentTime-startTime).seconds

    time = time_font.render(f"{second}", True, [255, 130, 20])
    screen.blit(time, [150, 660])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:
                selected_tile = 1

            elif event.key == pygame.K_KP2:
                selected_tile = 2

            elif event.key == pygame.K_KP3:
                selected_tile = 3

            elif event.key == pygame.K_KP4:
                selected_tile = 4


            elif event.key == pygame.K_KP5:
                selected_tile = 5

            elif event.key == pygame.K_KP6:
                selected_tile = 6

            elif event.key == pygame.K_KP7:
                selected_tile = 7

            elif event.key == pygame.K_KP8:
                selected_tile = 8


            elif event.key == pygame.K_UP:
                fromTile = Tiles.index( selected_tile )
                toTile = fromTile - 3
                swap( Tiles, fromTile, toTile )

            elif event.key == pygame.K_DOWN:
                fromTile = Tiles.index( selected_tile )
                toTile = fromTile + 3
                swap( Tiles, fromTile, toTile )

            elif event.key == pygame.K_LEFT:
                fromTile = Tiles.index( selected_tile )
                toTile = fromTile - 1
                swap( Tiles, fromTile, toTile )

            elif event.key == pygame.K_RIGHT:
                fromTile = Tiles.index( selected_tile )
                toTile = fromTile + 1
                swap( Tiles, fromTile, toTile )

            
            


    
    x = 50
    y = 200

    offsetX = 0
    for i in range(9):
        if Tiles[i] == 0:
            n = num_font.render(" ", True, [200, 230, 200])

        elif Tiles[i] == selected_tile:
            n = big_font.render(f"{Tiles[i]}", True, [255, 200, 200])

        else:
            n = num_font.render(f"{Tiles[i]}", True, [200, 230, 200])

        if i % 3 == 0:
            newL = i // 3
            offsetX = 0
        else:
            offsetX += 140

        screen.blit(n, [x+offsetX,y+newL*140])


    screen.blit(clock, [50, 670])



        
    pygame.display.update()
