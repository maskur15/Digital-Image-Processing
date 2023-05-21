# Load the FER2013 dataset
data = pd.read_csv("fer2013.csv")

# Prepare the image and label data
x = []
y = []
for i in range(len(data)):
    x.append([int(j) for j in data['pixels'][i].split()])
    y.append(data['emotion'][i])
x = np.array(x) / 255.0
y = np.array(y)

# Reshape the input data and convert labels to one-hot encoding
x = x.reshape(x.shape[0], 48, 48, 1)
y = pd.get_dummies(y).values
