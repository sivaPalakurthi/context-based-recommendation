# -*- coding: utf-8 -*-

import json
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer

class TopicModel:

    def __init__(self):
        self.train = fetch_20newsgroups(subset='train',shuffle=True, random_state=42)
        self.count_vect = CountVectorizer()
        self.X_train_counts = self.count_vect.fit_transform(self.train.data)                
        self.tfidf_transformer = TfidfTransformer()
        self.X_train_tfidf = self.tfidf_transformer.fit_transform(self.X_train_counts)
        
        self.clf = MultinomialNB().fit(self.X_train_tfidf, self.train.target)
        
        #docs_new = ['God is love']
            
    def model(self, docs_new):
        # categories text and return an array of categories
        
        #tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
        #X_train_tf = tf_transformer.transform(X_train_counts)
     
        print "Topic Modellllllllllllllllllllllll"
        print docs_new
        X_new_counts = self.count_vect.transform(docs_new)
        X_new_tfidf = self.tfidf_transformer.transform(X_new_counts)
        
        predicted = self.clf.predict(X_new_tfidf)
        
        for doc, category in zip(docs_new, predicted):
            return [self.train.target_names[category]]
            #print('%r => %s' % (doc, self.train.target_names[category]))        
        
        return False;
        #return ["cat1","cat2"];
ob = TopicModel();
print ob.model(["The goal of this guide is to explore some of the main scikit-learn tools on a single practical task: analysing a collection of text documents (newsgroups posts) on twenty different topics. In this section we will see how to: load the file contents and the categories extract feature vectors suitable for machine learning train a linear model to perform categorization use a grid search strategy to find a good configuration of both the feature extraction components and the classifier"]);