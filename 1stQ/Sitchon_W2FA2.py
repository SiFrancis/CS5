def sum_sqrs(n): # 1^2 + 2^2 + 3^2 + ...
    out:int = 0
    for i in range(1, n+1): 
        out+=(i**2)
    return out

def sqr_of_sum(n): #(1 + 2 + 3 + ...)^2
    sum:int = (n*(n+1))//2
    return sum**2

def main():
    running:bool = True
    num:int = 0
    while (running):
        num = int(input("Enter a number (enter -1 to quit): "))
        if (num < 0 and num != -1):
            print("Please enter a positive number, or use -1 to quit.\n")
        elif (num == -1):
            running = False
        else: 
            print(str(sqr_of_sum(num) - sum_sqrs(num)) + "\n")
    
    print("Quitting program...")
    quit()

if __name__ == "__main__":
    main()