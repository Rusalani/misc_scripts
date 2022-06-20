import calendar
def number_of_days(year, month):
    '''
    returns number of days given month and year
    '''
    assert isinstance(year,int)
    assert isinstance(month,int)
    assert 1 <= month <= 12
    assert year > 0
    return calendar.monthrange(year, month)[1]


def number_of_leap_years(year1,year2):
    '''
    returns number of leap years inclusive given two years
    '''
    assert isinstance(year1,int)
    assert isinstance(year2,int)
    assert year1 <= year2
    assert year1 > 0
    assert year2 > 0
    return calendar.leapdays(year1,year2+1)
            

def get_day_of_week(year,month,day):
    '''
    returns day of the week for given year month and day
    '''
    assert isinstance(year,int)
    assert isinstance(month,int)
    assert 1 <= month <= 12
    assert isinstance(day,int)
    assert 1 <= day <= number_of_days(year,month) 
    assert year > 0
    x=calendar.weekday(year,month,day)
    if x==0:
        return 'Monday'
    if x==1:
        return 'Tuesday'
    if x==2:
        return 'Wednesday'
    if x==3:
        return 'Thursday'
    if x==4:
        return 'Friday'
    if x==5:
        return 'Saturday'
    if x==6:
        return 'Sunday'
    
#print(number_of_leap_years(2000,2004))

