from gl import *


# Valores aleatorios
import random


# Desplegar resultado
# Referencia: https://www.geeksforgeeks.org/python-pil-image-show-method/
from PIL import Image

# Colores
red = color(1, 0, 0)
wh = color(1, 1, 1)

# Definicion de variables para versión aleatoria
firstValue = random.random()
secondValue = random.random()
thirdValue = random.random()

firstColor = random.randint(0, 1)
secondColor = random.randint(0, 1)
thirdColor = random.randint(0, 1)

firstX = random.randint(0, 1)
firstY = random.randint(0, 1)


def SoftwareRender1(fileName):
    r = Render(1000, 1000)
    r.glClearColor(firstValue, secondValue, thirdValue)
    r.glClear()
    r.glClearViewPort(color(0, 0, 0))
    r.glVertex(firstX, firstY, color(firstColor, secondColor, thirdColor))
    r.glFinish(fileName)
    im = Image.open(fileName)
    im.show()


def SoftwareRender2(filename):

    r = Render(1000, 1000)

    # Parte lateral 1
    r.glLine(100, 300, 300, 100, red)
    r.glLine(100, 300, 100, 500, red)
    r.glLine(100, 300, 400, 300, red)

    # Pared izquierda
    r.glLine(300, 100, 500, 100, red)
    r.glLine(400, 300, 500, 100, red)

    # Puerta
    r.glLine(100, 500, 250, 500, red)
    r.glLine(100, 650, 250, 650, red)
    r.glLine(250, 650, 250, 500, red)

    # Parte lateral 2
    r.glLine(100, 650, 100, 850, red)

    # Pared derecha
    r.glLine(100, 850, 400, 850, red)

    # Techo
    r.glLine(400, 850, 600, 600, red)
    r.glLine(600, 600, 400, 300, red)

    # Techo en 3D
    r.glLine(500, 100, 700, 400, red)
    r.glLine(600, 600, 700, 400, red)

    r.glFinish(filename)
    im = Image.open(filename)
    im.show()


def SoftwareRender3(filename):
    r = Render(1920, 1080)
    r.glModel(
        "Sonic.obj",
        translation=V3(1100, 80, 0),
        scalationFactor=V3(50, 50, 50),
    )
    r.glFinish(filename)
    im = Image.open(filename)
    im.show()


def Lab1(filename):
    r = Render(1920, 1080)
    figure1 = [
        V2(165, 380),
        V2(185, 360),
        V2(180, 330),
        V2(207, 345),
        V2(233, 330),
        V2(230, 360),
        V2(250, 380),
        V2(220, 385),
        V2(205, 410),
        V2(193, 383),
    ]
    figure2 = [V2(321, 335), V2(288, 286), V2(339, 251), V2(374, 302)]
    figure3 = [V2(377, 249), V2(411, 197), V2(436, 249)]
    figure4 = [
        V2(413, 177),
        V2(448, 159),
        V2(502, 88),
        V2(553, 53),
        V2(535, 36),
        V2(676, 37),
        V2(660, 52),
        V2(750, 145),
        V2(761, 179),
        V2(672, 192),
        V2(659, 214),
        V2(615, 214),
        V2(632, 230),
        V2(580, 230),
        V2(597, 215),
        V2(552, 214),
        V2(517, 144),
        V2(466, 180),
    ]

    r.glPolygon(figure1, wh)
    r.glPolygon(figure2, wh)
    r.glPolygon(figure3, wh)
    r.glPolygon(figure4, wh)

    r.glFinish(filename)
    im = Image.open(filename)
    im.show()


def SoftwareRender4(filename):
    r = Render(1920, 1080)
    r.shaderUsed = Shader.flatShading
    r.glModel(
        "Teddybear.obj",
        translation=V3(1100, 80, 1500),
        scalationFactor=V3(800, 800, 800),
        rotation=V3(90, 190, 90),
    )
    r.glFinish(filename)
    im = Image.open(filename)
    im.show()
