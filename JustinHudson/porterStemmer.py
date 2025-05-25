import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt_tab')
nltk.download('stopwords')

with open('corpus.txt','r') as file:
    text = file.read()

stop_words = set(stopwords.words('english'))
words = word_tokenize(text.lower())
words = [word for word in words if word.isalnum() and word not in stop_words]
unique_words = list(set(words))
unique_words.sort()

stemmer = PorterStemmer()

for word in unique_words:
    print("Original word: ", word)
    print("Stemmed Word: ", stemmer.stem(word),"\n")
