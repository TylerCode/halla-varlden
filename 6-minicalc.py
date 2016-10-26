# almost couldnt remember how to python
# mostly just a small example
# small example to show the basics to learning programmers

print "This will do very basic math. Input your problem like this <Number> <Operator> <Number>"
inputString = str(raw_input("input: ")) #The input string

tryparse(inputString)

# horrible program, sorry guys, don't look
# lets just sweep this under the rug


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
	parts = inputString.split(" ")
	if(parts[1].find("+") -not -1)
		add(parts[0],parts[2])
		return
	if(parts[1].find("-") -not -1)
		subtract(parts[0],parts[2])
		return
	if(parts[1].find("*") -not -1 -or parts[1].find("x") -not -1)
		multiply(parts[0],parts[2])
		return
	if(parts[1].find("/") -not -1)
		divide(parts[0],parts[2])
		return