# To prepare the marksheet for the students and workout the grade
# input

def marksheet (studentName, studentClass, sub1, sub2,sub3,sub4,sub5) :
    'enter the studentName and all the subjects'
    total = sub1+sub2+sub3+sub4+sub5
    avg = total/5
    if (sub1>=35 and sub2>=35 and sub3>=35 and sub4>=35 and sub5>=35) :        
        if (avg>=75 and avg<=100) :
            print("Remark: Grade A - Exceed Expectation")
        elif  (avg>=60 and avg<=75) :
            print("Remark: Grade B  - Outstanding")
        elif (avg>=30 and avg<=60) :
            print("Remark: Grade C - Need Improvement")
        elif (avg>0 and avg<30) :
            print("Remark: Grade D - Failed")   
    else :
        print("The subject failed")
    return total, avg
def main () :
    studentName = input("Enter the Student Name : ")
    studentClass = input ("Enter the Student Class : ") 
    sub1=int(input("Enter the sub1 mark: "))
    sub2=int(input("Enter the sub2 mark: "))
    sub3=int(input("Enter the sub3 mark:"))
    sub4=int(input("Enter the sub4 mark:"))
    sub5=int(input("Enter the sub5 mark:"))
    a,b = marksheet(studentName,studentClass,sub1,sub2,sub3,sub4,sub5)
    print("Total {}\n {}".format(a,b))
    return
main ()

