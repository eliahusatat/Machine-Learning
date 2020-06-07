from Point import Point
import doctest


class Rectangle():

    def __init__(self,points , internal = True):
        """
        constructor - got 2,3,4 Points and built  Rectangle
        :param points: tuple of Points
        >>> p = Point(3, 2 ,-1)
        >>> p1 = Point(4, 5 ,-1)
        >>> r = Rectangle((p,p1))
        >>> print(r.big_x)
        4
        >>> print(r.small_x)
        3
        >>> print(r.big_y)
        5
        >>> print(r.small_y)
        2
        """
        if(internal):
            self.internal = True
        else:
            self.internal = False
        if((not(len(points) == 2))and(not (len(points) == 3))and(not (len(points) == 4))): raise Exception('only 2,3,4 is point is alow!')
        else:
            if (len(points) == 2):
                self.big_x = max(points[0].temperature, points[1].temperature)
                self.small_x = min(points[0].temperature, points[1].temperature)
                self.big_y = max(points[0].pulse, points[1].pulse)
                self.small_y = min(points[0].pulse, points[1].pulse)
            if (len(points) == 3):
                self.big_x = max(points[0].temperature, points[1].temperature, points[2].temperature)
                self.small_x = min(points[0].temperature, points[1].temperature, points[2].temperature)
                self.big_y = max(points[0].pulse, points[1].pulse, points[2].pulse)
                self.small_y = min(points[0].pulse, points[1].pulse, points[2].pulse)
            if (len(points) == 4):
                self.big_x = max(points[0].temperature, points[1].temperature, points[2].temperature,
                                 points[3].temperature)
                self.small_x = min(points[0].temperature, points[1].temperature, points[2].temperature,
                                   points[3].temperature)
                self.big_y = max(points[0].pulse, points[1].pulse, points[2].pulse, points[3].pulse)
                self.small_y = min(points[0].pulse, points[1].pulse, points[2].pulse, points[3].pulse)



    def is_inside(self,p):
        """
        :param p: a Point
        :return: if this point is inside this rectangle
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
        >>> p1 = Point(56,90 -1)
        >>> p2 = Point(70, 100 ,1)
        >>> r =  Rectangle((p1,p2))
        >>> print(r.is_inside(Point(62, 95)))
        True
        >>> print(r.is_inside(Point(3, 95)))
        False
        >>> print(r.is_inside(Point(65, 3)))
        False
        >>> print(r.is_inside(Point(69, 90)))
        True
        """
        return (p.temperature >= self.small_x) and (p.temperature <= self.big_x) and (p.pulse >= self.small_y) and ( p.pulse <= self.big_y)




    def is_right(self, p):
        """
        :param p: a Point
        :return: if the rectangle is right abut the gender of this point
        if the point is inside the rectangle - according the rectangle - its  male (1)
        if the point is outside the rectangle - according the rectangle - its female (1)
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
        >>> p1 = Point(56,90 -1)
        >>> p2 = Point(70, 100 ,1)
        >>> r =  Rectangle((p1,p2))
        >>> print(r.is_right(Point(62, 95,1)))
        True
        >>> print(r.is_right(Point(3, 95 ,1)))
        False
        >>> print(r.is_right(Point(65, 3 ,-1)))
        True
        >>> print(r.is_right(Point(69, 90, -1)))
        False
        """
        if(self.internal):
            if (self.is_inside(p)):
                return (p.gender == 1)
            else:
                return (p.gender == -1)
        else:
            if (self.is_inside(p)):
                return (p.gender == -1)
            else:
                return (p.gender == 1)




    def __str__(self):
        return 'the rectangle is :\n {}\n , {}\n , {}\n , {}\n , is internal: {}'.format(self.big_x , self.small_x ,  self.big_y , self.small_y,self.internal)

    def __eq__(self, other):
        """
        :param other: Rectangle
        :return: if they equals
        >>> r1 = Rectangle((Point(1,1,1),Point(4,4,1)))
        >>> r2 = Rectangle((Point(2,2,1),Point(3,3,1)))
        >>> print(r1 == r2)
        False
        >>> r1 = Rectangle((Point(1,1,1),Point(4,4,1)))
        >>> r2 = Rectangle((Point(1,1,1),Point(4,4,1)))
        >>> print(r1 == r2)
        True
        >>> r1 = Rectangle((Point(1,1,-1),Point(4,4,-1)))
        >>> r2 = Rectangle((Point(1,1,1),Point(4,4,1)))
        >>> print(r1 == r2)
        True
        """
        return (self.big_x == other.big_x)and(self.small_x == other.small_x)and(self.big_y == other.big_y)and(self.small_y == other.small_y)and(self.internal == other.internal)


if __name__ == '__main__':
    """
    """
    r1 = Rectangle((Point(1, 1, -1), Point(4, 4, -1)))
    r2 = Rectangle((Point(1, 1, 1), Point(4, 4, 1)))
    print(r1 == r2)
    print(r1)
    print(r2)

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))


