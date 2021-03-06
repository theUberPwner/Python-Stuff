#USAGE: python rotN.py {file path} {shift}

#simple string shift script
#you can pass in the arguments or just enter data
#at runtime.

from string import maketrans
import sys

if len(sys.argv) > 1:
    path = sys.argv[1]

    try:
        with open(path) as f:
            data = f.read()
    except IOError as e:
        print 'Invalid File Path'
        print 'USAGE: python rotN.py {file path} {shift}'
        sys.exit()

    if len(sys.argv) > 2:
        try:
            shift = int(sys.argv[2])
        except:
            print 'Invalid shift'
            print 'USAGE: python rotN.py {file path} {shift}'
            sys.exit()
    else: #If no shift specified, use 13
        shift = 13

else:
    data = raw_input("Enter data to translate: ")
    while 1:
        s = raw_input("Enter shift: ")
        if s == "":
            shift = 13 #If no shift specified, use 13
            break
        else:
            try:
                shift = int(s)
                break
            except:
                print 'Invalid shift.'

intab = 'abcdefghijklmnopqrstuvwxyz'
outtab = intab[shift:] + intab[0:shift]

trantab = maketrans(intab,outtab)

print data.lower().translate(trantab)
