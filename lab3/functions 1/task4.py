arr=[90,17,2,3,4,5,6,7,8]
def filter_prime(arr):
    for i in arr:
        prime = 0
        for j in range(1,i):
            if( i%j == 0):
                prime+=1
        if(prime==1):
            print(i)
filter_prime(arr)
