

def FizzBuzz(start, finish):
    for i in range (start,finish+1):
        if i % 3 == 0:
            result.append ("Fizz")
        elif i % 5 == 0:
            result.append ("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            result.append ("FizzBuzz")
        else:
            result.append (i)
    return result
