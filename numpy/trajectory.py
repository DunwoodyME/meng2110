# -*- coding: utf-8 -*-
"""
trajectory.py
    HPL Exercise 5.13: Plot the trajectory of a ball
    Daniel Thomas
    October 31, 2017
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy

def f_x(x, theta, v_0, y_0 = 0):
    ''' Calculates the height (y position) of a ball's trajectory
        x      Horizontal (x) position, or numpy array of x values [m]
        theta  Launch angle [radians]
        v_0:   Initial velocity [m/s] 
        y_0:   Initial height [m]   '''
    g = 9.8     # [m/s2]
    y = x * np.tan(theta) - (g * x**2)/(2 * v_0**2 * np.cos(theta)**2) + y_0
    return y

def plot_trajectory(x_max, theta, v_0):
    dx = x_max/50
    x = np.arange(0,x_max+dx/2,dx)
    y = f_x(x, theta, v_0)
    plt.plot(x,y)
    plt.show()

def ball_range(theta, v_0, y_0 = 0, x_max = 100):
    ''' Calculates the range of a ball -- x-position when it lands.
        Uses same parameters as f_x() 
        x_i:  Initial guess for maximum range [m]  '''
    x_min   = 0
    while True:
        x_i = x_min + (x_max - x_min)/2
        y_i = f_x(x_i, theta, v_0, y_0)
        if abs(y_i) < 0.00001: break
        elif   y_i  < 0:  x_max = x_i
        elif   y_i  > 0:  x_min = x_i
        #print('  x,y = [{0:.2f},{1:.2f},{2:.2f}], {3:.2f}'.format(x_min,x_i,x_max,y_i))
    return x_i    
    
def optimum_theta(v_0, y_0 = 0):
    t_min = np.radians(0)
    t_max = np.radians(90)
    x_opt = 0
    t_opt = 0
    for t_i in np.arange(t_min, t_max, (t_max-t_min)/50):
        sol   = scipy.optimize.root(f_x, 20, (t_i, v_0))
        x_i = sol.x[0]
        print('  At theta = {0:.1f}, x = {1:.2f} m'.format(np.degrees(t_i),x_i))
        if x_i > x_opt: 
            x_opt = x_i
            t_opt = t_i
    return t_opt
    

if __name__ == "__main__":
    theta = np.radians(30)
    v_0   = 15  # [m/s]
    x_max = ball_range(theta, 15)
    sol = scipy.optimize.root(f_x, 10, (theta,v_0))
    print(sol.x[0], x_max)
    plot_trajectory(sol.x[0], theta, v_0)
    print('\n  Optimum theta = {0:.2f}'.format(np.degrees(optimum_theta(v_0))))

