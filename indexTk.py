# -*- coding: utf-8 -*-
'''
Реализация графического интерфейса для просмотра и изменения экземпляров класса,
хранящихся в хранилище;
хранилище находится на том же компьютере, где выполняется сценарий в виде одного
или более локальных файлов;
'''
#----------importing tkinter stuff----------
from tkinter.messagebox import showerror
from tkinter import filedialog
from tkinter import *
#----------importing analize stuff----------
from parcer import analize_logs
from filters import period_filter
from redusers import reqFreq

def choose_the_file():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    print(root.filename)

def show_logs():
    if root.filename is None or root.filename == '':
        root.withdraw()
        messagebox.showerror("Error", "Файл не выбран, выберите файл!")
        root.deiconify()
    else:
        file = open(root.filename)
        data_mass = analize_logs(file)

        output_window = Toplevel()
        output_window.geometry('600x600')

        textFrame = Frame(output_window, height=340, width=600)
        textFrame.pack(side='bottom', fill='both', expand=1)

        text = Text(textFrame,  font='Arial 14', wrap=WORD)
        for i in data_mass:
            text.insert(1.0, str(i) + '\n' + '\n')

        scroollbar = Scrollbar(textFrame)
        scroollbar['command'] = text.yview
        text['yscrollcommand'] = scroollbar.set

        scroollbar.pack(side=RIGHT, fill=Y)
        text.pack(side=RIGHT, fill=BOTH)

        output_window.mainloop()

def show_logs_info():
    #-----проверка на выбор файла-----
    if root.filename is None or root.filename == '':
        root.withdraw()
        messagebox.showerror("Error", "Файл не выбран, выберите файл по-жалу-йстаааа блять!")
        root.deiconify()
    #---------------------------------
    else:
    #-----смотрим логи за временной промежуток------
        #-----функция для получения дат-----
        def get_time_interval():
            global start_date, end_date
            start_date = start_date_field.get()
            end_date = end_date_field.get()

            if start_date == '' or end_date == '':
                messagebox.showerror("Error", "Даты не выбраны.")


        def period_filtering():
            get_time_interval()

            text.delete(1.0, END)

            period_data = period_filter(data_mass, start_date, end_date)

            for n in period_data:
                text.insert(1.0, str(n) + '\n' + '\n')

        def show_period_info():
            get_time_interval()

            text.delete(1.0, END)

            period_data = period_filter(data_mass, start_date, end_date)

            count = reqFreq(period_data)

            text.insert(1.0, 'запросов за временной промежуток - %s' % count, '\n', '\n', '\n')
            text.insert(1.0, 'среднее число запросов в секунду - %s' % (count / 86400), '\n', '\n', '\n')
            text.insert(1.0, 'среднее число запросов в минуту - %s' % (count / 1440), '\n', '\n', '\n')
            text.insert(1.0, 'среднее число запросов в час - %s' % (count / 24), '\n', '\n', '\n')

        #-----получаем файл-----
        file = open(root.filename)
        #-----анализ файла-----(filter massive by date)
        data_mass = analize_logs(file)
        #-----организовуем интерфейс-----
        output_window = Toplevel()
        output_window.geometry('600x600')

        textFrame = Frame(output_window, height=340, width=600)
        textFrame.pack(side='bottom', fill='both', expand=1)

        Label(textFrame, text="Введите начальную дату: (date/Mth/...)").pack(side=TOP)
        start_date_field = Entry(textFrame)
        start_date_field.pack(side=TOP)

        Label(textFrame, text="Введите конечную дату: (date/Mth/...)").pack(side=TOP)
        end_date_field = Entry(textFrame)
        end_date_field.pack(side=TOP)

        Button(textFrame, text='\n Подтвердить ввод \n', command=period_filtering).pack(side=TOP, fill=BOTH)
        Button(textFrame, text='\n Показать инфо за этот временной промежуток \n', command=show_period_info).pack(side=TOP, fill=BOTH)

        global text
        text = Text(textFrame, font='Arial 14', wrap=WORD)

        scroollbar = Scrollbar(textFrame)
        scroollbar['command'] = text.yview
        text['yscrollcommand'] = scroollbar.set

        scroollbar.pack(side=RIGHT, fill=Y)
        text.pack(side=RIGHT, fill=BOTH)
        #-----зацикливаем интерфейс-----
        output_window.mainloop()

#-------------main window-------------------
def makeWidgets():
    global entries
    root = Tk()
    root.title('Parser')
    form = Frame(root)
    form.pack()


    Button(root, text='\n Выбор файла логов \n', command=choose_the_file).pack(side=TOP, fill = BOTH)
    Button(root, text='\n Выход \n', command=root.quit).pack(side=BOTTOM, fill = BOTH)
    Button(root, text='\n Вывод информации о запросах \n', command=show_logs_info).pack(side=BOTTOM, fill = BOTH)
    Button(root, text='\n Вывод логов за всё время \n', command=show_logs).pack(side=BOTTOM, fill = BOTH)

    return root


root = makeWidgets()
root.filename = None
root.mainloop()
