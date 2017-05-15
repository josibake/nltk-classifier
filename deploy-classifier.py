import pickle

from features import gender_features

# model = argv[1]
# ^ seems like you should be able to deploy a model
# using parameters from a run, but that doesn't appear
# to be the case
        
def classify_inputs(*args):
    genders = classifier.classify_many([gender_features(name) for name in args])
    return {name:gender for name, gender in zip(args, genders)}

with open('results/deploy_model.pickle', 'rb') as f:
    classifier = pickle.load(f)
    
# test
# print(classify_inputs("josiah", "sarah"))
