import random

#level0
q00 = ['Самая высокая гора в Украине:', 'Говерла', 'Пикуй', 'Ай-Петри', 'Казбек', 'Говерла']
q01 = ['We live on:', 'Mars', 'Sun', 'Earth', 'Jupiter', 'Earth']
q02 = ['Самый популярный кинотеатр', 'Орбита Кино', 'Юпитер', 'Планета Кино', 'Мультикекс', 'Планета Кино']

#level1
q10 = ['Кавун це', 'Ягода', 'Фрукт', 'Овоч', 'Мясо', 'Ягода']
q11 = ['We live here:', 'Ukraine', 'France', 'Japan', 'USA', 'Ukraine']
q12 = ['The most popular website in Ukraine', 'Rozetka', 'OLX', 'Prom', 'Allo', 'OLX']

#level2
q20 = ['Your favorite programming language:', 'python', 'cobra', 'go', 'c++', 'python']
q21 = ['Амундсен підкорив', 'Південний полюс', 'Північний полюс', 'Еверест', 'Маріанську западину', 'Південний полюс']
q22 = ['The most popular website', 'Google', 'Goggles', 'Googel', 'Gugil', 'Google']

#level3
q30 = ['4 питання українською', 'тестінг', 'мастерінг', 'фіча', 'буква ї', 'тестінг']
q31 = ['4 вопрос на русском', 'Киев', 'Львов', 'Харьков', 'Одесса', 'Киев']
q32 = ['4 question in English', 'London', 'Berlin', 'Oslo', 'Warsaw', 'London']


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