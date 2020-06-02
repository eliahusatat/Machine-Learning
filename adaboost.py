from Point import Point
from Rectangle import Rectangle
import doctest
import itertools
import numpy as np
import random
import datetime
from H import H
import math

def rectangle_rate_error(rectangle , points):
    """
    :param rectangle:  Rectangle
    :param points: list of Point
    :return:  the sum of weights of all the points he is not right abut them
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
    >>> print(rectangle_rate_error(r1 , points))
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
    >>> print(rectangle_rate_error(r1 , points))
    2.0
    """
    rate = 0
    for p in points:
        if (rectangle.is_right(p) == False):
            rate += p.weight
            if(p.weight == 0):
                print("the w is : {}".format(p.weight))

    return rate


def best_rectangle(points):
    """
    :param points: list of points
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
    >>> r =  Rectangle((p1,Point(4, 6,1)))
    >>> ans = best_rectangle(points)
    >>> print(r == ans)
    True
    """
    best = Rectangle((points[0],points[1]))
    best_rate = rectangle_rate_error(best , points)
    for p in itertools.combinations(points, 2):
        temp = Rectangle(p)
        temp_rate = rectangle_rate_error(temp,points)
        if(temp_rate < best_rate):
            best = temp
            best_rate = temp_rate
    """
    for p in itertools.combinations(points, 3):
        temp = Rectangle(p)
        temp_rate = rectangle_rate_error(temp,points)
        if(temp_rate < best_rate):
            best = temp
            best_rate = temp_rate
    for p in itertools.combinations(points, 4):
        temp = Rectangle(p)
        temp_rate = rectangle_rate_error(temp, points)
        if (temp_rate < best_rate):
            best = temp
            best_rate = temp_rate
    """
    return best


def adaboost(points,r):
    w = np.longdouble(1/(len(points)))
    for p in points:
        p.weight = w
    at = np.longdouble(0.5)
    Hs = []
    As = []
    for i in range(0,r):
        sum = 0
        ht = best_rectangle(points)
        Hs.append(ht)
        et = rectangle_rate_error(ht , points)
        #if(et == 0):
        #print("the et:{} ".format(et))
        at = 0.5*(np.log((1 - et)/et))
        #print("at : {}".format(at))
        As.append(at)
        for p in points:
            if(ht.is_right(p)):
                p.weight = p.weight *(  math.e ** (at))
            else:
                p.weight = p.weight *(  math.e ** (-at))
            sum += p.weight
        for p in points:
            p.weight = p.weight/sum
    ans = H(Hs , As , r)
    for p in points:
        p.weight = 1
    return ans



def run(points , r , times):
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
            ans = adaboost(learn, i)
            rate = 0
            for p in test:
                #print(ans.is_right(p))
                if ans.is_right(p):
                    rate += 1
            #print("the success : {}".format((rate / len(test) * 100)))
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

    run(points , 8 , 100)












