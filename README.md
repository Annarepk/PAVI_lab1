# OAVI_lab1
_Color models and image resampling_

The following task was set:

### Color models
1. Select the R, G, and B components and save them as separate images.
2. Bring the image to the HSI color model, save the brightness component as a separate image.
3. Invert the brightness component in the original image and save the derived image.

### Oversampling
1. Stretching (interpolating) the image by M times;
2. Compression (decimation) of the image by N times;
3. Oversampling the image by K=M/N times by stretching and then compressing (in two passes);
4. Oversampling the image K times in one pass.

***

## Functions

Functions for the first part of the given task are in the file `color_models.py`.

- `selectRGB(filename: str, redFilename: str, greenFilename: str, blueFilename: str)`
    > Selects the R, G, B components from the image and saves them in new files.
    >
    > _PARAMETERS:_
    >    * **filename** - Name of the file with the original image.
    >    * **redFilename** - Name of the file with the red component of the original image.
    >    * **greenFilename** - Name of the file with the green component of the original image.
    >    * **blueFilename** - Name of the file with the blue component of the original image.

- `gatherRGB(redFilename: str, greenFilename: str, blueFilename: str, resultFilename: str)`
    > Collects the original image from saved components for checking the result.
    >
    > _PARAMETERS:_
    >    * **redFilename** - Name of the file with the red component of the original image.
    >    * **greenFilename** - Name of the file with the green component of the original image.
    >    * **blueFilename** - Name of the file with the blue component of the original image.
    >    * **resultFilename** - Name of the collected file from the given components.

- `convertHSI(filename: str, HSIFilename: str, intensityFilename: str)`
    > Converts the image to the HSI color model and saves the brightness component as a separate image.
    >
    > _PARAMETERS:_
    >    * **filename** - Name of the file with the original image.
    >    * **HSIFilename** - Name of the result file with the image in the HSI color model.
    >    * **intensityFilename** - Name of the file with the brightness component of the original image.

- `HSItoRGB(H: int, S: int, I: int)`
    > Calculates the RGB color coordinates based on the HSI color coordinates.
    >
    > _PARAMETERS:_
    >    * **H, S, I** - Color coordinates of the pixel in the HSI color model.

- `invertIntensity(HSIFilename: str, invIntensFilename: str, checkConvertFilename: str, invIntensHSIFilename: str)`
    > Inverts the brightness component in the original image and saves the derived image.
    >
    > _PARAMETERS:_
    >    * **HSIFilename** - Name of the file with the original image in the HSI color model.
    >    * **invIntensFilename** - Name of the result file with the image with the inverted brightness component in the RGB color model.
    >    * **checkConvertFilename** - Name of the result file with the converted original HSI-image from the HSI to RGB color model.
    >    * **invIntensHSIFilename** - Name of the result file with the image with the inverted brightness component in the HSI color model.

Functions for the second part of the given task are in the file `resampling.py`.

- `upNearest(filename: str, m: float, resultFilename: str)`
    > Interpolates the image with the Nearest Neighbour method.
    >
    > _PARAMETERS:_
    >    * **filename** - Name of the file with the original image.
    >    * **m** - Scale of interpolation.
    >    * **resultFilename** - Name of the file with the resulting interpolated image.


- `upBilinear(filename, m, resultFilename)`
    > Interpolates the image with the Bilinear method.
    >
    > _PARAMETERS:_
    >    * **filename** - Name of the file with the original image.
    >    * **m** - Scale of interpolation.
    >    * **resultFilename** - Name of the file with the resulting interpolated image.
- `downNearest(filename, n, resultFilename)`
    > Decimates the image with the Nearest Neighbor method.
    >
    > _PARAMETERS:_
    >    * **filename** - name of the file with the original image.
    >    * **n** - scale of decimation.
    >    * **resultFilename** - name of the file with the result decimated image.

- `downArea(filename, n, resultFilename)`
    > Decimates the image with the Area Resampling method.
    >
    > _PARAMETERS:_
    >    * **filename** - name of the file with the original image.
    >    * **n** - scale of decimation.
    >    * **resultFilename** - name of the file with the result decimated image.

- `twoPassResampling(filename, m, n, resultFilename)`
    > Resamples the image by K=M/N times by stretching and then compressing (in two passes).
    > 
    > _PARAMETERS:_
    >    * **filename** - name of the file with the original image.
    >    * **m** - scale of interpolation.
    >    * **n** - scale of decimation.
    >    * **resultFilename** - name of the file with the result resampled image.

- `singlePassResampling(filename, m, n, resultFilename)`
    > Resamples the image K times in one pass.
    > 
    > _PARAMETERS:_
    >    * **filename** - name of the file with the original image.
    >    * **m** - scale of interpolation.
    >    * **n** - scale of decimation.
    >    * **resultFilename** - name of the file with the result resampled image.
