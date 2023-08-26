# @Time: 2023/8/25 23:35 45
# @Author: charlatans
# @Name: time_utils.py
# Path: common/src/main
# ProjectName: UniTasker
#   Il n'ya qu'un héroïsme au monde :
#       c'est de voir le monde tel qu'il est et de l'aimer.

import datetime
import time
import calendar


class TimeUtils:
    @staticmethod
    def get_current_date():
        """
        获取当前日期
        """
        return datetime.date.today()

    @staticmethod
    def get_current_datetime():
        """
        获取当前日期时间
        """
        return datetime.datetime.now()

    @staticmethod
    def get_current_time():
        """
        获取当前时间
        """
        return datetime.datetime.now().time()

    @staticmethod
    def parse_datetime(datetime_str, format_str="%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.strptime(datetime_str, format_str)

    @staticmethod
    def get_timestamp(milli_seconds = False):
        """
        时间戳
        """
        if milli_seconds:
            return int(time.time() * 1000)
        return int(time.time())

    @staticmethod
    def timestamp_to_datetime(timestamp, format_str="%Y-%m-%d %H:%M:%S"):
        """
        时间转换到日期时间
        """
        return datetime.datetime.fromtimestamp(timestamp).strftime(format_str)

    @staticmethod
    def time_difference(start_time, end_time):
        """
        计算时间差
        """
        time_difference = end_time - start_time
        units = [
            (86400000, "天"),
            (3600000, "小时"),
            (60000, "分钟"),
            (1000, "秒"),
            (1, "毫秒")
        ]

        parts = []
        for unit_milliseconds, unit_name in units:
            unit_value, time_difference = divmod(time_difference, unit_milliseconds)
            if unit_value > 0:
                parts.append(f"{int(unit_value)}{unit_name}")

        return " ".join(parts)


if __name__ == '__main__':
    print(TimeUtils.get_timestamp())
    print(TimeUtils.timestamp_to_datetime(TimeUtils.get_timestamp()))
    difTime = TimeUtils.time_difference(1692980802, TimeUtils.get_timestamp())
    print(difTime)
    pass
