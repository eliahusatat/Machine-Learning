"""
Eliahu Satat - 204395644
Daniel Abergel - 315660712
"""





from Point import Point
from Rectangle import Rectangle
from Circle import Circle
import doctest
import itertools
import numpy as np
import random
import datetime
from H import H
import math

def shape_rate_error(shape ,points):

    """
    :param shape:  Rectangle or Circle
    :param points: list of Point
    :return:  the sum of weights of all the points the shape is not right abut them
    >>> points = []
    >>> p1 = Point(1 , 1 ,1)
    >>> points.append(p1)
    >>> p2 = Point(4, 4,1)
    >>> points.append(p2)
    >>> p3 = Point(5, 2,1)
    >>> points.append(p3)
    >>> p4 = Point(1, 2,-1)
    >>> points.append(p4)
    >>> p5 = Point(2, 2,-1)
    >>> points.append(p5)
    >>> p6 = Point(3, 2,1)
    >>> points.append(p6)
    >>> p7 = Point(3, 6,1)
    >>> points.append(p7)
    >>> r1 = Rectangle((p1,p2))
    >>> print(shape_rate_error(r1 , points))
    4.0
    >>> points = []
    >>> p1 = Point(1 , 1 ,1)
    >>> points.append(p1)
    >>> p2 = Point(4, 4,1)
    >>> points.append(p2)
    >>> p3 = Point(5, 2,-1)
    >>> points.append(p3)
    >>> p4 = Point(1, 2,1)
    >>> points.append(p4)
    >>> p5 = Point(2, 2,1)
    >>> points.append(p5)
    >>> p6 = Point(3, 2,-1)
    >>> points.append(p6)
    >>> p7 = Point(3, 6,1)
    >>> points.append(p7)
    >>> r1 = Rectangle((p1,p2))
    >>> print(shape_rate_error(r1 , points))
    2.0
    >>> points = []
    >>> p1 = Point(1 , 1 ,1)
    >>> points.append(p1)
    >>> p2 = Point(4, 4,1)
    >>> points.append(p2)
    >>> p3 = Point(5, 2,-1)
    >>> points.append(p3)
    >>> p4 = Point(1, 2,1)
    >>> points.append(p4)
    >>> p5 = Point(2, 2,1)
    >>> points.append(p5)
    >>> p6 = Point(3, 2,-1)
    >>> points.append(p6)
    >>> p7 = Point(3, 6,1)
    >>> points.append(p7)
    >>> r =  Rectangle((p1,Point(4, 6,1)))
    >>> print(shape_rate_error(r , points))
    1.0
    """
    rate = 0
    for p in points:
        if (shape.is_right(p) == False):
            rate += p.weight
            if(p.weight == 0):
                print("the w is : {}".format(p.weight))
    if(rate == 0):
        return 0.00000000001 # In order to be division by zero
    else:
        return rate


def best_shape(points , shape = "rectangle"):
    """
    :param points: list of points
    :param shape:  Rectangle or Circle
    :return: the Rectangle with the lower rectangle_rate_error
    >>> points = []
    >>> p1 = Point(1 , 1 ,1)
    >>> points.append(p1)
    >>> p2 = Point(4, 4,1)
    >>> points.append(p2)
    >>> p3 = Point(5, 2,-1)
    >>> points.append(p3)
    >>> p4 = Point(1, 2,1)
    >>> points.append(p4)
    >>> p5 = Point(2, 2,1)
    >>> points.append(p5)
    >>> p6 = Point(3, 2,-1)
    >>> points.append(p6)
    >>> p7 = Point(3, 6,1)
    >>> points.append(p7)
    >>> p8 = Point(4, 6, 1)
    >>> points.append(p8)
    >>> r =  Rectangle((Point(3, 2,1),Point(5, 2,1)),False)
    >>> ans = best_shape(points)
    >>> print(r == ans)
    True
    >>> print(shape_rate_error(ans,points))
    1e-11
    """
    if(shape == "rectangle"):
        best = Rectangle((points[0], points[1]))
        best_rate = shape_rate_error(best, points)
        for p in itertools.combinations(points, 2):
            temp = Rectangle(p, True)
            temp_rate = shape_rate_error(temp, points)
            if (temp_rate < best_rate):
                best = temp
                best_rate = temp_rate

        for p in itertools.combinations(points, 2):
            temp = Rectangle(p, False)
            temp_rate = shape_rate_error(temp, points)
            if (temp_rate < best_rate):
                best = temp
                best_rate = temp_rate
    else:
        best = Circle((points[0], points[1]))
        best_rate = shape_rate_error(best, points)
        for p in itertools.combinations(points, 2):
            temp = Circle(p, True , True)
            temp_rate = shape_rate_error(temp, points)
            if (temp_rate < best_rate):
                best = temp
                best_rate = temp_rate

        for p in itertools.combinations(points, 2):
            temp = Circle(p, True , False)
            temp_rate = shape_rate_error(temp, points)
            if (temp_rate < best_rate):
                best = temp
                best_rate = temp_rate
    return best


def adaboost(points,r , shape = "rectangle"):
    """
    the adaboost algorithm
    :param points: list of point
    :param r:  int
    :param shape:  Rectangle or Circle
    :return: tuple (list of rectangle , list of alpha , r)
    """
    n = len(points)
    w = 1 / n
    for p in points:
        p.weight = w
    at = 0.5
    Hs = []
    As = []
    for i in range(0,r):
        sum = 0
        ht = best_shape(points , shape)
        Hs.append(ht)
        et = shape_rate_error(ht, points)
        num = (1 - et)/et
        at = 0.5*(np.log(num))
        As.append(at)
        for p in points:
            if(ht.is_right(p) == False):
                p.weight = p.weight *(math.e ** (at))
            else:
                p.weight = p.weight *(math.e ** (-at))
            sum += p.weight
        for p in points:
            p.weight = p.weight/sum
    ans = H(Hs , As , r ,shape)
    for p in points:
        p.weight = 1
    return ans



def run(points , r , times, shape = "rectangle"):
    """
    :param points: list of Points
    :param r: int
    :param times: int
    :param shape:
    :return: run adaboost for each i from(1,r) (times) times with the shape
    """
    start = datetime.datetime.now()
    for i in range(1, r+1):
        multi_sum = 0
        for j in range(times):
            learn = []
            test = []
            for p in points:
                rand = random.randint(0, 1)
                if (len(learn) >= 65):
                    test.append(p)
                else:
                    if (len(test) >= 65):
                        learn.append(p)
                    else:
                        if (rand == 0):
                            test.append(p)
                        else:
                            learn.append(p)
            ans = adaboost(learn, i , shape)
            rate = 0
            for p in learn:
                if ans.is_right(p):
                    rate += 1
            multi_sum += (rate / len(test) * 100)
        multi_sum /= times
        print("the rate of success for {} is {} percent ".format(i, multi_sum))
    end = datetime.datetime.now()
    print("Total time for {} points and {} times, from 1 to {} is :{}".format(len(points), times , r , end - start))

if __name__ == '__main__':


    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))


    f = open("HC_Body_Temperature.txt", "r")
    points = []
    for x in f:
        points.append(Point(x))

    run(points , 8 , 100 , "rectanle")
    """
    
rectangle on test:
the rate of success for 1 is 50.46153846153847 percent 
the rate of success for 2 is 51.10769230769231 percent 
the rate of success for 3 is 52.67692307692309 percent 
the rate of success for 4 is 51.75384615384617 percent 
the rate of success for 5 is 54.061538461538454 percent 
the rate of success for 6 is 53.69230769230769 percent 
the rate of success for 7 is 53.87692307692308 percent 
the rate of success for 8 is 52.86153846153847 percent 
Total time for 130 points and 100 times, from 1 to 8 is :0:04:53.256524


rectangle on train:
the rate of success for 1 is 69.78461538461538 percent 
the rate of success for 2 is 68.30769230769232 percent 
the rate of success for 3 is 76.12307692307694 percent 
the rate of success for 4 is 74.73846153846154 percent 
the rate of success for 5 is 80.00000000000001 percent 
the rate of success for 6 is 77.50769230769231 percent 
the rate of success for 7 is 82.18461538461536 percent 
the rate of success for 8 is 81.5076923076923 percent 
Total time for 130 points and 100 times, from 1 to 8 is :0:04:58.633063

there is overfitting on rectangle !

circle on test:
the rate of success for 1 is 54.24615384615387 percent 
the rate of success for 2 is 54.18461538461539 percent 
the rate of success for 3 is 55.230769230769226 percent 
the rate of success for 4 is 55.75384615384616 percent 
the rate of success for 5 is 52.86153846153849 percent 
the rate of success for 6 is 53.076923076923094 percent 
the rate of success for 7 is 54.061538461538454 percent 
the rate of success for 8 is 54.18461538461539 percent 
Total time for 130 points and 100 times, from 1 to 8 is :0:09:09.288128


circle on train:
the rate of success for 1 is 69.87692307692309 percent 
the rate of success for 2 is 68.33846153846153 percent 
the rate of success for 3 is 71.66153846153844 percent 
the rate of success for 4 is 70.61538461538461 percent 
the rate of success for 5 is 73.01538461538462 percent 
the rate of success for 6 is 72.46153846153847 percent 
the rate of success for 7 is 76.64615384615385 percent 
the rate of success for 8 is 73.72307692307695 percent 
Total time for 130 points and 100 times, from 1 to 8 is :0:09:12.557027

there is overfitting on circle !
    """














