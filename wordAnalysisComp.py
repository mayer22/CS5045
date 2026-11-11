# -*- coding: utf-8 -*-
"""
@author: CS 5045 Fall 2025
"""
# =============================================================================
# Read in words_alpha.txt
# =============================================================================
word_list = []
file = open("words_alpha.txt", "r") #open in read mode

'''
# Read a line and print it
# .strip removes tabs and spaces at the beginning and end of a line
line = file.readline()
print(line.strip)
'''

# Loop through and read each line into a list 
# Use method .strip to get rid of white space at the beginning/end of the line
for line in file:
    word_list.append(line.strip())

# =============================================================================
# Create a list with 26 lists, each for words starting with a letter
# =============================================================================

# Initialize a list
alpha_list = []

# Add 26 empty sublists to our list (one for each starting letter)
for i in range(26):
    alpha_list.append([])
# Every sublist will be for words that start with a different letter
# Each sublist will contain 5 words starting with the same letter of the alphabet

# Iterate over all words in word_list
for word in word_list:
    # What is the first character (first_char)
    first_char = word[0]
    # Extract a list number from from word using first character's ASCII value
    # ord() provides us the ASCII value of the input to the function
    # .upper method turns the character to uppercase
    first_char_num = ord(first_char.upper()) - 65 # 65 is value for capital "A"   
    # If sublist for that char doesn't have 5 words, append this new word        
    if len(alpha_list[first_char_num]) < 5:
        alpha_list[first_char_num].append(word)
        # Optional code to remove one letter words
        '''
        if len(word) > 1:
            alpha_list[first_char_num].append(word)
        elif word.lower() == 'a' or word.lower() == 'i':
            alpha_list[first_char_num].append(word)        
        '''


        
# =============================================================================
# Print out list letter and words in list       
# A: a, aa, aaa, aah, aahed
# B: 1stword, 2ndword, ....
# =============================================================================

# Loop through all the subword lists
for start_letter in alpha_list:
    # Get and print letter for list title
    word_in_list = start_letter[0]
    first_char_in_word = word_in_list[0]
    # first_char = start_letter[0][0]
    print(first_char_in_word.upper() + ": ", end="") # end="" keeps us on the same line
    
    # Print each word in list
    for (idx,item) in enumerate(start_letter): # enumerate returns a tuple with
                                               # the item (word) and the index 
                                               # number of that item
        # Print the first four words with a comma
        if idx < 4:
            print(item + ", ", end="")
        # Print the last word without a comma and go to next line
        else:
            print(item)
    
# =============================================================================
# Count the number of words starting with each letter
# =============================================================================

# Initialize a dictionary to do the counting
first_letter_freq = {}
# Loop through all words in word list
for word in word_list:
    # Get first character of word
    first_char = word.lower()[0]
    # Check to see if letter is already in dictionary
    if first_char in first_letter_freq:
        # If seen already increase count by 1
        first_letter_freq[first_char] += 1
    else:
        # If not seen, set its value in the dictionary to 1
        first_letter_freq[first_char] = 1
   
for key in first_letter_freq.keys():
     print(key, ":", first_letter_freq[key])  
     
# =============================================================================
# Count the occurrence of each character
# =============================================================================

# Initialize a dictionary to do the counting  
total_letter_freq = {}
# Loop through all words in word list
for word in word_list:
    # Loop through all characters in word
    for char in word:
        # Check to see if letter is already in dictionary
        if char in total_letter_freq:
            # If seen already increase count by 1
            total_letter_freq[char] += 1
        else:
            # If not seen, set its value in the dictionary to 1
            total_letter_freq[char] = 1

# Print all character counts    
for key in first_letter_freq.keys():
    print(key, ":", first_letter_freq[key], "\t", total_letter_freq[key]) 
    
# =============================================================================
# Counting characters in all of Moby Dick
# =============================================================================
punctuation = [',', '.', ':', ';', '-', '(', ')', '"', "'"] # characters to not count
book_list = []
count = 1
file = open("mobydick.txt", "r")
for line in file:
    if count >= 312: # Skip the first several lines before book starts
        line = line.strip()
        for item in punctuation:
            line = line.replace(item, "") # Replace punctuation with empty string
        line_word_list = line.split(" ") # Line is a string and we split the string on spaces
        book_list = book_list + line_word_list
    count += 1
    
md_letter_freq = {}
for word in book_list:
    if len(word) > 0: # Skip over empty lines
        first_char = word.lower()[0]
        if first_char in md_letter_freq:
            md_letter_freq[first_char] += 1
        else:
            md_letter_freq[first_char] = 1 
    
md_total_letter_freq = {}    
for word in book_list:
    for char in word:
        if char in md_total_letter_freq:
            md_total_letter_freq[char] += 1
        else:
            md_total_letter_freq[char] = 1

for key in first_letter_freq.keys():
    print(key, ":", md_letter_freq[key], "\t", md_total_letter_freq[key])    