#Storing our input into a variable named input_strip
input_strip = input("input a word with 'est' as the suffix (eg. 'smallest', 'biggest'): ")

#Enabling the strip method to remove 'est' from our input. Printing results.
print(input_strip.strip('est'))
