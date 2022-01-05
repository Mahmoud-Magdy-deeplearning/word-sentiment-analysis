from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
res = {}
txt = "I am mahmoud , I love to be software engineer , I am afraid of snakes, depression joy"
sia = SentimentIntensityAnalyzer()
tokens = nltk.word_tokenize(txt)
for word in tokens:
    res = sia.polarity_scores(word)
    print (res)
    max_key = max(res, key=res.get)
    if max_key == 'neu' or (res['neu']==res['pos'] and res['neu']==res['neg']):
        print('word '+ word +' is NEUTRAL' + '\n')
    elif max_key == 'pos':
        print('word '+ word +' is POSITIVE' + '\n')
    else:
        print('word '+ word +' is NEGATIVE' + '\n')
