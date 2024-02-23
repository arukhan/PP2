import math
n=int(input())
l=int(input())
d=l/2
angle=((n-2)*180)/n
#print(int(angle))
#print((math.tan(math.radians(angle/2))))
A=(math.tan(math.radians(angle/2)))*d
p=l*n
S=(A*p)/2
#print(A)
#print(d)
print(round(S))
