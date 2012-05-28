from bs4 import BeautifulSoup

soup = BeautifulSoup(open("faculty.html"))

num = 0
firstnames = []
lastnames = []
degrees = []
websites = []
titles = []
departments = []
emails = []
blurbs = []

for faculty in soup.find_all('tr'):
    fullname = faculty.a.string.split(',',1)
    bothnames = fullname[0].split(' ',1)
    firstnames.append(bothnames[0].strip())
    lastnames.append(bothnames[1].strip())
    degrees.append(fullname[1].strip())
    websites.append(faculty.a.get('href').strip())
    italics = faculty.find_all('i')
    fulltitle = italics[0].string.split(',',1)
    titles.append(fulltitle[0].strip())
    departments.append(fulltitle[1].strip())
    emails.append(italics[1].string.strip())
    temp = faculty.find_all('br')
    blurbs.append(temp[2].get_text())
    #print faculty.br.get_text() + '\n\n\n'
    #print '----------------------------\n' + temp[2].get_text() + '\n--------------------------\n\n\n'
    num = num + 1

print 'firstnames: ' + str(len(max(firstnames,key=len)))
print 'lastnames: ' + str(len(max(lastnames,key=len)))
print 'degrees: ' + str(len(max(degrees,key=len)))
print 'websites: ' + str(len(max(websites,key=len)))
print 'titles: ' + str(len(max(titles,key=len)))
print 'departments: ' + str(len(max(departments,key=len)))
print 'emails: ' + str(len(max(emails,key=len)))
print 'blurbs: ' + str(len(max(blurbs,key=len)))
print 'Found ' + str(num) + ' faculty.'

print firstnames[0] + " " + lastnames[0] + " (" + degrees[0] + "), " + departments[0] + ", " + titles[0]
print '\n' + blurbs[0] + '\n'

# from main.models import Faculty
# for j in range(num):
      # u = Faculty(fullname=names[j], email=emails[j], title=titles[j], website=websites[j])
      # u.save()
