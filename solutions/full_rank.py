# -*- coding: utf-8 -*-
"""
Extract a gzipped file and print its contents.

Created on Tue Feb  9 12:30:45 2016

@author: yoav@yoavram.com
"""
from functools import reduce
import operator

import numpy as np
import matplotlib.pyplot as plt


def is_rank_full(M):
	return M.shape[0] == np.linalg.matrix_rank(M)

def create_random_matrix(n=2):
	return np.random.randint(0, 2, (n, n))

def full_rank_probability(n, reps):
	matrices = (create_random_matrix(n) for _ in range(reps))
	full_ranks = map(is_rank_full, matrices)
	return reduce(operator.add, full_ranks) / reps

if __name__ == '__main__':
	print(full_rank_probability(2, 100))
	