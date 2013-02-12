__author__ = 'Steven Shelby'

import os,sys

##### CORE FUNCTION #####
# This should be split out into multiple functions but
# this was literally a 15 minute project
def main(argv):
    # if no arguments then return -1 for error
    if not argv:
        return -1

    # get path from argv and attempt to walk directory
    print ""
    path = argv[0]

    # if invalid path then return -2
    if not os.path.exists(path):
        return -2

    for dirname, dirnames, filenames in os.walk(path):
         # print all filenames.
        for filename in filenames:
            print filename

    # get substring from user to remove from file names
    print ""
    sub = raw_input("Enter substring to remove from filenames: ")
    print "Removing \"" + sub + "\" from filenames..."
    for dirname, dirnames, filenames in os.walk(path):
        # check each file and rename accordingly
        for filename in filenames:
            newfname = filename.replace(sub, "")
            oldpath = os.path.join(dirname, filename)
            newpath = os.path.join(dirname, newfname)
            os.rename(oldpath, newpath)

    # print out new directory listing
    print ""
    for dirname, dirnames, filenames in os.walk(path):
        # print all filenames.
        for filename in filenames:
            print filename

##### MAIN #####
if __name__ == "__main__":
    print "Running File Renamer..."
    exitcode = main(sys.argv[1:])

    if exitcode == -1:
        # no argument provided
        print "No path specified"
    elif exitcode == -2:
        # invalid path specified
        print "Invalid path specified"