class FileManager:
    def __init__(self):
        pass

    def getFileText(self, filePath, removeLineJump = False):
        text = ""
        with open(filePath, 'r', encoding='UTF-8') as file:
            for line in file:
                if removeLineJump:
                    text += line.rstrip("\n")
                else:
                    text += line
        return text
        
class Constants:
    def __init__(self, stopWordsFilePath, punctuationMarksFilePath) -> None:
        fileManager = FileManager()
        self.stopWords = set(fileManager.getFileText(stopWordsFilePath, removeLineJump = True).lower().split(' '))
        self.punctuationMarks = set(fileManager.getFileText(punctuationMarksFilePath, removeLineJump = True).lower().split(' '))

class TextProcessor:
    def __init__(self, stopWordsFilePath, punctuationMarksFilePath) -> None:
        self.constants = Constants(stopWordsFilePath, punctuationMarksFilePath)

    def toLower(self, text):
        return text.lower()

    def removePunctuationMarks(self, text):
        newText = text

        for punctuationMark in self.constants.punctuationMarks:
            newText = newText.replace(punctuationMark, '')
        
        return newText
    
    def getWords(self, text):
        return text.split(' ')
    
    def removeStopWords(self, words):
        newWords = []

        for word in words:
            if word in self.constants.stopWords:
                continue
            else:
                newWords.append(word)

        return newWords
    
    def getTokens(self, text):
        newText = text
        newText = self.toLower(newText)
        newText = self.removePunctuationMarks(newText)
        words = self.getWords(newText)
        tokens = self.removeStopWords(words)

        return tokens

    def getDigrams(self, text):
        newText = text
        newText = self.toLower(newText)
        newText = self.removePunctuationMarks(newText)
        words = self.getWords(newText)
        tokens = self.removeStopWords(words)

        digrams = []

        for i in range(len(tokens) - 1):
            digrams.append((tokens[i], tokens[i + 1]))

        return digrams

    
class TextComparer:
    def __init__(self, stopWordsFilePath, punctuationMarksFilePath) -> None:
        self.textProcessor = TextProcessor(stopWordsFilePath, punctuationMarksFilePath)
        self.fileManager = FileManager()

    def cos_sim(vector_a, vector_b):
        # Calculating: sum(a_i * b_i) / ( sum(a_i ^2) * sum(b_i ^2) )
        numerator = 0
        for i in range (len(vector_a)):
            numerator += vector_a[i] * vector_b[i]

        square_sum_a = 0
        square_sum_b = 0
        for i in range (len(vector_a)):
            square_sum_a += vector_a[i] ** 2
            square_sum_b += vector_b[i] ** 2

        square_sum_a = square_sum_a ** (1/2)
        square_sum_b = square_sum_b ** (1/2)

        return numerator / (square_sum_a * square_sum_b)

    def compareTexts(self, text1FilePath, text2FilePath):
        text1 = self.fileManager.getFileText(text1FilePath)
        text2 = self.fileManager.getFileText(text2FilePath)

        text1Tokens = self.textProcessor.getTokens(text1)
        text2Tokens = self.textProcessor.getTokens(text2)

        text1TokenSet = set(text1Tokens)
        text2TokenSet = set(text2Tokens)

        text1TokenSet.update(text2TokenSet)
        allTokenSet = text1TokenSet

        dictText1 = {}
        dictText2 = {}

        # Defining dictionaries with same order of tokens
        for token in allTokenSet:
            dictText1[token] = 0
            dictText2[token] = 0
        
        for token in text1Tokens:
            dictText1[token] += 1

        for token in text2Tokens:
            dictText2[token] += 1
        
        vectorText1 = list(dictText1.values())
        vectorText2 = list(dictText2.values())

        return TextComparer.cos_sim(vectorText1, vectorText2)

    def compareTextsUsingDigrams(self, text1FilePath, text2FilePath):
        text1 = self.fileManager.getFileText(text1FilePath)
        text2 = self.fileManager.getFileText(text2FilePath)

        text1Digrams = self.textProcessor.getDigrams(text1)
        text2Digrams = self.textProcessor.getDigrams(text2)

        text1DigramSet = set(text1Digrams)
        text2DigramSet = set(text2Digrams)

        text1DigramSet.update(text2DigramSet)
        allDigramsSet = text1DigramSet

        dictText1 = {}
        dictText2 = {}

        # Defining dictionaries with same order of tokens
        for digram in allDigramsSet:
            dictText1[digram] = 0
            dictText2[digram] = 0
        
        for digram in text1Digrams:
            dictText1[digram] += 1

        for digram in text2Digrams:
            dictText2[digram] += 1
        
        vectorText1 = list(dictText1.values())
        vectorText2 = list(dictText2.values())

        return TextComparer.cos_sim(vectorText1, vectorText2)

def main():
    textComparer = TextComparer('stop-words.txt', 'punctuation-marks.txt')
    fileNames = [
        'infrared-space-observatory-abstract.txt',
        'james-webb-telescope-discoveries-abstract.txt',
        'james-webb-telescope-description-abstract.txt']

    for i in range(len(fileNames)):
        for j in range(i + 1, len(fileNames)):
            print(f"Compared texts: \n-> {fileNames[i]}\n-> {fileNames[j]}")
            similarity = textComparer.compareTextsUsingDigrams(fileNames[i], fileNames[j])
            print(f"Similarity: {similarity}\n")

    for i in range(len(fileNames)):
        for j in range(i + 1, len(fileNames)):
            print(f"Compared texts: \n-> {fileNames[i]}\n-> {fileNames[j]}")
            similarity = textComparer.compareTexts(fileNames[i], fileNames[j])
            print(f"Similarity: {similarity}\n")

if __name__ == "__main__":
    main()





