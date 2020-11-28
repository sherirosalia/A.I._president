import pandas as pd 
import os 
import re 
import csv 
import random
import string
from collections import defaultdict

# data = pd.read_csv('trump_tweets.csv', index_col=False, header=None)
# data.columns = [ "text",]

# create a "default" dictionary that will acumulate all words that appear after a word, the idea being that we can 
# later run words through it and words that do not have a "post" word will be an empty list and those that do will show a list of words
post_word = defaultdict(list)
beginning_word = []
with open('trump_tweets.csv', 'r') as tweets_file:
    tweets=tweets_file.readlines()
    # print(tweets[0:20])
    for tweet in tweets:
        words=re.findall(r"[\w'#@’]+|[.,!?;]", tweet)
        for i, word in enumerate(words):
            
            if i >0:
                # if this is not the first word of the tweet
                prev_word = words[i -1] 
                post_word[prev_word].append(word)

                # print(i)
                #print(word,words[i + 1])
            else:
                beginning_word.append(word)
    while '.' in beginning_word:
        beginning_word.remove('.')
        
    generated_tweets=[]         
    # print(post_word['.'])

    for x in range(200):
        # first_word=random.choice(list(post_word.keys()))
        # second_word=random.choice(post_word[first_word])
        # print(first_word, second_word)
        current_word = random.choice(beginning_word)
        # current_word = random.choice(list(post_word.keys()))
        range_choice = 100
        generated_tweet = ''
    
        for i in range(range_choice):
            # print(current_word, end=' ')
            if current_word not in string.punctuation:
                generated_tweet += ' '
            generated_tweet += current_word
            if post_word[current_word]==[] or len(generated_tweet)>270:
                break
            else:
                next_word=random.choice(post_word[current_word])
                current_word = next_word
        
        last_period=generated_tweet.rfind('.')
        last_question=generated_tweet.rfind('?')
        last_exclamation=generated_tweet.rfind('!')
        ultimate=max(last_period,last_exclamation,last_question)
        # print(ultimate)
        # print(generated_tweet)
        print(generated_tweet[0:ultimate+1])
        if ultimate == -1:
            generated_tweets.append(generated_tweet.strip())
        else:
            generated_tweets.append(generated_tweet[0:ultimate+1].strip())
df=pd.DataFrame(generated_tweets)
df.to_csv('generated_tweets_.csv', index=False, header=False)