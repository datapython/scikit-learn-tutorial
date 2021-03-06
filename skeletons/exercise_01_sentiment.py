"""Build a sentiment analysis / polarity model"""
# Author: Olivier Grisel <olivier.grisel@ensta.org>
# License: Simplified BSD

import sys
from scikits.learn.feature_extraction.text import CountVectorizer
from scikits.learn.feature_extraction.text import TfidfTransformer
from scikits.learn.svm.sparse import LinearSVC
from scikits.learn.pipeline import Pipeline
from scikits.learn.grid_search import GridSearchCV
from scikits.learn.datasets import load_files
from scikits.learn import metrics

#
# The real code starts here
#


# the training data folder must be passed as first argument
movie_reviews_data_folder = sys.argv[1]
dataset = load_files(movie_reviews_data_folder)

# split the dataset in training and test set:
n_samples_total = dataset.filenames.shape[0]

split = (n_samples_total * 3) / 4

docs_train = [open(f).read() for f in dataset.filenames[:split]]
docs_test = [open(f).read() for f in dataset.filenames[split:]]

y_train = dataset.target[:split]
y_test = dataset.target[split:]

# Build a vectorizer / classifier pipeline using the previous analyzer

# TODO

# Build a grid search to find out whether unigrams or bigrams are more
# useful

parameters = {
    'vect__analyzer__max_n': (1, 2),
}

# TODO

## Predict the outcome on the testing set
#y_predicted = clf.predict(docs_test)
#
## Print the classification report
#print metrics.classification_report(y_test, y_predicted,
#                                    class_names=dataset.target_names)
#
## Plot the confusion matrix
#cm = metrics.confusion_matrix(y_test, y_predicted)
#print cm
#
## import pylab as pl
##pl.matshow(cm)
##pl.show()

