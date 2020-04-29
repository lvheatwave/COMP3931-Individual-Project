import os, sys

def oxygen_map(heart_name): # creates an oxygenation map based off of the coordinates in the structure of the heart file
    with open('VascuSynthLocation.txt') as location: # open location of vascusynth
        vascusynthLocation = location.read().splitlines()[0] #
    try: # create the file
        os.remove(str(vascusynthLocation + "/HeartOx.txt"))
        print("Overwritting HeartOx.txt")
    except:
        print('No HeartOx.txt file to remove\nCreating new HeartOx.txt file')

    file_name = heart_name.split('/')[1].split(".")[0]

    with open(vascusynthLocation + '/imageNames.txt', "w") as file: # write the file name into this file so when VascuSynth
        file.writelines(file_name)                                  # generates the data it makes the directory match the name

    oxmap = open(str(vascusynthLocation + "/HeartOx.txt"), "w+")
    with open (heart_name) as h:
        heart = h.readlines()


    line = []
    coordinates = []
    heartline = 5
    oxline = 0

    firstCoordinates = [] # get the first set of coordinates and use the as root node
    firstCoordinates.append(float(heart[heartline].split()[0]) + 100)
    firstCoordinates.append(float(heart[heartline].split()[1]) + 100)
    firstCoordinates.append(float(heart[heartline].split()[2]) + 100)

    perfPoint = str("PERF_POINT: " + str(round(firstCoordinates[0], 1)) + " " + str(round(firstCoordinates[1], 1)) + " " + str(round(firstCoordinates[2], 1)) + "\n")

    with open(vascusynthLocation + '/p1.txt', "r") as file:
        p1 = file.readlines()

    p1[3] = perfPoint

    with open(vascusynthLocation + '/p1.txt', "w") as file:
        file.writelines(p1)


    while True:
        if heart[heartline] == "\n" or heart[heartline][0] == "P":
            break
        else:
            line = heart[heartline].split()                # Every Heart model is filled with (x, y, z) coordinates, and there is
            coordinates.append([])                         # up to 3 sets on each line, therefore if the line isnt empty or is not
            coordinates[oxline].append(float(line[0]))     # not the polygon header line, then read the first set, then try read
            coordinates[oxline].append(float(line[1]))     # for the second then try read for the third, while managing an appropriate
            coordinates[oxline].append(float(line[2]))     # counter for each line of data
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
            heartline += 1

    oxmap.write("200 200 200\n0 0 0 200 200 200\n0\n") # VascuSynth needs to know how big the space is that it will be populating
                                                       # Previous values are overwritten by the next, so therefore we set the
    volumefactor = 2                                   # oxygenation of the whole space to 0 to not have stray bifurcations that go
                                                       # outside of the heart
    for i in range(0, len(coordinates)):
        corner1 = []
        corner2 = []
        corner1.append(coordinates[i][0] - volumefactor + 100) # This section makes a box around every coordinate that we just got
        corner1.append(coordinates[i][1] - volumefactor + 100) # so that it can basically say that all the areas around the heart
        corner1.append(coordinates[i][2] - volumefactor + 100) # need to have maximum oxygenation

        corner2.append(coordinates[i][0] + volumefactor + 100)
        corner2.append(coordinates[i][1] + volumefactor + 100)
        corner2.append(coordinates[i][2] + volumefactor + 100)

        oxmap.write(str(round(corner1[0], 1)) + " " + str(round(corner1[1], 1)) + " " + str(round(corner1[2], 1)) + " ")
        oxmap.write(str(round(corner2[0], 1)) + " " + str(round(corner2[1], 1)) + " " + str(round(corner2[2], 1)) + "\n")
        oxmap.write(str(1) + "\n")

    oxmap.close() # closes the oxygenation file to have it ready to be used by vascusynth
    h.close()

if __name__ == '__main__':
    oxygen_map("../Heart Models/pa0002_se01.vtk") # main function to be able to test this file individually
