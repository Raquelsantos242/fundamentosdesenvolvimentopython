import turtle

turtle.bgcolor('black') #cor de fundo
turtle.color('#783c00') #cor da linha
turtle.shape('turtle') #escolhe o ícone que faz o desenho da tela

def desenha_hexagono(l):
   
    for i in range(6):
        turtle.forward(l)
        turtle.left(60)
        
desenha_hexagono(100)