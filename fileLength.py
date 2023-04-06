DOG_SOURCE_DIR = "/tmp/PetImages/Dog/"
c=0
for file in os.scandir(CAT_SOURCE_DIR):
  if os.path.getsize(file.path)==0:
    print(os.path.basename(file.path),'is zero length, so ignoring.')
