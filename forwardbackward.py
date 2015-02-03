#!/usr/bin/python
# -*- coding: utf-8 -*-

def forward(x, states, a_0, a, e, end_st):
    fwd = []
    f_prev = {}
    # forward part of the algorithm
    for i, x_i in enumerate(x):
        f_curr = {}
        for st in states:
            if i == 0:
                # base case for the forward part
                prev_f_sum = a_0[st]
            else:
                prev_f_sum = sum(f_prev[k]*a[k][st] for k in states)
 
            f_curr[st] = e[st][x_i] * prev_f_sum
 
        fwd.append(f_curr)
        f_prev = f_curr
 
    p_fwd = sum(f_curr[k]*a[k][end_st] for k in states)
    return (fwd, p_fwd)

def backward(x, states, a_0, a, e, end_st):
    bkw = []
    b_prev = {}
    # backward part of the algorithm
    for i, x_i_plus in enumerate(reversed(x[1:]+(None,))):
        b_curr = {}
        for st in states:
            if i == 0:
                # base case for backward part
                b_curr[st] = a[st][end_st]
            else:
                b_curr[st] = sum(a[st][l]*e[l][x_i_plus]*b_prev[l] for l in states)
 
        bkw.insert(0,b_curr)
        b_prev = b_curr
 
    p_bkw = sum(a_0[l] * e[l][x[0]] * b_curr[l] for l in states)
    return (bkw, p_bkw)


def fwd_bkw(x, states, a_0, a, e, end_st):
    L = len(x)
 
    fwd, p_fwd = forward(x, states, a_0, a, e, end_st)
    bkw, p_bkw = backward(x, states, a_0, a, e, end_st)
 
    # merging the two parts
    posterior = []
    for i in range(L):
        posterior.append({st: fwd[i][st]*bkw[i][st]/p_fwd for st in states})
 
    # return fwd, bkw, posterior
    return posterior

