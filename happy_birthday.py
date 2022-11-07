from datetime import datetime, timedelta
from collections import defaultdict, deque
import calendar

users = [{'name': 'Vlad', 'birthday': datetime(year=1989, month=11, day= 6)},
         {'name': 'Irina', 'birthday': datetime(year=1986, month=11, day= 12)},
         {'name': 'Tetiana', 'birthday': datetime(year=1992, month=11, day= 7)},
         {'name': 'Evgeniy', 'birthday': datetime(year=1993, month=11, day= 11)},
         {'name': 'Marina', 'birthday': datetime(year=1995, month=11, day= 13)},
         {'name': 'Peter', 'birthday': datetime(year=1986, month=11, day= 8)},
         {'name': 'Andrew', 'birthday': datetime(year=1989, month=11, day= 9)},
         {'name': 'Christina', 'birthday': datetime(year=1989, month=11, day= 10)}]

name_of_days = {
    0 : 'Monday',
    1 : 'Tuesday',
    2 : 'Wednesday',
    3 : 'Thursday', 
    4 : 'Friday',
    5 : 'Saturday',
    6 : 'Sunday'   
    }

current_day = datetime(year=2022, month=11, day=5)

d_name_of_days = deque(name_of_days)
d_name_of_days.rotate(-current_day.day-1)
name_of_days = {i : name_of_days[i] for i in d_name_of_days}

   
def get_birthday_per_week(users):
    birthday_list = defaultdict(list)
    for user in users:
        if user['birthday'].day == 29 and user['birthday'].month == 2 and  not calendar.isleap(current_day.year):
            user['birthday'] = datetime(year = current_day.year, month = 3, day = 1)
        else:
            user['birthday'] = datetime(year = current_day.year, month = user['birthday'].month, day = user['birthday'].day)
        if user['birthday'] > current_day and user['birthday'] < current_day + timedelta(days=7): 
            if user['birthday'].weekday() in (5, 6):
                if user['birthday'].weekday() == 5 and current_day.weekday() == 6:
                    pass
                else:
                    birthday_list['Monday'].append(user['name'])
            else: 
                birthday_list[name_of_days[user['birthday'].weekday()]].append(user['name'])
    for name in name_of_days:
        if birthday_list[name_of_days[name]]: 
            print(f'{name_of_days[name]} : {", ".join(birthday_list[name_of_days[name]])}') 


get_birthday_per_week(users)