from scrapemark import scrape

text = scrape("""{* <a class="link_nounderline" href="mailto:{{ [emails] }}">{{ [names] }}</a>" *}""", url='http://neuroscienceprogram.stanford.edu/students.php')

#media = scrape("""{*<img src="mugshots/{{ [images] }}" />*}""", url='http://neuroscienceprogram.stanford.edu/students.php')
#print media

print '\nFound ' + str(len(text['names'])) + ' students and ' + str(len(text['names'])) + ' e-mail addresses:'
for j in range(len(text['names'])):
    print text['names'][j] + ': ' + text['emails'][j]

# from main.models import Student
# for j in range(len(text['names'])):
      # s = str.split(str(text['names'][j]))
      # e = str(text['emails'][j])
      # u = Student(firstname=s[0], lastname=s[len(s)-1], email=e)
      # u.save()
