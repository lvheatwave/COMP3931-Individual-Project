# Networking in the Heart
This is a final year project created by Raitis Dzalbs for the module COMP3931 Individual Project for The University of Leeds.

# Pre-requisites
This software has been created in Linux and has not been tested to work on Windows. Specifically this software has been created in Kubuntu 19.10.

##Software

### Insight Toolkit
Installation instruction can be found on https://itk.org. When generating with CMake, enable the shared libraries options.

### - VascuSynth
This project uses a piece of software called VascuSynth to generate coronary arteries around a given model of a heart. This software can be installed following the installation process in the documentation from:
https://www.insight-journal.org/browse/publication/794

### - Python 3.7
Python 3.7 is used to actually run the software.

This project uses a piece of software called VascuSynth to generate coronary arteries around a given model of a heart. This software can be installed following the installation process in the documentation from:
https://www.insight-journal.org/browse/publication/794

However there are a few notes that need to be mentioned to be able to get the software running properly in 2020 as there have been some changes made.
## Installation of Software

1. It is mentioned that ITK needs to be installed to be able to get VascuSynth to run. This is indeed true however one part is not specifically pointed out: when using CMake to configure and generate the Makefile for ITK, the option for building shared libraries needs to be enabled.

2. When making VascuSynth, after generating using CMake, you will get an error mentioning that "-lITKIO" cannot be found. This is meant to be the ITKIO library after building the shared libraries when generating ITK in CMake and running Make on the resulting generated Makefile. This library does not exist anymore in the newer versions of ITK, as it has been split into more libraries that are different version of ITKIO. These are listed in the _itk_lib_link.txt_ in the correct format to be copied and pasted. To fix this issue, you need to go to _(vascusynth build directory)/CMakeFiles/VascuSynth.dir/link.txt_ and replace "-lITKIO" with the contents of _itk_lib_link.txt_. This should correctly link the appropriate ITK libraries to enable VascuSynth to be made properly.

Another requirement is the installation of the Python version of the VTK software. THis can be installed using pip by typing _$ pip install vtk_. Pip needs to fist be configured to python 3.7, as as of writing this, the library has not been released for the latest version, that being Python 3.8.

# Running the software

First, you need to specify the location of VascuSynth. In the file "_VascuSynthLocation.txt_" you need to write the path to the VascuSynth build directory, this being the directory containing the VascuSynth run file.

The software is made in Python 3 and is currently only compatible with Python 3.7, meaning that if it already isn't, you need to configure your machine, or create a virtual environment configured to, Python 3.7. To run the software:

_$ python generate_roots.py (vtk file which contains the model of the heart)_ for single structure generation

_$ python generate_roots.py Heart\ Models/Multipoint/myocardial.vtk_ for multiple structure generation

Warning: this software can take up to 50 minutes to run, with the currently set configurations in the configuration file _p1.txt_. This can become longer if more nodes are added. You times may vary depending on the single core performance of your CPU. This software created and run an 8 x Intel Core i5-8250U @ 1.60GHz

Some sample anatomical models have been provided in the "Heart Models" directory that can be used to create results. After generating the single roots, the results will be displayed in a window, and saved in the "results" directory. In this directory, the coordinates of the newly generated coronary artery tree have been saved, as well as the model that was used to generate the model. Also, the rendering of slices of images that VascuSynth produces has also been saved in the image subdirectory of the given model directory. This is done so that you can have a better view of the produced output in something like Paraview.

For multiple coronary artery generation, you should have a file structure such that; your files that contain the branch location point data is in a subdirectory of a directory, and along side this subdirectory you should have the VTK file that contains the myocardial structure. An example of this is in the _Heart Models_ directory in the _Multipoint_ directory.

On the other hand, when generating the multiple start point structure, the data will be saved under the file name of the main vtk file, and there will be subdirectories for all the structures generated for that file. These should be viewed in medical imaging software like ParaView.

## Coordinates.vtk
The software also produces a line representation of the arteries created by VascuSynth and stores this under a file named _coordinates.vtk_ under the directory corresponding to the model it was produced off of. This can be viewed simulatniously using the _readgrid.py_ script by running:

python readgrid.py (model) (coresponding coordinates.vtk file)

This however only works with PolyData models such as the models used for single point vascular structure generation.
