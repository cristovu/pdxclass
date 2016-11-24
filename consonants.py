
word = input("please type a word to extract the consonants from it: ").lower()
consonants = list("BCDFGHJKLMNPQRSTVXZWY".lower())

for i in range(0,len(word)):
    if word[i] in consonants:
        print(word[i])
