from art import logo
from replit import clear

def add(n1,n2):
	return n1 + n2

def subtract(n1,n2):
	return n1 - n2

def multiply(n1,n2):
	return n1 * n2
	
def divide(n1,n2):
	return n1 / n2

def calculator():
	clear()
	print(logo)
	
	operations = {
		"+": add,
		"-": subtract,
		"*": multiply,
		"/": divide,
	}
	
	num1 = float(input("What's the first number?: "))
	
	for key in operations:
		print(key)
	
	calculation = True
	while calculation:
		requested_operation = input("Pick an operation from the symbols above: ")
		num2 = float(input("What's the next number?: "))
	
		answer = operations[requested_operation](num1,num2)
		print(f"{num1} + {num2} = {answer}")
	
		if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == 'y':
			num1 = answer
		else:
			calculation =  False
			calculator()

calculator()