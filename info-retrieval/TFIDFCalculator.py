from FileManager import *
from TextProcessor import *
from TermDocumentMatrix import *

class TFIDFCalculator:
    def __init__(self):
        self.fileManager = FileManager()
        self.textProcessor = TextProcessor()
    
    def getTFIDF(self, word, termDocMatrix):
        
    