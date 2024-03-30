import nltk
from nltk.corpus import stopwords
#nltk.download('stopwords')

from icecream import ic
stop_words = stopwords.words('english')

tweet = """I’m amazed how often in practice, not only does a @huggingface NLP model solve your problem, but one of their public finetuned checkpoints, is good enough for the job.
Both impressed, and a little disappointed how rarely I get to actually train a model that matters :("""""")"""

ic(stop_words[0:5])

stop_words = set(stop_words)

tweet = tweet.lower().split()
tweet_no_stopwords = [word for word in tweet if word not in stop_words]
ic(tweet_no_stopwords)

