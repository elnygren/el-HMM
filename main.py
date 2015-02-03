#!/usr/bin/python
# -*- coding: utf-8 -*-

import Viterbi
import forwardbackward
import HMM


dna = {
	u"αββααββ": u"AAAHHHA",
	u"αααβααβ": u"HHAAHHH",
	u"βαααββ": u"AAAAHA",
	u"αββαααβα": u"AHAAAHAA"
}

states = (u'α', u'β')
end_state = 'E'
 
observations = ('A', 'H', 'H', 'A', 'A')
 
# start_probability = {u'α': 0.67, u'β': 0.33}
# emission_probability = {
#    u'α' : {'A': 0.56, 'H': 0.44},
# 	u'β' : {'A': 0.64, 'H': 0.36},
# }


start_probability = HMM.start_P(dna)
transition_probability = {
   u'α' : {u'α': 0.52, u'β': 0.47, 'E': 0.01},
   u'β' : {u'α': 0.54, u'β': 0.45, 'E': 0.01},
   }
 
emission_probability = HMM.emission_P(dna, states)



fb = forwardbackward.fwd_bkw(observations,
		states,
       	start_probability,
       	transition_probability,
       	emission_probability,
       	end_state)
 
for line in fb:
	print line
    # print('\n'.join(map(str, line)))

# viterbi = Viterbi.viterbi(observations,
#                    states,
#                    start_probability,
#                    transition_probability,
#                    emission_probability)
# print viterbi