import vtk
import numpy as np
import random as rnd
import math

def main():

    # generate the array of points(can be 2d for now) to figure out the rest
    a = [
        [0.0, 0.0, 0.0],
        [2.0, 2.0, 0.0],
        [2.0, 3.0, 0.0],
        [3.0, 2.5, 0.0],
        [4.0, 4.0, 0.0],
        [4.0, 2.0, 0.0]
        ]
    # calculate which points are closest to each other on a polygon edge of 2 (as in there are 2 points the polygon is connected to)

    pandd = []
    pp = []
    for x in range(0, len(a)):
        pandd.append([])
        pp.append([])
    for x in range(0, len(a)):
        for y in range(x+1, len(a)):
            d = math.sqrt(math.pow((a[x][0] - a[y][0]), 2) + math.pow((a[x][1] - a[y][1]), 2))
            pandd[x].append([x, y, d])
            pandd[y].append([x, y, d])
            pp[x].append([x, y])
            pp[y].append([x, y])

    distances = []
    pointpairs = []
    for x in range(0, len(pandd)):
        min = pandd[x][0]
        minpoints = pp[x][0]
        for y in range(0, len(pandd[x])):
            if min[2] > pandd[x][y][2]:
                min = pandd[x][y]
                minpoints = pp[x][y]
        distances.append(min)
        pointpairs.append(minpoints)

    matches = []
    for x in range(0, len(pointpairs)):
        for y in range(x + 1, len(pointpairs)):
            if pointpairs[x] == pointpairs[y]:
                matches.append(y)

    for x in matches:
        pointpairs.pop(x)

    with open("pandd.txt", "w") as file:
        file.write(str(pandd) + "\n")
        file.close()

    with open("distances.txt", "w") as file:
        file.write(str(pointpairs))
        file.close()


    # ActorColor=colors.GetColor3d("White");
    # BgColor=colors.GetColor3d("Gray");
    #
    # lineSource[] = vtk.vtkLineSource();
    # for x in range(0, len(distances)):
    #     lineSource[x].SetPoint1(a[], 0.0, 0.0);
    #     lineSource[x+1].SetPoint2(.0, 1.0, 0.0);



    # link them together

    # calculate the width of point before and after bifurcation



if __name__ == '__main__':
    main()
