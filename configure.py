import os, sys
import shutil
# this file populates the files that VascuSynth uses
def configure(vsLocation):
    with open("config.txt") as config:
        files = config.read().splitlines()
    for f in files:
        shutil.copyfile(str('config_files/' + f), str(vsLocation + '/' + f))

if __name__ == '__main__':
    configure('/home/raitis/vascusynthbuild')
