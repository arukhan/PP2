s=str(input())
def check(s):
    if s==s[::-1]:
        print("palindrome")
    else:
        print("not palindrome")
check(s)