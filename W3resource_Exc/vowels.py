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
sta = ""
def vowelConsonentDisplay(sta):
    vowels=0
    consonents=0
   
    for letter in sta:
        if letter.lower() in "aeiou" :
            vowels = vowels+1
        else:
            consonents =  consonents+1
    return (vowels, consonents)

def main():
    sta=input("Enter the statement > ") 
    # print(vowels)
    # print(consonents)
    vowels, consonents = vowelConsonentDisplay(sta)
    print("vowels {} consonents {} out of {}".format(vowels, consonents, len(sta)))

main()

