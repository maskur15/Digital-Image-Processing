from PIL import Image
import numpy as np
#goldFish is the numpy array 
numpy_image=goldFish*255.0
#if the numpy array is scaled in between 0 to 1 multiply by 255.0 to get the color image 
PIL_image = Image.fromarray(np.uint8(numpy_image)).convert('RGB')
PIL_image
#also the following code can work 
PIL_image = Image.fromarray(numpy_image.astype('uint8'), 'RGB')
