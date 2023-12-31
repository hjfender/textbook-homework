def map_reduce(inputs, mapper, reducer):
	"""runs MapReduce on the inputs using mapper and reducer"""
	collector = defaultdict(list)

	for input in inputs:
		for key, value in mapper(input):
			collector[key].append(value)

	return [output
			for key, values in collector.iteritems()
			for output in reducer(key, values)]

def reduce_value_using(aggregation_fn, key, values):
	"""reduces a key-values pair by applying aggregation_fn to the values"""
	yield (key, aggregation_fn(values))

def values_reducer(aggregation_fn):
	"""turns a function (values -> output) into a reducer
	that maps (key, values) -> (key, output)"""
	return partial(reduce_values_using, aggregation_fn)

sum_reducer = values_reducer(sum)
max_reducer = values_reducer(max)
min_reducer = values_reducer(min)
count_distinct_reducer = values_reducer(lambda values: len(set(values)))