import glob, re

# modify the path with wherever you've put the files
path = r"C:\spam\*\*"

data = []

# glob.glob returns every filename that matches the wildcarded path
for fn in glob.glob(path):
	is_spam = "ham" not in fn

	with open(fn, 'r') as file:
		for line in file:
			if line.startswith("Subject:"):
				# remove the leading "Subject: " and keep what's left
				subject = re.sub(r"^Subject: ", "", line).strip()
				data.append((subject, is_spam))

random.seed(0)	# just so you get the same answers as me
train_data, test_data = split_data(data, 0.75)

classifier = NaiveBayesclassifier()
classifier.train(train_data)

# triplets (subject, actual is_spam, predicted spam probability)
classified = [(subject, is_spam,classifier.classify(subject))
			  for subject, is_spam in test_data]

# assume that spam_probability > 0.5 corresponds to spam prediction
# and count the combinations of (actual is_spam, predicted is_spam)
count = Counter((is_spam, spam_probability > 0.5)
				for _, is_spam, spam_probability in classified)

# sort by spam_probability from smallest to largest
classified.sort(key=lambda row: row[2])

# the highest predicted spam probabilities among the non-spams
spammiest_hams = filter(lambda row: not row[1], classified)[-5:]

# the lowest predicted spam probabilities among the actual spams
hammiest_spams = filter(lambda row: row[1], classified)[:5]

def p_spam_given_word(word_prob):
	"""uses bayes's theorem to compute p(spam | message contains word)"""

	# word_prob is one of the triplets produced by word_probabilities
	word, prob_if_spam, prob_if_not_spam = word_prob
	return prob_if_spam / (prob_if_spam + prob_if_not_spam)

words = sorted(classifier.word_probs, key=p_spam_given_word)

spammiest_words = words[-5:]
hammiest_words = words[:5]

# stemmer functions
def drop_final_s(word):
	return re.sub("s$", "", word)