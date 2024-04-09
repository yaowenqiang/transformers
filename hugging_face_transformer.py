from transformers import BertForSequenceClassification, BertTokenizer
from icecream import ic

# initialize the tokenizer for BERT models
tokenizer = BertTokenizer.from_pretrained('ProsusAI/finbert')
# initialize the model for sequence classification
model = BertForSequenceClassification.from_pretrained('ProsusAI/finbert')

# this is our example text
txt = ("Given the recent downturn in stocks especially in tech which is likely to persist as yields keep going up, "
              "I thought it would be prudent to share the risks of investing in ARK ETFs, written up very nicely by "
              "[The Bear Cave](https://thebearcave.substack.com/p/special-edition-will-ark-invest-blow). The risks comes "
              "primarily from ARK's illiquid and very large holdings in small cap companies. ARK is forced to sell its "
              "holdings whenever its liquid ETF gets hit with outflows as is especially the case in market downturns. "
              "This could force very painful liquidations at unfavorable prices and the ensuing crash goes into a "
              "positive feedback loop leading into a death spiral enticing even more outflows and predatory shorts.")

tokens = tokenizer.encode_plus(txt, max_length=512, truncation=True, padding='max_length', add_special_tokens=True, return_tensors='pt')

ic(tokens)
