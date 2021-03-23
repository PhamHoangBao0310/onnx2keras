import onnx
from onnx2keras.converter import onnx_to_keras

onnx_model = onnx.load("insightface_model.onnx")

# Call the converter (input - is the main model input name, can be different for your model)
k_model = onnx_to_keras(onnx_model,input_names= ['data'],name_policy="short",input_shapes=[(1, 3, 112, 112)])

k_model.save("my_model.h5")