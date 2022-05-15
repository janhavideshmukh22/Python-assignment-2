a = int(input("Side a: "))
b = int(input("Side b: "))
c = int(input("Side c: "))

while a<b+c and b<a+c and c<a+b:
    print("Triangle is valid")
    break

while a>b+c or b>a+c or c>a+b:
    print("Triangle is invalid")
    break
