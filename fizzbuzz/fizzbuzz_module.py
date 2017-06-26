def fizzbuzz(number):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    return number

def main():
    fizzbuzz(3)

main()

if __name__ == '__main__':
    main()
