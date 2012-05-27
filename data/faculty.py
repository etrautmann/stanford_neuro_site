from bs4 import BeautifulSoup

soup = BeautifulSoup(open("faculty.html"))

num = 0
names = []
websites = []
titles = []
emails = []
blurbs = []

for faculty in soup.find_all('tr'):
    names.append(faculty.a.string)
    websites.append(faculty.a.get('href'))
    italics = faculty.find_all('i')
    titles.append(italics[0].string)
    emails.append(italics[1].string)
    num = num + 1

print 'names: ' + str(len(max(names,key=len)))
print 'websites: ' + str(len(max(websites,key=len)))
print 'titles: ' + str(len(max(titles,key=len)))
print 'emails: ' + str(len(max(emails,key=len)))
print 'Found ' + str(num) + ' faculty.'

# from main.models import Faculty
# for j in range(num):
      # u = Faculty(fullname=names[j], email=emails[j], title=titles[j], website=websites[j])
      # u.save()
