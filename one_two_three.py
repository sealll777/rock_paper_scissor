import pygame
import math
import time
from random import randint
Display = (800, 600)
pygame.init()
screen = pygame.display.set_mode(Display)
screen.fill((0,0,0))
clock = pygame.time.Clock()
##LOAD IMAGE AND DISPLAY IMAGE
background = pygame.image.load('background.jpg')
background = pygame.transform.smoothscale(background, (800,600))
screen.blit(background,(0,0))
scissors = pygame.image.load('Hand_scissors.png')
scissors = pygame.transform.smoothscale(scissors, (300,225))
scissors_enlarge = pygame.transform.smoothscale(scissors, (350,275))
rock = pygame.image.load('Hand_rock.png')
rock = pygame.transform.smoothscale(rock, (300,225))
rock_enlarge = pygame.transform.smoothscale(rock, (350,275))
paper = pygame.image.load('Hand_paper.png')
paper = pygame.transform.smoothscale(paper, (300,225))
paper_enlarge = pygame.transform.smoothscale(paper, (350,275))
girl = pygame.image.load('Girl.png')
girl_2 = pygame.image.load('Girl_2.png')
girl = pygame.transform.smoothscale(girl, (300,225))
girl_2 = pygame.transform.smoothscale(girl_2, (300,225))
girl_win = pygame.image.load('Girl_win.png')
girl_win = pygame.transform.smoothscale(girl_win, (300,225))
girl_lose = pygame.image.load('Girl_lose.png')
girl_lose = pygame.transform.smoothscale(girl_lose, (300,225))
boy = pygame.image.load('Boy.png')
boy_2 = pygame.image.load('Boy_2.png')
boy_lose = pygame.image.load('Boy_lose.png')
boy_win = pygame.image.load('Boy_win.png')
boy = pygame.transform.smoothscale(boy, (300,225))
boy_2 = pygame.transform.smoothscale(boy_2, (300,225))
boy_lose = pygame.transform.smoothscale(boy_lose, (300,225))
boy_win = pygame.transform.smoothscale(boy_win, (300,225))
text_2 = pygame.font.Font(None,100)
taunt_1 = pygame.image.load('taunt_1.png')
def load_background():
    screen.blit(background,(0,0))
    screen.blit(scissors, (75,25))
    screen.blit(rock, (85,200))
    screen.blit(paper, (75, 375))
    #START = pygame.surface.Surface((400,300),pygame.SRCALPHA)
    #pygame.draw.rect(START, pygame.Color(149,206,249),pygame.Rect(0,0,160,100))
    #screen.blit(START, (350,250))
    #text = pygame.font.Font(None,40)
    #screen.blit(text.render("START", True, (255,255,255)), (385,280))
    #pygame.display.flip()
    #screen.blit(girl, (550, 200))
done = False
boy_or_girl = None
animation_odd = 0
text = pygame.font.Font(None,40)
start = False
score = 0
status = 0
pygame.mixer.music.load('bensound-funkysuspense.mp3')
pygame.mixer.music.play(-1, 0)
while done == False:
    previous = score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.display.quit()
            pygame.mixer.music.stop()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
            pygame.display.quit()
            pygame.mixer.music.stop()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.dict["pos"] #get coordinates
            print(mouse_x, mouse_y)
            if start == False:
                if 350<mouse_x and mouse_x<508 and 251<mouse_y and mouse_y<348:
                    start = True
            if start == True:
                screen.blit(background, (0,0))
                if boy_or_girl==None:
                    if 160<mouse_x and mouse_x<320 and 200<mouse_y and mouse_y<400:
                          boy_or_girl = "girl"
                    if 480<mouse_x and mouse_x<640 and 200<mouse_y and mouse_y<400:
                        boy_or_girl = "boy"
                    continue
                if boy_or_girl != None:
                    if 10<mouse_x and mouse_x<87 and 10<mouse_y and mouse_y<60:#reset game
                        boy_or_girl = None
                        status = randint(0,10)
                        if status != 3:
                            score = 0
                        else:
                            screen.blit(taunt_1, (0,0))
                            mock = pygame.mixer.music.get_pos()
                            time.sleep(1)
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('it-was-me-dio_1.mp3')
                            pygame.mixer.music.play()
                            time.sleep(2)
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('bensound-funkysuspense.mp3')
                            pygame.mixer.music.play(-1,mock)
                        start = False
                    if 75<mouse_x and mouse_x<375 and 25<mouse_y and mouse_y<200:
                        screen.blit(scissors_enlarge, (60,10))
                        attack = "scissors"
                    if 75<mouse_x and mouse_x<375 and 250<mouse_y and mouse_y<362:
                        screen.blit(rock_enlarge, (70,185))
                        attack = "rock"
                    if 75<mouse_x and mouse_x<375 and 375<mouse_y and mouse_y<600:
                        screen.blit(paper_enlarge, (60,360))
                        attack = "paper"
                    if 75<mouse_x and mouse_x<375 and ((25<mouse_y and mouse_y<200) or \
                       (250<mouse_y and mouse_y<362) or (375<mouse_y and mouse_y<600)):
                        opponent = randint(0,2)
                        lst = [scissors, rock, paper]
                        opponent_display = pygame.transform.flip(lst[opponent], True, False)
                        screen.blit(opponent_display, (375, 200))
                        if boy_or_girl == "girl":
                            if attack == "rock":
                                if opponent == 0: #win
                                    screen.blit(girl_lose, (550,200))
                                    score += 1
                                elif opponent == 1: #draw
                                    screen.blit(girl, (550,200))
                                else: #lose
                                    screen.blit(girl_win, (550,200))
                                    score -= 1
                            if attack == "scissors":
                                if opponent == 2: #win
                                    screen.blit(girl_lose, (550,200))
                                    score += 1
                                elif opponent == 0: #draw
                                    screen.blit(girl, (550,200))
                                else: #lose
                                    screen.blit(girl_win, (550,200))
                                    score -= 1
                            if attack == "paper":
                                if opponent == 1: #win
                                    screen.blit(girl_lose, (550,200))
                                    score += 1
                                elif opponent == 2: #draw
                                    screen.blit(girl, (550,200))
                                else: #lose
                                    screen.blit(girl_win, (550,200))
                                    score -= 1
                        if boy_or_girl == "boy":
                            if attack == "rock":
                                if opponent == 0: #win
                                    screen.blit(boy_lose, (550,200))
                                    score += 1
                                elif opponent == 1: #draw
                                    screen.blit(boy, (550,200))
                                else: #lose
                                    screen.blit(boy_win, (550,200))
                                    score -= 1
                            if attack == "scissors":
                                if opponent == 2: #win
                                    screen.blit(boy_lose, (550,200))
                                    score += 1
                                elif opponent == 0: #draw
                                    screen.blit(boy, (550,200))
                                else: #lose
                                    screen.blit(boy_win, (550,200))
                                    score -= 1
                            if attack == "paper":
                                if opponent == 1: #win
                                    screen.blit(boy_lose, (550,200))
                                    score += 1
                                elif opponent == 2: #draw
                                    screen.blit(boy, (550,200))
                                else: #lose
                                    screen.blit(boy_win, (550,200))
                                    score -= 1
                        if score == -5 and previous > score:
                            screen.blit(text.render("Hehe, loser.",True,(0,0,0)),(600,200))
                        pygame.display.flip()
                        clock.tick(1)
    if start == False: #game not starting yet
        START = pygame.surface.Surface((400,300),pygame.SRCALPHA)
        pygame.draw.rect(START, pygame.Color(149,206,249),pygame.Rect(0,0,160,100))
        screen.blit(START, (350,250))
        screen.blit(text.render("START", True, (255,255,255)), (385,280))
        pygame.display.flip()
    elif start == True: #game starting
        if boy_or_girl==None:
            pygame.draw.rect(screen,pygame.Color('pink'),pygame.Rect(160,200,160,200))
            pygame.draw.rect(screen,pygame.Color('blue'),pygame.Rect(480,200,160,200))
            screen.blit(text_2.render("GIRL",True,(255,255,255)),(160,250))
            screen.blit(text_2.render("BOY",True,(255,255,255)),(490,250))
            screen.blit(text.render("Choose your opponent",True,(50,205,50)),(250,100))
            pygame.display.flip()
        if boy_or_girl == "girl":
            load_background()
            screen.blit(text.render("SCORE:",True,(255,255,255)),(500,10))
            screen.blit(text.render(str(score),True,(255,255,255)),(625,10))
            pygame.draw.rect(screen,pygame.Color('pink'),pygame.Rect(10,10,80,50))
            screen.blit(text.render("Main",True,(0,0,0)), (15,15))
            if animation_odd == 0:
                screen.blit(girl, (550,200))
                animation_odd = 1
            elif animation_odd == 1:
                screen.blit(girl_2, (550, 200))
                animation_odd = 0
        if boy_or_girl == "boy":
            load_background()
            screen.blit(text.render("SCORE:",True,(255,255,255)),(500,10))
            screen.blit(text.render(str(score),True,(255,255,255)),(625,10))
            pygame.draw.rect(screen,pygame.Color('pink'),pygame.Rect(10,10,80,50))
            screen.blit(text.render("Main",True,(0,0,0)), (15,15))
            if animation_odd == 0:
                screen.blit(boy, (550,200))
                animation_odd = 1
            elif animation_odd == 1:
                screen.blit(boy_2, (550, 200))
                animation_odd = 0
        pygame.display.flip()
        clock.tick(5)




