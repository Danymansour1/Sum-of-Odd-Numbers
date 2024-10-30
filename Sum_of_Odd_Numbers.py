
n = int(input("Enter a number "))  

sum = 0 

for j in range(1, n + 1): 

    if j % 2 == 1: 
        sum = sum + j  

print("The sum of all odd numbers is:", sum)
