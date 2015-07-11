#!/usr/bin/python

import sys
from collections import defaultdict


# example of program that calculates the total number of times each word has been tweeted.

#file_input=open("tweet_input/tweets.txt","r")
#file_output=open("tweet_output/ft1.txt","w")


def main():
    if len(sys.argv) == 3:
        file_input = open(sys.argv[1],"r")
        file_output = open(sys.argv[2],"w")
    elif len(sys.argv) == 1:
        file_input=open("tweet_input/tweets.txt","r")
        file_output=open("tweet_output/ft1.txt","w")
    else:
        print 'usage: ./words_tweeted.py fileinput fileoutput'
        sys.exit(1)


    wordcount={}
    for word in file_input.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1


    for key in sorted(wordcount):
        print "%s \t\t %s" % (key.ljust(20), wordcount[key])
        file_output.write("%s \t\t %s \n" % (key.ljust(20), wordcount[key]))



    file_input.close()
    file_output.close()

if __name__ == '__main__':
    main()
