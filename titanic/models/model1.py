from re import T
from titanic.features.transform import transform_data


# maybe a class here?
# class MyModel(Model):
#   def train(self, data)
#   def classify(self, data)

def run_model(training_filename, results_filename):
    data = open(training_filename,'r').read()
    data = transform_data(data)
    print("running model")
    print(data)
    outfile = open(results_filename, 'w')
    outfile.write(data)
    outfile.close()
    return data