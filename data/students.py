from bs4 import BeautifulSoup

soup = BeautifulSoup(open("students.html"))

num = 0
rowIdx = 0
firstnames = []
lastnames = []
emails = []
images = []
labs = []
labwebsites = []

imagefile = open('getimages.txt',"w")

for row in soup.find_all('tr'):
    rowIdx = rowIdx + 1
    col = row.find_all('td')
    for s in range(0,len(col)):
        if (s % 2) == 0:
            if (rowIdx % 2) == 0:
                student = col[s]
                img = "images/" + col[s+1].img['src']
                imagefile.write('-o \"' + col[s+1].img['src'][9:len(col[s+1].img['src'])] + '\" http://neuroscienceprogram.stanford.edu/' + col[s+1].img['src'] + '\n')
            elif (rowIdx % 2) == 1:
                student = col[s+1]
                img = "images/" + col[s].img['src']
                imagefile.write('-o \"' + col[s].img['src'][9:len(col[s].img['src'])] + '\" http://neuroscienceprogram.stanford.edu/' + col[s].img['src'] + '\n')
            num = num + 1
            fullname = student.a.string
            student.a.string = ""
            bothnames = fullname.split(' ',1)
            emails.append(student.a['href'][7:len(student.a['href'])].strip())
            firstnames.append(bothnames[0].strip())
            lastnames.append(bothnames[1].strip())
            images.append(img)
            links = student.find_all('a')
            if len(links) == 2:
                labwebsites.append(links[1]['href'])
            else:
                labwebsites.append("")
            labs.append(student.get_text().strip())
            print str(num) + ") " + firstnames[num-1] + " " + lastnames[num-1] + ", " + emails[num-1] + ", (" + img + ") " + labs[num-1] + " (" + labwebsites[num-1] + ")"

imagefile.close()
print 'firstnames: ' + str(len(max(firstnames,key=len)))
print 'lastnames: ' + str(len(max(lastnames,key=len)))
print 'emails: ' + str(len(max(emails,key=len)))
print 'images: ' + str(len(max(images,key=len)))
print 'labs: ' + str(len(max(labs,key=len)))
print 'lab websites: ' + str(len(max(labwebsites,key=len)))
print 'Found ' + str(num) + ' students.'

#from main.models import Student
#for j in range(num):
      #u = Student(firstname=firstnames[j], lastname=lastnames[j], email=emails[j], image=images[j], lab=labs[j], labwebsite=labwebsites[j])
      #u.save()
