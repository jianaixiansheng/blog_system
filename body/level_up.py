import datetime

from .models import UserInfo,levelsystem


class level_up():
    def __init__(self):
        head_info = levelsystem.objects.select_related('userid').get(userid=12)

    def Countdown_calculation(self):
        '''
        当前时间到明天凌晨3点的时间差
        :return:
        计时器中所使用的时间戳
        '''

        # 获取当前时间
        now_time = datetime.datetime.now()

        # 获取明天的日期
        new_day = now_time.date().day+1
        new_month = now_time.month
        new_years = now_time.year

        # 得到明天3点的值
        next_time = datetime.datetime.strptime(
            str(new_years) + "-" + str(new_month) + "-" + str(new_day) + " 03:00:00", "%Y-%m-%d %H:%M:%S")

        # 时间差
        time_difference = (next_time - now_time).total_seconds()

        return time_difference




level_up().Countdown_calculation()