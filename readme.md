# Networking in the Heart
This is a final year project created by Raitis Dzalbs for the module COMP3931 Individual Project for The University of Leeds.

# Pre-requisites
This project uses a piece of software called VascuSynth to generate coronary arteries around a given model of a heart. This software can be installed following the installation process in the documentation from:
https://www.insight-journal.org/browse/publication/794

However there are a few notes that need to be mentioned to be able to get the software running properly in 2020 as there have been some changes made.

1. It is mentioned that ITK needs to be installed to be able to get VascuSynth to run. This is indeed true however one part is not specified: when using CMake to configure and generate the Makefile for ITK, the option for building shared libraries needs to be enabled.

2. When making VascuSynth, after generating using CMake, you will get an error mentioning that "-lITKIO" cannot be found. This is meant to be the ITKIO library after building the shared libraries in CMake and running Make on the resulting generated Makefile. This library does not exist anymore in the newer versions of ITK, as it has been split into more libraries that are different version of ITKIO. These are listed in the _itk_lib_link.txt_ in the correct format to be copied and pasted. To fix this issue, you need to go to _(vascusynth build directory)/CMakeFiles/VascuSynth.dir/link.txt_ and replace "-lITKIO" with the contents of _itk_lib_link.txt_. This should correctly link the appropriate ITK libraries to enable VascuSynth to be made properly.

Another requirement is the installation of the Python version of the VTK software. THis can be installed using pip by typing _$ pip install vtk_. Pip needs to fist be configured to python 3.7, as as of writing this, the library has not been released for the latest version, that being Python 3.8.

# Running the software

The software is made in Python 3 and is currently only compatible with Python 3.7, meaning that if it already isn't, you need to configure your machine, or create a virtual environment configured to, Python 3.7. To run the software:

_$ python generate_roots.py (vtk file which contains the model of the heart)_

Some sample anatomical models have been provided in the "Heart Models" directory that can be used to create results. After generation, the results will be displayed in a window, and saved in the "results" directory. In this directory, the coordinates of the newly generated coronary artery tree have been saved, as well as the model that was used to generate the model. Also, the rendering of slices of images that VascuSynth produces has also been saved in the image subdirectory of the given model directory.
