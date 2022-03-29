n=100
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print(str(i)+" FizzBuz")
    else:
        if i%3==0:
            print(str(i)+" Fizz")
        if i%5==0:
            print(str(i)+" Buzz")
