# To display employee salary
# input

def displaySalary (employeeName, basicPay):
    'display the salary'
    # calculate the Hra
    if (basicPay <= 3500) :
        hra = 5/100 * basicPay 
    elif (basicPay <= 10000) :
        hra = 10/100 * basicPay     
    else:
        hra =  12/100 * basicPay

    lta = 12/100 * basicPay
    pf = 5/100 * basicPay
    crossSalary = (basicPay + hra + lta)
    deduction = (pf + 200)
    netSalary = crossSalary - deduction 
    starrepeat = '*'*100  
    print ("{}\n Employee Salary\n {} \n  Name\t\t:{}\t\tBasic Pay\t:{}\n HRA\t\t: {}\n lta : {} \n pf {} \n {} \n netSalary {}".format(starrepeat,starrepeat,employeeName,basicPay,hra,lta,pf,starrepeat,netSalary))

def main ():
    try:
        employeeName = input ("Enter the Employee Name: ")
        basicPay = float (input("Enter the Basic Pay: "))    
        displaySalary (employeeName, basicPay)
    except:
        print('Error found')


main () 
