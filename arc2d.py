import math
import numpy as np

def generate_circle(centre, r):
        theta = np.linspace(0, 2*np.pi, 100)
        x_circle = r*np.cos(theta) + centre.x
        y_circle = r*np.sin(theta) + centre.y
        return x_circle, y_circle

def generate_arc(centre, r, theta_initial, theta_final):
        while theta_initial > theta_final:
            theta_final += 2*np.pi
        theta = np.linspace(theta_initial, theta_final, 100)
        x_arc = r*np.cos(theta) + centre.x
        y_arc = r*np.sin(theta) + centre.y
        return x_arc, y_arc

def generate_line_segment(point1, point2):
        x = np.linspace(point1.x, point2.x, 100)
        y = np.linspace(point1.y, point2.y, 100)
        return x,y

def generate_line_full(point1, point2, extension_length = 3):
    # 计算延长后的起点坐标
    extended_start_x = point1.x - (point2.x - point1.x) / np.linalg.norm([point2.x - point1.x, point2.y - point1.y]) * extension_length
    extended_start_y = point1.y - (point2.y - point1.y) / np.linalg.norm([point2.x - point1.x, point2.y - point1.y]) * extension_length
    # 计算延长后的终点坐标
    extended_end_x = point2.x + (point2.x - point1.x) / np.linalg.norm([point2.x - point1.x, point2.y - point1.y]) * extension_length
    extended_end_y = point2.y + (point2.y - point1.y) / np.linalg.norm([point2.x - point1.x, point2.y - point1.y]) * extension_length
    # 生成延长后的线段
    x = np.linspace(extended_start_x, extended_end_x, 100)
    y = np.linspace(extended_start_y, extended_end_y, 100)
    return x, y


class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        
class Circle:
    def __init__(self, point: Point, r):
        self.centre = Point
        self.radius = r
        self.points = generate_circle(point, r)

class Arc(Circle): # did not inherit any thing yet
    def __init__(self, point: Point, r, theta_initial, theta_final):
        self.centre = Point
        self.radius = r
        self.points = generate_arc(point, r,theta_initial,theta_final)
        #this is in regular coordinate, not in L,k(that requires an additional theta of incline which is hard to deal with...)

def find_mindistance(set1, set2):
    #set1 / set2 are in form of (Xs, Ys)
    best_points = None
    shortest_dist = np.inf
    for i in range(len(set1[0])):
        for j in range(len(set2[0])):
            point1 = Point(set1[0][i],set1[1][i])
            point2 = Point(set2[0][j],set2[1][j])
            if point1.distance(point2) < shortest_dist:
                best_points = (point1, point2)
                shortest_dist = point1.distance(point2)
    return best_points

class Line_Segment():
    def __init__(self, point1: Point, point2: Point): #direct slope is not possible, since there could be 0
        self.points = generate_line_segment(point1, point2)
    
class Line():
    def __init__(self, point1: Point, point2: Point): #direct slope is not possible, since there could be 0
        self.points = generate_line_full(point1, point2)