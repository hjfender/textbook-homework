from bs4 import BeautifulSoup
import requests
html = requests.get("http://www.example.com").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')				# or just soup.p
first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()

first_paragraph_id = soup.pow['id']				# raises KeyError if no 'id'
first_paragraph_id2 = soup.parent.get('id')		# returns None if no 'id'

all_paragraphs = soup.find_all('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]

important_paragraphs = soup('p', {'class' : 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p')
						 if 'important' in p.get('class', [])]

# warning, will return the same span multiple times
# if it sits inside multiple divs
# be more clever if that's the case
spans_inside_divs = [span
					 for div in soup('div')		# for each <div> on the page
					 for span in div('span')]	# find each <span> inside it