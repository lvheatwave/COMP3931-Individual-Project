import os, argparse
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
    heart_name = get_program_parameters()
    oxygen_map(heart_name)
    os.system("cd vascusynth/vs ; ./VascuSynth paramFiles.txt imageNames.txt 0.08")
    gxl_to_vtk("vascusynth/vs/imageTest/tree_structure.xml")
    roots_file = "coordinates.vtk"
    render_project(heart_name, roots_file)

if __name__ == '__main__':
    main()
