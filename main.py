#!/usr/bin/python
# -*- coding: utf-8 -*-

import Viterbi
import ForwardBackward
import HMM

print '---- Hidden Markov Model ---'
dna = {
	u"αββααββ": u"AAAHHHA",
	u"αααβααβ": u"HHAAHHH",
	u"βαααββ": u"AAAAHA",
	u"αββαααβα": u"AHAAAHAA"
}

states = (u'α', u'β')
observations = ('A', 'H', 'H', 'A', 'A')
 
start_probability = HMM.start_P(dna)
transition_probability = HMM.transition_P(dna, states)
emission_probability = HMM.emission_P(dna, states)

posteriors = ForwardBackward.forward_backward(
	observations,
	states,
   	start_probability,
   	transition_probability,
   	emission_probability
)
 
viterbi = Viterbi.viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)

print 'Probabilities'
print start_probability
print transition_probability
print emission_probability

print 'Posteriors:'
for line in posteriors:
	print u'α: ' + str("%.4f" % line[u'α']) + u'   ' + u'β: ' + str("%.4f" % line[u'β'])

print 'Viterbi:'
for item in viterbi[1]:
	print item,