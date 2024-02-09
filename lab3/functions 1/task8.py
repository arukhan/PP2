nums=[]
def spy_game(nums):
    a=[]
    for i in nums:
        if(i==0):
            a.append(i)
            continue
        elif(i==7):
            a.append(i)
    #print(a)
    for j in range(0, len(a)-2):
        if(a[j]==0 and a[j+1]==0 and a[j+2]==7):
            print(True)
            return 0
    print(False)         
    
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])
