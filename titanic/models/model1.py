from re import T
from titanic.features.transform import transform_data


def run_model():
    data = [1,2,3]
    data = transform_data(data)
    print("running model")
    print(data)
    return data