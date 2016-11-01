#
# Program 2.1: A bouncing ball (bouncing_ball.py)
# J Wang, Computational modeling and visualization with Python
#

import visual as vp     # get VPython modules for animation

# draw the ball at (0,5,0) and a thin floor at (0,-5,0)
ball = vp.sphere(pos=(0,5,0), radius=1, color=vp.color.yellow) # ball  
floor = vp.box(pos=(0,-5,0), length=8, height=0.2, width=4)    # floor 

h = 0.01            # time step size                        
v = 0.0             # initial velocity                      
while True:         # loop forever
    vp.rate(400)    # limit animation rate to 400 loops/sec 
    ball.pos.y = ball.pos.y + v*h       # update y position 
    if ball.pos.y > floor.pos.y + ball.radius:  
        v = v - 9.8*h       # above floor, update velocity  
    else:                               
        v = - v             # below floor, reverse velocity 
       
