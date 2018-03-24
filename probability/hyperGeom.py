#!/usr/bin/python3

import math

def nCr(n, r):
	if r < 0 or r > n:
		return 0
	f = math.factorial
	return f(n) // f(r) // f(n-r)


def HyperGeom(k, K, n, N):
	return nCr(K, k) * nCr(N-K, n-k) / nCr(N,n)

def atLeast_k(k, K, n, N):
	return sum(HyperGeom(x, K, n, N) for x in range(k,K+1))

def atLeastOne(K, n, N):
	return atLeast_k(1,K,n,N)

def numDrawsForProb(p, K, N):
	it = (atLeastOne(K, x, N) for x in range(1,N+1))
	p_calc = 0
	draws = 0
	while p_calc < p:
		draws += 1
		p_calc = next(it)
	return draws

def allRarityProbs(p, N):
	return [numDrawsForProb(p,x,N) for x in range(1,5)]

