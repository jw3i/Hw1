# Author: Ran Wei rjw5762@psu.edu
# Collaborator:

a = []
cre = []

for i in range(3):

  grade = input(f"Enter your course {i+1} letter grade: ")
  credit = input(f"Enter your course {i+1} credit: ")

  if grade == "A":
    point = 4.0
  elif grade == "A-":
    point = 3.67
  elif grade == "B":
    point = 3.0
  elif grade == "B+":
    point = 3.33
  elif grade == "B-":
    point = 2.67
  elif grade =="C+":
    point = 2.33
  elif grade == "C":
    point = 2.0
  elif grade == "D":
    point = 1.0
  else:
    point = 0.0

  add = float(point)*int(credit)   #CALCULATES NUMERATOR
  a.append(add)             #ADDS PROCESSED NUMBER TO LIST
  cre.append(int(credit))   #ADDS CREDITS TO LIST

  print(f"Grade point for course {i+1} is: {point}")

gpa = sum(a)/sum(cre)
print(f"Your GPA is: {gpa}")