# 3-CountVowels

# A program that counts the number of vowels in a string, book etc. Breaks down every letter, number and common symbols
# and dumps out a count for each.

# Written by Tyler Christenson, this script was tested with the longest sentence ever written, found here http://www.theblogmocracy.com/2010/04/15/the-longest-sentence-ever-written/ 
# The entire sentence cannot be read into the program (thanks python) but works flawlessly on what does get imported.

# You can edit what it looks for by editing the letters variable. 

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','.',',','!','?','"',"'",'-','_','&',';',':','*','(',')']
counts = [];

def countThatShiz(r):
    for a in letters:
        counted = 0
        counted = r.count(a)
        counts.append(counted)


print "Get stats about any word, sentence, paragraph, page, or book"
inputString = str(raw_input("input: ")) #The input string
inputString = inputString.lower() #Makes sure capitol letters get counted, remove this if you add capitols above

countThatShiz(inputString)

loops = 0;

for r in counts:
    if r != 0:
        print letters[loops] + " - " + str(r)
    loops += 1
    
print "Anything with a value of 0, has been omitted"