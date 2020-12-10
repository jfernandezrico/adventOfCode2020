
def is_tree(line, position):
    return (line[position % len(line)] == '#')

with open("puzzle.txt", "r") as f:
    forest = f.readlines()
    forest.pop(0)
    result = sum(1 for index, line in enumerate(forest, start=1) if is_tree(line.rstrip(), index * 3))
    print(result)