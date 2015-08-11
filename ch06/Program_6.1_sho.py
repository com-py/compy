#
# Program 6.1: Simple harmonic oscillator (sho.py)
# J Wang, Computational modeling and visualization with Python
#

import visual as vp

ball = vp.sphere(pos=(-2,-2,0), radius=1, color=vp.color.green) # ball
wall = vp.box(pos=(-4,-2,0), length=.2, height=4, width=4)      # wall
floor = vp.box(pos=(0,-3.1,0), length=8, height=0.2, width=4)   # floor 
spring = vp.helix(pos=wall.pos, thickness=0.1, radius=0.5)      # spring 

h, v = 0.1, 0.0                         # step size, initial velocity  
while True:
    vp.rate(50)
    ball.pos.x = ball.pos.x + v*h       
    v = v - ball.pos.x*h                # Euler-Cromer method 
    spring.length = ball.pos.x + 3      # stretch spring (offset by 3) 
       
