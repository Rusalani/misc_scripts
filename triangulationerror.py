from scipy.optimize import minimize
from scipy import stats
import numpy as np
import math
def get_corrections(h1,h2,h3,theta1,theta2,theta3):
    '''

    :param h1:
    :param h2:
    :param h3:
    :param theta1:
    :param theta2:
    :param theta3:
    :return:
    '''
    assert isinstance(h1,int) or isinstance(h1,float)
    assert isinstance(h2, int)or isinstance(h2,float)
    assert isinstance(h3, int)or isinstance(h3,float)
    assert isinstance(theta1, float)or isinstance(theta1, int)
    assert isinstance(theta2, float)or isinstance(theta2, int)
    assert isinstance(theta3, float)or isinstance(theta3, int)
    def func(x):
        return pow(x[0],2) + pow(x[1],2)+pow(x[2],2)

    eq_cons = {'type': 'eq', 'fun': lambda x: h1 + x[3] * math.tan(theta1 + x[0]) - x[4]}
    eq_cons2 = {'type': 'eq', 'fun': lambda x: h2 + x[3] * math.tan(theta2 + x[1]) - x[4]}
    eq_cons3 = {'type': 'eq', 'fun': lambda x: h3 + x[3] * math.tan(theta3 + x[2]) - x[4]}
    res = minimize(func,[0,0,0,1,1],method='SLSQP',constraints=[eq_cons,eq_cons2,eq_cons3])
    return (res.x[0],res.x[1],res.x[2])
def get_corrections2(h1,h2,h3,theta1,theta2,theta3):
    '''

    :param h1:
    :param h2:
    :param h3:
    :param theta1:
    :param theta2:
    :param theta3:
    :return:
    '''
    assert isinstance(h1,int) or isinstance(h1,float)
    assert isinstance(h2, int)or isinstance(h2,float)
    assert isinstance(h3, int)or isinstance(h3,float)
    assert isinstance(theta1, float)or isinstance(theta1, int)
    assert isinstance(theta2, float)or isinstance(theta2, int)
    assert isinstance(theta3, float)or isinstance(theta3, int)
    def func(x):
        return pow(x[0],2) + pow(x[1],2)+pow(x[2],2)

    eq_cons = {'type':'eq','fun': lambda x: h1+x[3]*math.tan(theta1+x[0])-x[4]}
    eq_cons2 = {'type': 'eq', 'fun': lambda x: h2 + x[3]*math.tan(theta2 + x[1]) - x[4]}
    eq_cons3 = {'type': 'eq', 'fun': lambda x: h3 + x[3]*math.tan(theta3 + x[2]) - x[4]}
    res = minimize(func,[0,0,0,1,1],method='SLSQP',constraints=[eq_cons,eq_cons2,eq_cons3])
    return (res.x[3],res.x[4])

def get_stats_x(h1,h2,h3,phi1,phi2,phi3,sigma):
    '''

    :param h1:
    :param h2:
    :param h3:
    :param phi1:
    :param phi2:
    :param phi3:
    :param sigma:
    :return:
    '''
    assert isinstance(h1,int) or isinstance(h1,float)
    assert isinstance(h2, int)or isinstance(h2,float)
    assert isinstance(h3, int)or isinstance(h3,float)
    assert isinstance(phi1, float)or isinstance(phi1, int)
    assert isinstance(phi2, float)or isinstance(phi2, int)
    assert isinstance(phi3, float) or isinstance(phi3, int)
    assert isinstance(sigma,int)or isinstance(sigma,float)
    assert sigma >=0

    x=[]
    for i in range(30):
        error1, error2,error3 = stats.norm(0,sigma).rvs(3)
        x.append(get_corrections2(h1,h2,h3,phi1+error1,phi2+error2,phi3+error3)[0])
    return (np.mean(x),np.var(x))

def get_stats_z(h1,h2,h3,phi1,phi2,phi3,sigma):
    '''

    :param h1:
    :param h2:
    :param h3:
    :param phi1:
    :param phi2:
    :param phi3:
    :param sigma:
    :return:
    '''
    assert isinstance(h1,int) or isinstance(h1,float)
    assert isinstance(h2, int)or isinstance(h2,float)
    assert isinstance(h3, int)or isinstance(h3,float)
    assert isinstance(phi1, float)or isinstance(phi1, int)
    assert isinstance(phi2, float)or isinstance(phi2, int)
    assert isinstance(phi3, float) or isinstance(phi3, int)
    assert isinstance(sigma,int)or isinstance(sigma,float)
    assert sigma >=0

    x=[]
    for i in range(30):
        error1, error2,error3 = stats.norm(0,sigma).rvs(3)
        x.append(get_corrections2(h1,h2,h3,phi1+error1,phi2+error2,phi3+error3)[1])
    return (np.mean(x),np.var(x))
'''
h1,h2,h3=1,2,3
theta1,theta2,theta3=(0.16739555984988044, 0.08966865249116186, -2.6660268543053645e-06)
phi1,phi2,phi3 = get_corrections(h1,h2,h3,theta1,theta2,theta3)

print(get_stats_x(h1,h2,h3,phi1,phi2,phi3,.001))
print(get_stats_z(h1,h2,h3,phi1,phi2,phi3,.001))
'''