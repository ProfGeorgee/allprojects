n = 1
sumdigits = []

num = 0
for i in range(1, 101):
    
    n = n*i
   
    num = n

for numbers in str(num):
    sumdigits.append(int(numbers))


print(sum(sumdigits))
