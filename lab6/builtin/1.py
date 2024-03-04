def multiply_list(a):
    product = 1
    for i in a:
        product *= i
     
    return product
 
a = [1, 2, 3, 4, 5]
result = multiply_list(a)
print(result)