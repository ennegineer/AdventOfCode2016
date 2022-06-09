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

def PartOne():
    # Starting coords: (0,0)
    x = 0
    y = 0
    # Starting dir: facing North
    dir = 'North'

    for row in df['Input']:
    # If facing North, L move x negative the value; R move x positive the value
        # If L, dir = West; if R, dir = East
        if dir == 'North':
            if row[0] == 'L':
                x = x - int(row[1:])
                dir = 'West'
            if row[0] == 'R':
                x = x + int(row[1:])
                dir = 'East'
    # If facing East, L move y positive the value; R move y negative the value
        # If L, dir = North; if R, dir = South
        if dir == 'East':
            if row[0] == 'L':
                y = y + int(row[1:])
                dir = 'North'
            if row[0] == 'R':
                y = y - int(row[1:])
                dir = 'South'
    # If facing South, L move x positive the value; R move x negative the value
        # If L, dir = East; if R, dir = West
        if dir == 'South':
            if row[0] == 'L':
                x = x + int(row[1:])
                dir = 'East'
            if row[0] == 'R':
                x = x - int(row[1:])
                dir = 'West'
    # If facing West, L move y negative the value; R move y positive the value
        # If L, dir = South; if R, dir = North
        if dir == 'West':
            if row[0] == 'L':
                y = y - int(row[1:])
                dir = 'South'
            if row[0] == 'R':
                y = y + int(row[1:])
                dir = 'North'

    print(f'coordinates: ({x}, {y}) direction: {dir}')
    
    answer = (abs(0 - x)) + (abs(0 - y))
    print(answer)

PartOne()

# Results
# x1 = 0, y1 = 0
# x2 = -491, y1 = -114

# |x1 - x2| + |y1 - y2|
