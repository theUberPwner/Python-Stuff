from datetime import date,timedelta

#holidays#
##########
#0-Memorial Day (Last Monday in May)
#1-Labor Day (First Monday in September)
#2-Columbus Day (Second Monday in October)
#3-Thanksgiving (Fourth Thursday in November)

holidays = ['Memorial Day',\
            'Labor Day',\
            'Columbus Day',\
            'Thanksgiving']

print '##################Holidays####################'
print '1-Memorial Day (Last Monday in May)'
print '2-Labor Day (First Monday in September)'
print '3-Columbus Day (Second Monday in October)'
print '4-Thanksgiving (Fourth Thursday in November)'

holiday = int(raw_input("Enter Holiday #: "))
year = int(raw_input("Enter Year: "))

day = timedelta(days=1)
week = timedelta(days=7)

if holiday == 1: #Memorial Day
    d = date(year,5,1)
    while not d.strftime('%A') == 'Monday':
        d += day

    while (d + week).month == 5:
        d += week

elif holiday == 2: #Labor Day
    d = date(year,9,1)
    while not d.strftime('%A') == 'Monday':
        d += day

elif holiday == 3: #Columbus Day
    d = date(year,10,1)
    while not d.strftime('%A') == 'Monday':
        d += day

    d += week

elif holiday == 4: #Thanksgiving
    d = date(year,11,1)
    while not d.strftime('%A') == 'Thursday':
        d += day

    d += week*3

print holidays[holiday-1] + ' falls on ' + d.strftime('%x')



