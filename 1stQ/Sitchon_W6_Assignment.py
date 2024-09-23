def rot13(msg):
    alpha = "abcdefghijklmnopqrstuvwyz"
    print(''.join([alpha[(alpha.find(x.lower()) + 13) % 26] for x in msg if x != " "]))

def main():
    msg = input("Enter a message: ")
    print("Output: ", rot13(msg))

if __name__ == "__main__":
    main()