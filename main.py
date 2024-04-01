# Built-in imports
import math

# Your code below
GRADE = {}
score_ranges = [(70, 'A'), (60, 'B'), (55, 'C'), (50, 'D'), (45, 'E'), (40, 'S')]

for score, grade in score_ranges:
    GRADE[score] = grade

def read_testscores(filename):
    """
    Returns student data in the form of dict with the keys 'class', 
'name', 'overall', 'grade'
    """
    filename = "testscores.csv"
    header = []
    student_data = []
    with open(filename, 'r') as f:
        header = f.readline().strip().split(',')
        for row in f:
            data = row.strip().split(',')
            student_class, student_name, p1, p2, p3, p4 = data
            overall = ((int(p1)/30 * 15) + (int(p2)/40 * 30) + (int(p3)/80 * 35) + (int(p4)/30 * 20))
            overall = int(math.ceil(overall))
            grade = None
            for condition, letter in GRADE.items():
              if overall >= condition:
                  grade = letter
                  break
            if grade is None:
                grade = ''
            student = {
                        'class': student_class,
                        'name': student_name,
                        'overall': overall,
                        'grade': grade
                    }

            student_data.append(student)

        return student_data
def analyze_grades(studentdata):
    """
    Returns the count of each grade for each class

    Example
    analysis = analyze_grades(studentdata)
    analysis['Class1']['A']
    4
    """
    studentdata = read_testscores("testscores.csv")
    class_grades = {}
    for student in studentdata:
        student_class = student['class']
        if student_class not in class_grades:
                class_grades[student_class] = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'S': 0, 'U': 0}

  
    for student in studentdata:
        student_class = student['class']
        grade = student['grade']
        if grade != '':
            class_grades[student_class][grade] += 1

    return class_grades