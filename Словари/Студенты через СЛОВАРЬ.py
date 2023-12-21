student_str = input(
    'Введите информацию о студенте через пробел\n'
    '(имя, фамилия, город, место учёбы, оценки.):'
)

student_info = student_str.split()
student = dict()
print(student_info)
student['Имя'] = student_info[0]
student['Фамилия'] = student_info[1]
student['Город'] = student_info[2]
student['Место учёбы'] = student_info[3]
student['Оценки'] = []
for i_grade in student_info[4:]:
    student['Оценки'].append(int(i_grade))
#           (имя, фамилия, город, место учёбы, оценки.):Михаил Тара Москва МГУ 5 4 5 5 5
#           ['Михаил', 'Тара', 'Москва', 'МГУ', '5', '4', '5', '5', '5']
for i_info in student:
    print(i_info, '-', student[i_info])
#            Имя - Михаил
#            Фамилия - Тара
#            Город - Москва
#            Место учёбы - МГУ
#            Оценки - [5, 4, 5, 5, 5]
