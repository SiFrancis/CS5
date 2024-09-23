def prime_factors(n):
    factors = []
    divisor = 2
    
    while n >= 2:
        if n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        else:
            divisor += 1
    
    return factors

def main():
    num = int(input("Enter a number: "))
    print(prime_factors(num))

if __name__ == "__main__":
    main()