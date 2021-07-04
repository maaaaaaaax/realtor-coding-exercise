import sys
import time

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        s1_character_counts = {}
        s2_character_counts = {}
        for char in s1:
            if char in s1_character_counts:
                s1_character_counts[char] += 1
            else:
                s1_character_counts[char] = 1
        for char in s2:
            if char in s2_character_counts:
                s2_character_counts[char] += 1
            else:
                s2_character_counts[char] = 1
        for count in s1_character_counts:
            if count not in s2_character_counts:
                return False
            elif s1_character_counts[count] != s2_character_counts[count]:
                return False
        return True

if len(sys.argv) != 2:
    print("Please enter the name of a dictionary. I.e., python anagram.py dictionary.txt")
else:
    filename = sys.argv[1]
    root = input("Enter a word to find its anagrams: ").lower()
    continue_running = True
    while continue_running:
        anagrams_plus_originals = []
        dictionary_read_start_time = time.time()
        file = open(filename, "r")
        dictionary_read_end_time = time.time()
        time_to_load_dictionary = dictionary_read_end_time - dictionary_read_start_time
        anagram_set_request_start_time = time.time()
        for line in file:
            word = line.strip().lower()
            if is_anagram(root, word):
                anagrams_plus_originals.append(word)
        anagrams = ""
        for word in anagrams_plus_originals:
            if word != root:
                anagrams += word
                anagrams += ","
        anagram_set_request_end_time = time.time()      
        time_to_process_anagram =   anagram_set_request_end_time - anagram_set_request_start_time
        if len(anagrams) == 0:
            print("No anagrams found for " + root)
            print("Seconds taken to load dictionary: " + str(time_to_load_dictionary))
            print("Seconds taken to search for anagrams: " + str(time_to_process_anagram))
        else:
            print(anagrams.strip(","))
            print("Seconds taken to load dictionary: " + str(time_to_load_dictionary))
            print("Seconds taken to search for anagrams: " + str(time_to_process_anagram))
        root = input("Enter a word to find its anagrams, or enter \"exit\" to close: ").lower()
        if root == "exit":
            continue_running = False