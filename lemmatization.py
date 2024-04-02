import nltk
from nltk.stem import WordNetLemmatizer
from icecream import ic

nltk.download('wordnet')
words = ['amaze', 'amazed', 'amazing']


lemmatizer = WordNetLemmatizer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
ic(lemmatized_words)
