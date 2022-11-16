#FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
                print(f"{number} is divisable by 3 and 5, ergo \"fizzbuzz\"")
    elif number % 3 == 0:
        print(f"{number} is divisable by 3, ergo \"fizz\".")
    elif number % 5 == 0:
            print(f"{number} is divisable by 5, ergo \"buzz\".")
    else:
        print(number)