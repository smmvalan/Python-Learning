def revName(fName,surName):
 'Enter the Firstname and Surname correctly'
 return
def main ():
    try:
        fName=input("Enter the Firstname:")
        surName=input("Enter the Surname:")
        fN=fName
        sN=surName
        revName(fN,sN)
        print("Hello Mr. {} {} Welcome to HSBC" .format(sN,fN))
    except:
        print("Check your Names")

main()