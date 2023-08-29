import re

#Pig Latin - Pig Latin is a game of alterations played on the English language game. 
#To create the Pig Latin form of an English word the initial consonant sound is 
#transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). 
#Read Wikipedia for more information on rules.

#Written by Tyler Christenson, probably the most annoying program I've ever written
#It does it's job, albeit quickly, and dirtily. 

#Tested using: The quick brown fox jumps over the lazy dog

#Functions
#====================================================================================
def anaize(x): #Anaize refers to ananabay, it is in charge of determining the endstring 
    return {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 4,
        'u': 5,
    }.get(x, 9)
    
def stringSplit(r): #Splits the sentence, and returns a list
    return re.sub("[^\w]", " ",  r).split() #re.sub(pattern, repl, string, count=0, flags=0), Another annoying python "feature"
    
def removePuctuation(a): #Removes puctuation from the original string, I don't care enough to finish it now
    return ""
    
def translate(i): #Does the heavy lifting
    #Follows the rules outlined in https://en.wikipedia.org/wiki/Pig_Latin
    
    wordReturn = "" #Word to return
    firstLetter = i[0] #grabs the first letter
    
    if anaize(firstLetter) > 6: #Detects vowels 
        i = i[1:] #Removes the first letter of the word.
        wordReturn = i + "-" + firstLetter + "ay"
    else:
        wordReturn = i + "-" + "yay" #Remove the "-" from this line and the one above to get rid of the dash
        
    return wordReturn
    

def latinize(l): #Takes in a list of words, and returns a list of words that has been translated, 
    #just wanted to keep the loop isolated for code reusability 
    count = 0

    for s in l:
        l[count] = translate(l[count])
        count += 1 #Forgot this the first time, like a moron
    return l
    
    
def reconstruct(o): #Takes in a list of words put into pig latin, and rebuilds them into a stringSplit
    returnString = ""
    for c in o: #My hatred for python grows with this simplification. It makes it harder to read than c# or c++
        returnString += " " + c
        
    return returnString

def doTheBiz(stringy): #The main part of the program, I like things wrapped in functions
    outstring = ""
    #stringy = removePuctuation(stringy) #Put this in when complete
    listOfWords = stringSplit(stringy)
    listOfWords = latinize(listOfWords)
    outstring = reconstruct(listOfWords)
    return outstring
    
#EndFunctions
#=========================================================================================   
    
print "This will translate any string into PigLatin"
print "Enter a string to convert..."

inputString = str(raw_input("input: ")) #The input string
inputString = inputString.lower()
outputString = doTheBiz(inputString)

print "\n"
print outputString
print "\n"