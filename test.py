""" This if file help"""

def marks2Grade(marks):
    """ This is marks2Grade help"""
    asdf = "adf"
    if marks >= 90:
        return "A+"
    elif marks >= 80 and marks < 90:
        return "A"
    elif marks >= 70 and marks < 80:
        return "B"
    elif marks >= 60 and marks < 70:
        return "C"
    elif marks >= 50 and marks < 60:
        return "D"
    return "F"

def calculateGrade(student_marks):
    """ This is calculateGrade help"""
    result = []
    for row in student_marks:
        avg = sum(row)/len(row)
        result.append(marks2Grade(avg))

    return result

if _name_ == "_main_":
    res = calculateGrade([[66, 61, 88, 26, 13], [52, 38, 7, 74, 62]])
    print(res)
