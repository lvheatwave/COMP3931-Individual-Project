import os, argparse, time, shutil
from OxMap_manipulation.HeartOxMap import oxygen_map as oxygen_map
from gxl_to_vtk.GXLToVTK import gxl_to_vtk as gxl_to_vtk
from configure import configure as configure
from copyvs import copyvs as copyvs
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

    with open('VascuSynthLocation.txt', 'r') as location: # get location of VascuSynth
        vascusynthlocation = location.read().splitlines()[0]

    configure(vascusynthlocation, 'config_files') # configures vascusynth

    oxygen_map(heart_name, 1.7) # make oxygenation map

    file_name = heart_name.split('/')[1].split(".")[0] # get and format the name of the file to use to create an apporpriate directory for results
    if not os.path.exists('results/' + file_name):
        os.makedirs('results/' + file_name)

    print("Running VascuSynth") # run VascuSynth
    try:
        os.system("cd " + vascusynthlocation + " ; ./VascuSynth paramFiles.txt imageNames.txt 0.005")
    except:
        print("Error: VascuSynth not found.\nAborting")
        sys.exit(1)
    print("Vascular data generated")

    gxl_to_vtk(str(vascusynthlocation + '/' + file_name + '/tree_structure.xml'), str("results/" + file_name)) # convert gxl coordinate file to a vtk one
    print("Vascular data converted from GXL format to VTK")

    print("%f Seconds since start of generation" % (time.time() - starttime)) # display time it took to generate

    copyvs(vascusynthlocation, file_name) # copy the images into the same file for easy viewing
    print("Generation Complete")
    print("\nRendering")
    #render_project("results/" + file_name + '/' + file_name + ".vtk", "results/" + file_name + "/coordinates.vtk") # displays the generated roots and the heart model as one

if __name__ == '__main__':
    main()
