def check_perfect(number):
    try:
        number = int(number)
        if number <= 0:
            raise ValueError("Error: number must be greater than zero.")
        if number > 32767:
            raise ValueError("Number must be greater or equal to 32767.")
        divisors = [i for i in range(1, number) if number % i == 0]
        if sum(divisors) == number:
            number = int(number)