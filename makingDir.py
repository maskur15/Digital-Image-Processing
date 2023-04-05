
# grader-required-cell

# Define root directory
root_dir = '/tmp/cats-v-dogs'

# Empty directory to prevent FileExistsError is the function is run several times
if os.path.exists(root_dir):
  shutil.rmtree(root_dir)

# GRADED FUNCTION: create_train_val_dirs
def create_train_val_dirs(root_path):
  """
  Creates directories for the train and test sets
  
  Args:
    root_path (string) - the base directory path to create subdirectories from
  
  Returns:
    None
  """
  ### START CODE HERE

  # HINT:
  # Use os.makedirs to create your directories with intermediate subdirectories
  # Don't hardcode the paths. Use os.path.join to append the new directories to the root_path parameter
  root_dir = os.mkdir(root_path)
  val_path =os.path.join(root_path,'validation')
  train_path = os.path.join(root_path,'training')

  os.mkdir(val_path)
  os.mkdir(train_path)

  train_cats_path = os.path.join(train_path,'cats')
  train_dogs_path = os.path.join(train_path,'dogs')

  valid_cats_path = os.path.join(val_path,'cats')
  valid_dogs_path = os.path.join(val_path,'dogs')
  
  os.mkdir(train_cats_path)
  os.mkdir(train_dogs_path)
  os.mkdir(valid_cats_path)
  os.mkdir(valid_dogs_path)


  pass
  

  ### END CODE HERE

  
try:
  create_train_val_dirs(root_path=root_dir)
except FileExistsError:
  print("You should not be seeing this since the upper directory is removed beforehand")
