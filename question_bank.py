import random

#level0
q00 = ['Your favorite programming language:', 'python', 'cobra', 'go', 'c++', 'python']
q01 = ['We live on:', 'Mars', 'Sun', 'Earth', 'Jupiter', 'Earth']
q02 = ['The most popular website', 'Google', 'Goggles', 'Googel', 'Gugil', 'Google']

#level1
q10 = ['Level 1 question', 'this', 'that', 'go', 'c++', 'this']
q11 = ['We live here:', 'Ukraine', 'France', 'Japan', 'USA', 'Ukraine']
q12 = ['The most popular website in Ukraine', 'Rozetka', 'OLX', 'Prom', 'Allo', 'OLX']

#level2
q20 = ['Your favorite programming language:', 'python', 'cobra', 'go', 'c++', 'python']
q21 = ['We live on:', 'Mars', 'Sun', 'Earth', 'Jupiter', 'Earth']
q22 = ['The most popular website', 'Google', 'Goggles', 'Googel', 'Gugil', 'Google']

#level3
q30 = ['Your favorite programming language:', 'python', 'cobra', 'go', 'c++', 'python']
q31 = ['We live on:', 'Mars', 'Sun', 'Earth', 'Jupiter', 'Earth']
q32 = ['The most popular website', 'Google', 'Goggles', 'Googel', 'Gugil', 'Google']


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