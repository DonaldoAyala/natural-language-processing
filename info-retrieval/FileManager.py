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

