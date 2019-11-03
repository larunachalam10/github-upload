import numpy as np 

array_size=int(input("enter size of array"))
arr1=[]

while array_size > 0:
    n=int(input("enter the elements of array"))
    arr1.append (n)
    array_size -= 1
        


add1=0
count=0
add1= sum(arr1)
print(add1)
