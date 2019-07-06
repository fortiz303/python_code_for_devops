#Have a user input a string
my_string = input('Type some words you want to see reversed: ')

#Split each word from my_string
words_splitted = my_string.split()

#Reverse the words. Words are stored in words_splitted
words_splitted.reverse()

#Join the words and add a period after every string
result = ".".join(words_splitted) + "."

#Print the result
print(result)
