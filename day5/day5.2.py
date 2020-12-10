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

seats = [get_seat_id(get_row_column(line.rstrip()[:7], 0, 127, 'F'), get_row_column(line.rstrip()[-3:], 0, 7, 'L')) for line in lines]
seats.sort()

previous_seat = seats[0]
missing_seat = 0
for seat in seats[1:]:
    if seat - previous_seat > 1:
        missing_seat = previous_seat + 1
        break
    else:
        previous_seat = seat
print(missing_seat)