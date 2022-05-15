a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
n = a^b
count = 0
while n: 
    count += n & 1
    n >>= 1

print(count)
