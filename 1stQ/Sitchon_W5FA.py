import random

def Week5(*args):
    pass

def main():
    # input loop
    valid = False
    while not valid:
        n1 = int(input("Enter a positive integer: "))
        n2 = int(input("Enter another positive integer larger than this: "))
        if (n1 < n2) and (n1 > 0) and (n2 > 0):
            valid = True
        else: 
            print("NUMBERS INVALID: Please follow instructions.")
    
    rnum = random.randint(n1, n2)
    #r1
        