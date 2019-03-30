#!/usr/bin/python
"""
SFTW0000 localhost to sftw
1. moves localhost files to current folder
2. replaces all links, printing processed files
3. converts to zip, and clears directory
"""

import os
import time
import shutil
from distutils.dir_util import copy_tree


lclurl = 'http://localhost/' # string to replace
wwwurl = 'http://sftw.azurewebsites.net/' # replaced with
sftwdir = 'sftw' # temp directory


copy_tree('/var/www/html',sftwdir)

# get list of directories to modify
listdir = [sftwdir]
for floc in os.listdir(sftwdir):
    if os.path.isdir(sftwdir + '/' + floc):
        listdir.append(sftwdir + '/' + floc)

print('Files to replace')
for eachdir in listdir:
    for floc in os.listdir(eachdir):
        if floc.endswith('.html') or floc.endswith('.css'):
            shutil.move(eachdir + '/' + floc, './auxfile.txt')
            fdst = open(eachdir + '/' + floc, 'w')
            fsrc = open('./auxfile.txt', 'r')
            for saux in fsrc:
                fdst.write(saux.replace(lclurl,wwwurl))
            fdst.close()
            fsrc.close()
            os.remove('./auxfile.txt')
            print(' ' + eachdir + '/' + floc)

shutil.make_archive(sftwdir, 'zip', sftwdir)
shutil.rmtree(sftwdir)
print('Output available at ' + os.getcwd() + '/' + sftwdir + '.zip')
