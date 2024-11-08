# Início:

# 1. Importações:
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

# 2. Definições Iniciais:

# Tamanho da janela
janela = Window(900, 600)

# Estabelecendo input do teclado
teclado = Window.get_keyboard()

# Definição do cenário
cenario = GameImage("imagens/gramado-maracana.webp")

# Definição da bola e sua posição inicial
bola = Sprite("imagens/bolaCBF.png")
bolaX = janela.width/2 - bola.width/2
bola.x = bolaX
bolaY = janela.height/2 - bola.height/2
bola.y = bolaY

# Definição da variável de velocidade da bola
velX = 500
velY = 500

# Definição dos pads e suas posições
padEsq = Sprite("imagens/padMengo.png")
padEsqX = 10
padEsq.x = padEsqX
padEsqY = janela.height / 2 - padEsq.height / 2
padEsq.y = padEsqY

padEsqCima = Sprite("imagens/padMengoMenor.png")
padEsqCimaX = 10
padEsqCima.x = padEsqCimaX
padEsqCimaY = janela.height / 2 - padEsqCima.height / 2 - 80
padEsqCima.y = padEsqCimaY

padEsqBaixo = Sprite("imagens/padMengoMenor.png")
padEsqBaixoX = 10
padEsqBaixo.x = padEsqBaixoX
padEsqBaixoY = janela.height / 2 + padEsqBaixo.height / 2 + 80
padEsqBaixo.y = padEsqBaixoY

padDir = Sprite("imagens/padMengo.png")
padDirX = janela.width - padDir.width - 10
padDir.x = padDirX
padDirY = janela.height / 2 - padDir.height / 2
padDir.y = padDirY

padDirCima = Sprite("imagens/padMengoMenor.png")
padDirCimaX = janela.width - padDirCima.width - 10
padDirCima.x = padDirCimaX
padDirCimaY = janela.height / 2 - padDirCima.height / 2 - 80
padDirCima.y = padDirCimaY

padDirBaixo = Sprite("imagens/padMengoMenor.png")
padDirBaixoX = janela.width - padDirBaixo.width - 10
padDirBaixo.x = padDirBaixoX
padDirBaixoY = janela.height / 2 + padDirBaixo.height / 2 + 80
padDirBaixo.y = padDirBaixoY

# Definição de variáveis auxiliares
count = -1
pause = True
quebrado = False

# Definição das variáveis de contagem do placar
placarPlayer = 0
placarIA = 0

# Game Loop:
while True:

    # Quebra dos pads após 3 rebatidas
    if count < 3:
        padEsqCima.hide()
        padEsqBaixo.hide()
        padDirCima.hide()
        padDirBaixo.hide()
        padEsq.unhide()
        padDir.unhide()

    elif count == 3:
        quebrado = True
        padEsq.hide()
        padDir.hide()
        padEsqBaixo.unhide()
        padEsqCima.unhide()
        padDirBaixo.unhide()
        padDirCima.unhide()


    # Movimentação do pad do player
    if teclado.key_pressed("w") and padEsq.y >= 0 and not pause and not quebrado:
        padEsq.move_y(-400 * janela.delta_time())
    elif teclado.key_pressed("s") and padEsq.y + padEsq.height <= janela.height and not pause and not quebrado:
        padEsq.move_y(400 * janela.delta_time())

    # Movimentação do pad do player (quebrado)
    if teclado.key_pressed("w") and padEsqCima.y >= 0 and not pause and quebrado:
        padEsqCima.move_y(-400 * janela.delta_time())
        padEsqBaixo.move_y(-400 * janela.delta_time())
    elif teclado.key_pressed("s") and padEsqBaixo.y + padEsqBaixo.height <= janela.height and not pause and quebrado:
        padEsqCima.move_y(400 * janela.delta_time())
        padEsqBaixo.move_y(400 * janela.delta_time())

    # Movimentação do pad automático
    if velX > 0 and not pause and not quebrado:
        if velY > 0 and padDir.y + padDir.height <= janela.height:
            padDir.move_y(350 * janela.delta_time())
        elif velY < 0 <= padDir.y:
            padDir.move_y(-350 * janela.delta_time())

    # Movimentação do pad automático (quebrado)
    if velX > 0 and not pause and quebrado:
        if velY > 0 and padDirBaixo.y + padDir.height <= janela.height:
            padDirCima.move_y(350 * janela.delta_time())
            padDirBaixo.move_y(350 * janela.delta_time())
        elif velY < 0 <= padDirCima.y:
            padDirCima.move_y(-350 * janela.delta_time())
            padDirBaixo.move_y(-350 * janela.delta_time())

    # Gol
    if bola.x > janela.width:
        bola.x = bolaX
        bola.y = bolaY
        padEsq.y = padEsqY
        padEsq.x = padEsqX
        padEsqCima.y = padEsqCimaY
        padEsqCima.x = padEsqCimaX
        padEsqBaixo.y = padEsqBaixoY
        padEsqBaixo.x = padEsqBaixoX
        padDir.y = padDirY
        padDir.x = padDirX
        padDirCima.y = padDirCimaY
        padDirCima.x = padDirCimaX
        padDirBaixo.x = padDirBaixoX
        padDirBaixo.y = padDirBaixoY
        pause = True
        quebrado = False
        placarPlayer += 1
        velY = 500
        velX = 500
        count = 0

    elif bola.x + bola.width < 0:
        bola.x = bolaX
        bola.y = bolaY
        padEsq.y = padEsqY
        padEsq.x = padEsqX
        padEsqCima.y = padEsqCimaY
        padEsqCima.x = padEsqCimaX
        padEsqBaixo.y = padEsqBaixoY
        padEsqBaixo.x = padEsqBaixoX
        padDir.y = padDirY
        padDir.x = padDirX
        padDirCima.y = padDirCimaY
        padDirCima.x = padDirCimaX
        padDirBaixo.x = padDirBaixoX
        padDirBaixo.y = padDirBaixoY
        pause = True
        quebrado = False
        placarIA += 1
        velY = 500
        velX = 500
        count = 0

    # "Apito"
    if teclado.key_pressed("space"):
        pause = False

    # Colisão da bola com o teto/chão
    if bola.y + bola.height >= janela.height or bola.y <= 0:
        velY *= -1

    '''
    # Colisão com a parte de baixo dos pads (EM MANUTENÇÃO)
    elif (bola.y <= raqueteEsq.y - bola.height or bola.y <= raqueteDir.y - bola.height) or (bola.y >= raqueteEsq.y + 
    raqueteEsq.height or bola.y >= raqueteDir.y + raqueteDir.height) and not (raqueteEsq.x + raqueteDir.width < bola.x < 
    raqueteDir.x - bola.width):
        velY *= -1
    '''

    # Colisão da bola com as laterais dos pads
    if bola.collided_perfect(padEsq) or bola.collided_perfect(padDir) and not quebrado:
        count += 1
        if count <= 10:
            velY *= 1.025
            velX *= -1.025
        else:
            velX *= -1

    # Colisão da bola com as laterais dos pads quebrados
    if quebrado and bola.collided(padEsqCima) or bola.collided(padEsqBaixo) or bola.collided(padDirCima) or bola.collided(padDirBaixo):
        count += 1
        if count <= 10:
            velY *= 1.025
            velX *= -1.025
        else:
            velX *= -1

    # Aceleração da bola
    if not pause:
        bola.move_x(velX * janela.delta_time())
        bola.move_y(velY * janela.delta_time())

    # Desenho de todos os elementos
    cenario.draw()
    padEsq.draw()
    padDir.draw()
    bola.draw()
    padEsqCima.draw()
    padEsqBaixo.draw()
    padDirCima.draw()
    padDirBaixo.draw()

    # Desenho do placar
    janela.draw_text(str(placarPlayer), janela.width / 2 - 50, 25, 26, (0, 0, 0), "Arial", True, False)
    janela.draw_text("X", janela.width / 2, 25, 26, (0, 0, 0), "Arial", True, False)
    janela.draw_text(str(placarIA), janela.width / 2 + 50, 25, 26, (0, 0, 0), "Arial", True, False)

    # Reinicialização da janela
    janela.update()