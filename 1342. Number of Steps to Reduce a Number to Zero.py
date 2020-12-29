def numberOfSteps (num):
    counter = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -=1
        counter += 1
    return counter

for i in range(10):
    print(numberOfSteps(i), "  i = ", i )


