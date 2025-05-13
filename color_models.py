from PIL import Image
from math import acos, pi, sqrt


def selectRGB(filename, redFilename, greenFilename, blueFilename):
    with Image.open(filename) as img:
        redImg = img.copy()
        greenImg = img.copy()
        blueImg = img.copy()

        width, height = img.size

        pix = img.load()
        redPix = redImg.load()
        greenPix = greenImg.load()
        bluePix = blueImg.load()

        for x in range(width):
            for y in range(height):
                redPix[x, y] = (pix[x, y][0], 0, 0)
                greenPix[x, y] = (0, pix[x, y][1], 0)
                bluePix[x, y] = (0, 0, pix[x, y][2])
        redImg.save(redFilename)
        greenImg.save(greenFilename)
        blueImg.save(blueFilename)
    print(f"The R, G, B components are selected from the {filename.split('/')[2]}...")


def gatherRGB(redFilename, greenFilename, blueFilename, resultFilename):
    redImg = Image.open(redFilename)
    greenImg = Image.open(greenFilename)
    blueImg = Image.open(blueFilename)
    resultImg = redImg.copy()

    width, height = redImg.size

    redPix = redImg.load()
    greenPix = greenImg.load()
    bluePix = blueImg.load()
    resultPix = resultImg.load()

    for x in range(width):
        for y in range(height):
            resultPix[x, y] = (redPix[x, y][0], greenPix[x, y][1], bluePix[x, y][2])

    resultImg.save(resultFilename)
    print(f"{resultFilename.split('/')[2]} is compiled from the R, G, and B components for verification...")


def convertHSI(filename, HSIFilename, intensityFilename):
    with Image.open(filename) as img:
        HSIImg = img.copy()
        intensityImg = Image.new('L', img.size)

        width, height = img.size

        pix = img.load()
        HSIPix = HSIImg.load()
        intensityPix = intensityImg.load()

        for x in range(width):
            for y in range(height):
                r, g, b = pix[x, y]

                r = r / 255
                g = g / 255
                b = b / 255

                if r == g == b:
                    h = 0
                    if r == 0:
                        s = 0
                    else:
                        s = 1 - 3 / (r + g + b) * min(r, g, b)
                else:
                    h = 180 / pi * acos(((r - g) + (r - b)) / 2 / sqrt((r - g) ** 2 + (r - b) * (g - b)))
                    h = h if b <= g else 360 - h

                    s = 1 - 3 / (r + g + b) * min(r, g, b)

                i = (r + g + b) / 3
                HSIPix[x, y] = (int(round(h / 360 * 255)), int(round(s * 255)), int(round(i * 255)))
                intensityPix[x, y] = int(round(i * 255))

        HSIImg.save(HSIFilename)
        intensityImg.save(intensityFilename)
        print(f"{filename.split('/')[2]} was converted to HSI...")
        print(f"The intensity component is selected from {filename.split('/')[2]}...")


def HSItoRGB(H, S, I):
    H = H / 255 * 360
    S = S / 255
    I = I / 255

    if S == 0.0:
        R = I
        G = I
        B = I

    else:
        H /= 60.0
        i = int(H)
        f = H - i
        p = I * (1 - S)
        q = I * (1 - S * f)
        t = I * (1 - S * (1 - f))

        if i == 0:
            R = I
            G = t
            B = p

        elif i == 1:
            R = q
            G = I
            B = p

        elif i == 2:
            R = p
            G = I
            B = t

        elif i == 3:
            R = p
            G = q
            B = I

        elif i == 4:
            R = t
            G = p
            B = I

        else:
            R = I
            G = p
            B = q

    return int(round(R * 255)), int(round(G * 255)), int(round(B * 255))


def invertIntensity(HSIFilename, invIntensFilename, checkConvertFilename, invIntensHSIFilename):
    with Image.open(HSIFilename) as img:
        invIntensImg = img.copy()
        checkConvertImg = img.copy()
        invIntensHSIImg = img.copy()

        width, height = img.size

        HSIPix = img.load()
        invIntensPix = invIntensImg.load()
        checkConvertPix = checkConvertImg.load()
        invIntensHSIPix = invIntensHSIImg.load()

        for x in range(width):
            for y in range(height):
                invIntensPix[x, y] = HSItoRGB(HSIPix[x, y][0], HSIPix[x, y][1], (1 - HSIPix[x, y][2] / 255) * 255)
                invIntensHSIPix[x, y] = HSIPix[x, y][0], HSIPix[x, y][1], int((1 - HSIPix[x, y][2] / 255) * 255)
                checkConvertPix[x, y] = HSItoRGB(HSIPix[x, y][0], HSIPix[x, y][1], HSIPix[x, y][2])

        invIntensImg.save(invIntensFilename)
        checkConvertImg.save(checkConvertFilename)
        invIntensHSIImg.save(invIntensHSIFilename)
        print(f"The intensity component in {HSIFilename.split('/')[-1][:-7] + '.png'} is inverted")





