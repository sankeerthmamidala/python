#printing how many numbers are odd in a given range of numbers
x= eval(input('enter the number: '))
for i in range(x):
    if(i%2==0):
        print(i,'the number is even',)
    else:
        print(i,'the number is odd')
