
import math
class Polynomial(object):
    def __init__(self,dic):
        '''

        :param dict:
        :return:
        '''
        self._dic = dic
        assert isinstance(dic,dict)
        for x in dic.keys():
            assert isinstance(x,int)
            assert x >=0
            assert isinstance(dic[x],int)
    def __neg__(self):
        temp = Polynomial(self._dic.copy())
        for x in self._dic.keys():
            temp._dic[x] = int(-self._dic[x])
        return temp
    def __repr__(self):
        string=''
        drop = False
        for x in self._dic.keys():
            if self._dic[x] !=0:
                if x==0:
                    string += str(self._dic[x]) + ' + '
                elif x==1:
                    if self._dic[x] == 1:
                        string +=  'x + '
                    else:
                        string += str(self._dic[x]) + ' x + '
                else:
                    string += str(self._dic[x]) + ' x^('+str(x)  + ') + '
            else:
                drop = True

        if drop:
            return '\''+string[:-3].strip()+'\''
        return string[:-3].strip()

    def __mul__(self, other):
        temp = Polynomial({})
        if isinstance(other,int):
            for x in self._dic.keys():
                temp._dic[x]=int(self._dic[x]*other)
            return temp
        else:
            if isinstance(other, Polynomial):
                for x in other._dic.keys():
                    for y in self._dic.keys():
                        if x+y in temp._dic:
                            temp._dic[x + y] = self._dic[y] * other._dic[x] + temp._dic[x + y]
                        else:
                            temp._dic[x+y] = self._dic[y] * other._dic[x]

                dic2 = {}
                for i in sorted(temp._dic):
                    dic2[i] = temp._dic[i]
                temp._dic = dic2
                return temp

    def __rmul__(self, other):
        temp = Polynomial(self._dic.copy())
        if isinstance(other, float) or isinstance(other, int):
            for x in self._dic.keys():
                temp._dic[x] = int(self._dic[x] * other)
        return temp

    def __add__(self, other):
        temp = Polynomial(self._dic.copy())
        if isinstance(other,Polynomial):
            for x in other._dic.keys():
                if x in temp._dic.keys():
                    temp._dic[x] = int(temp._dic[x] + other._dic[x])
                else:
                    temp._dic[x] = int(other._dic[x])

            dic2={}
            for i in sorted(temp._dic):
                dic2[i] = temp._dic[i]
            temp._dic = dic2
            return temp
        else:
            if 0 in  temp._dic:
                temp._dic[0] = int(temp._dic[0] + other)
            else:
                temp._dic[0] = int(other)
            dic2 = {}
            for i in sorted(temp._dic):
                dic2[i] = temp._dic[i]
            temp._dic = dic2
            return  temp
    def __radd__(self, other):
        temp = Polynomial(self._dic.copy())
        if 0 in temp._dic:
            temp._dic[0] = int(temp._dic[0] + other)
        else:
            temp._dic[0] = int(other)
        dic2 = {}
        for i in sorted(temp._dic):
            dic2[i] = temp._dic[i]
        temp._dic = dic2
        return temp

    def __sub__(self, other):
        temp = Polynomial(self._dic.copy())
        if isinstance(other, Polynomial):
            for x in other._dic.keys():
                if x in temp._dic.keys():
                    temp._dic[x] = int(temp._dic[x] - other._dic[x])
                else:
                    temp._dic[x] = -int(other._dic[x])

            dic2 = {}
            for i in sorted(temp._dic):
                dic2[i] = temp._dic[i]
            while dic2[max(dic2.keys())] ==0 and max(dic2.keys())!=0:
                dic2.pop(max(dic2.keys()))
            temp._dic = dic2
            return temp
        else:
            if 0 in temp._dic:
                temp._dic[0] = int(temp._dic[0] - other)
            else:
                temp._dic[0] = -int(other)
            dic2 = {}
            for i in sorted(temp._dic):
                dic2[i] = temp._dic[i]
            temp._dic = dic2
            return temp
    def __rsub__(self, other):
        temp2 = -self
        temp = Polynomial(temp2._dic.copy())
        if 0 in temp._dic:
            temp._dic[0] = int(temp._dic[0] + other)
        else:
            temp._dic[0] = -int(other)
        dic2 = {}
        for i in sorted(temp._dic):
            dic2[i] = temp._dic[i]
        temp._dic = dic2
        return temp

    def subs(self,x):
        summ=0
        for i in self._dic.keys():
            summ+= pow(x,i) * self._dic[i]
        return summ

    def __eq__(self, other):
        if isinstance(other,int):
            for i in self._dic.keys():
                if i != other:
                    if self._dic[i] !=0:
                        return False
                else:
                    if self._dic[i] !=other:
                        return False
            return True
        for i in self._dic.keys():
            if i not in other._dic.keys():
                return False
            if self._dic[i] != other._dic[i]:
                return  False

        return True

    def degree(self):

        t= max(self._dic.keys())

        return t
    def lead(self):
        return self._dic[self.degree()]


    def __truediv__(self, other):
        #p/q
        assert other != 0
        if isinstance(other,int):

            dick = {}
            for x in self._dic.keys():
                dick[x] = int(self._dic[x]/other)
            return Polynomial(dick)
        if   (len(other._dic)==1 and other._dic[0]!=0):
            dick = {}
            for x in self._dic.keys():
                dick[x] = int(self._dic[x] / other._dic[0])
            return Polynomial(dick)


        if len(self._dic) == 1 and len(other._dic)==1:
            #print(Polynomial({self.degree()-other.degree():int(self.lead()/other.lead())}))
            return Polynomial({self.degree()-other.degree():int(self.lead()/other.lead())})
        q=Polynomial({0:0})
        r=Polynomial(self._dic.copy())
        while r!= 0 and r.degree() >= other.degree() :
            t= Polynomial({r.degree():r.lead()})/Polynomial({other.degree():other.lead()})
            q=q+t
            r=r-t*other
        if r==0:
            return q
        else:
            raise NotImplementedError



#p=Polynomial({1:2,3:4})
#q=Polynomial({0:8,1:2,2:8,4:4})

'''
p=Polynomial({0:8,1:2,3:4})
q=Polynomial({0:8,1:2,2:8,4:4})
print(repr(p))
print(p*3)
print(3*p)
print(p+q)
print(p*4 + 5 - 3*p - 1)
print(type(p-p))
print(p*q)
print(p.subs(10))
print((p-p)==0)
print(p==q)
p=Polynomial({0:8,1:0,3:4})
print(repr(p))
p = Polynomial({2:1,0:-1})
q = Polynomial({1:1,0:-1})
print(p/q)
print(p  / Polynomial({1:1,0:-3}))
'''
p = Polynomial({2:2,0:-2})
q = Polynomial({0:2})
q2=2
print(p/q2)
print(p/q)

