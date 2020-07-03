'''values = input("Input some comma seprated numbers : ")
list = values.split(",")
print('List : ',list)
'''

def commaSep (values):
    return values.split(',')
def main():
    values = input("Enter the values of the list:")
    a=commaSep(values)
    print ("Enter the values:{}".format(a))
   
main()
    
