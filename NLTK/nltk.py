import nltk
from nltk.tokenize import word_tokenize,sent_tokenize,word_tokenize
text = "Hello, world! How are you?"
# Word Tokenization
words = word_tokenize(text)
print(words)

# Sentence Tokenization
sentences = sent_tokenize(text)
print(sentences)

# line tokenization
sentence_data = "The First sentence is about Python. The Second:  about Django. You can learn Python,Django and Data Ananlysishere. "
nltk_tokens = nltk.sent_tokenize(sentence_data)
print (nltk_tokens)

# word Tokenization
word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
print (nltk_tokens)
