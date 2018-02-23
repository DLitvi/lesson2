### Задание 4 из Обработка exception-ов

answers = {'Привет':'И тебе привет!', 'как дела':'Лучше всех', 'Пока':'Увидимся'}

def get_answer(question, answers):
	return answers.get(question)
	

def ask_user(answers):
	while True:
		try:
			question = input ('Скажи что-нибудь: ')
			answer = get_answer(question, answers)	
			print(answer)
			if question == 'Пока':
				break
		except KeyboardInterrupt:
			print('\nТы еще вернешься?')
			break


ask_user(answers)