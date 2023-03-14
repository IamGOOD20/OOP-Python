# В конце последнего семестра профессор Джоуи Гринхорн внедрил онлайн-табель успеваемости
# для своих студентов, чтобы сэкономить бумагу. Тогда казалось, что все работает нормально,
# но с начала нового семестра он получил несколько электронных писем от студентов,
# жалующихся на ошибочные оценки, отображаемые в их онлайн-табелях успеваемости.
# Можете ли вы помочь ему исправить его реализацию класса «Студент»?
#
# Класс «Студент» должен вести себя следующим образом:
#
# someStudent = Student()
# someOtherStudent = Student()
# someStudent.add_grade(98)
# someOtherStudent.add_grade(77)
# someStudent.grades == [98] # Evaluates to True
# someOtherStudent.grades == [77] # Evaluates to True
# Но прямо сейчас происходит следующее:
#
# someStudent = Student()
# someOtherStudent = Student()
# someStudent.add_grade(98)
# someOtherStudent.add_grade(77)
# someStudent.grades == [98, 77] # Evaluates to True
# someOtherStudent.grades == [98, 77] # Evaluates to True

# class Student:
#
#     def __init__(self, first_name, last_name, grades=[]):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grades = grades
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def get_average(self):
#         return sum(self.grades) / len(self.grades)
#
# # someStudent = Student()
# # someStudent.add_grades(98)
# # print(someStudent.grades == [98])
#
# someStudent = Student('Eugene', 'Rukshenas', [60, 50])
# someOtherStudent = Student('Dana', 'Rukshenas', [30, 70])
# someStudent.add_grade(98)
# someOtherStudent.add_grade(77)
# print(someStudent.grades == [98]) # Evaluates to True
# print(someOtherStudent.grades == [77]) # Evaluates to True
