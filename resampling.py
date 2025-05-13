from PIL import Image


def upNearest(filename, m, resultFilename):
    with Image.open(filename) as img:
        width, height = img.size
        resultImg = Image.new('RGB', (round(width * m), round(height * m)))

        pix = img.load()
        resultPix = resultImg.load()

        for x in range(resultImg.width):
            for y in range(resultImg.height):
                X = int(x / m)
                Y = int(y / m)
                resultPix[x, y] = (pix[X, Y][0], pix[X, Y][1], pix[X, Y][2])

        resultImg.save(resultFilename)

    print(f"Nearest neighbor interpolation of {filename.split('/')[-1]} on x{m} is completed...")


def upBilinear(filename, m, resultFilename):
    with (Image.open(filename) as img):
        width, height = img.size
        resultImg = Image.new('RGB', (round(width * m), round(height * m)))

        pix = img.load()
        resultPix = resultImg.load()

        for x in range(resultImg.width):
            for y in range(resultImg.height):
                X = x / m
                Y = y / m
                x1, x2 = int(X), min(round(X), img.width - 1)
                y1, y2 = int(Y), min(round(Y), img.height - 1)
                dx, dy = X - x1, Y - y1

                # Вес для(x1, y1):
                f1 = (1 - dx) * (1 - dy)

                # Вес для(x2, y1):
                f2 = dx * (1 - dy)

                # Вес для(x1, y2):
                f3 = (1 - dx) * dy

                # Вес для(x2, y2):
                f4 = dx * dy

                q11 = pix[x1, y1]
                q21 = pix[x2, y1]
                q12 = pix[x1, y2]
                q22 = pix[x2, y2]

                red = q11[0] * f1 + q21[0] * f2 + q12[0] * f3 + q22[0] * f4
                green = q11[1] * f1 + q21[1] * f2 + q12[1] * f3 + q22[1] * f4
                blue = q11[2] * f1 + q21[2] * f2 + q12[2] * f3 + q22[2] * f4

                resultPix[x, y] = (int(red), int(green), int(blue))

        resultImg.save(resultFilename)

    print(f"Bilinear interpolation of {filename.split('/')[-1]} on x{m} is completed...")


def downNearest(filename, n, resultFilename):
    with Image.open(filename) as img:
        width, height = img.size
        resultImg = Image.new('RGB', (int(width * n), int(height * n)))

        pix = img.load()
        resultPix = resultImg.load()

        for x in range(resultImg.width):
            for y in range(resultImg.height):
                X = int(x / n)
                Y = int(y / n)
                resultPix[x, y] = pix[X, Y]

        resultImg.save(resultFilename)

    print(f"Nearest neighbor decimation of {filename.split('/')[-1]} on x{float(1 / n):2.1f} is completed...")


def downArea(filename, n, resultFilename):
    with Image.open(filename) as img:
        width, height = img.size
        resultImg = Image.new('RGB', (round(width * n), round(height * n)))

        pix = img.load()
        resultPix = resultImg.load()

        for x in range(resultImg.width):
            for y in range(resultImg.height):
                tmpPix = [0, 0, 0]
                x1, x2 = max(0, min(int(x / n), width - 1)), min(width - 1, int((x + 1) / n))
                y1, y2 = max(0, min(int(y / n), height - 1)), min(height - 1, int((y + 1) / n))
                N = (x2 - x1 + 1) * (y2 - y1 + 1)
                for X in range(x1, x2 + 1):
                    for Y in range(y1, y2 + 1):
                        tmpPix[0] += pix[X, Y][0]
                        tmpPix[1] += pix[X, Y][1]
                        tmpPix[2] += pix[X, Y][2]
                resultPix[x, y] = int(tmpPix[0] / N), int(tmpPix[1] / N), int(tmpPix[2] / N)

        resultImg.save(resultFilename)

    print(f"Area decimation of {filename.split('/')[-1]} on x{float(1 / n):2.1f} is completed...")


def twoPassResampling(filename, m, n, resultFilename):
    tmpResultFilename = resultFilename[:-4] + 'Tmp' + resultFilename[-4:]
    upBilinear(filename, m, tmpResultFilename)
    downArea(tmpResultFilename, 1 / n, resultFilename)
    print(f"Two-pass resampling of {filename.split('/')[-1]} on x{m / n:.1f} is completed...")


def singlePassResampling(filename, m, n, resultFilename):
    downArea(filename, m / n, resultFilename)
    print(f"Single-pass resampling of {filename.split('/')[-1]} on x{float(m / n):.1f} is completed...")


