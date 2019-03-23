import pygame as pg

def linha(screen,color):
    pg.init()
    a = pg.draw.line(screen,color,[0,200],[600,200],5)
    return a

def segmentoLinha(screen,color):
    pg.init()
    a = pg.draw.lines(screen,color,False,[(0,80),(80,90),(200,80),(220,30)],5)
    return a
def retangulo(screen,color):
    a = pg.draw.rect(screen,color,(150,10,50,20))
    return a
def poligono(screen,color):
    a = pg.draw.polygon(screen,color,([100,100],[0,200],[200,200]),2)
    return a
def circle(screen,color):
    a = pg.draw.circle(screen,color,(60,250),40)
    return a
def elipse(screen,color):
    a = pg.draw.ellipse(screen,color,(300 ,10 ,50 ,20 ),5)
    return a
def main():
    screen = pg.display.set_mode((600,400))
    pg.display.set_caption("PRIMEIRO JOGO EM PYTHON")
    white = (255,255,255)
    black = (0,0,0,0)
    green = (0,255,0,0)
    red = (255,0,0)
    blue = (0,191,255)
    screen.fill((white))
    pg.display.flip()
    print("Vamos testar...")
    escolheFuncao = int(input("Escolha: \n 1 - linha \n2 - Segmento de linha \n3 - Retângulo \n4 - Polígono \n5- Círculo \n6 - Elipse \n"))
    if escolheFuncao == 1:
        escolheCor = int(input("Escolha: 1 - branco, 2-preto,3-verde,4-vermelho, 5 blue - > "))
        if escolheCor == 1:
            b = linha(screen,white)
        elif escolheCor == 2:
            b = linha(screen,black)
        elif escolheCor == 3:
            b = linha(screen,green)
        elif escolheCor == 4:
            b = linha(screen,red)
        elif escolheCor == 5:
            b = linha(screen,blue)
        else:
            pg.display.quit()
    elif escolheFuncao == 2:
        escolheCor = int(input("Escolha: 1 - branco, 2-preto,3-verde,4-vermelho, 5 blue - > "))
        if escolheCor == 1:
            b = segmentoLinha(screen,white)
        elif escolheCor == 2:
            b = segmentoLinha(screen,black)
        elif escolheCor == 3:
            b = segmentoLinha(screen,green)
        elif escolheCor == 4:
            b = segmentoLinha(screen,red)
        elif escolheCor == 5:
            b = segmentoLinha(screen,blue)
        else:
            pg.display.quit()

    elif escolheFuncao == 3:
        escolheCor = int(input("Escolha: 1 - branco, 2-preto,3-verde,4-vermelho, 5 blue - > "))
        if escolheCor == 1:
            b = retangulo(screen,white)
        elif escolheCor == 2:
            b = retangulo(screen,black)
        elif escolheCor == 3:
            b = retangulo(screen,green)
        elif escolheCor == 4:
            b = retangulo(screen,red)
        elif escolheCor == 5:
            b = retangulo(screen,blue)
        else:
            pg.display.quit()
            
    elif escolheFuncao == 4:
        
        escolheCor = int(input("Escolha: 1 - branco, 2-preto,3-verde,4-vermelho, 5 blue - > "))
        if escolheCor == 1:
            b = poligono(screen,white)
        elif escolheCor == 2:
            b = poligono(screen,black)
        elif escolheCor == 3:
            b = poligono(screen,green)
        elif escolheCor == 4:
            b = poligono(screen,red)
        elif escolheCor == 5:
            b = poligono(screen,blue)
        else:
            pg.display.quit()

    elif escolheFuncao == 5:
        
        
        escolheCor = int(input("Escolha: 1 - branco, 2-preto,3-verde,4-vermelho, 5 blue - > "))
        if escolheCor == 1:
            b = circle(screen,white)
        elif escolheCor == 2:
            b = circle(screen,black)
        elif escolheCor == 3:
            b = circle(screen,green)
        elif escolheCor == 4:
            b = circle(screen,red)
        elif escolheCor == 5:
            b = circle(screen,blue)
        else:
            pg.display.quit()


    elif escolheFuncao == 6:
        escolheCor = int(input("Escolha: 1 - branco, 2-preto,3-verde,4-vermelho, 5 blue - > "))
        if escolheCor == 1:
            b = elipse(screen,white)
        elif escolheCor == 2:
            b = elipse(screen,black)
        elif escolheCor == 3:
            b = elipse(screen,green)
        elif escolheCor == 4:
            b = elipse(screen,red)
        elif escolheCor == 5:
            b = elipse(screen,blue)
        else:
            pg.display.quit()
    else:
        pg.display.quit()
    pg.display.flip()


    
    
main()

