def q1(): print([['F', 'E', 'D', 'C', 'B', 'A'][y] for y in [int(x) for x in input("Enter scores from 0 to 5 (separated by spaces): ").split()]])

def q2(): print(''.join([x.upper()[0] for x in input("Enter the phrase: ").split()]))

def q3(): print(sum(["ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(char.upper()) + 1 for char in input("Enter name: ")]))

q1()
q2()
q3()