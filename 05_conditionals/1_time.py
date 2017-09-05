'''
1_time.py
	Ex 5.1: Calculates time since epoch
	Daniel Thomas
	Sept 4, 2017
'''

import time

epoch = time.time()
days  = epoch // (24*60*60)
hours = (epoch % (24*60*60)) // (60*60)
mins  = (epoch % (60*60)) // 60
secs  = (epoch % 60) // 1

print('\n  Number of seconds since epoch: %0.6f s' % epoch)
print('  This is: %d days, %d hours, %d min, %d sec' % (days, hours, mins, secs))