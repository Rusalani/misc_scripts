class Interval(object):
    def __init__(self,a,b):
        """
        :a: integer
        :b: integer
        """
        assert a<b
        assert isinstance(a,int)
        assert isinstance(b,int)
        self._a = a
        self._b = b
        
    def __repr__(self):
        return "Interval"+str((self._a,self._b))
    def __eq__(self,other):
        return (self._a <= other._a) and  (self._b >= other._b)
 
    def __lt__(self,other):
        return  self._a < other._a and self._b < other._b
    
    def __gt__(self,other):
        return self._a > other._a and self._b > other._b
     
    def __ge__(self,other):
  
        return self > other and other._b > self._a
    def __le__(self,other):
  
        return self < other and self._b > other._a


    def __add__(self,other):
        if self == other:
            return self
        if other == self:
            return other
        if self <= other:
            return Interval(self._a,other._b)
        if self >= other:
            return Interval(other._a,self._b)
        if self < other:
            return [self,other]
        if self > other:
            return [other,self]

        pass




