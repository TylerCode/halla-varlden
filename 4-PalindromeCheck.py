print "This will check if its a palindrome"
inputstring = raw_input("Check: ")
inputstring = inputstring.lower()
revstring = (inputstring[::-1])

if revstring == inputstring:
    print "Yes: " + revstring
else:
    print "No: " + revstring