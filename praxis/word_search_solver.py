#Word Search Solver
import sys

#get command line arguments
if len(sys.argv) > 1:
    path = sys.argv[1]

    try:
        with open(path) as f:
            data = f.readlines()
    except IOError as e:
        print 'Invalid File Path'
        print 'USAGE: python word_search_solver.py {file path(req)}'
        sys.exit()

else:
    print 'Invalid File Path'
    print 'USAGE: python word_search_solver.py {file path(req)}'
    sys.exit()

#check the puzzle for a given word
def find_word(word):
    w,h = len(ws[0]),len(ws)
    l = len(word)
    
    for r_index in range(0,len(ws)):
        for c_index in range(0,len(ws[r_index])):
            if ws[r_index][c_index] == word[0]:
                #down
                if r_index + l - 1 < h:
                    for index in range(1,l-1):
                        if not ws[r_index+index][c_index] == word[index]:
                            break
                    else:
                        return 'row: ' + str(r_index) + ' col: ' + str(c_index) +  ' *DOWN'
                #up
                if r_index - l + 1 >= 0:
                    for index in range(1,l-1):
                        if not ws[r_index-index][c_index] == word[index]:
                            break
                    else:
                        return 'row: ' + str(r_index) + ' col: ' + str(c_index) +  ' *UP'
                #left
                if c_index - l + 1 >= 0:
                    for index in range(1,l-1):
                        if not ws[r_index][c_index-index] == word[index]:
                            break
                    else:
                        return 'row: ' + str(r_index) + ' col: ' + str(c_index) +  ' *LEFT'
                #right
                if c_index + l - 1 < w:
                    for index in range(1,l-1):
                        if not ws[r_index][c_index+index] == word[index]:
                            break
                    else:
                        return 'row: ' + str(r_index) + ' col: ' + str(c_index) +  ' *RIGHT'
                #up-left
                if r_index - l + 1 >= 0 and c_index - l + 1 >= 0:
                    for index in range(1,l-1):
                        if not ws[r_index-index][c_index-index] == word[index]:
                            break
                    else:
                        return 'row: ' + str(r_index) + ' col: ' + str(c_index) +  ' *UP-LEFT'
                #up-right
                if r_index - l + 1 >= 0 and c_index + l - 1 < w:
                    for index in range(1,l-1):
                        if not ws[r_index-index][c_index+index] == word[index]:
                            break
                    else:
                        return 'row: ' + str(r_index) + ' col: ' + str(c_index) +  ' *UP-RIGHT'
                #down-left
                if r_index + l - 1 < h and c_index - l + 1 >= 0:
                    for index in range(1,l-1):
                        if not ws[r_index+index][c_index-index] == word[index]:
                            break
                    else:
                        return 'row: ' + str(r_index) + ' col: ' + str(c_index) +  ' *DOWN-LEFT'
                #down-right
                if r_index + l - 1 < h and c_index + l - 1 < w:
                    for index in range(1,l-1):
                        if not ws[r_index+index][c_index+index] == word[index]:
                            break
                    else:
                        return 'row: ' + str(r_index) + ' col: ' + str(c_index) +  ' *DOWN-RIGHT'
                
    
    return 'Word Not Found.'

#add data to lists
ws = []
for line in data:
    ws.append(line.split())

#MAIN LOOP
while 1:
    w = raw_input("Enter word to find ('q' to quit): ")
    
    print find_word(w.upper())
    
    if w == 'q':
        break
