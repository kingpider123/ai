from engine import Value as Value

from keras.datasets import mnist
import keras
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()
train_images = np.asarray(x_train, dtype=np.float32) / 255.0
test_images = np.asarray(x_test, dtype=np.float32) / 255.0
train_images = train_images.reshape(60000, 784)
test_images = test_images.reshape(10000, 784)
y_train = keras.utils.to_categorical(y_train)

def forward(X,Y,W):
    y_predW = X.matmul(W)
    probs = y_predW.softmax()
    loss = probs.cross_entropy(Y)
    return loss

batch_size = 32
steps = 20000

X = Value(train_images); Y = Value(y_train) 
# new initialized weights for gradient descent
Wb = Value(np.random.randn(784, 10))
for step in range(steps):
    ri = np.random.permutation(train_images.shape[0])[:batch_size]
    Xb, yb = Value(train_images[ri]), Value(y_train[ri]) 
    lossb = forward(Xb, yb, Wb)
    lossb.backward()
    if step % 1000 == 0 or step == steps-1:
        loss = forward(X, Y, Wb).data/X.data.shape[0]
        print(f'loss in step {step} is {loss}')
    Wb.data = Wb.data - 0.01*Wb.grad 
    Wb.grad = 0
    
from sklearn.metrics import accuracy_score
print(f'accuracy on test data is {accuracy_score(np.argmax(np.matmul(test_images,Wb.data),axis = 1),y_test)*100} %')