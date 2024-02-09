import random
a=random.randint(1, 20)
#print(a)

print("Hello! What is your name?")
name=str(input())
print("Well,", name, ",I am thinking of a number between 1 and 20.","\n","Take a guess.")
k=1
while(a!=0):
    number=int(input())
    if number==a:
        print("Good job,", name,"!," ,"You guessed my number in" , k,  "guesses!")
        break
    else:
        if number<a:
            print("Your guess is too low.", "\n","Take a guess.")
        else:
            print("Your guess is too large.", "\n","Take a guess.")
        k+=1
