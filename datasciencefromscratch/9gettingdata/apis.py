# JSON API
import json
serialized = """{ "title" : "Data Science Book",
				"author" : "Joel Grus",
				"publicationYear" : 2014,
				"topics" : [ "data", "science", "data science"] }"""

# parse the JSON to create a Python dict
deserialized = json.loads(serialized)
if "data science" in deserialized["topics"]:
	print(deserialized)

# using an unauthenticated API
import requests
endpoint = "https://api.github.com/users/hjfender/repos"

repos = json.loads(requests.get(endpoint).text)

from dateutil.parser import parse

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(dAttributeError.weekday() for date in dates)

last_5_repositories = sorted(repos, key=lambda r: r["created_at"], reverse=True)[:5]

last_5_languages = [repo["language"] for repo in last_5_repositories]