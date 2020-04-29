import os, argparse, time
from OxMap_manipulation.HeartOxMap import oxygen_map as oxygen_map
from gxl_to_vtk.GXLToVTK import gxl_to_vtk as gxl_to_vtk
from readgrid import render_project as render_project

def get_program_parameters(): # get the required arguments for the software to start running
    description = 'Read an unstructured grid file.'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('heart_file', help='tetra.vtu.')
    args = parser.parse_args()
    return args.heart_file


def main():
    starttime = time.time() # timer to see how long the software takes to compile as it takes a while

    heart_name = get_program_parameters() # get the arguments

    file_name = heart_name.split('/')[1].split(".")[0] # get and format the name of the file to use to create an apporpriate directory for results
    if not os.path.exists('results/' + file_name):
        os.makedirs('results/' + file_name)

    oxygen_map(heart_name) # make oxygenation map

    with open('VascuSynthLocation.txt', 'r') as location: # get location of VascuSynth
        vascusynthlocation = location.read().splitlines()[0]

    print("Running VascuSynth") # run VascuSynth
    os.system("cd " + vascusynthlocation + " ; ./VascuSynth paramFiles.txt imageNames.txt 0.005")
    print("Root data generated")

    gxl_to_vtk(str(vascusynthlocation + '/' + file_name + '/tree_structure.xml'), str("results/" + file_name)) # convert gxl coordinate file to a vtk one
    print("Root data converted from GXL format to VTK")

    print("%f Seconds since start of generation" % (time.time() - starttime)) # display time it took to generate
    print("Rendering")
    render_project(heart_name, "results/" + file_name + "/coordinates.vtk") # displays the generated roots and the heart model as one

if __name__ == '__main__':
    main()
