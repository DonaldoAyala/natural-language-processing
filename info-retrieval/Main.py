from SearchEngine import *

searchEngine = SearchEngine()
searchEngine.initialize([
    'infrared-space-observatory-abstract.txt',
    'james-webb-telescope-description-abstract.txt',
    'james-webb-telescope-discoveries-abstract.txt',
    'videogame-text.txt'])
searchEngine.termDocumentMatrix.printMatrix()
searchEngine.searchQuery(['astronomical', 'telescope', 'astronomy'])