#train directoroy flow will convert the folder as label in one hot encoding where the folder is 
#label as the alphabetical order and assign value 0 based to the folder 

label = {0:'angry',1:'disgust',2:'happy',3:'worry'}
batch_size= 32
from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(    rescale=1./255,
    rotation_range = 10,
    horizontal_flip = True,
    width_shift_range=0.1,
    height_shift_range=0.1,
    fill_mode = 'nearest')
   
valid_datagen= ImageDataGenerator(rescale=1.0/255)
train_generator = train_datagen.flow_from_directory(
    '/content/output/train',
    target_size=(224,224),
    batch_size = batch_size,
    #color_mode = 'grayscale',
    class_mode='categorical'
)
valid_generator = valid_datagen.flow_from_directory(
    '/content/output/val',
    target_size = (224,224),
    batch_size = batch_size,
    #color_mode='grayscale',
    class_mode = 'categorical'

)
