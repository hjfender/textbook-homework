from model import knn_classify

# each entry is ([longitude, latitude], favorite_language)

cities = [([-122.3,  47.53], "Python"),	# Seattle
		  ([ -96.85, 32.85], "Java"),	# Austin
		  ([ -89.33, 43.13], "R")]		# Madison

# key is language, value is pair (longitudes, latitudes)
plots = { "Java" : ([], []), "Python" : ([], []), "R" : ([], []) }

# we want each language to have a different marker and color
markers = { "Java" : "o", "Python" : "s", "R" : "^" }
colors	= { "Java" : "r", "Python" : "b", "R" : "g" }

for (longitude, latitude), language in cities:
	plots[language][0].append(longitude)
	plots[language][1].append(latitude)

# create a scatter series for each language
#for language, (x, y) in plots.iteritems():
#	plt.scatter(x, y, color=colors[language], marker=markers[language],
#						label=language, zorder=10)

#plot_state_borders(plt)		# pretend we have a function that does this

#plt.legend(loc=0)			# let matplotlib choose the location
#plt.axis([-130,-60,20,55])	# set the axes

#plt.title("Favorite Programming Languages")
#plt.show()

# try several different values for k
for k in [1, 3, 5, 7]:
	num_correct = 0

	for city in cities:
		location, actual_language = city
		other_cities = [other_city
						for other_city in cities
						if other_city != city]
		predicted_language = knn_classify(k, other_cities, location)

		if predicted_language == actual_language:
			num_correct += 1

	print(k, "neighbor[s]:", num_correct, "correct out of", len(cities))

# 1 neighbor[s]: 40 correct out of 75
# 3 neighbor[s]: 44 correct out of 75
# 5 neighbor[s]: 41 correct out of 75
# 7 neighbor[s]: 35 correct out of 75

# classify an entire grid worth of points
plots = { "Java" : ([],[]), "Python" : ([], []), "R" : ([], []) }

k = 1 # or 3, or 5, or...

for longitude in range(-130, -60):
	for latitude in range(20, 55):
		predicted_language = knn_classify(k, cities, [longitude, latitude])
		plots[predicted_language][0].append(longitude)
		plots[predicted_language][1].append(latitude)

