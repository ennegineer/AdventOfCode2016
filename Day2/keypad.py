# KEYPAD
# 1 2 3
# 4 5 6
# 7 8 9

import csv

data = []
with open('./directions.txt', 'r') as file:
    csvreader = csv.reader(file, delimiter = '\n')

    for row in csvreader:
        data.append(row[0])

def PartOne():
    # set combination
    combo = ''

    for row in data:
        # set starting position
        position = 5
        for item in row:
            # if 5, down = 8, up = 2, left = 4, right = 6
            if position == 5:
                if item == 'U':
                    position = 2
                elif item == 'L':
                    position = 4
                elif item == 'R':
                    position = 6
                elif item == 'D':
                    position = 8
            # if 1, down = 4, right = 2
            elif position == 1:
                if item == 'R':
                    position = 2
                elif item == 'D':
                    position = 4
                else:
                    pass
            # if 2, down = 5, left = 1, right = 3
            elif position == 2:
                if item == 'L':
                    position = 1
                elif item == 'R':
                    position = 3
                elif item == 'D':
                    position = 5
                else:
                    pass
            # if 3, down = 6, left = 2
            elif position == 3:
                if item == 'L':
                    position = 2
                elif item == 'D':
                    position = 6
                else:
                    pass
            # if 4, down = 7, up = 1, right = 5
            elif position == 4:
                if item == 'U':
                    position = 1
                elif item == 'R':
                    position = 5
                elif item == 'D':
                    position = 7
                else:
                    pass
            # if 6, down = 9, up = 3, left = 5
            elif position == 6:
                if item == 'U':
                    position = 3
                elif item == 'L':
                    position = 5
                elif item == 'D':
                    position = 9
                else:
                    pass
            # if 7, up = 4, right = 8
            elif position == 7:
                if item == 'U':
                    position = 4
                elif item == 'R':
                    position = 8
                else:
                    pass
            # if 8, up = 5, left = 7, right = 9
            elif position == 8:
                if item == 'U':
                    position = 5
                elif item == 'L':
                    position = 7
                elif item == 'R':
                    position = 9
                else:
                    pass
            # if 9, up = 6, left = 8
            elif position == 9:
                if item == 'U':
                    position = 6
                elif item == 'L':
                    position = 8
                else:
                    pass
        combo = combo + str(position)

    print(combo)

def PartTwo():
    # set combination
    combo = ''

    for row in data:
        # set starting position
        position = 5
        for item in row:
            # if 5, down = 8, up = 2, left = 4, right = 6
            if position == 5:
                if item == 'R':
                    position = 6
                else:
                    pass
            # if 1, down = 4, right = 2
            elif position == 1:
                if item == 'D':
                    position = 3
                else:
                    pass
            # if 2, down = 5, left = 1, right = 3
            elif position == 2:
                if item == 'R':
                    position = 3
                elif item == 'D':
                    position = 6
                else:
                    pass
            # if 3, down = 6, left = 2
            elif position == 3:
                if item == 'L':
                    position = 2
                elif item == 'D':
                    position = 7
                elif item == 'U':
                    position = 1
                elif item == 'R':
                    position = 4   
            # if 4, down = 7, up = 1, right = 5
            elif position == 4:
                if item == 'L':
                    position = 3
                elif item == 'D':
                    position = 8
                else:
                    pass
            # if 6, down = 9, up = 3, left = 5
            elif position == 6:
                if item == 'U':
                    position = 2
                elif item == 'L':
                    position = 5
                elif item == 'D':
                    position = 'A'
                elif item == 'R':
                    position = 7
            # if 7, up = 4, right = 8
            elif position == 7:
                if item == 'U':
                    position = 3
                elif item == 'R':
                    position = 8
                elif item == 'L':
                    position = 6
                elif item == 'D':
                    position = 'B'
            # if 8, up = 5, left = 7, right = 9
            elif position == 8:
                if item == 'U':
                    position = 4
                elif item == 'L':
                    position = 7
                elif item == 'R':
                    position = 9
                elif item == 'D':
                    position = 'C'
            # if 9, up = 6, left = 8
            elif position == 9:
                if item == 'L':
                    position = 8
                else:
                    pass
            elif position == 'A':
                if item == 'U':
                    position = 6
                elif item == 'R':
                    position = 'B'
                else:
                    pass
            elif position == 'B':
                if item == 'U':
                    position = 7
                elif item == 'D':
                    position = 'D'
                elif item == 'L':
                    position = 'A'
                elif item == 'R':
                    position = 'C'
            elif position == 'C':
                if item == 'U':
                    position = 8
                elif item == 'L':
                    position = 'B'
                else:
                    pass
            elif position == 'D':
                if item == 'U':
                    position = 'B'
                else:
                    pass
        combo = combo + str(position)

    print(combo)

PartTwo()