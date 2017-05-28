import numpy as np
import pickle

def one_hot(l):
    return (np.arange(num_labels) == l).astype(np.float32)
    
def reformat(dataset, labels):
  dataset = dataset.reshape(
    (-1, image_height, image_length, num_channels)).astype(np.float32)
  one_hot_labels = [one_hot(labels[0])]
  for i in range(1, len(labels)):
    one_hot_labels= np.concatenate((one_hot_labels,[one_hot(labels[i])]), axis=0)
  return dataset, one_hot_labels

# reformat values
image_height = 28
image_length = 28
num_labels = 10
num_channels = 1 # grayscale

filename = 'notMNIST.pickle'
with open(filename, mode='rb') as file:
	save = pickle.load(file, encoding='latin1')
	features = save['train_dataset']
	labels = save['train_labels']
	valid_features = save['valid_dataset']
	valid_labels = save['valid_labels']
	del save

print(features.shape, labels.shape)
print(valid_features.shape, valid_labels.shape)

features, labels = reformat(features, labels)
valid_features, valid_labels = reformat(valid_features, valid_labels)
print(features.shape, labels.shape)
print(valid_features.shape, valid_labels.shape)

filename = 'train_data.p'
pickle.dump((features, labels), open(filename, 'wb'))
filename = 'valid_data.p'
pickle.dump((valid_features, valid_labels), open(filename, 'wb'))