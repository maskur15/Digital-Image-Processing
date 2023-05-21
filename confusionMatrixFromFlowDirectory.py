from sklearn.metrics import confusion_matrix
num_of_test_samples = 262 #number of images in test directory
Y_pred = model.predict(valid_generator, num_of_test_samples // batch_size+1)
y_pred = np.argmax(Y_pred, axis=1)
print('Confusion Matrix')
confusion_matrix = confusion_matrix(valid_generator.classes, y_pred)
print(confusion_matrix)

#display the confusion_matrix using color 
from sklearn import metrics
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ['angry','disgust','happy','worry'])

cm_display.plot()
plt.show()
