a = 20000
b = "3"
total = []
for i in range(1, a+1):
   if i % 3 ==0:
      total.append(i)
   elif b in str(i):
      total.append(i)

print(sum(total))