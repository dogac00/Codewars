# The problem is:

# This time no story, no theory. The examples below show you how to write function accum:

# Examples:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

# First I solve this problem with a for loop. This is to get the main idea behind the problem and see the tests and outputs
# on the screen. This is my first and more readable solution.

def accum(s):
    st = ""
    for i, letter in enumerate(s):
        st += letter.upper()
        st += letter.lower()*(i)
        st += "-"
    return st[:-1]
    
# The function creates an empty string and for each letter it adds every letter and dash. Returns without the last element.

# Then I tested a few samples on the compiler. I thought I can do this in a one-liner using list comprehension and join method.

# Then I came up with this beautiful one-liner.

def accum(s):
    return "-".join([letter.upper()+letter.lower()*i for i, letter in enumerate(s)])
    
# I checked their execution time with time.time() method in time module. There is no significant time differences
# to execute for both functions.
