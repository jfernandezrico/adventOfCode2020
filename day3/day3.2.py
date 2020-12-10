def is_tree(line, position):
    return (line[position % len(line)] == '#')

def get_number_of_trees(file_name, right, down):
    with open(file_name, "r") as f:
        forest = f.readlines()

    result = 0
    index = 0
    while (len(forest) > down):
        index += 1
        del forest[:down]
        if is_tree(forest[0].rstrip(), index * right):
            result += 1 
    return result

r1_d1 = get_number_of_trees("puzzle.txt", 1, 1)
r3_d1 = get_number_of_trees("puzzle.txt", 3, 1)
r5_d1 = get_number_of_trees("puzzle.txt", 5, 1)
r7_d1 = get_number_of_trees("puzzle.txt", 7, 1)
r1_d2 = get_number_of_trees("puzzle.txt", 1, 2)

print(r1_d1 * r3_d1 * r5_d1 * r7_d1 * r1_d2)