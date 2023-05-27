#!/usr/bin/env python

"""monte_carlo_biased_coins.py: a quick monte carlo program to figure out probability of getting over N heads from a list of differently weighted biased coins. 
This is the monte carlo solution to Poisson binomial distributions because I'm too lazy to figure out the analytic solution.

https://en.wikipedia.org/wiki/Poisson_binomial_distribution
"""

import random

def get_at_least_n_heads(probabilities:list[float], min_heads: int)-> bool:
  heads = 0
  for probability in probabilities:
    heads += int(probability > random.random()) # random.random() returns a float between 0 and 1 at uniform probability
  return heads >= min_heads

def monte_carlo_at_least_n_heads (probabilities:list[float], min_heads: int, num_runs: int)-> float:
  if min_heads < 0 or min_heads > len(probabilities):
    raise Exception("min_heads not compatible with number of coins flipped")
  success = 0.0
  for i in range(num_runs):
    if get_at_least_n_heads(probabilities, min_heads):
      success += 1.0
  return success/num_runs
