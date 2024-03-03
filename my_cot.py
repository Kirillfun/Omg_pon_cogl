from pygame import *
from time import sleep

init()
clock = time.Clock()
FPS = 60
window = display.set_mode((1000, 700))
display.set_caption("Догонялки")
background = transform.scale(image.load("1-2.jpg"), (1000, 700))
sprite1 = transform.scale(
    image.load('омг.png'), 
    (100, 150)
)
sprite2 = transform.scale(
    image.load('кнайт.png'), 
    (100, 150)
)

font = font.SysFont(None, 30)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

x1 = 850
y1 = 500
x2 = 5
y2 = 5
speed = 10
speed2 = 5

game = True
while game:
    window.blit(background,(0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    keys_pressed = key.get_pressed()


    
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed2
    if keys_pressed[K_RIGHT] and x1 < 900:
        x1 += speed2
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed2
    if keys_pressed[K_DOWN] and y1 < 550:
        y1 += speed2
    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 900:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 550:
        y2 += speed

    if x1-100 == x2-100 and y1 == y2:
        game = False
    if x1+100 == x2+100 and y1 == y2:
        game = False
    if x1 == x2 and y1+100 == y2+100:
        game = False
    if x1 == x2 and y1-100 == y2:
        game = False
    if x1 == x2 and y1 == y2:
        game = False



    for e in event.get():
        if e.type == QUIT:
           game = False
    display.update()
    clock.tick(FPS)
        
