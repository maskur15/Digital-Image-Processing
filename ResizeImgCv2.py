img=cv2.imread('/content/drive/MyDrive/Colab Notebooks/image-processing/datasets/flower_photos/roses/7345657862_689366e79a.jpg')
print(img.shape)
cropImage=cv2.resize(img,(224,224))
print(cropImage.shape)
cv2_imshow(cropImage)

