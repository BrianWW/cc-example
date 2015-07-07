#!/usr/bin/python

def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]

def read_words(words_file):
        return [word for line in open(words_file, 'r') for word in line.split()]


file_input=open("tweet_input/tweets.txt","r")
file_output=open("tweet_output/ft2.txt","w")


unique_word_count = []

for tweet in file_input:
    unique_word_count.append(len(set(w.lower() for w in tweet.split())))
    print median(unique_word_count)
    file_output.write( str(median(unique_word_count)) + "\n")

