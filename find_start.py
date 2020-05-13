import os, argparse, time, shutil

def findstart(locationfile):
    with open('VascuSynthLocation.txt', 'r') as location: # open location of vascusynth
        vascusynthLocation = location.read().splitlines()[0]
    with open(locationfile, "r") as file:
        lines = file.readlines()

    line = []
    coordinates = []
    startline = 5
    oxline = 0

    while True:
        if lines[startline] == "\n" or lines[startline][0] == "C":
            break
        else:
            line = lines[startline].split()
            coordinates.append([])
            coordinates[oxline].append(float(line[0]))
            coordinates[oxline].append(float(line[1]))
            coordinates[oxline].append(float(line[2]))
            oxline += 1
            try:
                coordinates.append([])
                coordinates[oxline].append(float(line[3]))
                coordinates[oxline].append(float(line[4]))
                coordinates[oxline].append(float(line[5]))
                oxline += 1
            except:
                coordinates.pop()
            try:
                coordinates.append([])
                coordinates[oxline].append(float(line[6]))
                coordinates[oxline].append(float(line[7]))
                coordinates[oxline].append(float(line[8]))
                oxline += 1
            except:
                coordinates.pop()
            startline += 1

    startCoordinates = []
    for x in range(5, len(lines)):
        l = lines[x].split(" ")
        if l[0] == "CELLS":
            startCoordinates = int(lines[x + 1].split(" ")[1])

    perfPoint = str("PERF_POINT: " + str(round(coordinates[startCoordinates][0], 1)) + " " + str(round(coordinates[startCoordinates][1], 1)) + " " + str(round(coordinates[startCoordinates][2], 1)) + "\n")
    with open(vascusynthLocation + '/p1.txt', "r") as file:
        p1 = file.readlines()

    p1[3] = perfPoint

    with open(vascusynthLocation + '/p1.txt', "w") as file:
        file.writelines(p1)

if __name__ == '__main__':
    findstart('Heart Models/Multipoint/points/p_d1.vtk')
