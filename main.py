import pygame
pygame.init()
import random
import time

screen = pygame.display.set_mode([800, 600])
bg = pygame.image.load("dungeon.png").convert()

dragon_sleep = pygame.image.load("dragon-asleep.png")
dragon_sleep = pygame.transform.scale(dragon_sleep, [250, 120])


dragon_awake = pygame.image.load("dragon-awake.png")
dragon_awake = pygame.transform.scale(dragon_awake, [250,150])

isMoving = True

fried_egg = pygame.image.load("friedegg.png")
fried_egg = pygame.transform.scale(fried_egg, [50,50])

player = pygame.image.load("player.png")
player = pygame.transform.scale(player, [75, 150])

fire = pygame.image.load("fire.png")
fire = pygame.transform.scale(fire, [150, 150])

skeleton = pygame.image.load("skeleton.png")
skeleton = pygame.transform.scale(skeleton, [75, 150])

skeleton_fall = pygame.transform.rotate(skeleton, 90)

player_state = 1

class Dragon:

    def __init__(self, state_duration, sleep, state):
        self.state_duration = state_duration
        self.sleep = sleep
        self.state = state
        self.updateTime = time.time() #not going to be a parameter
        

    def wake(self):
        current_time = time.time()
   
        if current_time - self.updateTime < self.state_duration:
            
            return
            #print(f"Going back to sleep! {current_time}, {self.updateTime}, {self.awake}")
        else:
            
            print("Waking up")
            #self.state = 1
            if self.state == 1:
                self.state = 0
                self.state_duration = random.randint(1, 5)
                print(f"sleeping for {self.state_duration}")
                
            else:
                self.state = 1
                self.state_duration = random.randint(1, 5)
                print(f"awake for {self.state_duration}")

            self.updateTime = current_time
                

    
        

isMovingRight = False    
isMovingLeft = False
isMovingUp = False
isMovingDown = False


awakeTime = random.randint(3, 5)
asleepTime = random.randint(3, 7)

dragon1 = Dragon(awakeTime, asleepTime, 0)
dragon2 = Dragon(awakeTime, asleepTime, 0)
dragon3 = Dragon(awakeTime, asleepTime, 0)
dragon4 = Dragon(awakeTime, asleepTime, 0)

dragonsList = [ dragon1, dragon2, dragon3, dragon4 ]

dragonXY = [500, 100]

player_pos = [100, 200]
skeleton_pos_list = []
deathTimeList = []

while True:
    
    screen.blit(bg, [0,0])


    screen.blit(player, player_pos)

    for idx, skeleton_pos in enumerate(skeleton_pos_list):
        if time.time() - deathTimeList[idx] >= 1:
            screen.blit(skeleton_fall, [skeleton_pos[0] - 50, skeleton_pos[1] + 50] )
            

        else:
            screen.blit(skeleton, [skeleton_pos[0], skeleton_pos[1]] )
        
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT and isMoving:
                #player_pos[0] += 0.1
                isMovingRight = True

            elif event.key == pygame.K_LEFT and isMoving:
                #player_pos[0] -= 1
                isMovingLeft = True


            elif event.key == pygame.K_UP and isMoving:
                #player_pos[1] -= 1
                isMovingUp = True

            elif event.key == pygame.K_DOWN and isMoving:
                #player_pos[1] += 1
                isMovingDown = True






        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                isMovingRight = False
            elif event.key == pygame.K_LEFT:
                isMovingLeft = False
            elif event.key == pygame.K_UP:
                isMovingUp = False
            elif event.key == pygame.K_DOWN:    
                isMovingDown = False


        







    if isMovingRight:
        #print("movings")
        player_pos[0] += 0.7

        if player_pos[0] >= 725:
            player_pos[0] = 725
                
    elif isMovingLeft:        
        player_pos[0] = player_pos[0] - 0.7

        if player_pos[0] <= 0:
            player_pos[0] = 0
                

    elif isMovingUp:
        player_pos[1] = player_pos[1] - 0.7

        if player_pos[1] <= 0:
            player_pos[1] = 0

    elif isMovingDown:
        player_pos[1] = player_pos[1] + 0.7

        if player_pos[1] >= 450:
            player_pos[1] = 450




    yOffset = 0
    for dragon in dragonsList:
    
        if dragon.state == 0:
            screen.blit(dragon_sleep, [dragonXY[0], dragonXY[1] + yOffset ])
            #print("sleeping")

        else:
            #$print(player_pos[1])
            #print(player_pos[0])
            screen.blit(dragon_awake, [500, 100 + yOffset ])
            if player_pos[0] >=  370 and player_pos[0] <= 500 and player_pos[1] <= 200 + yOffset and player_pos[1] >= 100:
                #print("Roasted")
                #player_state = 0
                skeleton_pos_list.append( [player_pos[0] - 25, player_pos[1]] )

                deathTimeList.append(time.time())
                
                screen.blit(fire, [player_pos[0] - 25, player_pos[1]])
                
                #isMoving = False

                #   Reset player's position to starting point
                player_pos = [100, 200]

        yOffset += 100
                

        dragon.wake()



    pygame.display.flip()
            
