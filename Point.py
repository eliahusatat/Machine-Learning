"""
Eliahu Satat - 204395644
Daniel Abergel - 315660712
"""
import doctest
import numpy as np
import math

class Point():

    def __init__(self, point ,pulse = None ,gender = None):
        """
        A constructor if its got one param (Point or string)
        used as copy constructor or string constructor
        if its got 3 param - regular constructor
        :param point: Point or string or int ( = temperature)
        :param pulse: int ( = pulse)
        :param gender: int ( = gender)
        checked!
        >>> p = Point(3, 2 ,-1)
        >>> p1 = Point(p)
        >>> print(p1 == p)
        True
        >>> p2 = Point("3    -1    2")
        >>> print(p2 == p)
        True
        """
        if(pulse == None): # if its got only one param
            if isinstance(point ,str): # if its line = string from file string constructor
                arr = point.split()
                self.temperature = float(arr[0])
                if (arr[1] == "1"):
                    self.gender = int(arr[1])
                else:
                    self.gender = -1
                self.pulse = float(arr[2])
                #self.weight = np.longdouble(1)
                self.weight = 1.0
            else: # if its point = copy constructor
                self.temperature = point.temperature
                self.gender = point.gender
                self.pulse = point.pulse
                #self.weight = np.longdouble(1)
                self.weight = 1.0

        else: # got  temperature and pulse - and built the point
            self.temperature = point
            self.gender = gender
            self.pulse = pulse
            #self.weight = np.longdouble(1)
            self.weight = 1.0


    def distance(self , p):
        return math.sqrt((self.temperature - p.temperature)**2 + (self.pulse - p.pulse)**2)


    def __str__(self):
        return 'the point is : {} , {} , {} '.format(self.temperature  ,  self.pulse , self.gender)

    def __eq__(self, other):
        return (self.temperature == other.temperature)and(self.gender == other.gender)and(self.pulse == other.pulse)and(self.weight == other.weight)


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

