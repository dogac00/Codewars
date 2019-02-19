# This is a simple problem of how to find the middle charachter of a string.

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"

# There is a simple way for both odd length texts and even length texts. It is:

def get_middle(s):
    return s[(len(s)-1)/2:len(s)/2+1]
    
# But my code follows. I think my program is faster because it doesn't have to calculate the length twice.
# and it goes through a simple if else block.

def get_middle(s):
    l = len(s)
    if l%2==0:
        return (s[(l/2)-1:l/2+1])
    else:
        return (s[l//2])
        
        
# And I did some tests and I saw that my execution time is faster than the other one.
# And it is more pythonic.
