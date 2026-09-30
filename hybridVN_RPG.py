import pygame
import math
#define draphic display
Display = (800,600)
#initialise gameplay
pygame.init()#init funstion
screen = pygame.display.set_mode(Display)#pass through the tuple representing window
screen.fill((30,100,160))#color fill
#image = pygame.image.load('mascot_v2.png')
#screen.blit(image,(0,0))
#pygame.display.flip()
#Initialising images (If you have a picture file you want to display)
imagebird = pygame.image.load('mascot_v2.png')
#scale an object to any preferred size
imagebird5 = pygame.transform.smoothscale(imagebird,(400,800))

#Drawing images
#screen.blit(imageobject, xy-coordinates)
screen.blit(imagebird5,(0,0))

#Display objects blitted into memory
#pygame.display.flip()
man=pygame.surface.Surface((65,72),pygame.SRCALPHA)

#Draw on that surface first (we are not drawing on the screen here)
#to complete the picture of a man
pygame.draw.circle(man,pygame.Color('tan'),(32,8),8) #16 pixel diameter face
pygame.draw.circle(man,pygame.Color('black'),(28,6),1) #left eye
pygame.draw.circle(man,pygame.Color('black'),(36,6),1) #right eye
pygame.draw.arc(man,pygame.Color('black'),pygame.Rect(26,5,12,8),math.pi,math.pi*2) #mouth
pygame.draw.rect(man,pygame.Color('tan'),pygame.Rect(18,27,6+16+6,12)) #hands
pygame.draw.rect(man,pygame.Color('brown'),pygame.Rect(16,17,8+16+8,10)) #shirt sleeves
pygame.draw.rect(man,pygame.Color('brown'),pygame.Rect(23,17,18,30)) #30 pix long shirt
pygame.draw.rect(man,pygame.Color('Red'),pygame.Rect(24,47,7,25)) #25 pix long pants
pygame.draw.rect(man,pygame.Color('Red'),pygame.Rect(33,47,7,25)) #25 pix long pants
pygame.draw.line(man,pygame.Color('black'),(32,17),(32,37)) #20 pix long collar line

screen.blit(man,(100,100)) #draw the man on the display screen at 100,100
screen.blit(man,(200,100)) #draw the man on the display screen at 200,100

upsidedownman=pygame.transform.flip(man,False,True)
screen.blit(upsidedownman,(300,100)) #draw the upsidedownman on the display screen at 300,100

rotatedman=pygame.transform.rotate(man,30)
screen.blit(rotatedman,(100,200)) #draw the rotatedman on the display screen at 100,200

pygame.display.flip()
pygame.time.Clock().tick(1)

clock = pygame.time.Clock()
for x in range(10,250):
    #a. clear: fill the background to empty it
    screen.fill((30, 100, 160))

    #b. draw:
    #White Rectangle 1 at a location (x,100) with width 50 ht 20
    pygame.draw.rect(screen,pygame.Color('white'), pygame.Rect(x, 100, 50, 20))
    #Rectangle 2 at a location (x,200) with width 50 ht 20, with varying colour
    #If colour is (x,0,0), what will it look like?
    pygame.draw.rect(screen,(x,0,0), pygame.Rect(x, 200, 50, 20))
    
    #c. display: flip the page, to display it
    pygame.display.flip()

    #d. Control Framerate : delay 1/40th of a second every loop, to slow down, to see the animation
    clock.tick(20)
#initialise game variables
xloc = 10
yloc = 100
done = False

#Game Loop
while done == False:

    ############
    # 1. INPUT #
    ############

    #>>>>>  1a. Process one time events  <<<<<
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xloc-=10
                print("User pressed the Left button")
            if event.key == pygame.K_RIGHT:
                xloc+=10
                print("User pressed the Right button")
            if event.key == pygame.K_UP:
                yloc-=10
                print("User pressed the Up button")
            if event.key == pygame.K_DOWN:
                yloc+=10
                print("User pressed the Down button")
            if event.key == pygame.K_ESCAPE:
                print("User pressed the escape button")
                done=True  #set done to True to leave the game loop.

    #>>>>>  1b. Process keys that are held down  <<<<<
    pygame.event.get()
    pressed = pygame.key.get_pressed() 
    if pressed[pygame.K_LEFT]:
        xloc-=2
        #generally not a good idea to put print statements here
    if pressed[pygame.K_RIGHT]:
        xloc+=2
    if pressed[pygame.K_UP]:
        yloc-=2
    if pressed[pygame.K_DOWN]:
        yloc+=2

    ######################################################################
    #Game Design: Usually you either detect a key for the key press,     #
    #             or when it is held down. Do not detect the same key at #
    #             two different places or it can be confusing why the    #
    #             object is not moving smoothly                          #
    ######################################################################

    #############
    # 2.PROCESS #
    #############

    xloc+=1  #moves the rectangle 1 pixel right each frame (each 1/40th of a sec)
             #perhaps this can be simulating a flowing river.

    if xloc + 50 > Display[0]:  #if out of screen
        xloc = Display[0] - 50  #make it within screen


    ############################
    # 3.Display/Refresh OUTPUT #
    ############################

    #a. clear: fill the background to empty it
    screen.fill((30, 100, 160))

    #b. draw:
    # Rectangle at a location (xloc,yloc) with width 50 ht 20
    pygame.draw.rect(screen,(255,0,255), pygame.Rect(xloc, yloc, 50, 20))#Animation
    
    #c. display: flip the page, to display it
    pygame.display.flip()

    #d. Control Framerate. (Optional, include this for better control on framerate) 
    #delay 1/40th of a second every loop, to slow down, to see the animation
    if pygame.font:
        font = pygame.font.Font(None,40)  #40 is the font height
    else:
        font = None
    clock.tick(40)
    

#Syntax: screen.blit(font.render("your text to display", Antialiasing? T/F, colour), xy-coord)
# With 'Antialiasing' set to True, the text display should be smoother.

    screen.blit(font.render("Example 1", False, (0,0,0)), (5,10))  #(0,0,0) is black
    screen.blit(font.render("Example 2", True, (255,0,0)), (5,200)) #(255,0,0) is red


#Display objects blitted into memory
pygame.display.flip()

#Out of game loop. Close display
pygame.display.quit()
