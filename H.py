




class H():
    def __init__(self, ht, at, r):
        self.ht = ht
        self.at = at
        self.r = r

    def sing(self , p):
        sum = 0
        for i in range(0 , self.r):
            if(self.ht[i].is_inside(p)):
                sum += self.at[i]
            else: sum += -self.at[i]
        if(sum >= 0): return 1
        else: return -1

    def is_right(self, p):
        if(self.sing(p) == p.gender): return True
        else: return False
