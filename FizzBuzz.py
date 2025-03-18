eded = int(input("eded daxil edin"))

if eded % 3 == 0 and eded % 5 == 0:
    print("FizzBUzz")
elif eded % 3 == 0:
    print("Fizz")
elif eded % 5 == 0:
    print("Buzz")
else:
    print(eded)
