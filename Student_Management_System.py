# Student_Management_System.py
# Author: Punit Sundar
# Last Updated: June 28, 2020
# Purpose: Write an object-oriented program for managing students in a class.
#          This system helps keep track of project team info, assignments,
#          team project report, and exams. Using this system, the instructor
#          can easily update or query information for any student.

## Add:
# 1. Query search
#       - get assignment score for particular student
# 2. CSV file


class StudentManagement(object):

    def __init__(self): 
        """ Initializes a dictionary to keep track of students' grades """
        self.student_dict = {}
    
    def add_student(self,num_students): 
        """ Add students to your student dictionary only after adding assignments. 
        All newly added students will have 0 for all asignment scores."""

        for i in range(num_students):
            student_id = input("Type in student ID for student " + str(i+1) + ": ")
            self.student_dict[student_id] = 0
        print(self.student_dict)
    
    def add_initial_assignments(self, assignment_name): # list of assignment names
        """ Add assignments to student dictionary. All assignments will be set to 0"""

        self.assignment_dict = {}
        for assignment in assignment_name:
            self.assignment_dict[assignment] = 0
        for key in self.student_dict:
            self.student_dict[key] = self.assignment_dict.copy()
        print(self.student_dict)
    
    def add_new_assignment(self, new_assignment): # one new assignment only
        """ Add a new assignment to existing assignments in student dictionary"""

        for key in self.student_dict:
            self.student_dict[key][new_assignment] = 0
        print(self.student_dict)

    def update(self, student_id, assignment_name, value):
        """Updates the assignment score for a given student id"""
        
        updated_dict = {}
        for key in self.student_dict:
            updated_dict[key] = 0
            if key == student_id:
                self.student_dict[student_id][assignment_name] = value
        print(self.student_dict)



new = StudentManagement()
print("ADDED 3 students")
new.add_student(3)
print("\n")
print("ADDED Initial assignments")
new.add_initial_assignments(['Exam 1','Exam 2'])
print("\n")
print("ADDED new Quiz assignment")
new.add_new_assignment('Quiz 1')
print("\n")
print("UPDATED score for student Student_1")
new.update(student_id = 'Student_1',assignment_name = 'Quiz 1',value = 100)
