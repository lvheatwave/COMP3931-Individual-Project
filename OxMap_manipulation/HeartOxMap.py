import os, sys

# sys.path.append('../')

def oxygen_map(heart_name):
    try:
        os.remove("vascusynth/vs/HeartOx.txt")
        print("Overwritting HeartOx.txt")
    except:
        print('No HeartOx.txt file to remove\nCreating new heartOx.txt file')
    oxmap = open("vascusynth/vs/HeartOx.txt", "w+")
    with open (heart_name) as h:
        heart = h.readlines()


    line = []
    coordinates = []
    heartline = 5
    oxline = 0

    while True:
        if heart[heartline] == "\n" or heart[heartline][0] == "P":
            break
        else:
            line = heart[heartline].split()
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
            heartline += 1

    probability = 1/len(coordinates)

    oxmap.write("200 200 200\n0 0 0 200 200 200\n0.0001\n")

    x = 0

    for i in range(0, len(coordinates)):
        corner1 = []
        corner2 = []
        corner1.append(coordinates[i][0] - 0.5 + 100)
        corner1.append(coordinates[i][1] - 0.5 + 100)
        corner1.append(coordinates[i][2] - 0.5 + 100)

        corner2.append(coordinates[i][0] + 0.5 + 100)
        corner2.append(coordinates[i][1] + 0.5 + 100)
        corner2.append(coordinates[i][2] + 0.5 + 100)

        oxmap.write(str(round(corner1[0], 1)) + " " + str(round(corner1[1], 1)) + " " + str(round(corner1[2], 1)) + " ")
        oxmap.write(str(round(corner2[0], 1)) + " " + str(round(corner2[1], 1)) + " " + str(round(corner2[2], 1)) + "\n")
        oxmap.write(str(1) + "\n")

    oxmap.close()
    h.close()

if __name__ == '__main__':
    oxygen_map("../Heart Models/pa0002_se01.vtk")
