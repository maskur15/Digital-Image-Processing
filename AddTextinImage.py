# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# Open an Image
img=Image.open('/content/drive/MyDrive/Colab Notebooks/image-processing/gold fish.jpg').resize((224,224))
font = ImageFont.load_default()

draw = ImageDraw.Draw(img)
draw.text(( 20, 32), image_label[predicted_class], (255,0,0), font=font)
img
