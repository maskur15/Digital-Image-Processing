import numpy as np
import time

import PIL.Image as Image
import matplotlib.pylab as plt
IMAGE_SHAPE=(224,224)
goldFish=Image.open('/content/drive/MyDrive/Colab Notebooks/image-processing/gold fish.jpg').resize(IMAGE_SHAPE)

