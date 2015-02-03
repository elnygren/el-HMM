#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Viterbi is defined by the recursive formula:
w(z) = p(x_n | z_n) * max( w_{z-1}*p(z_n | z_{n-1}) )

This implementation is built as a loop from z_0 to z_n. It is a (slightly) modified version of
http://en.wikipedia.org/wiki/Viterbi_algorithm

'''

def viterbi(x, states, start_P, trans_P, emission_P):    
    V = [{}]
    path = {}
 
    # Init base case
    for y in states:
        # w(z_1) = p(z_1) * p(x_1 | z_1)
        V[0][y] = start_P[y] * emission_P[y][x[0]]
        path[y] = [y]
 
    
    # w(z) = p(x_n | z_n) * max( w_{z-1}, p(z_n | z_{n-1}) )
    for t in range(1, len(x)):
        V.append({})
        newpath = {}
        
        for y in states:
            # max( w(z_{n-1}*p(z_n|z_{n-1}) )
            (prob, state) = max((V[t-1][y0] * trans_P[y0][y] * emission_P[y][x[t]], y0) for y0 in states)
            
            V[t][y] = prob
            newpath[y] = path[state] + [y]
 
        path = newpath
               
    if len(x) != 1:
        n = t
    else:
        n = 0

    # w(z_n), last iteration as we have reached n
    (prob, state) = max((V[n][y], y) for y in states)
    return (prob, path[state])

