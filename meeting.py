# John has invited people. His list is:

# s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

# Could you make a program that

# makes this string uppercase
# gives it sorted in alphabetical order by last name. When the last names are the same, sort them by first name.
# Last name and first name of a guest come in the result between parentheses separated by a comma. So the result of
# function meeting(s) will be:

# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"

# It can happen that in two distinct families with the same family name two people have the same first name too.
# Notes
# You can see another examples in the "Sample tests".
# Translators are welcome for all languages.

# So the question is pretty clear.

# My solution follows:

def meeting(s):
    
    s = s.upper()    # first I make it all uppercase
    
    fullNames = s.split(";")    # and split it into full names like "Fred:Corwill"
    
    fullNamesDict = {}    # created an empty dictionary where I will fill full names in a bit
    
    for fullName in fullNames:
        firstName, lastName = fullName.split(":")    # split full names into "Fred" and "Corwill"
        if lastName in fullNamesDict.keys():
            fullNamesDict[lastName].append(firstName)    # look if it already exists, if it is append it
        else:
            fullNamesDict[lastName] = [firstName]     # if it does not exists create an array with an element in it
            
    # the reason I created an array for every last name is, there is a couple of people having the same
    # last name, and if you don't make it an array, you can not know in the dictionary which one is which
    # and you assign every first name to the same last name
    
    for lastName in fullNamesDict:
        fullNamesDict[lastName].sort()    # I loop through and sort the people having the same last name
    
    meeting = ""
    
    for lastName in sorted(fullNamesDict.keys()):    # It is important to be sorted because it comes in random
        for firstName in fullNamesDict[lastName]:
            meeting += "({0}, {1})".format(lastName, firstName)    # concatenate every full name into meeting string
    
    return meeting

# I looked up the solutions and found an elegant solution too:

def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))

# Basically it loops through all the full names in upper forms, then for every element in splitted full name which
# is first name and last name it formats the string and joins the sorted ones.
