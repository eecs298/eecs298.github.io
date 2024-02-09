import numpy as np
import csv

np.random.seed(298) # for the autograder

class SemesterGrade:

    def __init__(self, hw1: float, hw2: float, hw3: float, midterm: float, hw4: float, final: float):
        """A class to calculate the student's semester grade based on all assignment grades.

        Attribtutes:
            hw1: Grade on homework 1 out of 100
            hw2: Grade on homework 2 out of 100
            hw3: Grade on homework 3 out of 100
            midterm: Grade on midterm out of 100
            hw4: Grade on homework 4 out of 100
            final: Grade on final out of 100
        """
        self.hw1 = hw1
        self.hw2 = hw2
        self.hw3 = hw3
        self.midterm = midterm
        self.hw4 = hw4
        self.final = final
        self.homework_weight = 0.15 # weight of each homework
        self.midterm_weight = 0.2 # weight of midterm
        self.final_weight = 0.2 # weight of final
    
    def calculate_semester_grade(self):
        """A function to calculate a student's letter grade according to their semester grades.

        Arguments:
            None
        Modifies:
            None
        Returns:
            Grade from A-F according to spec.
        """
        # TODO: Calculate the weighted average of the semester grades




class StudentGrades:

    def __init__(self, grades_file_path: str):
        """A class to hold student grades.

        Attributes:
            grades_file_path: path to csv file with student grade information
        """
        self.student_grades = self._read_student_grades(grades_file_path)
    
    def _read_student_grades(self, grades_file_path: str):
        """Local function to read in student grades from given file path.

        Arguments:
            grades_file_path: File path to grades.csv
        Modifies:
            None
        Returns:
            A dictionary with StudentID as each key and corresponding SemesterGrade object.
        """
        
        student_grades = {}
        # TODO: read in grades.csv and fill student_grades dictionary

        return student_grades

    def query_student_grade_rr(self, student_id: str):
        """Returns the true grade with probability 1/2 and 
        returns a uniformly random output over all possible grades with probability 1/2.

        Arguments:
            student_id: Student ID to query a grade from.
        Modifies:
            None
        Returns:
            Output of the Randomized Response scheme or appropriate Exception as given in the spec
        """
        # TODO 1: Raise appropriate exceptions
        
        # TODO 2: Implement Randomized Response
        pass
        
            

if __name__ == "__main__":
    """
    TODO:
        - Create an instance of StudentGrades populated with grades.csv. 
        - Using a while True loop, read in student IDs from input with the prompt given in the spec.
        - Break the loop if an Exception is raised and print the Exception out.
    """
    pass



            
            


