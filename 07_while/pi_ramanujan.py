'''
pi_ramanujan.py
	Ex 7-3: Estimate of pi using Ramanujan series.
	Daniel Thomas
	Sept 24, 2017
'''

from math import pi, factorial, sqrt

def estimate_pi():
    ''' Calculates an estimate for pi using Srinivasa Ramanujan's infinite series.
        Returns the estimate for pi and number of iterations of the series.'''
    k   = 0
    pie = 3
    sum = 0
    while abs(pi - pie) > 1e-17:
        sum+= factorial(4*k)*(1103 + 26390*k)/(factorial(k)**4 * 396**(4*k))
        pie = 1 / ((2*sqrt(2)/9801)*sum)
        k  += 1
    return pie, k

pi_est, iter = estimate_pi()
print('\n  pi = %0.15f after %d iterations\n' % (pi_est, iter))