"""STUDENT GRADE MANAGEMENT SYSTEM

Create a system that manages student grades, calculates averages,
and determines the highest and lowest grades.

Input student names and their corresponding grades.
Calculate the average grade.
Find and display the highest and lowest grades.
Display the grades of all students"""

Students={}

while True:
    Name=input('Enter your name:')
    if Name=='Done':
        break
    Grade=float(input('Enter your grades:'))
    Students[Name]=Grade

if Students:
    Average=sum(Students.values())/len(Students.values())
    Highest_score=max(Students.values())
    Lowest_score=min(Students.values())
    
    print(f'Average={Average}')
    print(f'Highest={Highest_score}')
    print(f'Lowest={Lowest_score}')
    
    for name,grade in Students.items():
        print(f'{Name};{Grade}')
        
else:
    print('No students data found.')