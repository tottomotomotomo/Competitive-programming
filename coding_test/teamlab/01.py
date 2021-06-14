a = 1234567890
b = 5000000
total = []

for i in range(1, a+1):
   if a % i == 0:
      if i <= b:
         total.append(i)

print(sum(total))