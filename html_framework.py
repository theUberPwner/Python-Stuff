from datetime import date
import Tkinter
import tkFileDialog
import os

rel_js_path = 'js/'
js_fname = 'external.js'

rel_css_path = 'css/'
css_fname = 'external.css'

def add_js(curr_path):
    d = curr_path + rel_js_path
    if not os.path.exists(d):
        os.makedirs(d)
    with open(d + js_fname, "w") as file:
        #Initial Comments
        file.write("//Originally Created: " + today.isoformat() + "\n//Original Author: Steven Shelby\n\n//Last Modified: " + today.isoformat() + "\n//Last Author: Steven Shelby\n\n//[Description]\n\n")
        
def add_css(curr_path):
    d = curr_path + rel_css_path
    if not os.path.exists(d):
        os.makedirs(d)
    with open(d + css_fname, "w") as file:
        #Initial Comments
        file.write("/*\nOriginally Created: " + today.isoformat() + "\nOriginal Author: Steven Shelby\n\nLast Modified: " + today.isoformat() + "\nLast Author: Steven Shelby\n\n[Description]\n*/\n\n")

if __name__ == '__main__':
    # define options for opening or saving a file
    file_opt = options = {}
    #options['defaultextension'] = '' # couldn't figure out how this works
    options['filetypes'] = [('HTML file', '.html')]
    options['initialdir'] = 'C:\\'
    options['initialfile'] = 'index.html'
    #options['parent'] = Tkinter.Tk() 
    options['title'] = 'Select Output File'
    
    #Get date for commenting document
    today = date.today()
    
    #Get user input
    js_input = raw_input("Include external js? (y or n): ")
    include_js = True if js_input == 'y' else False
    
    jQuery_input = raw_input("Include jQuery? (y or n): ")
    include_jQuery = True if jQuery_input == 'y' else False
    
    css_input = raw_input("Include external css? (y or n): ")
    include_css = True if css_input == 'y' else False
    
    #Open our file for writing and write to it using with
    with tkFileDialog.asksaveasfile(mode='w', **file_opt) as file:
        #Initial Comments
        file.write("<!-----------------------------\nOriginally Created: " + today.isoformat() + "\nOriginal Author: Steven Shelby\n\nLast Modified: " + today.isoformat() + "\nLast Author: Steven Shelby\n\n[Description]\n------------------------------>\n\n")
        
        #Main HTML
        file.write("!DOCTYPE html")
        file.write("<html lang = 'en'>\n")
        file.write("<head>\n")
        file.write("    <meta charset=\"UTF-8\">\n")
        file.write("    <title></title>\n")
        
        #Check if including jQuery
        if (include_jQuery):
            file.write("    <script type=\"text/javascript\" src=\"//ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js\"></script>\n")
        
        #Check if including js and/or css
        if (include_js):
            file.write("    <script type=\"text/javascript\" src=\"" + rel_js_path + js_fname + "\"></script>\n")
            add_js(os.path.split(file.name)[0] + "/")
        if (include_css):
            file.write("    <link rel=\"stylesheet\" href=\"" + rel_css_path + css_fname + "\" type=\"text/css\">\n")
            add_css(os.path.split(file.name)[0] + "/")
            
        file.write("</head>\n")
        file.write("<body>\n    \n    \n    \n")
        
        
        file.write("</body>\n")
        file.write("</html>")
        