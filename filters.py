# -*- coding: utf-8 -*-
'''
RU: Модуль-фильтр для выборки данных
Функция, принимает:
- файл данных .txt
- начальную дату (включительно)
- конечную дату (не включительно,
  поэтому, если надо проверить 1 день,
  неоюходимо в качестве конечной даты
  ставить следующий)
и создаёт массив данных логов,
которые находятся в этом временном
промежутке.

EN: Filter module for data retrieval
Function, accepts:
- data file.txt
- start date (inclusive)
- the end date (not inclusive,
   so if you need to check 1 day,
   as an end date
   put next)
and creates an array of log data,
who are in this temporary
gap.
'''
from parcer import analize_logs

def period_filter(data_mass, date_start, date_end):

    period_data = [] #it will be name for calling function

    #take around all vocabularies
    for i in data_mass:

        #var for comparison
        var_for_compare = i.get('dateandtime')

        #is date start var, in
        #value for 'dateandtime' key?
        if date_start in var_for_compare:
            period_data.append(i)

        #is date end var, in
        #value for 'dateandtime' key?
        elif date_end in var_for_compare:
            break

        #is date start var, not in
        #value for 'dateandtime' key?
        elif date_start not in var_for_compare:
            period_data.append(i)

    return period_data

#test if play filters.py
if __name__ == '__main__':

    test_logs = open('log.txt')

    data_mass = analize_logs(test_logs)

    period_data = period_filter(data_mass, '30/Apr', '02/May') #calling function

    for n in period_data:
        print(n, '\n')
















