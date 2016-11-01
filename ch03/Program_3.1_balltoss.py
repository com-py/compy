#
# Program 3.1: Ball toss (balltoss.py)
# J Wang, Computational modeling and visualization with Python
#

import visual as vp                 # get VPython modules for animation

vp.display(background=(.2,.5,1))    # make scene, ball, floor, and path 
ball  = vp.sphere(pos=(-4,-4,0), radius=1, color=vp.color.yellow)
floor = vp.box(pos=(0,-5,0), length=12, height=0.2, width=4)
path  = vp.points(pos=ball.pos, size=4)     # use make_trail in newer VP
h, g, vx, vy = 0.01, 9.8, 4.0, 9.8          # $\Delta t$, g, and initial velocity
while True:
    vp.rate(400)                            # limit animation rate
    ball.pos.x += vx*h                      # update position 
    ball.pos.y += vy*h     
    path.append(pos=ball.pos, retain=300)   # draw path, keep 300 pts 
    if ball.pos.y > floor.pos.y + ball.radius:  
          vy = vy - g*h                     # above floor, update vy
    else: vx, vy = - vx, - vy               # below floor, reverse vel.
