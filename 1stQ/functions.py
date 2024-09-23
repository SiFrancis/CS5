from inspect import signature

def odd_even(x): return f"{x} is even" if x % 2 == 0 else f"{x} is odd"

def square(x): return x*x

def sign(x):
    if x > 0: return f"{x} is positive"
    elif x < 1: return f"{x} is negative"
    else: return f"{x} is zero"
    
def fact(x): return 1 if x <= 0 else x * fact(x - 1)

def divis(x, y): return x % y == 0

def greatest(x, y, z): return max([x, y, z])

def process(func):
    args_len = len(signature(func).parameters)
    args_in = []
    for i in range(args_len): x = input(f"Enter argument {i+1}: "); args_in.append(x)
    print(f"The result is: {func(args_in)}")
        

def main():
    func_list = [odd_even, square, sign, fact, divis, greatest]
    print("""
          Choose a function from the list:
          [1] Find if a number is odd or even
          [2] Find the square of a number
          [3] Find if a number is positive, negative, or zero
          [4] Find the factorial of a number
          [5] Check if a number is divisible by another
          [6] Find the greatest of three numbers
          """)
    key_in = int(input("Enter a choice from 1-6: ")) - 1
    process(func_list[key_in])
    
if __name__ == "__main__":
    main()