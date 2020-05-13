import os, argparse, time, shutil
from OxMap_manipulation.HeartOxMap import oxygen_map as oxygen_map
from gxl_to_vtk.GXLToVTK import gxl_to_vtk as gxl_to_vtk
from configure import configure as configure
from copymultivs import copymultivs as copymultivs
from readgrid import render_project as render_project
from find_start import findstart as findstart

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

    configure(vascusynthlocation, 'config_multi') # configures vascusynth

    oxygen_map(heart_name, 2.1) # make oxygenation map

    file_name = heart_name.split('/')[2].split(".")[0]
    file_location = heart_name.split(".")[0] # get and format the name of the file to use to create an apporpriate directory for results
    if not os.path.exists('results/' + file_name):
        os.makedirs('results/' + file_name)

    print("Running VascuSynth") # run VascuSynth

    try:
        startpoints = []
        startpointsdirs = file_location.split("/")
        startpointlocation = str(startpointsdirs[0] + "/" + startpointsdirs[1] + "/points/")
        for files in os.listdir(startpointlocation):
            if os.path.isfile(os.path.join(startpointlocation, files)):
                findstart(str(startpointlocation + files))
                save_name = str(file_name + '/' + files.split(".")[0])
                with open(vascusynthlocation + '/imageNames.txt', "w") as file: # write the file name into this file so when VascuSynth
                    file.writelines(files.split(".")[0])
                print(files)
                os.system("cd " + vascusynthlocation + " ; ./VascuSynth paramFiles.txt imageNames.txt 0.005")

            print("Vascular data generated")
            copymultivs(vascusynthlocation, file_name, save_name, file_location) # copy the images into the same file for easy viewing
            gxl_to_vtk(str(vascusynthlocation + '/' + save_name.split("/")[1] + '/tree_structure.xml'), str("results/" + save_name)) # convert gxl coordinate file to a vtk one
            print("Vascular data converted from GXL format to VTK")


    except:
        print("Error: VascuSynth not found.\nAborting")
        sys.exit(1)
    print("%f Seconds since start of generation" % (time.time() - starttime)) # display time it took to generate
    print("Generation Complete")

if __name__ == '__main__':
    main()
