CAT_SOURCE_DIR = "/tmp/PetImages/Cat/"
DOG_SOURCE_DIR = "/tmp/PetImages/Dog/"
c=0
TRAINING_DIR = "/tmp/cats-v-dogs/training/"
VALIDATION_DIR = "/tmp/cats-v-dogs/validation/"

TRAINING_DOGS_DIR = os.path.join(TRAINING_DIR,'dogs/')
VALIDATION_DOGS_DIR = os.path.join(VALIDATION_DIR, "dogs/")

img_path = []
split_size = .9
c=0
for file in  os.scandir(DOG_SOURCE_DIR):
  if os.path.getsize(file.path)==0:
    print(os.path.basename(file.path),'is zero length, so ignoring.')
  else : 
    img_path.append(os.path.basename(file.path))

random.shuffle(img_path) 
index =  int(split_size* len(img_path))
train_path,valid_path = img_path[:index],img_path[index:]
for path in train_path:
   src = os.path.join(DOG_SOURCE_DIR,path)
   dest = os.path.join(TRAINING_DOGS_DIR,path)
   copyfile(src,dest)
for path in valid_path :
  src = os.path.join(DOG_SOURCE_DIR,path)
  dest = os.path.join(VALIDATION_DOGS_DIR,path)
  copyfile(src,dest)
