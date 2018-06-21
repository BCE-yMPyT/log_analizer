# -*- coding: utf-8 -*-
'''
RU: Модуль для управления программой,
позволяет выбирать операцию для обработки логов,
и сам обрабатываемый лог.

EN: The module for managing the program,
allows you to select the operation for log processing,
and the log itself.
'''
#-----Общая функция--------------------------------
def condition_describer():
    '''
RU: Позволяет получить инфу от пользователя,
такую как: путь к логу, дату для начала анализа
и дату конца анализа.

EN: Allows you to receive information from the user,
such as: the path to the log, the date to start the analysis
and the end date of the analysis.
    '''
    from parcer import analize_logs
    from filters import period_filter

    print("Enter the path, in that format:",
          '\n',
          'C:\\test.../file.txt')
    path_to_file = input()
    file = open(path_to_file)
    print("Enter the date for start, in that format:",
          '\n',
          'date/Mth/...')
    start_date = input()
    print("Enter the date for end, in that format:",
          '\n',
          'date/Mth/...')
    end_date = input()
    data_mass = analize_logs(file)
    period_data = period_filter(data_mass, start_date, end_date)
    # filter massive by date
    return period_data


#-------------------------Scenario---------------------
print(
    'Choose an available function: ',
    '\n',
    '1) Parcer.py (prints an array of all logs)',
    '\n',
    "2) Filters.py (outputs logs for the time period)",
    '\n',
    "3) Redusers.py (gives info about requests)"
    '\n',
    "4) Archive_processor.py (unpacking archives)",
    '\n',
    "5) DBWriter.py (writing data to database)",
    '\n'
)

first_decision = int(input()) #-----decision of user---

if first_decision == 1:       #-if chosen Iterator---It work's
    print("Your choise: Parcer.py")
    from parcer import analize_logs
    print("Enter the path, in that format:",
          '\n',
          'C:\\test.../file.txt')
    path_to_file = input()
    file = open(path_to_file)
    data_mass = analize_logs(file)
    for i in data_mass:
        print(i, '\n')

if first_decision == 2:      #-if chosen Filters---
    print("Your choise: Filters.py")

    period_data = condition_describer()

    for n in period_data:
        print(n, '\n')

if first_decision == 3:     #-if chosen Redusers---
    from redusers import reqFreq
    print("Your choise: Redusers.py")

    period_data = condition_describer()

    count = reqFreq(period_data)

if first_decision == 4:
    print("Your choise: archive_processor.py",
          '\n',
          "Choose function for unpacking:",
          '\n',
          "1. unpack_targz (unpacking one .tar.gz archive)",
          '\n',
          "2. unpack_gz (unpacking one .gz archive)",
          '\n',
          "3. unpack_all (unpacking all archives in folder)",
          )
    second_decision = int(input())
    if second_decision == 1:
        from archive_processor import unpack_targz
        sd = unpack_targz()
    if second_decision == 2:
        from archive_processor import unpack_gz
        sd = unpack_gz()
    if second_decision == 3:
        from archive_processor import unpack_all
        sd = unpack_all()

if first_decision == 5:
    print("Your choise: DBWriter.py")
    from dbwriter import DBwriter
    won = DBwriter()
