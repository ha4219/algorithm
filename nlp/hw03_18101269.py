#!/usr/bin/python
#-*- coding: utf-8 -*-
"""NLP Homework #3: Twenty Newsgroups Classification

This is a skeleton file for NLP homework.
Please complete your task with respect to the given guideline.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import (datasets, feature_extraction, linear_model, metrics)
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def train(dataset, target):
    '''
    Train my model with the given training dataset

    Parameters
    ----------
    dataset: list or numpy.array
        The given training dataset

    target: list or numpy.array
        The given training target (true labels)

    Returns
    -------
    object or tuple of objects
        My trained model such as a feature extractor and classifier

    Notes
    -----
    * My name: 정동하
    * My student ID: 18101269
    * My accuracy (max. 1): 0.700 (예: 0.999)
    * Brief description
      - tf_idf, model parameter를 변경해서 실험했습니다.
    * Discussion
      - tf_idf, model parameter를 변경해서 실험했습니다.
    * Collaborators: 김연수
    * References
      - [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier)
      - [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer)
    '''

    # PLEASE WRITE YOUR CODE HERE
    # (The following lines are my example, you can remove them.)
    vectorizer = feature_extraction.text.TfidfVectorizer(ngram_range=(1, 2), max_df=300, sublinear_tf=True, smooth_idf=False)
    vector = vectorizer.fit_transform(dataset)
    classifier = linear_model.SGDClassifier(loss='modified_huber', random_state=42)
    classifier.fit(vector, target)
    return (vectorizer, classifier)

def predict(model, dataset):
    '''
    Predict lables of the given test dataset

    Parameters
    ----------
    model: object or tuple of objects
        My trained model such as a feature extractor and classifier

    dataset: list or numpy.array
        The given test dataset

    Returns
    -------
    list or numpy.array
        Predicted labels
    '''

    # PLEASE MODIFY THE FOLLOW IF NECESSARY
    vectorizer, classifier = model
    vector = vectorizer.transform(dataset)
    pred = classifier.predict(vector)
    return pred



if __name__ == '__main__':
    # Load a dataset (Note: For the first time, it spent long time to download the datasets.)
    remove = ('headers', 'footers', 'quotes')
    news20_train = datasets.fetch_20newsgroups(subset='train', remove=remove)
    news20_test  = datasets.fetch_20newsgroups(subset='test',  remove=remove)

    # Train a model and evaluate it
    model = train(news20_train.data, news20_train.target)
    pred = predict(model, news20_test.data)
    accuracy = metrics.balanced_accuracy_score(news20_test.target, pred)

    # Print the results
    print('### My results')
    print(f'* My accuracy: {accuracy:.3}')