num = int(input("Enter number to check prime or not: "))

if num > 1: # Negative numbers, 0 and 1 are not primes
    # Iterate from 2 to num-1
    for i in range(2, num):
        # If num is divisible by any number between 2 and num-1, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
