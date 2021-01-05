import numpy as np

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import glob

from sklearn.model_selection import train_test_split

physical_devices = tf.config.experimental.list_physical_devices('GPU')
print("Num GPUs Available: ", len(physical_devices))

boot_data = glob.glob('imgs/boots/*.*')

data = []
labels = []

for i in boot_data:   
    image=tf.keras.preprocessing.image.load_img(i, color_mode='rgb', 
    target_size= (200,200))
    image=np.array(image)
    data.append(image)
    labels.append(0)

data = np.array(data)
labels = np.array(labels)