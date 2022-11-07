from datetime import datetime, timedelta
from collections import defaultdict, OrderedDict, deque

users = [{'name': 'Vlad', 'birthday': datetime(year=1989, month=11, day= 6)},
         {'name': 'Irina', 'birthday': datetime(year=1986, month=11, day= 12)},
         {'name': 'Tetiana', 'birthday': datetime(year=1992, month=11, day= 7)},
         {'name': 'Evgeniy', 'birthday': datetime(year=1993, month=11, day= 11)},
         {'name': 'Marina', 'birthday': datetime(year=1995, month=11, day= 13)},
         {'name': 'Peter', 'birthday': datetime(year=1986, month=11, day= 8)},
         {'name': 'Andrew', 'birthday': datetime(year=1989, month=11, day= 9)},
         {'name': 'Christina', 'birthday': datetime(year=1989, month=11, day= 10)}]

current_day = datetime(year=2022, month=11, day=7 )

def sort_day_2():
    name_of_days = {
    0 : 'Monday',
    1 : 'Tuesday',
    2 : 'Wednesday',
    3 : 'Thursday', 
    4 : 'Friday',
    5 : 'Saturday',
    6 : 'Sunday'   
    }
    deque_dict = deque(name_of_days)
    deque_dict.rotate(-current_day.weekday()-1)
    return {i: name_of_days[i] for i in deque_dict}

def len_week():
    if current_day.weekday() == 6:
        len_of_week = timedelta(days=5) 
    elif current_day.weekday() == 5:
        len_of_week = timedelta(days=6)
    else:
        len_of_week = timedelta(days=7)
    return len_of_week


def get_birthday_per_week(users):
    birthday_list = defaultdict(list)
    for user in users:
        this_year_day = datetime(year=current_day.year, month=user.get('birthday').month, day=user.get('birthday').day)
        if current_day < this_year_day <= current_day + len_week():
            if this_year_day.weekday() in (5,6):
                birthday_list['Monday'].append(user.get('name'))
            else: 
                birthday_list[this_year_day.strftime('%A')].append(user.get('name'))
    name_days = sort_day_2()
    for day in name_days:
        if birthday_list[name_days[day]]:
            print(f'{name_days[day]} : {", ".join(birthday_list[name_days[day]])}')


get_birthday_per_week(users)
