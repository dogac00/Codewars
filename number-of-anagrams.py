# An anagram is a word, a phrase, or a sentence formed from another by rearranging its letters.
# An example of this is "angel", which is an anagram of "glean".

# Write a function that receives an array of words, and returns the total number of distinct pairs of anagramic words inside it.

# Some examples:

# There are 2 anagrams in the array ["dell", "ledl", "abc", "cba"]
# There are 7 anagrams in the array ["dell", "ledl", "abc", "cba", "bca", "bac"]

# Here is my solution

def is_anagram(w1, w2):
    """
    A function checks whether the given two words is an anagram
    """
    if set(w1) == set(w2):    # if their sets are equal, they are anagrams
        return True
    else:
        return False

def anagram_counter(words):
    pair = 0    # count the pairs from 0
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:    # Don't count themselves
                continue
            if is_anagram(words[i], words[j]):
                pair += 1
    return pair/2   # Divide by 2 because there's a duplicate of all anagrams
    
# Another solution which I've found on the Codewars uses Counter

# Here is another solution

from collections import Counter

def anagram_counter(words):
    return sum(n*(n-1)// 2 for n in Counter(''.join(sorted(x)) for x in words).values())
    
    # Counts the sorted words in 'words' array, iterates through values and calculates their combination of 2.
    
