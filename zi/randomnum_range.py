import random
range_val = int(input("Enter the range"))
c = []
for i in range(range_val+1):
    c.append(i)
result = random.choice(c)
print(c)
print(result)