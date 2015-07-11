#!/usr/bin/python


import sys

def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

def main():
    if len(sys.argv) == 3:
        file_input = open(sys.argv[1],"r")
        file_output = open(sys.argv[2],"w")
    elif len(sys.argv) ==1:
        file_input=open("tweet_input/tweets.txt","r")
        file_output=open("tweet_output/ft2.txt","w")
    else:
        print 'usage: ./median_unique.py fileinput fileoutput'
        sys.exit(1)

    unique_word_count = []

    for tweet in file_input:
        unique_word_count.append(len(set(w.lower() for w in tweet.split())))
        print median(unique_word_count)
        file_output.write( str(median(unique_word_count)) + "\n")

    file_input.close()
    file_output.close()

if __name__ == '__main__':
    main()
