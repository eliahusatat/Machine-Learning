from Point import Point
import doctest


class Rectangle():

    def __init__(self,points):
        if(len(points) == 2):
            self.big_x = max(points[0].temperature, points[1].temperature)
            self.small_x = min(points[0].temperature, points[1].temperature)
            self.big_y = max(points[0].pulse, points[1].pulse)
            self.small_y = min(points[0].pulse, points[1].pulse)
        if(len(points) == 3):
            self.big_x = max(points[0].temperature, points[1].temperature, points[2].temperature)
            self.small_x = min(points[0].temperature, points[1].temperature, points[2].temperature)
            self.big_y = max(points[0].pulse, points[1].pulse, points[2].pulse)
            self.small_y = min(points[0].pulse, points[1].pulse, points[2].pulse)
        if(len(points) == 4):
            self.big_x = max(points[0].temperature, points[1].temperature, points[2].temperature, points[3].temperature)
            self.small_x = min(points[0].temperature, points[1].temperature, points[2].temperature, points[3].temperature)
            self.big_y = max(points[0].pulse, points[1].pulse, points[2].pulse, points[3].pulse)
            self.small_y = min(points[0].pulse, points[1].pulse, points[2].pulse, points[3].pulse)


    """
    def __init__(self, tp1, tp2, tp3 = None , tp4 = None):
        if(tp3 == None):
            big_temperature = max(tp1.temperature, tp2.temperature)
            small_temperature = min(tp1.temperature, tp2.temperature)
            big_pulse = max(tp1.pulse, tp2.pulse)
            small_pulse = min(tp1.pulse, tp2.pulse)
        else:
            if(tp4 == None):
                big_temperature = max(tp1.temperature, tp2.temperature, tp3.temperature)
                small_temperature = min(tp1.temperature, tp2.temperature, tp3.temperature)
                big_pulse = max(tp1.pulse, tp2.pulse, tp3.pulse)
                small_pulse = min(tp1.pulse, tp2.pulse, tp3.pulse)
            else:
                big_temperature = max(tp1.temperature, tp2.temperature, tp3.temperature, tp4.temperature)
                small_temperature = min(tp1.temperature, tp2.temperature, tp3.temperature, tp4.temperature)
                big_pulse = max(tp1.pulse, tp2.pulse, tp3.pulse, tp4.pulse)
                small_pulse = min(tp1.pulse, tp2.pulse, tp3.pulse, tp4.pulse)
        self.p1 = Point(small_temperature, big_pulse)
        self.p2 = Point(small_temperature, small_pulse)
        self.p3 = Point(big_temperature, big_pulse)
        self.p4 = Point(big_temperature, small_pulse)
    """

    def is_inside(self,p):
        """

        :param p:
        :return:
        >>> p1 = Point(1,1 -1)
        >>> p2 = Point(4, 4 ,1)
        >>> p3 = Point(3, 3 ,1)
        >>> r =  Rectangle((p1,p2))
        >>> print(r.is_inside(p3))
        True
        >>> print(r.is_inside(Point(5, 5)))
        False
        >>> print(r.is_inside(Point(3, 5)))
        False
        >>> print(r.is_inside(Point(5, 3)))
        False
        >>> print(r.is_inside(Point(1, 2)))
        True
        """
        return (p.temperature >= self.small_x)and(p.temperature <= self.big_x)and(p.pulse >= self.small_y)and(p.pulse <= self.big_y)

    def is_right(self, p):
        """
        :param p:
        :return:
        >>> p1 = Point(1,1 -1)
        >>> p2 = Point(4, 4 ,1)
        >>> p3 = Point(3, 3 ,1)
        >>> r =  Rectangle((p1,p2))
        >>> print(r.is_right(p3))
        True
        >>> p4 = Point(3, 3 ,-1)
        >>> print(r.is_right(p4))
        False
        >>> p5 = Point(5, 5 ,-1)
        >>> r =  Rectangle((p1,p2))
        >>> print(r.is_right(p5))
        True
        >>> p6 = Point(5, 5 ,1)
        >>> r =  Rectangle((p1,p2))
        >>> print(r.is_right(p6))
        False
        """
        if(self.is_inside(p)):
            return (p.gender == 1)
        else:
            return (p.gender == -1)


    def __str__(self):
        return 'the rectangle is :\n {}\n , {}\n , {}\n , {}'.format(self.big_x , self.small_x ,  self.small_x , self.small_y)

    def __eq__(self, other):
        return (self.big_x == other.big_x)and(self.small_x == other.small_x)and(self.small_x == other.small_x)and(self.small_y == other.small_y)


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
