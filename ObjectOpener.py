"""
Created by:
Alejandro Gomez

Features:
Loading an object from a file
to use it on the rer.
"""


import struct


class ObjectOpener:
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.lines = file.read().splitlines()
        self.vertices = []
        self.texcoords = []
        self.normals = []
        self.faces = []
        self.glLines1()

    def glLines1(self):
        for line in self.lines:
            try:
                prefix, value = line.split(" ", 1)
            except:
                continue
            if prefix == "v":
                self.vertices.append(list(map(float, value.split(" "))))
            elif prefix == "f":
                self.faces.append(
                    [list(map(int, vert.split("/"))) for vert in value.split(" ")]
                )
            elif prefix == "vt":
                self.texcoords.append(list(map(float, value.split(" "))))
            elif prefix == "vn":
                self.normals.append(list(map(float, value.split(" "))))


class Texture(object):
    def __init__(self, filename):
        with open(filename, "rb") as file:
            file.seek(10)
            hS = struct.unpack("=l", file.read(4))[0]
            file.seek(18)
            self.width = struct.unpack("=l", file.read(4))[0]
            self.height = struct.unpack("=l", file.read(4))[0]
            file.seek(hS)
            self.pixels = []
            for y in range(self.height):
                pR = []
                for x in range(self.width):
                    b = ord(file.read(1)) / 255
                    g = ord(file.read(1)) / 255
                    r = ord(file.read(1)) / 255
                    pR.append([r, g, b])
                self.pixel.append(pR)

    def getColor(self, u, v):
        if 0 <= u <= 1 and 0 <= v <= 1:
            valueTemp = [int(v * self.height)][int(u * self.width)]
            return self.pixels[int(v * self.height)][int(u * self.width)]
        else:
            return None


"""
Referencia:
https://j2logo.com/args-y-kwargs-en-python/
https://es.wikipedia.org/wiki/Sombreado_plano
https://graphics.fandom.com/wiki/Flat_shading
https://www.giantbomb.com/flat-shading/3015-2277/
https://cglearn.codelight.eu/pub/computer-graphics/shading-and-lighting
"""


class Shader:
    @staticmethod
    def flatShading(render, **kwargs) -> None:

        u, v, w = kwargs["baryCoords"]
        b, g, r = kwargs["colorU"]
        tA, tB, tC = kwargs["textureCoords"]
        tN = kwargs["triangleNormal"]

        b = b / 255
        g = g / 255
        r = r / 255

        if render.textureUsed:
            tU = tA[0] * u + tB[0] * v + tC[0] * w
            tV = tA[1] * u + tB[1] * v + tC[1] * w

            text_color = render.textureUsed.getColor(tU, tV)
            b *= text_color[2]
            g *= text_color[1]
            r *= text_color[0]

        luzDirecta = [render.luzDirecta.x, render.luzDirecta.y, render.luzDirecta.z]
        invertedLight = [(-i) for i in luzDirecta]

        result = 0
        for i in range(0, len(tN)):
            result += tN[i] * invertedLight[i]
        finalValue = result

        b *= finalValue
        g *= finalValue
        r *= finalValue

        if finalValue > 0:
            return r, g, b
        return 0, 0, 0
