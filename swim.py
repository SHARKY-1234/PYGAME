import pygame
import random
import shelve
import sys

pygame.init()#initializes pygame
pygame.mixer.init()
screen = pygame.display.set_mode([1600,800])

databaseFile = 'data2.dat'

bg_img = pygame.image.load("poolBG.jpg").convert() #makes images run better
bg_img = pygame.transform.scale(bg_img, [1600, 800])


record_btn = pygame.image.load("recordbutton.png")
record_btn = pygame.transform.scale(record_btn, [400, 100])

recordedtime = pygame.image.load("newtime.png")
recordedtime = pygame.transform.scale(recordedtime, [400, 100])

font_big = pygame.font.SysFont("tahoma", 90)
font_normal = pygame.font.SysFont("tahoma", 60)
font_small = pygame.font.SysFont("tahoma", 30)
#input_text = ""






def askSwimName():
    name_entered = False
    is_shift = False
    input_text = ""
        
    while True:    
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN: #if the keyboard keys are being pressed

                if event.key == pygame.K_RETURN:
                    is_typing = False #exit loop if enter is pressed
                    #swimScreen(input_text)
                    #print("KEY ENTER")
                    return input_text #send out value of input_text.

                elif event.key == pygame.K_BACKSPACE:
                    #remove last character when backspace is pressed
                    input_text = input_text[:-1]
                    #print("BACKSPACE PRESSED")


                else:
                    #add typed charcter
                    input_text += event.unicode
                    print("TYPING")


        screen.fill((255,255,255))
        text = font_normal.render("Enter name: " + input_text, True, (100,0,205))
        screen.blit(text, [50, 50])
        pygame.display.update()

recordpos = [300, 300]
entered_recordpos = [800, 300]
#end of askName loop







def swimScreen(name):
    global canGetTime
    canGetTime = False
    
    while True:
        #print("Entered swim screen!")
        screen.fill((255,255,255))

        screen.blit(bg_img, [0,0])
        displayName = font_normal.render(name, True, (255, 60, 50))
        screen.blit(displayName, [1300, 50])
        screen.blit(record_btn, recordpos)
        screen.blit(recordedtime, entered_recordpos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    


        mousepos = pygame.mouse.get_pos()
        record_rect = recordedtime.get_rect()
        record_rect.topleft = recordpos

        entered_records_rect = record_btn.get_rect()
        entered_records_rect.topleft = entered_recordpos
        



        if entered_records_rect.collidepoint(mousepos): #Enter record
            if pygame.mouse.get_pressed()[0]:
                time = Record(name)
                
                

        if record_rect.collidepoint(mousepos): #recorded records
            if pygame.mouse.get_pressed()[0]:
                displayTime(name)

                
                
        #pygame.display.flip()
        pygame.display.update()
        
        








def Record(name):
    time = ""
    screen.fill((255, 255, 255))

    while True:
        
        #pygame.display.flip()
        screen.blit(bg_img, [0,0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN: #if the keyboard keys are being pressed

                if event.key == pygame.K_RETURN:
                    #is_typing = False #exit loop if enter is pressed
                    #swimScreen(input_text)
                    print(f"KEY ENTER, time={time}")

                    swim = shelve.open( databaseFile, writeback=True ) #if data needs to be updated then writeback is needed

                    if name not in swim.keys():
                        swim[name] = []

                    timeList = swim[name]
                    timeList.append( time )
                    print( f'Recored {name}: {swim[name]}' )

                    swim.close()

                    swimScreen(name)

                elif event.key == pygame.K_BACKSPACE:
                    #remove last character when backspace is pressed
                    time = time[:-1]


                else:
                    #add typed charcter
                    time += event.unicode
                    


        screen.fill((255,255,255))
        text = font_normal.render("Put Time and Stroke here: " + time, True, (100,0,205))
        screen.blit(text, [300, 200])
        pygame.display.update()




        
        


        pygame.display.flip()
        pygame.display.update()




def displayTime(name):

    bg_img = pygame.image.load("swimpool2.jpg").convert() #makes images run better
    bg_img = pygame.transform.scale(bg_img, [1600, 800])

    
    
    swim = shelve.open( databaseFile )
    try:
        recordedList = swim[name]
    except KeyError as e:
        print(f'there is no time for {name} in our records')
        recordedList = []
        
    swim.close() 


    print(f'recordedList = {recordedList}')

    iteration = 0
    yUpper = 250
    yLower = 650
    while True:
        screen.fill((255, 255, 255))
        screen.blit(bg_img, [0,0])
        
        name_text = font_big.render(f"{name}'s Records", True, (51, 51, 255))
        screen.blit(name_text, [200, 100])

        for i, time in enumerate( recordedList ):   #i is index of how many time for loop has been loop. time is just the value of the thing on that iteration
            time_text = font_normal.render(f"{time}", True, (255, 51, 255))

            y = yUpper+75*i-iteration
            y = y%(yLower - yUpper) + yUpper
            screen.blit(time_text, [200, y])

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        iteration -= 0.1  
        pygame.display.update()
        
    print(time)



# main
name = askSwimName() #Get results of variable in askSwimName and store in variable name
canGetTime = swimScreen(name)
#swimScreen(name) #Use variable in swimScreen
#if canGetTime:
 #   timeEntered = Record(name) #same as above but different functions
  #  recorded(timeEntered)



#recorded() is not being called
        
        
