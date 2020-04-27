import os, argparse, time
from OxMap_manipulation.HeartOxMap import oxygen_map as oxygen_map
from gxl_to_vtk.GXLToVTK import gxl_to_vtk as gxl_to_vtk
from readgrid import render_project as render_project

def get_program_parameters():
    description = 'Read an unstructured grid file.'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('heart_file', help='tetra.vtu.')
    args = parser.parse_args()
    return args.heart_file


def main():
    starttime = time.time()

    heart_name = get_program_parameters()

    file_name = heart_name.split('/')[1].split(".")[0]
    if not os.path.exists('results/' + file_name):
        os.makedirs('results/' + file_name)

    oxygen_map(heart_name)

    with open('VascuSynthLocation.txt', 'r') as location:
        vascusynthlocation = location.read().splitlines()[0]

    print("Running VascuSynth")
    os.system("cd " + vascusynthlocation + " ; ./VascuSynth paramFiles.txt imageNames.txt 0.005")
    print("Root data generated")

    gxl_to_vtk(str(vascusynthlocation + '/' + file_name + '/tree_structure.xml'), str("results/" + file_name))
    print("Root data converted from GXL format to VTK")

    roots_file = "results/" + file_name + "/coordinates.vtk"
    print("%f Seconds since start of generation" % (time.time() - starttime))
    print("Rendering")
    render_project(heart_name, roots_file)

if __name__ == '__main__':
    main()
