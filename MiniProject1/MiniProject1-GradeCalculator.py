# <<< Final >>>

# Const Variables
homework_max = 800.0
quizzes_max = 400.0
midterm_max = 150.0
final_max = 200.0

student_status = input('Student Status: ')
if student_status == 'UG' or student_status == 'G' or student_status == 'DL':
    # Inputs
    homework_points = float(input('Points earned on Homework: '))
    quiz_points = float(input('Points earned on Quizzes: '))
    midterm_points = float(input('Points earned on Midterm: '))
    final_points = float(input('Points earned on Final: '))

    # Calculations
    homework_final = (homework_points / homework_max) * 100 if (homework_points / homework_max) * 100 <= 100 else 100
    quiz_final = (quiz_points / quizzes_max) * 100 if (quiz_points / quizzes_max) * 100 <= 100 else 100
    midterm_final = (midterm_points / midterm_max) * 100 if (midterm_points / midterm_max) * 100 <= 100 else 100
    final_final = (final_points / final_max) * 100 if (final_points / final_max) * 100 <= 100 else 100

    if student_status == 'UG':
        average = (homework_final * 4 + quiz_final * 4 + midterm_final * 6 + final_final * 6) / 20
    elif student_status == 'G':
        average = (homework_final * 3 + quiz_final + midterm_final * 7 + final_final * 9) / 20
    else:
        average = (homework_final + quiz_final + midterm_final * 8 + final_final * 10) / 20

    if average >= 90.0:
        letter_grade = 'A'
    elif average >= 80.0:
        letter_grade = 'B'
    elif average >= 70.0:
        letter_grade = 'C'
    elif average >= 60.0:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    print(f'Homework: {homework_final:2.1f}%\nQuizzes: {quiz_final:2.1f}%\nMidterm: {midterm_final:2.1f}%\nFinal: {final_final:2.1f}%\n{student_status} average: {average:2.1f}%\nCourse Grade: {letter_grade}')

else:
    print('Error: student status must be UG, G or DL')

# <<< Step 1 >>>

'''
# Const Variables
homework_max = 800.0
quizzes_max = 400.0
midterm_max = 150.0
final_max = 200.0

student_status = input('Student Status: ')
if student_status == 'UG' or student_status == 'G' or student_status == 'DL':
    # Inputs
    homework_points = float(input('Points earned on Homework: '))
    quiz_points = float(input('Points earned on Quizzes: '))
    midterm_points = float(input('Points earned on Midterm: '))
    final_points = float(input('Points earned on Final: '))

    # Calculations
    homework_final = (homework_points / homework_max) * 100
    quiz_final = (quiz_points / quizzes_max) * 100
    midterm_final = (midterm_points / midterm_max) * 100
    final_final = (final_points / final_max) * 100

    print(f'Homework: {homework_final:2.1f}%\nQuizzes: {quiz_final:2.1f}%\nMidterm: {midterm_final:2.1f}%\nFinal: {final_final:2.1f}%')

else:
    print('Error: student status must be UG, G or DL')
'''

# <<< Step 2 >>>

'''
# Const Variables
homework_max = 800.0
quizzes_max = 400.0
midterm_max = 150.0
final_max = 200.0

student_status = input('Student Status: ')
if student_status == 'UG' or student_status == 'G' or student_status == 'DL':
    # Inputs
    homework_points = float(input('Points earned on Homework: '))
    quiz_points = float(input('Points earned on Quizzes: '))
    midterm_points = float(input('Points earned on Midterm: '))
    final_points = float(input('Points earned on Final: '))

    # Calculations
    homework_final = (homework_points / homework_max) * 100 if (homework_points / homework_max) * 100 <= 100 else 100
    quiz_final = (quiz_points / quizzes_max) * 100 if (quiz_points / quizzes_max) * 100 <= 100 else 100
    midterm_final = (midterm_points / midterm_max) * 100 if (midterm_points / midterm_max) * 100 <= 100 else 100
    final_final = (final_points / final_max) * 100 if (final_points / final_max) * 100 <= 100 else 100

    print(f'Homework: {homework_final:2.1f}%\nQuizzes: {quiz_final:2.1f}%\nMidterm: {midterm_final:2.1f}%\nFinal: {final_final:2.1f}%')

else:
    print('Error: student status must be UG, G or DL')
'''

# <<< Step 3 >>>

'''
# Const Variables
homework_max = 800.0
quizzes_max = 400.0
midterm_max = 150.0
final_max = 200.0

student_status = input('Student Status: ')
if student_status == 'UG' or student_status == 'G' or student_status == 'DL':
    # Inputs
    homework_points = float(input('Points earned on Homework: '))
    quiz_points = float(input('Points earned on Quizzes: '))
    midterm_points = float(input('Points earned on Midterm: '))
    final_points = float(input('Points earned on Final: '))

    # Calculations
    homework_final = (homework_points / homework_max) * 100 if (homework_points / homework_max) * 100 <= 100 else 100
    quiz_final = (quiz_points / quizzes_max) * 100 if (quiz_points / quizzes_max) * 100 <= 100 else 100
    midterm_final = (midterm_points / midterm_max) * 100 if (midterm_points / midterm_max) * 100 <= 100 else 100
    final_final = (final_points / final_max) * 100 if (final_points / final_max) * 100 <= 100 else 100

    if student_status == 'UG':
        average = (homework_final * 4 + quiz_final * 4 + midterm_final * 6 + final_final * 6) / 20
    elif student_status == 'G':
        average = (homework_final * 3 + quiz_final + midterm_final * 7 + final_final * 9) / 20
    else:
        average = (homework_final + quiz_final + midterm_final * 8 + final_final * 10) / 20

    print(f'Homework: {homework_final:2.1f}%\nQuizzes: {quiz_final:2.1f}%\nMidterm: {midterm_final:2.1f}%\nFinal: {final_final:2.1f}%\n{student_status} average: {average:2.1f}%')

else:
    print('Error: student status must be UG, G or DL')
'''