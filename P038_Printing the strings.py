#Printing the Strings
word = input("Enter the word to print: ")
word_len = len(word)
for i in range (0, word_len-1, 2):
    print(word[i])

