"""def addition(numb):
    total=0
    for i in range (0,numb+1,1):
        total = total+i
    return total
print(addition(100))"""

def addition1(r):
    sum=0
    for i in range(1,r+1,1):
        sum=sum+i
    return sum

def main():
    r=int(input("Enter the number to be added:"))
    tot=addition1(r)
    print(tot)

main()

# Square number calculation


def squareAdd(r):
    sum=0
    for i in range(1,r+1,1):
        sum=sum+(i*i)
    return sum

def main():
    r=int(input("Enter the number to be added:"))
    tot=squareAdd(r)
    print(tot)

main()