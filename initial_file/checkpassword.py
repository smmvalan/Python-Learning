print('Enter correct username and password combo to continue')
count=1
password='Ryan'
username='zoe'
while(count <=3):
    username=input('Enter the User Name') 
    password=input('Enter the Password')
    if password=='Ryan' and username=='zoe':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
    count= count+1