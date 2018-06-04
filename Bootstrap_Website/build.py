# Template files
top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

#index file
content = open('content/index.html').read()
index_html = top + content + bottom
open('docs/index.html', 'w+').write(index_html)

#experience file
content = open('content/experience.html').read()
experience_html = top + content + bottom
open('docs/experience.html', 'w+').write(experience_html)

#projects file
content = open('content/projects.html').read()
projects_html = top + content + bottom
open('docs/projects.html', 'w+').write(projects_html)