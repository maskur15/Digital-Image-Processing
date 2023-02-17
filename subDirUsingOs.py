#get all the current directory under the directory

#put the directory 

dataSet='/content/drive/MyDrive/Colab Notebooks/image-processing/motion/train'
subdirectory=list(os.scandir(dataSet))
for  sub in subdirectory:
  print(sub.name)
  
  
########################################
#get all the sub directory 
dir=list(os.walk(dataSet))
print(len(dir))
print(dir)
########################
