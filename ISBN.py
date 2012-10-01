#Python ISBN/EAN Lookup/Conversion/Validation

from urllib2 import urlopen
from xml.dom.minidom import parseString

class ISBN2():
    KEY = "ZB9NSKFX" #developer key for isbndb.com
    URL = "http://isbndb.com/api/books.xml?access_key=" + KEY #our base URL
    
    #calculate ISBN checksum
    def isbn_checksum(self,i):
        i = i.replace('-','').replace(' ','')
        
        s = 0
        m = [10,9,8,7,6,5,4,3,2]
        
        for index,d in enumerate(i):
            s += (int(d) * m[index])
            
        r = s % 11
        check = ['0','X','9','8','7','6','5','4','3','2','1']
        
        return check[r]
        
    #calculate EAN checksum
    def ean_checksum(self,e):
        e = e.replace('-','').replace(' ','')
        
        s = 0
        m = [1,3,1,3,1,3,1,3,1,3,1,3]
        
        for index,d in enumerate(e[0:12]):
            s += (int(d) * m[index])
            
        r = s % 10
        check = ['0','9','8','7','6','5','4','3','2','1']
        
        return check[r]
        
    #validate ISBN by calculating checksum and comparing
    def validate_isbn(self,i):
        i = i.replace('-','').replace(' ','')
        if not len(i) == 10:
            pass
            #throw exception
            
        if i[9] == isbn_checksum(i[0:9]):
            return True
            
        return False
        
    #validate EAN by calculating checksum and comparing
    def validate_ean(self,e):
        e = e.replace('-','').replace(' ','')
        if not len(ean) == 13:
            pass
            #throw exception
            
        if e[12] == ean_checksum(e[0:12]):
            return True
        
        return False
        
    #validate isbn or ean
    def validate(self,val):
        val = val.replace('-','').replace(' ','')
        if len(val) == 10:
            return self.validate_isbn(val)
        elif len(val) == 13:
            return self.validate_ean(val)
            
        return False
    
    #get book data from either ISBN or EAN
    def get_by_val(self,val):
        u = self.URL + "&index1=isbn&value1=" + val
        f = urlopen(u)
        d = f.read()
        f.close()
        return d
    
    #convert 10 digit ISBN to 13 digit EAN
    def isbn2ean(self,i):
        i = i.replace('-','').replace(' ','')
        if not self.validate_isbn(i):
            pass
            #throw exception
            
        e = '978' + i[0:len(i)-1]
        m = [1,3,1,3,1,3,1,3,1,3,1,3]
        
        s = 0
        for index,d in enumerate(e):
            s += (int(d) * m[index])
            
        r = s % 10
        if r == 0:
            e += '0'
        else:
            e += str(10-r)
            
        return e
    
    #convert 13 digit EAN to 10 digit ISBN
    def ean2isbn(self,e):
        e = e.replace('-','').replace(' ','')
        if not self.validate_ean(e):
            pass
            #throw exception
            
        i = e[3:len(e)-1]
        m = [10,9,8,7,6,5,4,3,2]
        
        s = 0
        for index,d in enumerate(i):
            s += (int(d) * m[index])
            
        r = s % 11
        if r == 0:
            i += '0'
        elif r == 1:
            i += 'X'
        else:
            i += str(11-r)
            
        return i
     
    #format isbn
    def format_isbn(self,i):
        new_i = i[0] + '-' + i[1:4] + '-' + i[4:9] + '-' + i[9]
        return new_i
        
    #format ean
    def format_ean(self,e):
        new_e = e[0:3] + '-' + e[3] + '-' + e[4:7] + '-' + e[7:12] + '-' + e[12]
        return new_e
        
    #print out book data neatly
    def f_print(self,v,t,a,p):
        print '######################################'
        if len(v) == 10:
            print 'ISBN: ' + self.format_isbn(v)
        elif len(v) == 13:
            print 'EAN: ' + self.format_ean(v)
        print 'Title: ' + t
        print 'Author(s): ' + a
        print 'Publisher: ' + p
        print '######################################'
        
        
if __name__ == '__main__':
    I = ISBN2()
    
    while 1:
        val = raw_input('Enter ISBN (\'q\' to quit): ')
        val = val.replace('-','').replace(' ','')
        
        print val
        
        if val == 'q':
            break
            
        if I.validate(val):
            data = I.get_by_val(val)
            
            dom = parseString(data)
            
            title_long = dom.getElementsByTagName('TitleLong')[0].firstChild.data
            authors = dom.getElementsByTagName('AuthorsText')[0].firstChild.data
            publisher = dom.getElementsByTagName('PublisherText')[0].firstChild.data
            
            I.f_print(val,title_long,authors,publisher)
        else:
            print 'Invalid ISBN/EAN'
            continue
