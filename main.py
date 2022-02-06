from titanic.models import model1
import os
training_filename = "train.csv"
results_filename = "results.csv"
# filename=os.path.abspath(filename)
results = model1.run_model(training_filename, results_filename)