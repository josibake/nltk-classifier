# different features to use with model

def gender_features(word):
    return {'suffix1': word[-1:],
            'suffix2': word[-2:],
            'length' : len(word)
           }