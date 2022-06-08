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

df['Movement'] = df.Input.str[1:]
df['Direction'] = df.Input.str[0]
# print(df['Input'].str[0])

# print(data)
print(df.head())

