
import pandas as pd
df = pd.read_csv('train1.csv')
df

dataset = df.values
dataset


X = dataset[:,0:10]
Y = dataset[:,10]

from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)
X_scale

from sklearn.model_selection import train_test_split

X_train,X_val_test, Y_train, Y_val_test = train_test_split(X_scale,Y,test_size = 0.3)

X_val,X_test, Y_val, Y_test = train_test_split(X_scale,Y,test_size = 0.5)

print(X_train.shape,X_val.shape, X_test.shape)

from keras.models import Sequential
from keras.layers import Dense
import tensorflow
model = Sequential([    Dense(32, activation='relu', input_shape=(10,)),    Dense(32, activation='relu'),    Dense(1, activation='sigmoid'),])

model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

hist = model.fit(X_train, Y_train, batch_size=32, epochs=100, validation_data=(X_val, Y_val))

model.evaluate(X_test,Y_test)[1]

# import matplotlib.pyplot as plt
#
# plt.plot(hist.history['loss'])
# plt.plot(hist.history['val_loss'])
# plt.title('Model Loss')
# plt.ylabel('Loss')
# plt.xlabel('Epoch')
# plt.legend(['Train', 'Val'], loc='upper right')
# plt.show()
#
# plt.plot(hist.history['acc'])
# plt.plot(hist.history['val_acc'])
# plt.title('Model accuracy')
# plt.ylabel('Accuracy')
# plt.xlabel('Epoch')
# plt.legend(['Train', 'Val'], loc='lower right')
# plt.show()
#
