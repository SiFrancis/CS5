def process(num):
    div_sum = 0
    # iterate over every number below the input number
    # include them in the list if they are divisors of the number
    divisors = [x for x in range(1, num) if num % x == 0]
    # sum all the item of the 'divisors' list
    for d in divisors: div_sum += d
    # returns True if the sum of the divisors is equal to the number
    # (i.e. if the number is perfect)
    return div_sum == num

def main():
    # sentinel to check if user quit the program
    running = True
    while running:
        # Input dialogue
        inp = int(input("Enter a positive integer (or -1 to quit): "))
        # quits if -1
        if inp == -1: running = False
        # if the input is engative but not -1, program prompts user to enter a POSITIVE number
        elif inp < 0: print("Please enter a POSITIVE integer.")
        # returns True if the number is perfect; otherwise returns False
        else: print(process(inp))

if __name__ == "__main__":
    main()