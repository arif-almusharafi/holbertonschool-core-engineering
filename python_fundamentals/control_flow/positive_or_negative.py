number = __import__('random').randint(-10, 10)

if number > 0:
    print("is positive")
elif number < 0:
    print(" is negative")
else:
    print("is zero")
