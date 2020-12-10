def get_row_column(row_column_str, min, max, lower_letter):
    for letter in row_column_str:
        diff = max - min + 1
        half = diff / 2
        if letter == lower_letter:
            max -= half
        else:
            min += half
    return int(min)

def get_seat_id(row, column):
    return int(row * 8 + column)

with open("puzzle.txt", "r") as f:
    lines = f.readlines()

max_seat_id = 0
for line in lines:
    seat = line.rstrip()
    row = get_row_column(seat[:7], 0, 127, 'F')
    column = get_row_column(seat[-3:], 0, 7, 'L')
    seat_id = get_seat_id(row, column)
    if seat_id > max_seat_id:
        max_seat_id = seat_id