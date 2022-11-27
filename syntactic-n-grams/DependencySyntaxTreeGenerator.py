import stanza
from FileManager import *
from TextProcessor import *

class DependencySyntaxTreeGenerator:
    def __init__(self):
        self.fileManager = FileManager()
        self.textProcessor = TextProcessor()

    def generateTree(self, inputFile):
        text = self.fileManager.getFileText(inputFile)
        text = self.textProcessor.removePunctuationMarks(text)
        nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
        doc = nlp(text)

        for sentence in doc.sentences:
            for word in sentence.words:
                print(f'{word.deprel}({sentence.words[word.head-1].text if word.head > 0 else "root"}-{word.head}, {word.text}-{word.id})')


treeGenerator = DependencySyntaxTreeGenerator()
treeGenerator.generateTree('input.txt')