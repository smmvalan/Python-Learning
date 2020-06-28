# To Find out given number is prime or not
# input
employeeName = str(input ("Enter the Employee Name: "))
basicPay = float (input("Enter the Basic Pay: "))
HRA = float ( )
LTA = float (12/100 * basicPay) 
PF = float (5/100 * basicPay)
CrossSalary = float (basicPay + HRA + LTA)
Deduction = float (PF + 200)
NetSalary = float ((CrossSalary - Deduction))

if (basicPay <= 3500) :
     HRA = 5/100 * basicPay 
elif (basicPay <= 10000) :
    HRA = 10/100 * basicPay     
else:
    HRA =  12/100 * basicPay
print ("Employee Name", employeeName)
print ("Basic Pay ", basicPay)
print ("HRA", HRA)
print ("LTA", LTA)
print ("PF", PF)
print ("Cross Salary", CrossSalary)
print ("Deduction", Deduction)
print ("Net Salary", NetSalary)

print ("Employee Name", employeeName, "Basic Pay ", basicPay , "HRA", HRA, "LTA", LTA , "PF", PF ,"Cross Salary", CrossSalary ,"Deduction", Deduction , "Net Salary", NetSalary)