# grader-required-cell

# GRADED FUNCTION: parse_data_from_input
def parse_data_from_input(filename):
  """
  Parses the images and labels from a CSV file
  
  Args:
    filename (string): path to the CSV file
    
  Returns:
    images, labels: tuple of numpy arrays containing the images and labels
  """
  with open(filename) as file:
    ### START CODE HERE

    # Use csv.reader, passing in the appropriate delimiter
    # Remember that csv.reader can be iterated and returns one line in each iteration
    csv_reader = csv.reader(file, delimiter=',')
    
    labels = []
    array = []
    c=0
    for row in csv_reader:
      if c==0: c+=1; continue ; #skipping the first row 
      array.append(row[1:])
      labels.append(row[0])
     
    images = np.array(array).reshape(len(array),28,28).astype(int)
    labels= np.array(labels).astype(int)
    
    ### END CODE HERE

    return images, labels
  
TRAINING_FILE = './sign_mnist_train.csv'

images,labels= parse_data_from_input(TRAINING_FILE)
