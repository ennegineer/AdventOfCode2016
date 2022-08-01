# The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

# Starting coords: (0,0)
    # x = 0
    # y = 0
# Starting dir: facing North
    # dir = North
    
# If facing North, L move x negative the value; R move x positive the value
    # If L, dir = West; if R, dir = East
# If facing East, L move y positive the value; R move y negative the value
    # If L, dir = North; if R, dir = South
# If facing South, L move x positive the value; R move x negative the value
    # If L, dir = East; if R, dir = West
# If facing West, L move y negative the value; R move y positive the value
    # If L, dir = South; if R, dir = North

# Let's do the thing!
import csv
import pandas as pd

data = []
with open('./directions.txt', 'r') as file:
    csvreader = csv.reader(file, delimiter=',')

    for row in csvreader:
        data = row

df = pd.DataFrame(data, columns=['Input'])

df['Direction'] = df.Input.str[0]
df['Movement'] = df.Input.str[1:]

# print(df.head())

test = ['R5','L5','R5','R3']
def PartOne():
    # Starting coords: (0,0)
    x = 0
    y = 0
    # Starting dir: facing North
    dir = 'North'
# df['Input']
    for row in df['Input']:
    # If facing North, L move x negative the value; R move x positive the value
        # If L, dir = West; if R, dir = East
        if dir == 'North':
            if row[0] == 'L':
                x = x - int(row[1:])
                dir = 'West'
                # print('North - L')
                # print(x)
                # print(y)
            elif row[0] == 'R':
                x = x + int(row[1:])
                dir = 'East'
                # print('North - R')
                # print(x)
                # print(y)
    # If facing East, L move y positive the value; R move y negative the value
        # If L, dir = North; if R, dir = South
        elif dir == 'East':
            if row[0] == 'L':
                y = y + int(row[1:])
                dir = 'North'
                # print('East - L')
                # print(x)
                # print(y)
            elif row[0] == 'R':
                y = y - int(row[1:])
                dir = 'South'
                # print('East - R')
                # print(x)
                # print(y)
    # If facing South, L move x positive the value; R move x negative the value
        # If L, dir = East; if R, dir = West
        elif dir == 'South':
            if row[0] == 'L':
                x = x + int(row[1:])
                dir = 'East'
                # print('South - L')
                # print(x)
                # print(y)
            elif row[0] == 'R':
                x = x - int(row[1:])
                dir = 'West'
                # print('South - R')
                # print(x)
                # print(y)
    # If facing West, L move y negative the value; R move y positive the value
        # If L, dir = South; if R, dir = North
        elif dir == 'West':
            if row[0] == 'L':
                y = y - int(row[1:])
                dir = 'South'
                # print('West - L')
                # print(x)
                # print(y)
            elif row[0] == 'R':
                y = y + int(row[1:])
                dir = 'North'
                # print('West - R')
                # print(x)
                # print(y)

    print(f'coordinates: ({x}, {y}) direction: {dir}')

    answer = (abs(0 - x)) + (abs(0 - y))
    print(answer)
    print(x+y)


def PartTwo():
    test = ['R8', 'R4', 'R4', 'R8']
    # For each 'if', capture coords in a list. 
    # Then check at each additional row to see if the last coordinates match any others

    # Starting coords: (0,0)
    x = 0
    y = 0
    # Starting dir: facing North
    dir = 'North'

    # Create a coord list
    coords = []

    for row in test:
    # If facing North, L move x negative the value; R move x positive the value
        # If L, dir = West; if R, dir = East
        if dir == 'North':
            if row[0] == 'L':
                x = x - int(row[1:])
                dir = 'West'

            elif row[0] == 'R':
                x = x + int(row[1:])
                dir = 'East'

    # If facing East, L move y positive the value; R move y negative the value
        # If L, dir = North; if R, dir = South
        elif dir == 'East':
            if row[0] == 'L':
                y = y + int(row[1:])
                dir = 'North'

            elif row[0] == 'R':
                y = y - int(row[1:])
                dir = 'South'

    # If facing South, L move x positive the value; R move x negative the value
        # If L, dir = East; if R, dir = West
        elif dir == 'South':
            if row[0] == 'L':
                x = x + int(row[1:])
                dir = 'East'

            elif row[0] == 'R':
                x = x - int(row[1:])
                dir = 'West'

    # If facing West, L move y negative the value; R move y positive the value
        # If L, dir = South; if R, dir = North
        elif dir == 'West':
            if row[0] == 'L':
                y = y - int(row[1:])
                dir = 'South'

            elif row[0] == 'R':
                y = y + int(row[1:])
                dir = 'North'
    # Add coordinates to list
        newcoord = str(x)+"-"+str(y)
        coords.append(newcoord)

    # Check if coords already existed in the list
        if coords.count(newcoord) == 2:
            print(newcoord)
            print(coords)
            print((abs(0 - x)) + (abs(0 - y)))
            break
        else:
            pass

    print(f'coordinates: ({x}, {y}) direction: {dir}')

    answer = (abs(0 - x)) + (abs(0 - y))
    print(answer)
    print(x+y)

# 277 is too high
# it's not 12 or 4 or 2
PartTwo()

def Test():
    # input = ['R8', 'R4', 'R4', 'R8']
    directions = []
    for row in df['Input']:
        # look for first input that exists in the list twice
        # Add coordinates to list
        currentInput = row
        directions.append(currentInput)

    # Check if coords already existed in the list
        if directions.count(currentInput) == 2:
            print(currentInput)
            print(directions)
            # print((abs(0 - x)) + (abs(0 - y)))
            break
        else:
            pass

# Test()