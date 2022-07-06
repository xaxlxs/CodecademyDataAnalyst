
import time

words = []

types = ["plural noun", "adjective", "verb ending in 's'", "verb", "verb", "adverb", "noun", "noun", "verb ending in 'ing'", "verb", "verb", "adjective", "adjective", "noun", "noun", "verb"]

print("Welcome to madlibs!")
for i in types:
    word = input("Please enter a " + i + ": ")
    words.append(word)

print("Generating madlib.  It's a doozy!")

time.sleep(2)

# BREAK THIS LINE DOWN FOR READIBILITY AND MAKE THE FORMATTING NICE

print("Yesterday, all my", words[0], "seemed so", words[1], "Now it", words[2], "as though they`re here to", words[3], "Oh, I", words[4], "in yesterday.", words[5], ", I`m not half the", words[6], "I used to be. There`s a", words[7], words[8], "over me. Oh, yesterday came", words[5], ". Why she had to", words[9], "I don`t know she wouldn`t", words[10], ". I said something", words[11], ", now I long for yesterday. Yesterday, love was such an", words[12], words[13], "to play. Now I need a", words[14], "to", words[15], "away. Oh, I", words[4], "in yesterday.")