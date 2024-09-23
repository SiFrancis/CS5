def power(exp, base:float = 10):
    return base**exp
print("Items 1-2: ")
print(power(2))
print(power(2, 5))

def summate(*args):
    out = 0
    for arg in args: out += arg
    return out

print("Item 3:")
print(summate(1, 3, 5, 7, 9))

def print_even(*args):
    evens = [x for x in args if x % 2 == 0]
    for n in evens: print(n)

print("Item 4:")
print_even(1, 2, 3, 4, 5, 6, 8, 10)

def check_in_range(*args):
    for arg in args[:-1]:
        print(arg in args[-1])
 
print("Item 5:")       
check_in_range(2, 3, 5, 7, range(1, 4))