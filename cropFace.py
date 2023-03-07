import os 
import cv2
dir_path = r'F:\it18021\archive\python\photos\disgust\img'
save_inDir=r'F:\it18021\disgust_face'
img_list=([ (os.path.join(dir_path,img)) for img in os.listdir(dir_path) ])
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
num=0
for img in img_list:
    num+=1
    img=cv2.imread(img)
  #  plt.imshow(img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h),
                    (0, 0, 255), 2)

        faces = img[y:y + h, x:x + w]
        #cv2.imshow("face",faces)
        cv2.imwrite(os.path.join(save_inDir,('disgust'+str(num)+'.jpg')), faces)


