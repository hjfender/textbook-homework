def fix_unicode(text):
	return text.replace(u"\u2019", "'")

from bs4 import BeautifulSoup
import requests
url = "http://radar.oreilly.com/2010/06/what-is-data-science.html"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

context = soup.find("div", "entry-content")
regex = r"[\w']+|[\.]"

document = []

for paragraph in content("p"):
	words = regex.findall(regex, fix_unicode(paragraph.text))
	document.extend(words)

bigrams = zip(document, document[1:])
transitions = defaultdict(list)
for prev, current in bigrams:
	 transitions[prev].append(current)

def generate_using_bigrams():
	current = "."
	result = []
	while True:
		next_word_candidates = transitions[current]
		current = random.choice(next_word_candidates)
		result.append(current)
		if current == ".": return " ".join(result)

trigrams = zip(document, document[1:], document[2:])
trigram_transitions = defaultdict(list)
starts = []

for prev, current, next in trigrams:
	if prev == ".":
		starts.append(current)

	trigram_transitions[(prev, current)].append(next)

def generate_using_trigrams():
	current = random.choice(starts)
	prev = "."
	result = [current]
	while True:
		next_word_candidates = trigram_transitions[(prev, current)]
		next_word = random.choice(next_word_candidates)

		prev, current = current, next_word
		result.append(current)

		if current == ".":
			return " ".join(result)