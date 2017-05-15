# add local folder to data path
import nltk
import pickle
from sys import argv
from features import gender_features

training_data = argv[1]
model_output = argv[2]

nltk.data.path.append(training_data)

# load the data
from nltk.corpus import names
import random

labeled_names = (
    [(name, 'male') for name in names.words('male.txt')] +\
    [(name, 'female') for name in names.words('female.txt')]
    )
         
full_set = [(gender_features(n), gender) for (n, gender) in labeled_names]
final_classifier = nltk.NaiveBayesClassifier.train(full_set)

with open(model_output, 'wb') as out:
    pickle.dump(final_classifier, out)