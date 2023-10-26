# Course information to be accessed from an array
class Course:
    def __init__(self, course_name, room_number, instructor, meeting_time):
        self.course_name = course_name
        self.room_number = room_number
        self.instructor = instructor
        self.meeting_time = meeting_time
    def print_course_info(self):
        print(f'Class: {self.course_name}\nRoom: {self.room_number}\nInstructor: {self.instructor}\nTime: {self.meeting_time}')

# Creates the dictionary of courses
courses = {'CS101' : Course('CS101', '3004', 'Haynes', '8:00am'), 'CS102' : Course('CS102', '4501', 'Alvarado', '9:00am'), 'CS103' : Course('CS103', '6755', 'Rich', '10:00am'), 'NT110' : Course('NT110', '1244', 'Burke', '11:00am'), 'CM241' : Course('CM241', '1411', 'Lee', '1:00pm')}

# Takes in the input and output course info
courses[input('Enter a class name: ')].print_course_info()