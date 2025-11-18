x = int(input("x = "))
y = int(input("y = "))
i = 1
n = 1
m = 1
while i <= y:
    print("#"*x)
    i+=1
while n <= y:
    print("#"*n)
    n+=1
while m <= y:
    if m==1 or m==y:
        print("#"*x)
    if m>=1 and m<=y-1:
        print("#", " "*(x-4), "#")
    m+=1
