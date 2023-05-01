  train_datagen = ImageDataGenerator(rescale=1.0/255,
                                     horizontal_flip=True,
                                     vertical_flip=True,
                                     rotation_range = 30,
                                     brightness_range = [0.4,0.99],
                                     width_shift_range= 0.1,
                                     height_shift_range=0.1,
                                     zoom_range=[0.8,1.25],
                                     shear_range=30,
                                     )
  train_datagen = ImageDataGenerator(rescale = 1./255.,
                                   rotation_range = 40,
                                   width_shift_range = 0.2,
                                   height_shift_range = 0.2,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

   train_datagen = ImageDataGenerator(rescale=1.0/255,rotation_range=30,
                                     width_shift_range=.3,
                                     shear_range=.3,
                                     zoom_range=0.2,
                                     fill_mode='nearest',horizontal_flip=True,)
