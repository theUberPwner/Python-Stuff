#######################################################
#The user is asked for the possible letters and
#the length of the word to be guessed and this
#will output all of the possible answers based
#on a user supplied dictionary text file. Dictionaries
#are expected to contain each word on a new line
#
#This was really designed for the game draw something where
#you are given the length of the word and a bank of letters,
#but could be usefull for many other things
#######################################################

def generate_words():
    input_str = str(raw_input("Enter Jumbled String...\n(\"!\" to exit)"))
    if input_str == "!":
        exit()
    input_length = input("Enter Length of Answer: ")

    #bank of dictionaries
    #add file path to dictionary files
    dictionary_list = ["files/wwf.txt",]

    #loop through each dictionary
    for dfile in dictionary_list:
        f = open(dfile, "r")
        words = f.readlines()
        f.close()
        possible_words = []
        
        #loop through each word in current dictionary
        for word in words:
            word = word.lower().rstrip()
            
            # check if word is the right length
            if not len(word) == input_length:
                continue

            # if length check passes, then check characters
            for c in word:
                if input_str.find(c) == -1:
                    break
            else:
                possible_words.append(word)
            
        # print the results after each dictionary
        print "Dictionary %d:"%dictionary_list.index(dfile)
        print repr(possible_words)
        
if __name__ == '__main__': 
    generate_words()

