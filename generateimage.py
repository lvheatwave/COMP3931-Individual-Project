from evtk.hl import imageToVTK

import numpy as np

# Dimensions

nx, ny, nz = 17, 4, 60

ncells = nx * ny * nz

npoints = (nx + 1) * (ny + 1) * (nz + 1)

# Variables

pressure = np.random.rand(ncells).reshape( (nx, ny, nz), order = 'C')

temp = np.random.rand(npoints).reshape( (nx + 1, ny + 1, nz + 1))

imageToVTK("./image", cellData = {"pressure" : pressure}, pointData = {"temp" : temp} )