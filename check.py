from color_models import selectRGB, gatherRGB, convertHSI, invertIntensity
from resampling import upNearest, upBilinear, downNearest, downArea, twoPassResampling, singlePassResampling

files = 'check'

directory = f"Pictures/check"
filename = f"{directory}/check.png"

RGBPath = f"{directory}/RGB/"
HSIPath = f"{directory}/HSI/"

RGBFiles = dict(red=f"{RGBPath}Red.png", green=f"{RGBPath}Green.png", blue=f"{RGBPath}Blue.png", check=f"{RGBPath}Check.png")

HSIFiles = dict(HSI=f"{HSIPath}HSI.png", intensity=f"{HSIPath}Intensity.png", invIntensity=f"{HSIPath}InvIntensity.png", checkConvert=f"{HSIPath}CheckConvert.png", invIntensHSI=f"{HSIPath}InvIntensHSI.png")

selectRGB(filename, RGBFiles['red'], RGBFiles['green'], RGBFiles['blue'])

gatherRGB(RGBFiles['red'], RGBFiles['green'], RGBFiles['blue'], RGBFiles['check'])

convertHSI(filename, HSIFiles['HSI'], HSIFiles['intensity'])

invertIntensity(HSIFiles['HSI'], HSIFiles['invIntensity'], HSIFiles['checkConvert'], HSIFiles['invIntensHSI'])

print('\n')

print(f"Work with the color models is completed\n")

upsamplPath = f"{directory}/upsampling"
downsamplPath = f"{directory}/downsampling"
resamplPath = f"{directory}/resampling"

upNearestFiles = [f"{upsamplPath}/x1.3/Nearest.png", f"{upsamplPath}/x0.5/Nearest.png", f"{upsamplPath}/x2/Nearest.png"]
upBilinearFiles = [f"{upsamplPath}/x1.3/Bilinear.png", f"{upsamplPath}/x0.5/Bilinear.png", f"{upsamplPath}/x2/Bilinear.png"]
downNearestFiles = [f"{downsamplPath}/x0.3/Nearest.png", f"{downsamplPath}/x0.5/Nearest.png", f"{downsamplPath}/x2/Nearest.png"]
downAreaFiles = [f"{downsamplPath}/x0.3/Area.png", f"{downsamplPath}/x0.5/Area.png", f"{downsamplPath}/x2/Area.png"]
twoPassFiles = [f"{resamplPath}/TwoPass1.png", f"{resamplPath}/TwoPass0.7.png", f"{resamplPath}/TwoPass1.6.png"]
singlePassFiles = [f"{resamplPath}/SinglePass0.3.png", f"{resamplPath}/SinglePass1.6.png"]

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





