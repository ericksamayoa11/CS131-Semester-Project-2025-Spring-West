import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

positive = []
negative = []

with open('positive.txt', 'r') as file:
    for line in file:
        words = word_tokenize(line.lower())
        words = [word for word in words if word.isalnum() and word not in stop_words]
        positive.append(words)

with open('negative.txt', 'r') as file:
    for line in file:
        words = word_tokenize(line.lower())
        words = [word for word in words if word.isalnum() and word not in stop_words]
        negative.append(words)

while True:
    user_input = input("\nEnter word: ")
    # Calculate P("input") 
    count_input_positive = 0
    count_total_positive = 0
    for sentence in positive:
        for word in sentence:
            if word == user_input:
                count_input_positive += 1
                count_total_positive += 1
            else:
                count_total_positive += 1
    count_input_negative = 0
    count_total_negative = 0
    for sentence in negative:
        for word in sentence:
            if word == user_input:
                count_input_negative += 1
                count_total_negative += 1
            else:
                count_total_negative += 1
    p_input = (count_input_positive + count_input_negative) / (count_total_positive + count_total_negative)
    if p_input != 0:
        break
    else:
        print("That word does not appear in the corpus.")

# Calculate P(positive)
p_positive = len(positive) / (len(positive) + len(negative))

# Calculate P("input"|positive)
p_input_given_positive = (count_input_positive) / (count_total_positive)

# Calculate P(positive|"input")
# Bayes Theorem:
# P(A|B) = P(B|A)P(A) / P(B)
p_positive_given_input = p_input_given_positive * p_positive / p_input

print(f"The probability of a review being positive given it contains the word \"{user_input}\" is {p_positive_given_input * 100}%")
