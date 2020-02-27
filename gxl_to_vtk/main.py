from xml.dom import minidom
from xml.etree import ElementTree as ET
import os, sys

import vtk

gxl = ET.parse("tree_structure.xml") # open gxl file
root = gxl.getroot()

file = open("coordinates.vtk", "w+") # open the file the points will be written

file.write("# vtk DataFile Version 3.0\nvtk output\nASCII\nDATASET POLYDATA\n") # Write the format of the vvtk file into the

nodecount = 0 # Count the number of nodes
for n in root[0]:
    if n.tag == "node":
        nodecount += 1

file.write("POINTS " + str(nodecount) + " float\n") # a line for the amount of points

nodeids = []
for n in range(0, len(root[0])): # get all the nodes and their coordinates and write them in to the new file
    if root[0][n].tag == "node":
        file.write(root[0][n][1][0][0].text + " " + root[0][n][1][0][1].text + " " + root[0][n][1][0][2].text + "\n")
        nodeids.append(str(root[0][n].attrib.get("id")))

file.write("\nLINES " + str(len(root[0]) - nodecount) + " " + str((len(root[0]) - nodecount) * 3) + "\n") # wwrite number of lines

for e in range(nodecount, len(root[0])): # get all the points that are connected and make them into lines that connect
    file.write("2 ")
    fromid = str(root[0][e].attrib.get("from"))
    toid = str(root[0][e].attrib.get("to"))
    for n in range(0, len(nodeids)):
        if fromid == nodeids[n]:
            file.write(str(n) + " ")
        if toid == nodeids[n]:
            file.write(str(n) + " ")
    file.write("\n")

file.close() # close new file
