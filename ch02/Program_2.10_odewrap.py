#
# Program 2.10: {SciPy} ODE wrapper (odewrap.py)
# J Wang, Computational modeling and visualization with Python
#

from scipy.integrate import odeint      # SciPy integrator

def odewrapper(diffeq, y0, t, h):       # ode wrapper
    y = odeint(diffeq, y0, [t, t+h])
    return y[1]

Euler = RK2 = RK4 = RK45 = RK4n = RK45n = odewrapper    # alias
