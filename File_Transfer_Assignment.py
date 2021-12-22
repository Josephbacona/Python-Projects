import shutil
import os

#set where the source of the files are
source = 'folderA/'

#set the destination path to folderB
destination = 'folderB/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)

#This source is for files that were added or modified in the last 24 hours
source2 = 'newFiles/'

#The destination is a folder that the home office can access
destination2 = 'newFilesCopied/'
newfiles = os.listdir(source2)

for i in newfiles:
    #we are saying move the newly created or modified files repressented
    #by 'i' to their destination
    shutil.move(source2+i, destination2)



