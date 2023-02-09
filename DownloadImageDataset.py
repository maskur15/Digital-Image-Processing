import numpy as np
import time

import PIL.Image as Image
import matplotlib.pylab as plt

import tensorflow as tf
import tensorflow_hub as hub


import datetime

%load_ext tensorboard
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file('flower_photos', origin=dataset_url,  cache_dir='/content/drive/MyDrive/Colab Notebooks/image-processing', untar=True)
# cache_dir indicates where to download data. I specified . which means current directory
# untar true will unzip it
data_dir

#converting the path in  os readable 
import pathlib
data_dir = pathlib.Path(data_dir)
data_dir
image_count=len(list(data_dir.glob('*/*.jpg'))) #all image path in data_dir ending with .jpg
image_count

#############
roses=(list(data_dir.glob('roses/*'))) #all the images path in the roses folder 
daisy=(list(data_dir.glob('daisy/*')))
print('rose: ',len(roses),'daisy: ',len(daisy))
###################
#show the image using Image.open()
roses[:4]
Image.open(roses[0])
###################
