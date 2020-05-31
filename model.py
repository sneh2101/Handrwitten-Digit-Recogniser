import tensorflow as tf
from tensorflow import keras
from keras.datasets import mnist


(x_train,y_train),(x_test,y_test)  = mnist.load_data()

#preprocessing images
x_train = x_train.reshape(x_train.shape[0],28,28,1)
x_test = x_test.reshape(x_test.shape[0],28,28,1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train =x_train/255
x_test = x_test/255

y_train = keras.utils.to_categorical(y_train,10)
y_test = keras.utils.to_categorical(y_test,10)


#Creating the model
batch_size = 128
epochs =10

model = keras.models.Sequential()
model.add(keras.layers.Conv2D(64,(3,3),activation='relu',input_shape=(28,28,1)))
model.add(keras.layers.MaxPool2D(2,2))
model.add(keras.layers.Conv2D(64,(3,3),activation='relu'))
model.add(keras.layers.MaxPool2D(2,2))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(128,activation = 'relu'))
model.add(keras.layers.Dense(10,activation = 'softmax'))

#model.summary()

#fitting the model
model.compile(loss ='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
hist = model.fit(x_train,y_train,epochs=epochs,batch_size=batch_size, validation_data =(x_test,y_test))

print(model.predict(x_test[5]))
import numpy as np
print(np.argmax(y_test[5]))
      
                    
#saving the model
model.save('mnist.h5')

#evaluating the model
score = model.evaluate(x_test,y_test)
print('Loss:',score[0])
print('Accuracy:',score[1])


