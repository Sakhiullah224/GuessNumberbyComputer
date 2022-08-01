#get and Make a list of marks
marks = []
for i in range(0, 5):
    m = int(input("Enter your marks of 5 subjects:"))
    marks.append(m)  # adding the element to list
print('You have entered below marks',marks)

#function to find avg marks
def find_average_marks(marks):
    sum_of_marks=sum(marks)
    total_subjects=len(marks)
    average=sum_of_marks/total_subjects
    return average

average_marks=find_average_marks(marks)
print('your average marks are',average_marks)

#Calculate the grades and retuen it
def find_grades(average_marks):
    if average_marks>=80:
        grade='A'
    elif average_marks>=60:
        grade='B'
    else:
        grade='F'
    return grade
grade= find_grades(average_marks)
print('your grade is:',grade)