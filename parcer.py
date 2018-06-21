# -*- coding: utf-8 -*-
'''
RU: модуль который вмещает регулярное выражение, и
функцию для поиска данных в запросе(ip адрес, время,
тип, результат, и информацию пользователя для запроса).

EN: module that contain the regular expression, and
function for searching data in the request (ip address, time,
type, result, and user information for the request).
'''

import re

lineformat = re.compile(r"""
(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})       #check ip address block
\s-\s-\s                                                #check " - - " block
\[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2}\s(\+|\-)\d{4})\]
                                                        #check date, time and
                                                        #time-belt move block
\s                                                      #check " "
((\"(?P<reqtype>POST|PUT|GET|DELETE|OPTIONS)\s)(?P<url>.+)(http\/1\.1"))      
                                                        #check type, url and
                                                        #HTTP proto of request
\s                                                      #check " "
(?P<statuscode>\d{3})                                   #check req statuse code
\s                                                      #check " "
(?:\d+)                                                 #check bytessend without
                                                        #result catching
\s                                                      #check " "
(["](?:(\-)|(.+))["])                                   #check refferer type
                                                        #without result catching
\s                                                      #check " "
(["](?P<useragent>.+)["])
""", re.I | re.X)

def analize_logs(file):
    '''
RU: функция, которая принимает файл, читает
строки и возвращает данные в более "удобном"
формате для проведения последующих операций
т.е. список из словарей.

EN: function that takes a file, reads
strings and returns the data in a more "convenient"
format for follow-up operations
i.e. list of dictionaries.
    '''
    data_mass = [] #it will be name for calling function

    for line in file.readlines():

        data = re.search(lineformat, line)

        try:
            datadict = data.groupdict()
            data_mass.append(datadict)
        except:
            if data is None:
                pass

    return data_mass


if __name__ == '__main__':

    import time

    test_logs = open('logs.txt')

    start = time.time()
    data_mass = analize_logs(test_logs)
    end = time.time()

    for i in data_mass:
        print(i, '\n')

    print(len(data_mass))
    print('time of performing module: ', end - start)




