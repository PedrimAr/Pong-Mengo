# Início:

# 1. Importações:
from PPlay.window import *
from PPlay.gameimage import *

# 2. Definições Iniciais:

# Tamanho da janela
janela = Window(900, 600)

# Estabelecendo input do teclado
teclado = Window.get_keyboard()

# Definição do cenário
cenario = GameImage("imagens/gramado-maracana.webp")

# Definição da bola e sua posição inicial
bola = GameImage("imagens/bolaCBF.png")
bolaX = janela.width/2 - bola.width/2
bola.x = bolaX
bolaY = janela.height/2 - bola.height/2
bola.y = bolaY

# Definição dos pads e suas posições
padEsq = GameImage("imagens/padMengo.png")
padEsqX = 10
padEsq.x = padEsqX
padEsqY = janela.height / 2 - padEsq.height / 2
padEsq.y = padEsqY

padDir = GameImage("imagens/padMengo.png")
padDirX = janela.width - padDir.width - 10
padDir.x = padDirX
padDirY = janela.height / 2 - padDir.height / 2
padDir.y = padDirY

# Definição da variável de velocidade da bola
velX = 1
velY = 1

count = 0

pause = True

# Game Loop:
while True:

    # Movimentação do pad do player
    if teclado.key_pressed("w") and padEsq.y >= 0:
        padEsq.y -= 1
    elif teclado.key_pressed("s") and padEsq.y + padEsq.height <= janela.height:
        padEsq.y += 1

    # Movimentação do pad automático
    if velX > 0:
        if velY > 0 and padDir. y + padDir.height <= janela.height:
            padDir.y += 0.75
        elif velY < 0 <= padDir.y:
            padDir.y -= 0.75

    # Gol
    if bola.x > janela.width or bola.x < 0:
        bola.x = bolaX
        bola.y = bolaY
        padEsq.y = padEsqY
        padEsq.x = padEsqX
        padDir.y = padDirY
        padDir.x = padDirX
        pause = True

    # "Apito"
    if teclado.key_pressed("space"):
        pause = False

    # Colisão da bola com o teto/chão
    if bola.y >= janela.height - bola.height or bola.y <= 0:
        velY *= -1

    '''
    # Colisão com a parte de baixo dos pads (EM MANUTENÇÃO)
    elif (bola.y <= raqueteEsq.y - bola.height or bola.y <= raqueteDir.y - bola.height) or (bola.y >= raqueteEsq.y + 
    raqueteEsq.height or bola.y >= raqueteDir.y + raqueteDir.height) and not (raqueteEsq.x + raqueteDir.width < bola.x < 
    raqueteDir.x - bola.width):
        velY *= -1
    '''

    # Colisão da bola com as laterais dos pads
    if bola.collided(padEsq) or bola.collided(padDir):
        count += 1
        if count <= 15:
            velY *= -1.05
            velX *= 1.05
        else:
            velX *= -1

    # Aceleração da bola
    if not pause:
        bola.x += velX
        bola.y += velY

    # Desenho de todos os elementos
    cenario.draw()
    padEsq.draw()
    padDir.draw()
    bola.draw()

    # Reinicialização da janela
    janela.update()
