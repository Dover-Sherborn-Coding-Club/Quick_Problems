import math  # math library
word = input("what is your word?")  # gets word
if len(word) % 2 == 0:  # if even amount of letters:
    print(word[int(len(word) / 2) - 1] + word[int(len(word) / 2)])  # return two middle letters
else:  # if odd amount of letters:
    print(word[math.floor(len(word)/2)])  # return middle letter
    
