from titanic.models import model1
import os
training_filename = "train.csv"
results_filename = "results.csv"
# filename=os.path.abspath(filename)
results = model1.run_model(training_filename, results_filename)

# maybe something like this?
# myModel = model1.MyModel()
# myModel.train(training_filename)
# myModel.classify(unlabeled_filename)

# though at what point are you just re-hashing functionlity provided by these model libraries?
# what is the benefit of your own class?
#  repeatable functionality common to the kaggle challenge
#  class can hold a stateful member like onehotencoder or standardscaler whose info needs to persist on subsequent calls?
#    would this maybe be better for a "transformer" class rather than a model class?