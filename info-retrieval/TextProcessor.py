from FileManager import *

class TextProcessor:
    def __init__(self):
        self.fileName = "punctuation-marks.txt"
        self.fileManager = FileManager()
        self.punctuationMarks = self.fileManager.getFileText(self.fileName).split(' ')
    
    def removePunctuationMarks(self, text):
        answer = text
        for punctuationMark in self.punctuationMarks:
            answer = answer.replace(punctuationMark, '')
        return answer

    def getTermFrequencies(self, fileName):
        fileText = self.fileManager.getFileText(fileName)
        fileText = fileText.lower()
        fileText = self.removePunctuationMarks(fileText)
        words = fileText.split(' ')
        
        frequencies = dict()
        for word in words:
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1
        #print(frequencies)
        return frequencies