from color_models import selectRGB, gatherRGB, convertHSI, invertIntensity
from resampling import upNearest, upBilinear, downNearest, downArea, twoPassResampling, singlePassResampling

files = ['boy', 'carps', 'japan', 'landscape', 'strawberry', 'cat', 'cinderella', 'city', 'dino', 'street']

for name in files[:5]:
    directory = f"Pictures/color_models/{name}"
    filename = f"{directory}/{name}.png"

    RGBPath = f"{directory}/RGB/{name}"
    HSIPath = f"{directory}/HSI/{name}"

    RGBFiles = dict(red=f"{RGBPath}Red.png", green=f"{RGBPath}Green.png", blue=f"{RGBPath}Blue.png", check=f"{RGBPath}Check.png")

    HSIFiles = dict(HSI=f"{HSIPath}HSI.png", intensity=f"{HSIPath}Intensity.png", invIntensity=f"{HSIPath}InvIntensity.png", checkConvert=f"{HSIPath}CheckConvert.png", invIntensHSI=f"{HSIPath}InvIntensHSI.png")

    selectRGB(filename, RGBFiles['red'], RGBFiles['green'], RGBFiles['blue'])

    gatherRGB(RGBFiles['red'], RGBFiles['green'], RGBFiles['blue'], RGBFiles['check'])

    convertHSI(filename, HSIFiles['HSI'], HSIFiles['intensity'])

    invertIntensity(HSIFiles['HSI'], HSIFiles['invIntensity'], HSIFiles['checkConvert'], HSIFiles['invIntensHSI'])

    print('\n')

print(f"Work with the color models is completed\n")

for name in files[5:]:
    directory = f"Pictures/resampling/{name}"
    filename = f"{directory}/{name}.png"

    upsamplPath = f"{directory}/upsampling"
    downsamplPath = f"{directory}/downsampling"
    resamplPath = f"{directory}/resampling"

    upNearestFiles = [f"{upsamplPath}/x1.3/{name}Nearest.png", f"{upsamplPath}/x0.5/{name}Nearest.png", f"{upsamplPath}/x2/{name}Nearest.png"]
    upBilinearFiles = [f"{upsamplPath}/x1.3/{name}Bilinear.png", f"{upsamplPath}/x0.5/{name}Bilinear.png", f"{upsamplPath}/x2/{name}Bilinear.png"]
    downNearestFiles = [f"{downsamplPath}/x0.3/{name}Nearest.png", f"{downsamplPath}/x0.5/{name}Nearest.png", f"{downsamplPath}/x2/{name}Nearest.png"]
    downAreaFiles = [f"{downsamplPath}/x0.3/{name}Area.png", f"{downsamplPath}/x0.5/{name}Area.png", f"{downsamplPath}/x2/{name}Area.png"]
    twoPassFiles = [f"{resamplPath}/{name}TwoPass1.png", f"{resamplPath}/{name}TwoPass0.7.png", f"{resamplPath}/{name}TwoPass1.6.png"]
    singlePassFiles = [f"{resamplPath}/{name}SinglePass0.3.png", f"{resamplPath}/{name}SinglePass1.6.png"]

    # scale = float(input("Enter the decrease level of the image: "))
    scalesUp = [1.3, 0.5, 2]
    scalesDown = [0.3, 0.5, 2]
    scalesTwoPass = [[3, 3], [2, 3], [5, 3]]
    scalesSinglePass = [[1, 3], [5, 3]]

    for i in range(3):
        upNearest(filename, scalesUp[i], upNearestFiles[i])
        upBilinear(filename, scalesUp[i], upBilinearFiles[i])
        downNearest(filename, scalesDown[i], downNearestFiles[i])
        downArea(filename, scalesDown[i], downNearestFiles[i])
        print('\n')

    for i in range(1):
        twoPassResampling(filename, scalesTwoPass[i][0], scalesTwoPass[i][1], twoPassFiles[i])
        print('\n')

    for i in range(2):
        singlePassResampling(filename, scalesSinglePass[i][0], scalesSinglePass[i][1], singlePassFiles[i])

print(f"Work on resampling is completed")





