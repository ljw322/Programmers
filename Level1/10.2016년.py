import datetime

def solution(a, b):
    answer = ''
    dayList = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    day = datetime.date(2016, a, b).weekday()
    answer = dayList[day]
    
    return answer