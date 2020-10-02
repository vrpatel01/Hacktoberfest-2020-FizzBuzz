
# Vipul Patel Hectoberfest

def fun1(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)

num = 100
# Change num to change range
fun1(num)
