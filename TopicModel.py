# -*- coding: utf-8 -*-

import json
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer

class TopicModel:

    def __init__(self):
        self.train = fetch_20newsgroups(subset='train',shuffle=True, random_state=42)
            
    def model(self, docs_new):
        # categories text and return an array of categories
        count_vect = CountVectorizer()
        X_train_counts = count_vect.fit_transform(self.train.data)
        X_train_counts.shape
        
        
        
        #tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
        #X_train_tf = tf_transformer.transform(X_train_counts)
     
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        
        clf = MultinomialNB().fit(X_train_tfidf, self.train.target)
        
        #docs_new = ['God is love']
        X_new_counts = count_vect.transform(docs_new)
        X_new_tfidf = tfidf_transformer.transform(X_new_counts)
        
        predicted = clf.predict(X_new_tfidf)
        
        for doc, category in zip(docs_new, predicted):
            return self.train.target_names[category]
            #print('%r => %s' % (doc, self.train.target_names[category]))        
        
        return False;
        #return ["cat1","cat2"];
ob = TopicModel();
print ob.model(["God is love"]);