# To prepare the marksheet for the students and workout the grade
# input
studentName = input("Enter the Student Name : ")
studentClass = input ("Enter the Student Class : ")
marks= []
for subject in range(5) :
    n = int(input("Enter the Subject Marks"+str(subject+1)+ ": "))
    marks.append(n)
Total = sum(marks)
Avg = Total/5
print (" ******************************************\n\t\t Student Marklist\n\n ******************************************\n Name\t\t:{}\n Class\t\t:{}\n Tamil\t\t:{}\n English\t:{}\n Maths\t\t:{}\n Science\t:{}\n History\t:{}\n".format(studentName, studentClass,marks[0],marks[1],marks[2],marks[3],marks[4]))

if(marks[0]>=0 and marks[0]<= 100) and (marks[1]>=0 and marks[1]<= 100) and (marks[2]>=0 and marks[2]<=100) and (marks[3]>=0 and marks[3]<=100) and (marks[4]>=0 and marks[4]<=100) :
  
    if (Avg>=75 and Avg<=100) :
            print("Remark: Grade A - Exceed Expectation")
    elif  (Avg>=60 and Avg<=75) :
            print("Remark: Grade B  - Outstanding")
    elif (Avg>=30 and Avg<=60) :
            print("Remark: Grade C - Need Improvement")
    elif (Avg>0 and Avg<30) :
            print("Remark: Grade D - Failed")        
else :
   print("You have typed wrong marks") 
        
if (marks[0]<30) :
        print("Subject: Tamil Failed")
if (marks[1]<30) :
    print("Subject: English Failed")
if (marks[2]<30) :
    print("Subject: Maths Failed")
if (marks[3]<30) :
    print("Subject: Science Failed")
if (marks[4]<30):
    print("Subject: History Failed")


   