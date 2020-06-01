import doctest


class Point():
    """
    def __init__(self, line):
        arr = line.split()
        self.temperature  = float(arr[0])
        if(arr[1]=="1"):
            self.gender = int(arr[1])
        else:
            self.gender = -1
        self.pulse = float(arr[2])
        self.weight = 0


    def __init__(self, point):
        self.temperature = point.temperature
        self.gender = point.gender
        self.pulse = point.pulse
        self.weight = 0
    
    def __init__(self, temperature ,pulse):
        self.temperature  = temperature
        self.gender = 0
        self.pulse = pulse
        self.weight = 0
    """

    def __init__(self, point ,pulse = None ,gender = None):
        """
        :param point:
        :param pulse:
        :param gender:
        >>> p = Point(3, 2 ,-1)
        >>> p1 = Point(p)
        >>> print(p1 == p)
        True
        >>> p2 = Point("3    -1    2")
        >>> print(p2 == p)
        True
        """
        if(pulse == None): # if its got only one param
            if isinstance(point ,str): # if its line = string from file
                arr = point.split()
                self.temperature = float(arr[0])
                if (arr[1] == "1"):
                    self.gender = int(arr[1])
                else:
                    self.gender = -1
                self.pulse = float(arr[2])
                self.weight = 1
            else: # if its point = copy constructor
                self.temperature = point.temperature
                self.gender = point.gender
                self.pulse = point.pulse
                self.weight = 1
        else: # got  temperature and pulse - and built the point
            self.temperature = point
            self.gender = gender
            self.pulse = pulse
            self.weight = 1



    def __str__(self):
        return 'the point is : {} , {} , {} '.format(self.temperature  ,  self.pulse , self.gender)

    def __eq__(self, other):
        return (self.temperature == other.temperature)and(self.gender == other.gender)and(self.pulse == other.pulse)and(self.weight == other.weight)


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))