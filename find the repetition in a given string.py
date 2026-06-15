sentence=input("enter a sentence: ")
word=input("enter a word to find its occurance in the given sentence: ")
repetition=sentence.split().count(word)
if repetition>0:
    print(1)
else:
    print(-1)
