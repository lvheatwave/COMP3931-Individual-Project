import os, sys, shutil

def copymultivs(vslocation, filename, save_name, file_location): # this copies the images and the model into the results directory
    try:
        shutil.rmtree(str('results/' + save_name + '/images'))
    except:
        None
    shutil.copy(str(file_location + '.vtk'), str('results/' + filename + '/' + filename + '.vtk'))
    shutil.copytree(str(vslocation + '/' + save_name.split("/")[1] + '/original_image' ) , str('results/' + save_name + '/images'))

if __name__ == '__main__':
    copymultivs('/home/raitis/vascusynthbuild', 'pa0002_se02')
