angry=list(data_dir.glob('angry/*'))
c=0
for em in angry:
  print(c)
  img=cv2.imread(str(em))
  try:
    img=cv2.resize(img,(224,224))
    c+=1
    X.append(img)
  except:
    print(em)
