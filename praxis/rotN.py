#USAGE: python rotN.py {file path} {shift}

from string import maketrans
import sys

#Read command line args and set variables
if len(sys.argv) > 1:
    path = sys.argv[1]

    try:
        with open(path) as f:
            data = f.read()
    except IOError as e:
        print 'Invalid File Path'
        print 'USAGE: python rotN.py {file path(opt)} {shift(opt)}'
        sys.exit()

    if len(sys.argv) > 2:
        try:
            shift = int(sys.argv[2])
        except:
            print 'Invalid shift'
            print 'USAGE: python rotN.py {file path(opt)} {shift(opt)}'
            sys.exit()
    else: #If no shift specified, use 13(ROT13)
        shift = 13

else:#no args so take data in from user
    data = raw_input("Enter data to translate: ")
    while 1:
        try:
            shift = int(input("Enter shift: "))
            break
        except:
            print 'Invalid shift.'

#create the translation
intab = 'abcdefghijklmnopqrstuvwxyz'
outtab = intab[shift:] + intab[0:shift]

trantab = maketrans(intab,outtab)

#print the translated data
print data.lower().translate(trantab)
