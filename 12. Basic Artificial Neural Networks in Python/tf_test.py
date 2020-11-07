import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

features = tf.keras.Input(shape=(4,))
hidden = tf.keras.layers.Dense(3, activation=t.nn.sigmoid)(features)
labels =tf.keras.layers.Dense(1, activation = tf.nn.sigmoid)(hidden)
model = tf.keras.Model(inputs=inputs, outputs=labels)

mse = tf.keras.losses.MeanSquaredError()

optimizer = tf.keras.optimizers.sgd(learning_rate=le-1)

np.random.seed(0)
x_data, y_data = datasets.make_moons(200, noise=0.10)
plt.figure(figsize=(10,7))
plt.scatter(features[:,0], features[:,1], c=labels, cmap=plt.cm.winter)

model.compile(loss=mse, optimizer=optimizer)

for _ in range(20000):
    for step, (x,y) in enumerate(zip(x_data, y_data)):
        model.train_on_batch(np.array([x]),np.array([y]))

x = tf.convert_to_tensor(np.array(x_data[0]),dtype=tf.float64)
print(model(x).numpy())
