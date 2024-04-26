
import numpy as np
import tensorflow as tf
print(np.__version__)
print(tf.__version__)

import tensorflow_models as tfm
print("Top-level modules: ", dir(tfm))
print("NLP modules: ", dir(tfm.nlp))
print("Vision modules: ", dir(tfm.vision))