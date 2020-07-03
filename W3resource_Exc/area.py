def areaOfCircle (radius) :
    'enter the circle radius value'
    area= float(3.14*radius**2)
    return area
def main ():
    try:
        radius=float(input("Enter the radius Value:"))  
        rad= areaOfCircle(radius)
        print("Area of the circle is {}".format(rad))
    except: 
        print("Enter the correct number")

main()
