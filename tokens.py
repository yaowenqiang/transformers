import nltk
from nltk.corpus import stopwords
#nltk.download('stopwords')

from icecream import ic
stop_words = stopwords.words('english')

tweet = """I’m amazed how often in practice, not only does a @huggingface NLP model solve your problem, but one of their public finetuned checkpoints, is good enough for the job.
Both impressed, and a little disappointed how rarely I get to actually train a model that matters :("""""")"""

