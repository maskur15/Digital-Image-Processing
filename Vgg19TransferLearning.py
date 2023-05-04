import os 
import zipfile 
import tensorflow as tf 
from tensorflow.keras.optimizers import RMSprop
path = '/content/drive/MyDrive/Colab Notebooks/DeeplearningAi/Dataset/'
path = os.path.join(path,'archive.zip')
zip_ref = zipfile.ZipFile(path,'r')
zip_ref.extractall('tmp/emotion')
train_dir = '/content/tmp/emotion/train'
test_dir= '/content/tmp/emotion/test'
!pip install split-folders

import splitfolders

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio(train_dir, output="output",
    seed=1337, ratio=(.8, .2), group_prefix=None, move=False) # default values

train_dir = "/content/output/train"
valid_dir = '/content/output/valid'
print(os.listdir(train_dir))

from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
                                   horizontal_flip = True,
                                   rotation_range=35)
   
valid_datagen= ImageDataGenerator()
train_generator = train_datagen.flow_from_directory(
    '/content/output/train',
target_size=(224,224),
    batch_size = 32,
    class_mode='categorical'
)
valid_generator = valid_datagen.flow_from_directory(
    '/content/output/val',
target_size=(224,224),
    batch_size = 32,
    class_mode = 'categorical'

)

from tensorflow import keras
from tensorflow.keras import layers

base_model = tf.keras.applications.VGG19(
    include_top=False,
    weights="imagenet",
    input_shape=(224,224,3),
)

base_model.trainable= False 
base_model.summary()
x=layers.Flatten()(base_model.output)
x=layers.Dense(1024,activation='relu')(x)
x=layers.Dense(512,activation='relu')(x)
x=layers.Dense(512,activation='relu') (x)

x=layers.Dense(7,activation='softmax')(x)
model = keras.Model(base_model.input,x)

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

epoch = 15
history = model.fit(
    train_generator,
    steps_per_epoch= 717,
    epochs=epoch,
    verbose =1,
    validation_data= valid_generator,
    validation_steps=179
)
