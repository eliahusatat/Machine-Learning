import doctest
from Point import Point
from Rectangle import Rectangle


class H():
    def __init__(self, ht, at, r , shape ="rectangle"):
        self.ht = ht
        self.at = at
        self.r = r
        self.shape = shape

    def sing(self , p):
        """
        :param p: a Point
        :return: if the point is male or female (1 ,-1) according to H
        >>> p = Point(3, 2 ,-1)
        >>> p1 = Point(4, 5 ,-1)
        >>> r1 = Rectangle((p,p1))
        >>> p = Point(3, 2 ,-1)
        >>> p1 = Point(4, 5 ,-1)
        >>> r2 = Rectangle((p,p1))
        >>> p = Point(3, 2 ,-1)
        >>> p1 = Point(4, 5 ,-1)
        >>> r3 = Rectangle((p,p1))
        >>> p = Point(3, 2 ,-1)
        >>> p1 = Point(4, 5 ,-1)
        >>> r4 = Rectangle((p,p1))
        >>> ht = [r1,r2,r3,r4]
        >>> at = [1,-2,3,-4]
        >>> test = H(ht,at,4)
        >>> print(test.sing(Point(3,3,-1)))
        -1
        >>> p = Point(1, 1 ,-1)
        >>> p1 = Point(4, 4 ,-1)
        >>> r1 = Rectangle((p,p1))
        >>> p = Point(2, 2 ,-1)
        >>> p1 = Point(5, 5 ,-1)
        >>> r2 = Rectangle((p,p1))
        >>> p = Point(3, 3 ,-1)
        >>> p1 = Point(6, 6 ,-1)
        >>> r3 = Rectangle((p,p1))
        >>> p = Point(4, 4 ,-1)
        >>> p1 = Point(7, 7 ,-1)
        >>> r4 = Rectangle((p,p1))
        >>> ht = [r1,r2,r3,r4]
        >>> at = [1,-2,3,-4]
        >>> test = H(ht,at,4)
        >>> print(test.sing(Point(5,5,-1)))
        -1
        """
        sum = 0
        if(self.shape == "rectangle"): # for rectangle
            for i in range(0, self.r):

                if (self.ht[i].internal):
                    if (self.ht[i].is_inside(p)):
                        sum += self.at[i]
                    else:
                        sum -= self.at[i]
                else:
                    if (self.ht[i].is_inside(p)):
                        sum -= self.at[i]
                    else:
                        sum += self.at[i]
        else:                             # for circle
            for i in range(0, self.r):
                if (self.ht[i].is_inside(p)):
                    sum += self.at[i]
                else:
                    sum -= self.at[i]
        if(sum >= 0): return 1
        else: return -1

    def is_right(self, p):
        if(self.sing(p) == p.gender): return True
        else: return False


    def __str__(self):
        print("the H is: \n ht = {}\n at = {}\n r = {}".format(self.ht ,self.at ,self.r))


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))