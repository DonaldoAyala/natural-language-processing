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
        selfsearchQuery(queryWords)
    
    def searchQuery(self, query):
        noDocs = len(self.fileNames)
        tfidfPerDoc = dict()
        for word in query:
            for doc in self.fileNames:
                matchDocs = self.termDocumentMatrix.getDocumentAppereances(word)
                wordAppearsInDoc = len(matchDocs)
                wordOccurrences = 0
                if (word, doc) in self.termDocumentMatrix.termDocumentMatrix:
                    wordOccurrences = self.termDocumentMatrix.termDocumentMatrix[(word, doc)]
                tf = log(1 + wordOccurrences)
                idf = 0
                if wordAppearsInDoc > 0:
                    idf = log(noDocs / wordAppearsInDoc)

                tfidf = tf*idf

                if doc in tfidfPerDoc:
                    tfidfPerDoc[doc] += tfidf
                else:
                    tfidfPerDoc[doc] = 0
        
        print("---RESULTS---")
        for doc in tfidfPerDoc:
            print(f"{doc}\tTFIDF: {tfidfPerDoc[doc]}")

                


searchEngine = SearchEngine()
searchEngine.initialize([
    'infrared-space-observatory-abstract.txt',
    'james-webb-telescope-description-abstract.txt',
    'james-webb-telescope-discoveries-abstract.txt',
    'videogame-text.txt'])
searchEngine.termDocumentMatrix.printMatrix()
searchEngine.searchQuery(['astronomical', 'telescope', 'astronomy'])