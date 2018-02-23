
def  average_score(sum, lot):
	return(sum/lot)


list_assessments = [{'school_class': '4a', 'scores':[3, 4, 4, 5, 2] },
					{'school_class': '4b', 'scores':[4, 2, 4, 3, 5] },
					{'school_class': '5a', 'scores':[2, 3, 3, 5, 4] },
					{'school_class': '5b', 'scores':[3, 5, 5, 4, 4] },
					{'school_class': '6a', 'scores':[2, 3, 5, 4, 5] }]
sum_in_school = 0
for element in list_assessments:
	average_score_class = average_score(sum(element['scores']), len(element['scores']))
	print('Средний балл по классу {}: {}'.format(element['school_class'],average_score_class))
	sum_in_school += average_score_class
	
average_score_school = average_score(sum_in_school, len(list_assessments))
print ('Средний балл по школе: {}'.format(average_score_school))
	


