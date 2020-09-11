sta = ""
def vowelConsonentDisplay():
    vowels=0
    consonents=0
    global sta
   
    for letter in sta:
        if letter.lower() in "aeiou" :
            vowels = vowels+1
        else:
            consonents =  consonents+1
    return (vowels, consonents)

def main():
    global sta
    sta=input("Enter the statement > ") 
    vowels, consonents = vowelConsonentDisplay()
    print("vowels {} consonents {} out of {}".format(vowels, consonents, len(sta)))

main()