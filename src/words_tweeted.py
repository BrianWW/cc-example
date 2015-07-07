#!/usr/bin/python


from collections import defaultdict


# example of program that calculates the total number of times each word has been tweeted.

#file=open("../tweet_input/tweets.txt","r")
file_input=open("tweet_input/tweets.txt","r")
file_output=open("tweet_output/ft1.txt","w")

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
