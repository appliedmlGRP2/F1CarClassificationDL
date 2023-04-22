## Boosting Fan Experience with F1 Car Image Analysis

<img width="617" alt="Webapp" src="https://user-images.githubusercontent.com/93938450/233799574-d226a25a-ca48-4eed-be8c-66595e9e6083.png">



This repository contains all the code developed for Formula one cars image classification project using deep learning and flask as part of module [BT5153 - NUS MSBA cohort 2022-23](https://bt5153msba.github.io/).


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
  * [Image Augmentation](#preprocessing)
  * [Modelling](#Modelling)


# Setup and Requirements <a id="installation"></a>
For a list of required python packages see the *requirements.txt*
or just install them all at once using pip.
```
pip install -r requirements.txt
```

# Pipeline <a id="pipeline"></a>
<img width="362" alt="image" src="https://user-images.githubusercontent.com/93938450/233799030-8f993977-32f9-422f-8812-ff2d36d0ae70.png">

The above diagram captures the main steps and the flow of the process:

# Dataset <a id="dataset"></a>
Dataset is from kaggle - [link](https://www.kaggle.com/datasets/vesuvius13/formula-one-cars)

Dataset contains following image combinations for different constructor teams:
* AlphaTauri : 123 Images
* Ferrari : 374 Images
* McLaren : 372 Images
* Mercedes : 324 Images
* Racing Point : 290 Images
* Red Bull : 340 Images
* Renault : 323 Images
* Williams : 340 Images

Note: snapshot of the dataset is uploaded to this repo.

# Preprocessing
For image processing, [imgaug](https://imgaug.readthedocs.io/en/latest/) package was utilized.

We perform the following augmentations sequentially:
1)	Flipping the original image horizontally but with a probability of 50% i.e., it would not flip every time it is called. This is to include more randomness.
2)	Rotating the images by -45 to 45 degrees.
3)	Scaling the images by 50% to 150%.
4)	Changing the brightness by 50% to 150%.
5)	Applying Gaussian blur with sigma between 0 and 2. Gaussian blur is the result of blurring an image by a Gaussian function and it is typically done to reduce image noise and reduce detail.

![image](https://user-images.githubusercontent.com/93938450/233798183-d3f54203-56b0-4b20-aaaa-bb39468e1ec5.png)

# Modelling
* Baseline CNN Model
* ResNet-18 - Finetuned with and w/o layers freeze.
* VGG-16 - Finetuned with and w/o layers freeze.
* MobileNet_V2 - Finetuned with and w/o layers freeze.




