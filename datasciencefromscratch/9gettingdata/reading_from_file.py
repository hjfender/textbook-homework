import re

# 'r' means read-only
file_for_reading = open('reading_file.txt', 'r')

# 'w' is write - will destroy the file if it already exists!
file_for_writing = open('writing_file.txt', 'w')

# 'a' is append - for adding to the end of the file
file_for_appending = open('appending_file.txt', 'a')

# don't forget to close your files when you're done
file_for_writing.close()

# another way to use files without the close statement
with open(filename, 'r') as f:
	data = function_that_gets_data_from(f)

# at this point f has already been closed, so don't try to use it
process(data)

# iterate line by line reading style
starts_with_hash = 0

with open('input.txt', 'r') as f:
	for line in file:				# look at each line in the file
		if re.match("^#", line):	# use a regex to see if it starts with '#'
			starts_with_hash += 1	# if it does, add 1 to the count

def get_domain(email_address):
	"""split of '@' and return the last piece"""
	return email_address.lower().split("@")[-1]

with open('email_addresses.txt', 'r') as f:
	domain_counts = Counter(get_domain(line.strip())
							for line in f
							if "@" in line)