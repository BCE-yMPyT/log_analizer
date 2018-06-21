from parcer import analize_logs
from filters import period_filter
from redusers import reqFreq

#-----user interface function--------------------------------
def Getter():
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
    #--------------------------------------------------------------------
    data_mass = analize_logs(file)
    period_data = period_filter(data_mass, start_date, end_date)
    count = reqFreq(period_data)

    req_per_sec = count / 86400
    req_per_min = count / 1440
    req_per_hour = count / 24

    #result_table = (anal_day, requests_count, req_per_sec, req_per_min, req_per_hour)

    result = [(start_date, count, req_per_sec, req_per_min, req_per_hour)]

    return result
    #-----end of function--------------------------------------------------

if __name__ == '__main__':
    result = Getter()
    print(result)