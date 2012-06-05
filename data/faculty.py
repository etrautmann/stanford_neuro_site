from bs4 import BeautifulSoup

soup = BeautifulSoup(open("data/faculty.html"))
concise = BeautifulSoup(open("data/faculty_concise.html"))

num = 0
numc = 0
firstnames = []
lastnames = []
degrees = []
websites = []
titles = []
departments = []
emails = []
blurbs = []
taglines = []
themes = []
allthemes = []

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

for faculty in concise.find_all('tr'):
		numc = numc + 1
		#print str(numc) + ") "
		colidx = 1
		for col in faculty.find_all('td'):
				#print "\t" + str(col.string)
				if colidx == 2:
						if col.string != None:
								taglines.append(col.string)
						else:
								taglines.append("")
				elif colidx == 3:
						mythemes = []
						if col.string != None:
								for t in col.string.split(','):
										mythemes.append(t.strip())
										allthemes.append(t.strip())
						themes.append(mythemes)
				colidx = colidx + 1

# find unique themes
uniquethemes = list(set(allthemes))
uniquethemes.sort()
print "\n\nList of themes: "
print(uniquethemes)

print '\nfirstnames: ' + str(len(max(firstnames,key=len)))
print 'lastnames: ' + str(len(max(lastnames,key=len)))
print 'degrees: ' + str(len(max(degrees,key=len)))
print 'websites: ' + str(len(max(websites,key=len)))
print 'titles: ' + str(len(max(titles,key=len)))
print 'departments: ' + str(len(max(departments,key=len)))
print 'emails: ' + str(len(max(emails,key=len)))
print 'blurbs: ' + str(len(max(blurbs,key=len)))
print 'taglines: ' + str(len(max(taglines,key=len)))
print 'Found ' + str(num) + ' faculty.\n'

idx = 0
print firstnames[idx] + " " + lastnames[idx] + " (" + degrees[idx] + "), " + departments[idx] + ", " + titles[idx]
print taglines[idx] + '\n' + str(themes[idx])
print '\n' + blurbs[idx] + '\n'

for t in themes[idx]:
		if t in uniquethemes:
				print "Prof. " + lastnames[idx] + "'s lab has a " + t + " theme."

#from main.models import Faculty
#themelist = []
#for j in range(len(uniquethemes)-1):
			#themelist.append(Theme(j))
			#themelist[j].save()
#for j in range(num):
			#u = Faculty(firstname=firstnames[j], lastname=lastnames[j], degree=degrees[j], website=websites[j], title=titles[j], department=departments[j], email=emails[j], blurb=blurbs[j], tagline=taglines[j])
			#u.save()
			#for t in themes[j]:
				#u.themes.add(uniquethemes.index(t) + 1)
