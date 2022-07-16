import pygame
import random
import  time
pygame.init()
clock=pygame.time.Clock()
  #display_surface
gd=pygame.display.set_mode((580,600))
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
light_green=(0,200,0)
gray=(0,118,110)
blue=(0,0,255)
car_img=pygame.image.load('sour/img/player.jpg')
# car_img=pygame.transform.scale(car_img,(,100))
background=pygame.image.load('sour/img/ba.jpg')
mass = pygame.image.load('sour/img/message.png')

def Message(size,mess,x_pos,y_pos):
    font=pygame.font.SysFont(None,size)
    render=font.render(mess,True,white)
    gd.blit(render , (x_pos,y_pos))

Message(100,"START",150,100)
clock.tick(1)


def car(x,y):
    gd.blit(car_img, (x, y))

    if 0<x<30 or 700<x+170:
        Message(100, "GAME-OVER", 100, 100)
        pygame.display.update()
        # clock.tick(0.10)
        game_intro()

def enmy_car(x_r,y_r):
    gd.blit(car_img,(x_r,y_r))


def button(x_button,y_button,mess_b):
    pygame.draw.rect(gd,gray,[x_button,y_button,100,30])
    Message(50,mess_b,x_button,y_button)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x_button<mouse[0]<x_button+100 and y_button<mouse[1]<y_button+30:
        pygame.draw.rect(gd, light_green, [x_button, y_button, 100, 30])
        Message(50, mess_b, x_button, y_button)
        if click==(1,0,0) and mess_b=="PLAY":
            Game_loop()
        elif click==(1,0,0) and mess_b=="QUIT":
            pygame.quit()
            quit()

def car_crash(x,x_r,y,y_r):
    if x_r<x<x_r+50 and y_r<y<y_r+50 or x_r<x+50<x_r+50 and y_r<y<y_r+50:
        Message(50,"CRASHED!",200,200)
        pygame.display.update()
        game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def score(count):
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render('score :' + str(count), True, white)
    gd.blit(screen_text, (0, 0))


def game_intro():
    intro=False
    while intro == False:
        gd.blit(background, (0, 0))
        gd.blit(mass,(100,40))
        button(100,300,"PLAY")
        button(405,300,"QUIT")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def Game_loop():
   x=300
   count=0
   x_r=random.randrange(100,500)
   y_r=0
   y=490
   x_change=0
   game_over=False
   while game_over==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=+10
            elif event.key==pygame.K_RIGHT:
                x_change=-10
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                x_change=0
    gd.blit(background,(0,0))


    car(x,y)
    score(count)
    enmy_car(x_r,y_r)
    y_r+=10
    if y_r==600:
        y_r=0
        x_r=random.randrange(100,560)
        count+=1
    car_crash(x,x_r,y,y_r)
    x=x-x_change
    clock.tick(40)
    pygame.display.update()

game_intro()
pygame.display.update()
pygame.quit()
quit()