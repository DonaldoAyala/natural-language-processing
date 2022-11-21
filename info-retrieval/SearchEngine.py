from TermDocumentMatrix import *
from math import log

class SearchEngine:
    def __init__(self):
        self.termDocumentMatrix = TermDocumentMatrix()
        self.fileNames = list()

    def initialize(self, fileNames):
        self.termDocumentMatrix.initialize(fileNames)
        self.fileNames = fileNames

    def search(self, string):
        queryWords = string.split(' ')
        self.searchQuery(queryWords)
    
    def searchQuery(self, query):
        noDocs = len(self.fileNames)
        tfidfPerDoc = dict()
        for word in query:
            matchDocs = self.termDocumentMatrix.getDocumentAppereances(word)
            wordAppearsInDoc = len(matchDocs)
            #print(word, " appears in ", wordAppearsInDoc, " document")
            for doc in self.fileNames:
                wordOccurrences = 0
                if (word, doc) in self.termDocumentMatrix.termDocumentMatrix:
                    wordOccurrences = self.termDocumentMatrix.termDocumentMatrix[(word, doc)]
                #print(word, " appears", wordOccurrences, " times in ", doc)
                tf = log(1 + wordOccurrences)
                idf = 0
                if wordAppearsInDoc > 0:
                    idf = log(noDocs / wordAppearsInDoc)
                #print(f"tf: {tf} idf: {idf} tf*idf: {tf*idf}")
                tfidf = tf*idf

                if doc in tfidfPerDoc:
                    tfidfPerDoc[doc] += tfidf
                else:
                    tfidfPerDoc[doc] = tfidf


        print("---RESULTS---")
        print("query: ", query)
        for doc in tfidfPerDoc:
            print(f"{doc}\tTFIDF: {tfidfPerDoc[doc]}")