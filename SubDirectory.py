folder='/content/drive/MyDrive/Colab Notebooks/image-processing/fer2013'
subfolders = [ f.name for f in os.scandir(folder) if f.is_dir() ] # use f.path to get the path of each subfolder 
subfolders
