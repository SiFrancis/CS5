def input_list():
    output = []
    while True:
        inp = input("Enter a value (or put 'fin') to finish input: ")
        if inp == "fin": return output
        output.append(inp)

def q1(l):
    l.pop(0)
    l.pop(1)
    l.pop(3)
    print(l)

def q2(l):
    int_l = [float(x) for x in l]
    print("Maximum: ", max(int_l))
    print("Minimum: ", min(int_l))
    
def main():
    choice = 0
    while True:
        choice = int(input("Choose Problem [1] or [2]: "))
        if choice not in [1, 2]: print("Please choose either 1 or 2.")
        else: break
    inlist = input_list()
    if choice == 1: q1(inlist)
    elif choice == 2: q2(inlist)
    
if __name__ == "__main__": main()