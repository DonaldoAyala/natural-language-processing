from FileManager import *
from TextProcessor import *

class TermDocumentMatrix:
    def __init__(self):
        self.textProcessor = TextProcessor()
        self.fileManager = FileManager()
        self.termDocumentMatrix = dict()
        self.allFilesWords = set()
        self.documents = list()

    def initialize(self, fileNames):
        self.documents = fileNames
        self.documents.sort()
        for docName in fileNames:
            fileFrequencies = self.textProcessor.getTermFrequencies(docName)

            for key in fileFrequencies:
                self.termDocumentMatrix[(key, docName)] = fileFrequencies[key]
                if key not in self.allFilesWords:
                    self.allFilesWords.add(key)
    
    def getDocumentAppereances(self, word):
        appereances = list()
        for doc in self.documents:
            if (word, doc) in self.termDocumentMatrix:
                appereances.append(doc)
        return appereances

    def printMatrix(self):
        count = 1
        for doc in self.documents:
            print(f"{count}: {doc}")
            count += 1
        count = 1
        for doc in self.documents:
            print(count, '\t', end='')
            count += 1
        print()

        allWords = list(self.allFilesWords)
        allWords.sort()
        for word in allWords:
            for doc in self.documents:
                if (word, doc) in self.termDocumentMatrix:
                    print(self.termDocumentMatrix[(word, doc)], '\t', end='')
                else:
                    print(0, '\t', end='')
            print('\t', word)
