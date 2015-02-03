#!/usr/bin/python
# -*- coding: utf-8 -*-


states = (u'α', u'β')

'''
Helper used to calculate probability and add-1 smoothing.
'''

def __calculate_P__(k, n, smoothing=True):
	if not smoothing:
		return 1.0 * k / n
	else:
		return 1.0 * (k+1) / (n + len(states))

'''
Calculates the start values' probabilities'. 
Data should be in a dict 'hidden states': 'observations'

data = {
	 u"αββααββ": u"AAAHHHA"
}
'''

def start_P(data):
	start_vals = {}	

	# Count all start values
	for row in data:
		key = row[0]
		if key in start_vals:
			start_vals[key] = start_vals[key]+1
		else:
			start_vals[key] = 1

	# Probabilities
	total = sum(start_vals.values())
	for key in start_vals: 
		start_vals[key] = __calculate_P__(start_vals[key], total)
	
	return start_vals


'''
Calculates the emission probabilities. 
Data should be in a dict 'hidden states': 'observations'. (same length)

data = {
	 u"αββααββ": u"AAAHHHA"
}
'''
def emission_P(data, states):
	
	# Init count
	counts = {}
	for state in states: counts[state] = {}
	
	# Count all emissions
	for row in data:
		key = row
		val = data[key]

		for i in range(0, len(row)):
			observed = val[i]
			state = key[i]

			if observed in counts[state]:
				counts[state][observed] = counts[state][observed] + 1
			else:
				counts[state][observed] = 1

	# Calculate probabilities
	for count in counts:
		total = sum(counts[count].values())
		for observed in counts[count]:
			counts[count][observed] = __calculate_P__(counts[count][observed], total)

	return counts

'''
Calculates the transition probabilities. 
Data should be in a dict 'hidden states': 'observations'. (same length)

data = {
	 u"αββααββ": u"AAAHHHA"
}
'''
def transition_P(data, states):
	# Init count
	counts = {}
	for state in states: counts[state] = {}

	# Count pairs
	pairs = []
	for row in data:
		for i in range(0, len(row)-1):
			pairs.append( (row[i], row[i+1]) )

	# Count all transmissions from pairs
	for pair in pairs:
		first, second = pair[0], pair[1]

		if second in counts[first]:
			counts[first][second] = counts[first][second] + 1
		else:
			counts[first][second] = 1

	# Probabilities
	for count in counts:
		total = sum(counts[count].values())
		for observed in counts[count]:
			counts[count][observed] = __calculate_P__(counts[count][observed], total)

	return counts

# print start_P(dna)
# print emission_P(dna, states)
# print transition_P(dna, states)
