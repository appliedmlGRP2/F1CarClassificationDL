# F1CarClassificaionDL
This repository contains all the code developed for Formula one cars image classification project using deep learning and flask as part of module BT5153 - NUS MSBA cohort 2022-23.


The project aims to classify formula one car's images into one of the 8 constructors (the teams):
   -  AlphaTauri
   -  Ferrari
   -  McLaren
   -  Mercedes
   -  Racing Point
   -  Red Bull
   -  Renault
   -  Williams

# Table of Contents
  * [Setup and Requirements](#installation)
  * [Working Pipeline](#pipeline)
  * [Dataset](#dataset) 
  * [Imageaugmentation](#preprocessing)
  * [Usage](#usage)


# Setup and Requirements <a id="installation"></a>
For a list of required python packages see the *requirements.txt*
or just install them all at once using pip.
```
pip install -r requirements.txt
```

# Pipeline <a id="pipeline"></a>
<img width="508" alt="image" src="https://user-images.githubusercontent.com/93938450/233798673-850a8eb9-46e8-4b0e-9c8f-bd0cbc5d6c00.png">

The above diagram captures the main steps and the flow of the process:

# Dataset <a id="dataset"></a>
Dataset is from [kaggle]([https://www.flowkey.com/en](https://www.kaggle.com/datasets/vesuvius13/formula-one-cars)).

Dataset contains following image combinations for different constructor teams:
AlphaTauri : 123 Images
Ferrari : 374 Images
McLaren : 372 Images
Mercedes : 324 Images
Racing Point : 290 Images
Red Bull : 340 Images
Renault : 323 Images
Williams : 340 Images

# preprocessing
For image processing, [imgaug](https://imgaug.readthedocs.io/en/latest/) package was utilized.

We perform the following augmentations sequentially:
1)	Flipping the original image horizontally but with a probability of 50% i.e., it would not flip every time it is called. This is to include more randomness.
2)	Rotating the images by -45 to 45 degrees.
3)	Scaling the images by 50% to 150%.
4)	Changing the brightness by 50% to 150%.
5)	Applying Gaussian blur with sigma between 0 and 2. Gaussian blur is the result of blurring an image by a Gaussian function and it is typically done to reduce image noise and reduce detail.

![image](https://user-images.githubusercontent.com/93938450/233798183-d3f54203-56b0-4b20-aaaa-bb39468e1ec5.png)


# Usage
To run the webapp, please follow the instrucitons in the notebook.



