def input_students():
    num_pairs = int(input("Enter number of students: "))
    pairs_list = []
    print("Enter each grouping on a new line (student names separated by spaces: )")
    print("Press Enter with no input to exit.")
    while True:
        inp = input()
        if inp == "":
            break
        pairs_list.append(inp.split())
    return pairs_list

def map_collaborations(pairs_list:list):
    collab_dict = dict()
    students_set = set([pair[0] for pair in pairs_list]) | set([pair[1] for pair in pairs_list])
    for student in students_set:
        partners = set()
        for pair in pairs_list:
            if pair[0] is student: partners.add(pair[1])
            if pair[1] is student: partners.add(pair[0])
        collab_dict.update({student : partners})
    
    print(collab_dict)

def find_shared_partners(partners_1:set, partners_2:set):
    return partners_1 & partners_2

def main():
    p = input_students()
    print(p)
    map_collaborations(p)

if __name__ == "__main__": main()