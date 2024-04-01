from nltk.stem import PorterStemmer, LancasterStemmer
from icecream import ic

words_to_stem = ['happy', 'happiest', 'happier', 'cactus', 'cactii', 'elephant', 'elephants', 'amazed', 'amazing', 'amazingly', 'cement', 'owed', 'maximum']
porter = PorterStemmer()
lancaster = LancasterStemmer()

stemmed = [(porter.stem(word), lancaster.stem(word)) for word in words_to_stem]

ic("Porter | Lancaster")
for stem in stemmed:
        ic(f"{stem[0]} | {stem[1]}")
