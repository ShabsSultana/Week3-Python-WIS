#ask for percentage then converts to letter grade

#function that converts mark to grade
def mark_grade():
    #global variable, can use outside function
    global grade
    #compares what the mark is to a boundary
    #either outside or range or assigns a letter grade to grade variable
    if (mark > 100):
        grade = "too high"
    elif (mark >= 90):
        grade = "A*"  
    elif (mark >= 80):
        grade = "A"
    elif (mark >= 70):
        grade = "B"
    elif (mark >= 60):
        grade = "C"
    elif (mark >= 0):
        grade = "F"
    else:
        grade = "too low"  

#welcomes student tp grade calulator
print("Welcome to your grade calculator")  
#asks user to input the percentage they got in a test
mark = int(input("What mark did you get in the test? "))
#calls mark_grade function
mark_grade()

#prints out what grade the student got/error is number is out of range
#correct grammar for Grade
if ((grade == "A*") or (grade =="A")):
    print("Your grade is an " + grade)
elif ((grade == "too high") or (grade == "too low")):
    print("The mark you entered is " + grade)
else:
    print("Your grade is a " + grade)