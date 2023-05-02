path = '/content/drive/MyDrive/Colab Notebooks/DeeplearningAi/Dataset/'
path = os.path.join(path,'archive.zip')
zip_ref = zipfile.ZipFile(path,'r')
zip_ref.extractall('tmp/emotion') #zip file extract to this folder 
