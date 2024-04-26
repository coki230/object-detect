import tensorflow_datasets as td
import tensorflow as tf


data, info = td.load("tf_flowers", as_supervised=True, with_info=True)
print(data[0:3])

def pre_processs(img, label):
    re_img = tf.image.resize(img, [224, 224])
    f_img = tf.keras.applications.xception.preprocess_input(re_img)
    return f_img, label


model_base = tf.keras.applications.xception.Xception(weights="imagenet", include_top=False)

avg_layer = tf.keras.layers.GlobalAveragePooling2D()(model_base.output)
out_put = tf.keras.layers.Dense(1, activation="sofemax")(avg_layer)

model = tf.keras.Model(inputs=model_base.input, outputs=out_put)

for layer in model_base.layers:
    layer.trainable = False

