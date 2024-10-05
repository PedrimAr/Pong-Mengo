# Início:

# 1. Importações:
from PPlay.window import *
from PPlay.gameimage import *

# 2. Definições Iniciais:

# Tamanho da janela
janela = Window(900, 600)

# Definição do cenário
cenario = GameImage("imagens/gramado-maracana.webp")

# Definição da bola e sua posição inicial
bola = GameImage("imagens/bolaCBF.png")
bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2

# Definição dos pads e suas posições
raqueteEsq = GameImage("imagens/raqueteMengo.png")
raqueteEsq.x = 0
raqueteEsq.y = janela.height/2 - raqueteEsq.height/2
raqueteDir = GameImage("imagens/raqueteMengo.png")
raqueteDir.x = janela.width - raqueteDir.width
raqueteDir.y = janela.height/2 - raqueteDir.height/2

# Definição da variável de velocidade da bola
velX = 0.75
velY = 0.75

# Game Loop:
while True:

    # Colisão da bola com as paredes laterais
    if bola.x >= janela.width - bola.width or bola.x <= 0:
        velX *= -1

    # Colisão da bola com o teto/chão
    elif bola.y >= janela.height - bola.height or bola.y <= 0:
        velY *= -1

    # Colisão com a lateral dos pads (FUNCIONANDO)
    elif (bola.x >= raqueteDir.x - bola.width or bola.x <= raqueteEsq.width) and not (bola.y < raqueteDir.y + bola.height or bola.y > raqueteDir.y + raqueteDir.height or bola.y < raqueteEsq.y + bola.height or bola.y > raqueteEsq.y + raqueteDir.height):
        velX *= -1.1

    # Colisão com a parte de baixo dos pads (EM MANUTENÇÃO)
    '''
    elif (bola.y <= raqueteEsq.y - bola.height or bola.y <= raqueteDir.y - bola.height) or (bola.y >= raqueteEsq.y + 
    raqueteEsq.height or bola.y >= raqueteDir.y + raqueteDir.height) and not (raqueteEsq.x + raqueteDir.width < bola.x < 
    raqueteDir.x - bola.width):
        velY *= -1
    '''

    # Aceleração da bola
    bola.x += velX
    # bola.y += velY (Interditado por conta da funcionalidade em manutenção)

    # Desenho de todos os elementos
    cenario.draw()
    raqueteEsq.draw()
    raqueteDir.draw()
    bola.draw()

    # Reinicialização da janela
    janela.update()
