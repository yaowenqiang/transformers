# pip install flair

import flair

model = flair.models.TextClassifier.load('en-sentiment')

text = 'I like you'

sentence = flair.data.Sentence(text)

print(sentence)

