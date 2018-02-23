list_names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

### Задание 1 ###
while list_names[0]!= 'Валера':
	print(list_names[0], list_names)
	list_names.pop(0)
print ('Валера нашелся!')


### Задание 2 ###
def find_person(list_names, name):
	while list_names[0] != name:
		list_names.pop(0)
	print("{} нашелся!".format(name))


### Задание 3 ###
def ask_user1():
	while True:
		answer = input ('Как дела? ')
		if answer == 'Хорошо':
			break


### Задание 4 ###
def get_answer(question, answers):
	return answers.get(question)
	

def ask_user2(answers):
	while True:
		question = input ('Скажи что-нибудь: ')
		answer = get_answer(question, answers)	
		print(answer)
		if question == 'Пока':
			break

answers = {'Привет':'И тебе привет', 'как дела?':'Лучше всех', 'Пока':'Увидимся'}

if __name__ == "__main__":
	find_person(list_names, "Саша")
	ask_user1()
	ask_user2(answers)