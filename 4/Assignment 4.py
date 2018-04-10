# Brennan Huber
# Assignment 4

def main():
    # do stuff
    
    readFile = open('C:/School/Junior/Spring/SciComp/Assignment/4/Grades.csv', 'r')
    writeFile = open('C:/School/Junior/Spring/SciComp/Assignment/4/Grades.csv', 'w')
    
    wholeFile = readFile.readlines()
    
    for i in wholeFile:
        students = i.split(',')
        


def calcAvg(grades):
        grade = 0.2*grades[1] + 0.2*grades[2]
        
        for i in grades:
            if(i > 2):
                grade += 0.6*i

def calcLetter(grade):
     if(grade > 90):
         return 'A'
     elif(grade > 80):
         return 'B'
     elif(grade > 70):
         return 'C'
     elif(grade > 60):
         return 'D'
     else:
         return 'F'

main()