from PIL import Image

pathIn = "Pictures/resampling/street/resampling/streetTwoPass1.6.png"
pathOut = "Pictures/resampling/street/resampling/streetTwoPass1.6Crop.png"

with Image.open(pathIn) as img:
    imgCrop = img.crop((2225*0.3, 3333*0.5, 2225*0.4, 3333*0.56))    # left, up, right, down
    imgCrop.save(pathOut)
