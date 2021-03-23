import tensorflow as tf
from tensorflow import keras



my_model = keras.models.load_model("my_model_2.h5")

my_model.summary()

# converter = tf.lite.TFLiteConverter.from_keras_model(my_model)
# converter.optimizations = [tf.lite.Optimize.DEFAULT]
# converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
# converter.inference_input_type = tf.uint8  # or tf.int8
# converter.inference_output_type = tf.uint8  # or tf.int8
# converter.allow_custom_ops = False
# converter.experimental_new_converter = True
# tflite_model = converter.convert()

# Save the model.
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)