def my_function(number1,number2):
    plus = number1 + number2
    divide = number1 / number2
    minus = number1 - number2
    return plus,divide,minus
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
results = my_function(number1,number2)
print(results)