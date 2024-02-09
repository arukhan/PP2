nums=[]
def has_33(nums):
    for i in range(0, len(nums)-1):
        #print(i)
        if nums[i]==3 and nums[i+1]==3:
            print(True)
            return 0
    print(False)
        
has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3]) 