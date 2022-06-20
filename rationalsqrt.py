import math


def gcd(top, bottom):
    m = math.gcd(top, bottom)
    return Rational(int(top / m), int(bottom / m))
class Rational(object):
    def __init__(self, a, b):
        """
        :a: integer
        :b: integer
        """
        assert isinstance(a, int)
        assert isinstance(b, int)
        self._a = a
        self._b = b



    def __repr__(self):

        if self._a % self._b == 0 :
            return str(int(self._a / self._b))
        return  str(('\''+str(self._a)+'/' +str(self._b)+'\''))

    def __eq__(self, other):
        return (self._a == other._a) and (self._b == other._b)
    def __lt__(self, other):
        return self._a*1.0/self._b < other._a*1.0/other._b
    def __gt__(self, other):
        return self._a*1.0/self._b > other._a*1.0/other._b

    def __add__(self, other):
        if isinstance(other, int):
            return Rational(self._a + (other * self._b), self._b)
        temp = self._b
        temp1 = self._a * other._b
        temp2 = self._b * other._b

        tempa = other._a * temp
        tempb = other._b * temp

        return gcd(temp1 + tempa,temp2)

    def __sub__(self, other):
        if isinstance(other, int):
            other = other * self._b
            return gcd(self._a-other, self._b)

        temp = self._b
        temp1 = self._a * other._b
        temp2 = self._b * other._b

        tempa = other._a * temp
        tempb = other._b * temp

        return gcd(temp1 - tempa, temp2 )

    def __truediv__(self, other):
        if isinstance(other, int):
            return gcd(self._a , self._b * other)

        return  gcd(self._a*other._b,self._b*other._a)
    def __mul__(self, other):
        if isinstance(other,int):
            return gcd(self._a * other , self._b)
        return gcd(self._a*other._a,self._b*other._b)

    def __radd__(self, other):
        return gcd(self._a+(other*self._b),self._b)
    def __rsub__(self, other):
        other = other * self._b
        return gcd(other- self._a,self._b)
    def __rtruediv__(self, other):

        return gcd(self._b*other,self._a)
    def __rmul__(self, other):
        return gcd(self._a * other , self._b)

    def __float__(self):
        return self._a*1.0/self._b
    def __int__(self):
        return math.trunc(self._a/self._b)
    def __neg__(self):
        return Rational(-self._a,self._b)




def square_root_rational(x,abs_tol=Rational(1,1000)):
    '''

    :param x:
    :param abs_tol:
    :return:
    '''
    assert isinstance(x,Rational)
    assert isinstance(abs_tol,Rational)
    low =0
    high = max(1.0,x._a)
    t=(high+low)/2


    while abs(t**2-float(x)) >= float(abs_tol):
        if t ** 2 < float(x):
            low = t
        else:
            high = t
        t = (high + low)/2

    t = math.trunc(t*10/float(abs_tol))

    #print(10/float(abs_tol))
    return Rational(t,int(10/float(abs_tol)))



r = Rational(4,3)
r2 = Rational(3,4)
#print(square_root_rational(r2))





