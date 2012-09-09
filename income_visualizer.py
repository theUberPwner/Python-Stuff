#The user provide his/her yearly salary and the date to start calculating
#from and this program shows a live update of how much money you are making
#if you were to calculate your yearly salary over every second.

import pygame, sys, datetime
from pygame.locals import *

#Initialize pygame and game clock
pygame.init()
clock = pygame.time.Clock()

#Create the surface
the_display = pygame.display.set_mode((300, 90))
pygame.display.set_caption('My Wealth')

#Define the colors that we will be using
red_col = (255,0,0)
green_col = (0,255,0)
white_col = (255,255,255)
black_col = (0,0,0)

#Define the font we will be using
text_font = pygame.font.Font(None, 30)

#global variables
global earned_since
global total_earned
global yearly_salary

def calculate_income():
    global total_earned
    global earned_since
    global yearly_salary
    
    time_elapsed = datetime.datetime.now() - earned_since
    
    days_elapsed = time_elapsed.days
    seconds_elapsed = time_elapsed.seconds
    
    total_earned = days_elapsed * (yearly_salary / 365)
    total_earned += seconds_elapsed * (yearly_salary / 365.0 / 24.0 / 60.0 / 60.0)
    total_earned = float('%0.2f' % total_earned)
    
def display_wealth():
    global total_earned
    
    #Calculate bar width based on income
    cents = total_earned % 1.0
    #print cents
    new_width = ((cents % .25) * 300.0) / .25
    
    #Draw the bar
    pygame.draw.rect(the_display, green_col, (0,0,new_width,30))

def display_info():
    global earned_since
    global total_earned
    
    #The text to display
    earned_text = "$" + str(total_earned) + " earned since: "
    date_text = earned_since.strftime("%m/%d/%Y %H:%M.%S")
    
    #Render the text into surfaces using our font we created
    cap_surface = text_font.render("25 cents", False, white_col)
    earned_surface = text_font.render(earned_text, False, white_col)
    date_surface = text_font.render(date_text, False, white_col)
    
    #Create the rectangles and set the positions of the text
    cap_rect = cap_surface.get_rect()
    cap_rect.topleft = (150 - (cap_surface.get_width() / 2), 16 - (cap_surface.get_height() / 2))
    earned_rect = earned_surface.get_rect()
    earned_rect.topleft = (0, 35)
    date_rect = date_surface.get_rect()
    date_rect.topleft = (0, 65)
    
    #Draw the text
    the_display.blit(date_surface, date_rect)
    the_display.blit(earned_surface, earned_rect)
    the_display.blit(cap_surface, cap_rect)

if __name__ == '__main__':
    global earned_since
    global yearly_salary
    global total_earned
    
    #Get date to start calculating from
    while True:
        date_input = raw_input("Start Date dd/mm/yy\n(Enter 'now' for now): ")
        if date_input.lower() == 'now':
            earned_since = datetime.datetime.now()
            break
        try:
            earned_since = datetime.datetime.strptime(date_input, "%d/%m/%y")
            print earned_since
            break
        except:
            print "Invalid Date"
    
    #Get yearly salary of human lifeform
    yearly_salary = input("Yealry Salary: $")
    print yearly_salary
    
    #Main Program Loop
    while 1:
        the_display.fill(black_col)
        pygame.draw.rect(the_display, red_col, (0,0,300,30))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        calculate_income()
        display_wealth()
        display_info()
        
        pygame.display.update()
