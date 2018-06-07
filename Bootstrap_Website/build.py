pages = [
{
	'filename': 'content/index.html',
	'title': 'About Me',
	'output_file': 'docs/index.html'
},
{
	'filename': 'content/experience.html',
	'title': 'Professional Experience',	
	'output_file': 'docs/experience.html'
},
{
	'filename': 'content/projects.html',
	'title': 'Professional projects',
	'output_file': 'docs/projects.html'
}
]

def main():
	for dictionary in pages:
		base = open('template/base.html').read()
		content = open(dictionary['filename']).read()
		full_web_page = base.replace('{{content}}', content).replace('{{title}}', dictionary['title'])

		open(dictionary['output_file'], 'w+').write(full_web_page)
main()



# if __name__ == '__main__':
# 	main()
