def main():
    running:bool = True
    num:int = 0

    while (running):
        num = int(input("Enter a number between 10 and 1000 (enter -1 to quit): "))
        if (num < 10 and num > 1000 and num != -1):
            print("Please enter a number between 10 and 1000, or use -1 to quit.\n")
        elif (num == -1):
            running = False
        else: 
            out:int = 0
            print("\nMultiples of 3 or 5 below the input: ")
            for i in [x for x in range(1, num) if (x % 3 == 0 or x % 5 == 0)]:
                print(i)
                out += i
            print(f"------\nSum: {out}\n")
    
    print("Quitting program...")
    quit()

if __name__ == "__main__":
    main()