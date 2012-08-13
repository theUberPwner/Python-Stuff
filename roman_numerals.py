conv2roman = {1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}
conv2dec = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

#still working on the simplifying part but otherwise works
def decimal2roman(dec):
    rom = ''
    
    for key in sorted(conv2roman.iterkeys())[::-1]:
        if key > dec:
            continue
        else:
            count = 0
            while key <= dec:
                count += 1
                dec -= key
            rom += conv2roman[key] * count
    
def roman2decimal(rom):
    dec = 0
    
    index = 0
    while index < len(rom):
        curr_val = conv2dec[rom[index]]
        if index < len(rom)-1 and conv2dec[rom[index+1]] > curr_val:
            dec += (conv2dec[rom[index+1]] - curr_val)
            index += 2
        else:
            dec += curr_val
            index += 1
            
    return dec
    
if __name__ == '__main__':
    print decimal2roman(1956)
    print roman2decimal('MCMLVI')
