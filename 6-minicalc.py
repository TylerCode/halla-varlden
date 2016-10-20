# almost couldnt remember how to python
# mostly just a small example
# small example to show the basics to learning programmers

print "This will do very basic math. Input your problem like this <Number> <Operator> <Number>"
inputString = str(raw_input("input: ")) #The input string

# the functions for operations

def add (num1,num2)
	return num1 + num2

def multiply (num1,num2)
	return num1 * num2

def subtract (num1,num2)
	return num1 - num2

def divide (num1,num2)
	return num1 / num2
	
# the other functions

def tryParse (s)
	if(inputString.find("+") -not -1)
		#Do stuff