#Python Program to convert an integer into a word representation

#conversion table
conv = {'0':'','1':'one','2':'two','3':'three',
        '4':'four','5':'five','6':'six','7':'seven',
        '8':'eight','9':'nine','10':'ten','11':'eleven',
        '12':'twelve','13':'thirteen','14':'fourteen',
        '15':'fifteen','16':'sixteen','17':'seventeen',
        '18':'eighteen','19':'nineteen','20':'twenty',
        '30':'thirty','40':'forty','50':'fifty','60':'sixty',
        '70':'seventy','80':'eighty','90':'ninety'}

#suffix table
suffix = ['',
          'thousand',
          'million',
          'billion',
          'trillion',
          'quadrillion',
          'quintillion',
          'sextillion',
          'septillion',
          'octillion',
          'nonillion',
          'decillion']

#takes a 3 digit number and returns the word form
def triplet(trip):
    t_word = ""
    hundred = trip // 100
    if hundred > 0:
        trip = trip % 100
        if trip == 0:
            t_word = conv.get(str(hundred)) + ' hundred'
        else:
            t_word = conv.get(str(hundred)) + ' hundred and'

    if trip < 20:
        return t_word + ' ' + conv.get(str(trip))
    else:
        d,r = divmod(trip,10)
        return t_word + ' ' + conv.get(str(d*10)) + ' ' + conv.get(str(r))

#takes any length number and returns the word form by passing
#3 digits at a time to the triplet function and adding the appropriate
#suffix each time
def num_to_word(num):
    word = ""

    s_num = str(num)
    index = 0
    while len(s_num) > 3:
        t = s_num[len(s_num)-3:]
        s_num = s_num[0:len(s_num)-3]
        word = triplet(int(t)) + ' ' + suffix[index] + ' ' + word
        index += 1

    word = triplet(int(s_num)) + ' ' + suffix[index] + ' ' + word
    return word

#MAIN PROGRAM
if __name__ == '__main__':
    user_input = raw_input('Enter Number to Convert: ')
    print num_to_word(int(user_input)).strip()
