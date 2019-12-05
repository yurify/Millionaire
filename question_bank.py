import random

#level0
q00 = ['Q1The highest mountain in Ukraine', 'Hoverla', 'Pikuy', 'Brebeneskul', 'Kazbek', 'Hoverla']
q01 = ['Q1Your favorite programming language:', 'python', 'cobra', 'go', 'c++', 'python']
q02 = ['Q1Package installer for Python', 'pop', 'bip', 'otp', 'pip', 'pip']

#level1
q10 = ['Q2You have to include it in a function declaration:', 'main', 'def', 'void', 'aud', 'def']
q11 = ['Q2Python was created by:', 'Van der Sar', 'Virgil van Dijk', 'Guido van Rossum', 'Van der Vile', 'Guido van Rossum']
q12 = ['Q2Popular python web framework', 'Django', 'Joomla', 'jQuery', 'Jungle', 'Django']

#level2
q20 = ['Q3Using import statement you connect a python:', 'module', 'kursova', 'sector', 'element', 'module']
q21 = ['Q3With the statement firstObject = MyClass(), you', 'create a class', 'create an object', 'delete an object', 'define a function', 'create an object']
q22 = ['Q3The most popular website', 'Google', 'Goggles', 'Googel', 'Gugil', 'Google']

#level3
q30 = ['Q4 singleton = "hello", ', 'singleton is a string', 'singleton is a tuple', 'singleton is a dict', 'singleton is a list', 'singleton is a tuple']
q31 = ['Q4 which of these constructions is not supported in python', 'switch-case', 'if', 'for', 'while', 'switch-case']
q32 = ['Q4 Which of these statements is not true': 'bool is a subclass of int', 'int is a subclass of bool', 'int is a subclass of bool', 'bool is a sublass of object', 'bool is a subclass of int'']


def get_question(level):
	if level == 0:
		question = random.choice([q00, q01, q02])
	elif level == 1:
		question = random.choice([q10, q11, q12])
	elif level == 2:
		question = random.choice([q20, q21, q22])
	elif level == 3:
		question = random.choice([q30, q31, q32])
	return question
