'''
vowel=0
consonents=0
for letter in "onion":
    if letter.lower() in"aeiou":
        vowel=vowel+1
    else:
        consonents=consonents+1
        print("Vowels:{}".format(vowel))
        print("Consonents:{}".format(consonents))
 
'''
def vowelConsonentDisplay():
    vowels=0
    consonents=0
   
    for letter in sta:
        if letter.lower() in "aeiou" :
            return vowels+1
        else:
            return consonents+1

def main():
    sta=input("Enter the statement") 
    print(vowels)
    print(consonents)
    vowelConsonentDisplay()

main()

