import pickle
import numpy as np

with open('static/model/model_pkl', 'rb') as f:
    lr = pickle.load(f)


def RockVsMine(input_data):
    # changing the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = lr.predict(input_data_reshaped)
    return prediction[0]
