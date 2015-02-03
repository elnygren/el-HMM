#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Forward is defined by the recursive formula:
a(z_n) = p(x_n | z_n) * \sum a(z_{n-1}) * p(z_n | z_{n-1})

This implementation is built as a loop from z_last to z_n. It is a modified version of
http://en.wikipedia.org/wiki/Forward%E2%80%93backward_algorithm

'''
def forward(x, states, start_P, trans_P, emission_P):
    fwd = [] # stores saved results
    
    a_prev = {} #represents a_{n-1}
    for i, x_i in enumerate(x):
        a_curr = {}

        for st in states:
            if i == 0: 
                # \sum a(z_{n-1} * P(z_n | z_{n-1}), previous is the start
                z_curr = start_P[st]
            else: 
                # \sum a(z_{n-1} * P(z_n | z_{n-1})
                z_curr = sum(a_prev[k]*trans_P[k][st] for k in states)
 
            # P(x_n | z_n)
            a_curr[st] = emission_P[st][x_i] * z_curr
 
        fwd.append(a_curr) # save result
        a_prev = a_curr
 
    # a(z_n) * P(z_n is the ending state)
    # p_fwd = sum(a_curr[k]*trans_P[k][end_st] for k in states)

    p_fwd = sum(a_curr[k] for k in states)

    return (fwd, p_fwd)

'''
Backward is defined by the recursive formula:
b(z_n) = \sum b(z_{n+1}) p(x_{n+1}|x{n}) p(z_{n+1}|z_n)

This implementation is built as a loop from z_0 to z_n. It is a modified version of
http://en.wikipedia.org/wiki/Forward%E2%80%93backward_algorithm

'''

def backward(x, states, start_P, trans_P, emission_P):
    bkw = [] # stores saved results
    
    b_next = {} # represents b_{n+1}
    for i, x_i in enumerate(reversed(x[1:]+(None,))):
        b_curr = {}
        for st in states:
            if i == 0:
                #b(z_N) = 0
                b_curr[st] = 1
            else:
                # \sum b(z_{n+1}) p(x_{n+1}|x{n}) p(z_{n+1}|z_n)
                b_curr[st] = sum(b_next[k]*emission_P[k][x_i]*trans_P[st][k] for k in states)
 
        bkw.insert(0,b_curr) #save result
        b_next = b_curr
 
    # z_n is the start state
    p_bkw = sum(b_curr[k] * emission_P[k][x[0]] * start_P[k] for k in states)
    return (bkw, p_bkw)


'''
The forward-backward algorithm.
Returns posterior probabilities for each hidden states.
'''
def forward_backward(x, states, start_P, trans_P, emission_P):
    L = len(x)
 
    fwd, p_fwd = forward(x, states, start_P, trans_P, emission_P)
    bkw, p_bkw = backward(x, states, start_P, trans_P, emission_P)
 
    posterior = []
    for i in range(len(x)):
        
        # forward * backward / p(forward) 
        posterior.append({st: fwd[i][st]*bkw[i][st]/p_fwd for st in states})

        # forward * backward
        # posterior.append({st: fwd[i][st]*bkw[i][st] for st in states})
 
    return posterior

