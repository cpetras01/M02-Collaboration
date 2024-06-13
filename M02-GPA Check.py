# M02 Lab - Case Study: if... else and while
# M02-GPA Check
# Coleman Petas
# SDEV 220
# 12 June 2024

# Write an app that accepts input of a student's last name and GPA
# Take that information and test whether the student made the 
# Dean's List or the Honor Roll

# Allow input until 'ZZZ' is entered for student last name

honorRollFirst = []
honorRollLast = []
deansListFirst = []
deansListLast = []

def main():
    while True:
        studentLast = input('Please enter student last name: ')
        if studentLast == 'ZZZ':
            break
        else:
            studentFirst = input('Please enter student First name: ')
            studentGPA = float(input('Please enter student GPA: '))
            if studentGPA >= 3.5:
                deansListFirst.append(studentFirst)
                deansListLast.append(studentLast)
            elif studentGPA >= 3.25:
                honorRollFirst.append(studentFirst)
                honorRollLast.append(studentLast)
            else:
                pass

def deans_list():
    print('Deans List:')
    deansList = zip(deansListFirst, deansListLast)
    [print(i) for i in deansList]
    print()

def honor_roll():
    print('Honor Roll:')
    honor_Roll = zip(honorRollFirst, honorRollLast)
    [print(i) for i in honor_Roll]

main()
deans_list()
honor_roll()