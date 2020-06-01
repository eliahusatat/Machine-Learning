from Point import Point
from Rectangle import Rectangle
import doctest
import itertools
import numpy as np
import random
import datetime
from H import H

def rectangle_rate_error(rectangle , points):
    """
    :param rectangle:  Rectangle
    :param points: list of Point
    :return: the number of point that in the Rectangle
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
    4
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
    2
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
    :return: the Rectangle with the best rectangle_rate
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
    best = None
    best_rate = len(points)
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
        if(et == 0):
            print("the et:{} ".format(et))
        at = 0.5*(np.log((1 - et)/et))
        print("at : {}".format(at))
        As.append(at)
        for p in points:
            if(ht.is_right(p)):
                p.weight = pow(p.weight , at)
            else:
                p.weight = pow(p.weight , -at)
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
                if (len(learn) >= 35):
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




    """
    f = open("HC_Body_Temperature.txt", "r")
    points = []


    for x in f:
        points.append(Point(x))
    for i in range(1,9):
        multi_sum = 0
        for j in range(100):
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
            sum = 0

            ans = adaboost(learn, i)
            for p in test:
                if (ans.is_right(p)):
                    sum += 1
            rate = sum / len(test) * 100
            multi_sum += rate
            # print("the rate for {} is {} precent ".format(1 ,rate))
        multi_sum = multi_sum / 100
        print("the rate of success for {} is {} percent ".format(i, multi_sum))

    

    start = datetime.datetime.now()
    #for i in range(1,9):

    #for i in range(1,9):

    #end = datetime.datetime.now()
    #print("Total time for {} points  :{}".format(len(points), end - start))

    
    
    
    Total time for 130 points  :0:14:44.112061
    
the rate for 1 is 56.92307692307692 precent 
the rate for 2 is 56.92307692307692 precent 
the rate for 3 is 56.92307692307692 precent 
the rate for 4 is 56.92307692307692 precent 
the rate for 5 is 56.92307692307692 precent 
the rate for 6 is 56.92307692307692 precent 
the rate for 7 is 56.92307692307692 precent 
the rate for 8 is 56.92307692307692 precent 
Total time for 130 points  :0:14:55.424025
    
    
    
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
    
    r = 4
    for i in range(1,r+1):
        print(i)
    f = open("HC_Body_Temperature.txt", "r")
    points = []
    for x in f:
        points.append(Point(x))
    for pair in itertools.combinations(points, 4):
        print(*pair)
    
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
    
    points = []
    p1 = Point(1 , 1)
    p2 = Point(4, 4)
    p3 = Point(5, 2)
    points.append(p3)
    p4 = Point(1, 2)
    points.append(p3)
    p5 = Point(2, 2)
    points.append(p3)
    p6 = Point(3, 2)
    points.append(p3)
    p7 = Point(3, 6)
    points.append(p3)
    r1 = Rectangle(p1,p2)
    for p in points:
        print(p)
    print(rectangle_rate(r1 , points))
    

    f = open("HC_Body_Temperature.txt", "r")
    points = []
    for x in f:
        points.append(Point(x))
        print(Point(x))


    p1 = Point(1,1)
    p2 = Point(4, 4)
    p3 = Point(5, 2)
    r1 = Rectangle(p1,p2)
    r2 = Rectangle(p1, p2 ,p3)
    print(p1)
    print(p2)
    print(p3)
    print(r1)
    print(r2)
    """









