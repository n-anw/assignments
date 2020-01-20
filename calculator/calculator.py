# Nick funcitons HW

# define a and b variable for testing

a = 2
b = 3

# define a funtion multiply

def multiply(a, b):
	return a * b

# test function
# print(multiply(a, b))

# define a function add

def add(a, b):
	return a + b

# test function
# print(add(a, b))

# define a fuction subtract

def subtract(a, b):
	return a - b

# test function
# print(subtract(a, b))

# define a function divide

def divide(a, b):
	return a / b

# test function
# print (divide(a, b))

# step 5
print("I'm going use the calculator functions to multiply 5 and 6")
x = multiply(5,6)
print(x)

# bonus

def square(a):
	return a ** 2

def cube(a):
	return a ** 3



def square_n_times(number, n):
	if n > 0:
		output = 0
		while n > 0:
			output += number ** 2
			n -= 1
		return output
	else:
		print("Use a positive int for n!")

# test function
# number = 2
# n = 2
# print(square_n_times(number, n))



