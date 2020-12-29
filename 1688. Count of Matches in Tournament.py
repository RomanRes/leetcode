def numberOfMatches(n):
    counter = 0
    while n != 1:
        rest = n % 2
        n //= 2
        counter += n
        n += rest
    return  counter

print(numberOfMatches(7))
