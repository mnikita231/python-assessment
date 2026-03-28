#task1_7.py 

from keras.datasets import mnist
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# load dataset
(trainX, trainY), (testX, testY) = mnist.load_data()

# reshape dataset to have a single channel
width, height, channels = trainX.shape[1], trainX.shape[2], 1
trainX = trainX.reshape((trainX.shape[0], width, height, channels))
testX = testX.reshape((testX.shape[0], width, height, channels))

# report pixel means and standard deviations
print('Statistics train=%.3f (%.3f), test=%.3f (%.3f)' % 
      (trainX.mean(), trainX.std(), testX.mean(), testX.std()))

# create generator for standardization
datagen = ImageDataGenerator(featurewise_center=True,
                             featurewise_std_normalization=True)

# calculate mean and std on training dataset
datagen.fit(trainX)
print('Data Generator mean=%.3f, std=%.3f' % 
      (datagen.mean.item(), datagen.std.item()))

# demonstrate effect on a single batch
iterator = datagen.flow(trainX, trainY, batch_size=64)
batchX, batchy = next(iterator)
print('Batch shape:', batchX.shape)
print('Batch mean:', batchX.mean())
print('Batch std:', batchX.std())

# demonstrate effect on entire training dataset
iterator = datagen.flow(trainX, trainY, batch_size=len(trainX), shuffle=False)
batchX, batchy = next(iterator)
print('Full dataset shape:', batchX.shape)
print('Full dataset mean:', batchX.mean())
print('Full dataset std:', batchX.std())