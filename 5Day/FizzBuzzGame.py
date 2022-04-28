
def fizz_buzz(end_number):
    for number in range(1, end_number):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)


end_range = int(input("Enter the last number: \n"))
fizz_buzz(end_range)
