
from time import sleep

words = []

types = ["plural noun", "adjective", "verb ending in 's'", "verb", "verb", "adverb", "noun", "noun", "verb ending in 'ing'", "verb", "verb", "adjective", "adjective", "noun", "noun", "verb"]

print("Welcome to madlibs!")
for i in types:
    word = input("Please enter a " i)
    words.append(word)

print("Generating madlib.  It's a doozy!")

time.sleep(2)



print("Yesterday, all my " + words[1])




"""
   seemed so           [2]          
Now it           [3]           as though they`re here to           [4]          
Oh, I           [5]           in yesterday.

          [6]          , I`m not half the           [7]           I used to be,
There`s a           [8]                     [9]           over me.
Oh, yesterday came           [6]          .

Why she had to           [10]           I don`t know she wouldn`t           [11]          .
I said something           [12]          , now I long for yesterday.

Yesterday, love was such an           [13]                     [14]           to play.
Now I need a           [15]           to           [16]           away.
Oh, I           [5]           in yesterday.
"""