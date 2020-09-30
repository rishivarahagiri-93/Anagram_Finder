# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:13:09 2020

@author: rishi
"""
# gloabal imports
import sys
import time
import math
import pathlib

def anagram_finder(words_list,word):
    
    #Searching through list of words for anagram match  
    counter = 0 # Counter
    # List to hold all the anagram matches
    anagram_words = [] 
    # Filtering the words that match the length of input word to limit no of searches for performance improvement
    filtered_list = [l for l in words_list if len(l) == len(word)] 
    # Anagram finder Initialization time
    anagram_start_time =  time.time() 
    # Logic to check anagram matches for a word
    for l in filtered_list:
      if(sorted(word) == sorted(l)):
          counter+= 1
          anagram_words.append(l)
    # Anagram finder execution time  
    anagram_end_time = math.ceil((time.time() - anagram_start_time)*1000)

    # Print anagram_finder statistics
    if(counter > 1):
        #Count duplicate words as a single entity
         if(len(anagram_words) > 1 and  anagram_words[0] == word):
            print('\n1'+' Anagram(s) found for '+word+ ' in '+str(anagram_end_time) +'ms')
            print(word)
         else:
             print('\n'+ str(counter) +' Anagrams found for '+word+ ' in '+str(anagram_end_time) +'ms')
             print(','.join(anagram_words))
       
    elif(counter == 1):
        print('No anagrams found for ' +word+ ' in '+str(anagram_end_time) +'ms')
    else:
        print('No anagrams found for ' +word+ ' in '+str(anagram_end_time) +'ms')
# main function
if __name__ == "__main__":
    # check for arguments 
    if(len(sys.argv) == 2 ):
        file_path = sys.argv[1]  
        file_path = pathlib.Path(file_path)
        #Check if the file exists
        if(file_path.exists()):
            #Reading contents of file to list
            initialization_start_time = time.time()  # Initialization time
            file = open(file_path)
            words_list = [(line.strip()).lower() for line in file]
            file.close()
            initialization_end_time = math.ceil((time.time() - initialization_start_time)*1000)
            # Total Initialization time
            print('\nWelcome to the Anagram Finder\n-----------------------------')
            print('Initialized in ' + str(initialization_end_time) +' ms')
            while True:
                word = input()
                if(word.isalpha()):
                    if (word == 'exit'):
                        break
                    anagram_finder(words_list,word)
 
            # Exception handlers
                else:
                    print('Please check the type of the input and re enter the word')  
        else:
            print('Please enter a correct filepath and retry')

    else:
        print('Please pass the filepath for anagram finder application')