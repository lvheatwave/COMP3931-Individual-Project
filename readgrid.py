#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import vtk

def get_program_parameters():
    import argparse
    description = 'Read an unstructured grid file.'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('heart_file', help='tetra.vtu.')
    parser.add_argument('roots_file')
    args = parser.parse_args()
    return args.heart_file, args.roots_file

def main():
    colors = vtk.vtkNamedColors()
    heart_name, roots_file = get_program_parameters()

    # Read the source file.
    heart_reader = vtk.vtkPolyDataReader()
    heart_reader.SetFileName(heart_name)
    heart_reader.Update()  # Needed because of GetScalarRange
    heart_output = heart_reader.GetOutput()
    heart_scalar_range = heart_output.GetScalarRange()

    root_reader = vtk.vtkPolyDataReader()
    root_reader.SetFileName(roots_file)
    root_reader.Update()
    root_output = root_reader.GetOutput()
    root_scalar_range = root_output.GetScalarRange()

    # Create the mapper that corresponds the objects of the vtk.vtk file
    # into graphics elements
    heart_mapper = vtk.vtkDataSetMapper()
    heart_mapper.SetInputData(heart_output)
    heart_mapper.SetScalarRange(heart_scalar_range)
    heart_mapper.ScalarVisibilityOff()

    root_mapper = vtk.vtkDataSetMapper()
    root_mapper.SetInputData(root_output)
    root_mapper.SetScalarRange(root_scalar_range)
    root_mapper.ScalarVisibilityOff()

    # Create the Actors
    actor = vtk.vtkActor()
    actor.SetMapper(heart_mapper)
    actor.GetProperty().EdgeVisibilityOn()
    actor.GetProperty().SetLineWidth(1.0)

    rootactor = vtk.vtkActor()
    rootactor.SetMapper(root_mapper)
    rootactor.GetProperty().EdgeVisibilityOn()
    rootactor.GetProperty().SetLineWidth(3.0)

    backface = vtk.vtkProperty()
    backface.SetColor(colors.GetColor3d("black"))
    actor.SetBackfaceProperty(backface)
    rootactor.SetBackfaceProperty(backface)

    # Create the Renderer
    renderer = vtk.vtkRenderer()
    renderer.AddActor(rootactor)
    renderer.AddActor(actor)
    renderer.SetBackground(0, 0, 1)  # Set background to white
    renderer.SetBackground(colors.GetColor3d("Wheat"))

    # Create the RendererWindow
    renderer_window = vtk.vtkRenderWindow()
    renderer_window.AddRenderer(renderer)

    # Create the RendererWindowInteractor and display the vtk_file
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderer_window)
    interactor.Initialize()
    interactor.Start()


if __name__ == '__main__':
    main()
