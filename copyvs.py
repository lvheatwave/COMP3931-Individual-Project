import os, sys, shutil

def copyvs(vslocation, filename): # this copies the images and the model into the results directory
    try:
        shutil.rmtree(str('results/' + filename + '/images'))
    except:
        None
    shutil.copy(str('Heart Models/' + filename + '.vtk'), str('results/' + filename + '.vtk'))
    shutil.copytree(str(vslocation + '/' + filename + '/original_image' ) , str('results/' + filename + '/images'))

if __name__ == '__main__':
    copyvs('/home/raitis/vascusynthbuild', 'pa0002_se02')
