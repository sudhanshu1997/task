
n= int(input())
if(n<0):
    print('wrong input')
elif(n == 0):
    print('fact', 1)
else:
    fact=1
    for i in range(1,n+1):
        fact = i*fact
    print('factorial',fact)

