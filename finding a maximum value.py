# finding a maximum value from list
a=[7,3,4,5,5]
num1=0
num2=0
final=0
for i in range(0,len(a)):
    if(i==0):
        final=a[i]
    else:
        num1=a[i]
        num2=a[i-1]
        if(num1>num2 and final<num1):
            final =num1
print(final)
