from bs4 import BeautifulSoup

soup = BeautifulSoup(open("data/alumni.html"))

num = 0
firstnames = []
lastnames = []
advisors = []
currentpos = []
links = []

for alumni in soup.find_all('tr'):
    cols = alumni.find_all('td')
    fullname = cols[0].string
    bothnames = fullname.split(' ',1)
    firstnames.append(bothnames[0].strip())
    lastnames.append(bothnames[1].strip())
    if cols[1].string == None:
        advisors.append('')
    else:
        advisors.append(cols[1].string.strip())
    if cols[2].string == None:
        currentpos.append('')
    else:
        currentpos.append(cols[2].string.strip())
    if cols[0].a == None:
        links.append('')
    else:
        links.append(cols[0].a['href'].strip())
    num = num + 1

print 'firstnames: ' + str(len(max(firstnames,key=len)))
print 'lastnames: ' + str(len(max(lastnames,key=len)))
print 'advisors: ' + str(len(max(advisors,key=len)))
print 'currentpos: ' + str(len(max(currentpos,key=len)))
print 'links: ' + str(len(max(links,key=len)))

print firstnames[0] + " " + lastnames[0] + " (" + advisors[0] + "), " + currentpos[0] + ", " + links[0]
print "found " + str(num) + " alumni"

#from main.models import Alumnus
for j in range(num):
      u = Alumnus(firstname=firstnames[j], lastname=lastnames[j], advisor=advisors[j], currentpos=currentpos[j], links=links[j])
      u.save()
