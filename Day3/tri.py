import csv

data = []
with open('./triangles.txt', 'r') as file:
    csvreader = csv.reader(file, delimiter = '\n')

    for row in csvreader:
        data.append(row[0])

triangles = []

for row in data:
    triangles.append([row[0:5].strip(), row[5:10].strip(), row[10:15].strip()])

# print(triangles)

def PartOne():
    # Each row contains 3 numbers: the sides of a triangle.
    # Sum of any two sides must be larger than the remaining side
    # How many triangles are possible?
    # Possible IF: A + B > C and B + C > A and A + C > B
    possible = 0

    for row in triangles:
        if (int(row[0]) + int(row[1]) > int(row[2])) and (int(row[1]) + int(row[2]) > int(row[0])) and (int(row[0]) + int(row[2]) > int(row[1])):
            possible += 1
    print(possible)

PartOne()