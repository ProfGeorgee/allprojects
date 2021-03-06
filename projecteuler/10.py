lower = 1
upper = 2000000
sum = 0

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           sum += num


print(sum)