import pygame as pg

def linha(screen,color):
    a = pg.draw.line(screen,color,[0,200],[600,200],5)
    return a

def segmentoLinha(screen,color):
    pg.init()
    a = pg.draw.lines(screen,color,False,[(0,80),(80,90),(200,80),(220,30)],5)
    return a
def retangulo(screen,color):
    pg.init()
    a = pg.draw.rect(screen,color,(150,10,50,20))
    return a
def poligono(screen,color):
    pg.init()
    a = pg.draw.polygon(screen,color,([100,100],[0,200],[200,200]),2)
    return a
def circle(screen,color):
    pg.init()
    a = pg.draw.circle(screen,color,(60,250),40)
    return a
def elipse(screen,color):
    pg.init()
    a = pg.draw.ellipse(screen,color,(300 ,10 ,50 ,20 ),5)
    return a

screen = pg.display.set_mode((600,400))
pg.display.set_caption("PRIMEIRO JOGO EM PYTHON")
white = (255,255,255)
black = (0,0,0,0)
green = (0,255,0,0)
red = (255,0,0)
blue = (0,191,255)
screen.fill((white))
pg.display.flip()
a = True
while a == True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                c = retangulo(screen,green)
                print("Primeiro retângulo")
                print(c)

            elif event.type == pg.K_w:
                d = retangulo(screen,red)
                print("Segundo retângulo")
                print(d)

            elif event.type == pg.K_e:
                e = elipse(screen,red)
                print("Primeira elipse")
                print(e)

            elif event.type == pg.K_r:
                f = retangulo(screen,green)
                print("Segunda elipse")
                print(f)

            elif event.type == pg.K_t:
                g = poligono(screen,red)
                print("Poligono")
                print(g)

            elif event.type == pg.K_y:
                h = circle(screen,red)
                print("Circle")
                print(h)
            else:
                pg.display.update()
    pg.display.update()

