def job (age):
	if age < 0 or age > 110:
		print("Ошибка в вводимых данных!")
	elif age <= 6:
		print ('Вы ходите в детский сад.')
	elif age >= 7 and age < 18:
	    print ('Вы учитесь в школе.')
	elif age >= 18 and age <= 23:
	    print('Вы учитесь в ВУЗе.')
	elif age > 23:
		print ('Вы работаете или уже на пенсии.')


def comparison(str1, str2):
	if str1 == str2:
		return 1
	elif len(str1) > len(str2):
		return 2
	elif str2 == 'learn':
		return 3


age = input ('Введите Ваш возраст: ')
age = int (age)
job(age)

str1 = input('Введите первую строку: ')
str2 = input ('Введите вторую строку: ')
print (comparison(str1, str2))