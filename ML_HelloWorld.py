import tensorflow as tf
from tensorflow import keras
import numpy as np

def funcao(x):
    x1 = (5 * x) - 2 # se x = 1, x1 = 3
    return x1

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

#dados
xs = np.array([-2.0, -1.0, 0.0, 1.0, 2.0, 4.0], dtype=float)
ys = np.array([-12.0, -7.0, -2.0, 3.0, 8.0, 18.0], dtype=float)

#treino
model.fit(xs, ys, epochs=500)

print(f"Valor na função: {funcao(72)}") #retorno do valor calculado na função (esperado)

print(f"Valor na RNA: {model.predict([72.0])}") #retorno do valor da RNA (aprendido/predição)
