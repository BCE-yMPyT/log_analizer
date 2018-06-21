# -*- coding: utf-8 -*-
'''
RU - Модуль для получения среднестатистических данных.

EN - The module for obtaining the average statistical data.
'''
from parcer import analize_logs
from filters import period_filter

def reqFreq(period_data):
    '''
RU - Функция, которая принимает:
массив данных и выводит количество запросов за
временной промежуток и среднее количество запросов.

EN - A function that accepts:
data array and displays the number of requests for
time interval and average number of requests.
    '''

    count = len(period_data)
    sec_in_day = 86400
    min_in_day = 1440
    hour_in_day = 24
    print('requests for time period - ', count)
    print('average number of requests per second - ', count / sec_in_day)
    print('average number of requests per minute - ', count / min_in_day)
    print('average number of requests per hour - ', count / hour_in_day)

    return count


#test if play redusers.py
if __name__ == '__main__':

    test_logs = open('logs.txt')

    data_mass = analize_logs(test_logs)

    period_data = period_filter(data_mass, '30/Apr', '01/May')

    count = reqFreq()
