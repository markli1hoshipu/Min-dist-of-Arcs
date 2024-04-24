import numpy as np
import matplotlib.pyplot as plt
import random
import arc2d

random.seed(16)

#16 is a good seed

fig, ax = plt.subplots()

#randomly generate 2 circles, here WLOG let the centres be symmetrical and on x-axis
centre_shift_x = random.uniform(0.5,5.5)
centre1 = arc2d.Point(centre_shift_x,0);    centre2 = arc2d.Point(-centre_shift_x,0)
radius1 = random.uniform(0.5,10.5);         radius2 = random.uniform(0.5,10.5)
circle1 = arc2d.Circle(centre1,radius1);    circle2 = arc2d.Circle(centre2,radius2)

# select arc region 
'''
theta1_i = random.uniform(0,2*np.pi);                   theta2_i = random.uniform(0,2*np.pi)
theta1_f = random.uniform(0,2*np.pi);                   theta2_f = random.uniform(0,2*np.pi)
''' 
#control the arcs a bit
theta1_i = random.uniform(0,2*np.pi);                   theta2_i = random.uniform(0,2*np.pi)
theta1_f = random.uniform(theta1_i,theta1_i+0.5*np.pi);                   theta2_f = random.uniform(theta2_i,theta2_i+0.5*np.pi)
arc1 = arc2d.Arc(centre1,radius1,theta1_i,theta1_f);   arc2 = arc2d.Arc(centre2,radius2,theta2_i, theta2_f)

#find shortest
locate_set = arc2d.find_mindistance(arc1.points, arc2.points)
short_line = arc2d.Line_Segment(locate_set[0], locate_set[1])
long_line = arc2d.Line(locate_set[0], locate_set[1])

#graph the following 

#graph the 2 centres

ax.scatter(centre2.x, centre2.y, color='red', linewidth=2, label='O1')
ax.scatter(centre1.x, centre1.y, color='blue', linewidth=2, label='O2')

ax.plot(circle2.points[0],circle2.points[1],color='red', linewidth=1)
ax.plot(circle1.points[0],circle1.points[1],color='blue', linewidth=1)

ax.plot(arc2.points[0],arc2.points[1],color='purple', linewidth=3)
ax.plot(arc1.points[0],arc1.points[1],color='purple', linewidth=3)

ax.plot(short_line.points[0],short_line.points[1],color='green', linewidth=2)
ax.plot(long_line.points[0],long_line.points[1],color='black', linewidth=0.5)

ax.legend()
ax.set_title('shortested distance(green) of 2 arcs(purple)')


plt.axis('equal')  
plt.grid(True)     
plt.show()
