from Shape import Shape


class Circle(Shape):



    def __init__(self,points , internal = True ,  center_first = True):
        """
        constructor - got 2 Points and built  Circle
        :param points: tuple of Points
        :param internal: only for rectangle ..
        :param center_first: if the first point is the center or the second point is the center
        """
        if (center_first):
            self.center = points[0]
            self.radius = self.center.distance(points[1])
        else:
            self.center = points[1]
            self.radius = self.center.distance(points[0])


    def is_inside(self, p):
        """
        :param p: a Point
        :return: if this point is inside this circle
        """
        return (self.center.distance(p) <= self.radius)

    def is_right(self, p):
        """
        :param p: a Point
        :return: if the rectangle is right abut the gender of this point
        """
        if(self.is_inside(p)):
            return (p.gender == 1)
        else:
            return (p.gender == -1)
