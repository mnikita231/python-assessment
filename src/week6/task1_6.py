#task1_6.py

from keras.datasets import mnist
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# load dataset
(trainX, trainY), (testX, testY) = mnist.load_data()

# reshape dataset to have a single channel
width, height, channels = trainX.shape[1], trainX.shape[2], 1
trainX = trainX.reshape((trainX.shape[0], width, height, channels))
testX = testX.reshape((testX.shape[0], width, height, channels))

# report mean pixel value
print('Means train=%.3f, test=%.3f' % (trainX.mean(), testX.mean()))

# create generator that centers pixel values
datagen = ImageDataGenerator(featurewise_center=True)

# calculate mean on training dataset
datagen.fit(trainX)
print('Data Generator Mean: %.3f' % datagen.mean)

# demonstrate effect on a single batch
iterator = datagen.flow(trainX, trainY, batch_size=64)
batchX, batchy = next(iterator)
print('Batch shape:', batchX.shape)
print('Batch mean:', batchX.mean())

# demonstrate effect on entire training dataset
iterator = datagen.flow(trainX, trainY, batch_size=len(trainX), shuffle=False)
batchX, batchy = next(iterator)
print('Full dataset shape:', batchX.shape)
print('Full dataset mean:', batchX.mean()) 