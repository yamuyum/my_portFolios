# coding: utf-8
import math
import datetime
import os
import glob
from typing import Any
# import openpyxl
import random


# -------

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# --------

# 各種ツイッターのキーをセット
CURRENT_PATH = os.getcwd()
DT_NOW = datetime.datetime.now().strftime('%y%m%d')
DT_YEAR = datetime.datetime.now().strftime('%Y')
DT_MONTH = datetime.datetime.now().strftime('%m')


def discardNum(num: float):
    """
    最大桁数の他切り捨て.
    """
    """
    self.videos_count int:
        self.videos_count is a videos_count of <self>.
    """
    try:
        len_num = len(str(math.floor(num)))
        if(1 < len_num):
            pow_10s = pow(10, len_num-1)
            return math.floor(num / pow_10s) * pow_10s
        else:
            return 0
    except:
        # print("空欄だから空(-1でもいい)に設定")
        return 0
        # return None


def setHourZero(pre_post_hour):
    """
    時間(hhmmss)に合わせて0の整理
    """
    """
    3237 → 003237(str)
    """
    len_hour = len(pre_post_hour)
    if(len_hour < 6):
        for i in range(0, 6-len_hour):
            pre_post_hour = "0"+pre_post_hour
    return pre_post_hour


def get_nth_week_datetime(year, month, day):
    '''
    年月日(月曜始まり→0 ※日曜始まりの場合はここ6にする)
    '''
    firstweekday = 0
    first_dow = datetime.date(year, month, 1).weekday()
    offset = (first_dow - firstweekday) % 7
    return (day + offset - 1) // 7 + 1


def get_nth_week_datetime2(yyyymmdd: str):
    '''
    年月日が一気にまとまった場合
    '''
    year = int(yyyymmdd[:4])
    month = int(yyyymmdd[4:6])
    day = int(yyyymmdd[6:])
    # print(f"{year}/{month}/{day}")
    firstweekday = 0
    first_dow = datetime.date(year, month, 1).weekday()
    offset = (first_dow - firstweekday) % 7
    week = (day + offset - 1) // 7 + 1
    return yyyymmdd[:6] + "0" + str(week)


def get_nth_week(day):
    return (day - 1) // 7 + 1


def get_nth_dow_datetime(year, month, day):
    '''
    第n週、X曜日 を返す
    '''
    return get_nth_week(day), datetime.date(year, month, day).weekday()


def get_nth_dow_datetime2(yyyymmdd: str):
    """
    ※年月日が一気にまとまった場合
    日時 → 何周目,曜日(0~6?)
    """
    year = int(yyyymmdd[:4])
    month = int(yyyymmdd[4:6])
    day = int(yyyymmdd[6:])
    # print(f"{year}/{month}/{day}")
    return get_nth_week(day), datetime.date(year, month, day).weekday()


def main():
    # テストで動かす時
    # value = discardNum(385.56)

    # headCode = getHeadCode(0)
    # getCode = getRandomCode(headCode)
    # print(getCode)
    print(000)


if __name__ == "__main__":
    main()
