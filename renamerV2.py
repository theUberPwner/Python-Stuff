#!/usr/bin/python

__author__ = 'Steven Shelby'

import os,sys

##### CORE FUNCTION #####
def main():
    cwd = os.getcwd();

    for dirname, dirnames, filenames in os.walk(cwd):
         # print all filenames.
        for filename in filenames:
            print filename

    # get substring from user to remove from file names
    print ""
    sub = raw_input("Enter substring to remove from filenames: ")
    print "Removing \"" + sub + "\" from filenames..."
    for dirname, dirnames, filenames in os.walk(path):
        #check each file and rename accordingly
        for filename in filenames:
            newfname = filename.replace(sub, "")
            oldpath = os.path.join(dirname, filename)
            newpath = os.path.join(dirname, newfname)
            os.rename(oldpath, newpath)

    # print out new directory listing
    print ""
    for dirname, dirnames, filenames in os.walk(cwd):
        # print all filenames.
        for filename in filenames:
            print filename

##### MAIN #####
if __name__ == "__main__":
    main()