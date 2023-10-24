import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self):
        self.win = tk.Tk()

        self.win.title('Calc')
        self.win.geometry("600x300+100+200")  # размеры окна и отступы от верхнего
        # левого угла экрана
        self.lab1 = tk.Label(self.win, text='Number1: ')
        self.lab2 = tk.Label(self.win, text='Number2: ')
        self.lab1.grid(row=1, column=0)
        self.lab2.grid(row=1, column=2)
        self.entry1 = tk.Entry(self.win)
        self.entry2 = tk.Entry(self.win)
        self.entry1.grid(row=1, column=1)
        self.entry2.grid(row=1, column=3)
        self.pluscond = tk.BooleanVar()
        self.pluscond.set(False)
        self.plus = tk.Checkbutton(self.win, text='+',
                                   variable=self.pluscond)
        self.minuscond = tk.BooleanVar()
        self.minuscond.set(False)
        self.minus = tk.Checkbutton(self.win, text='-',
                                    variable=self.minuscond)
        self.multicond = tk.BooleanVar()
        self.multicond.set(False)
        self.multi = tk.Checkbutton(self.win, text='*',
                                    variable=self.multicond)
        self.divcond = tk.BooleanVar()
        self.divcond.set(False)
        self.div = tk.Checkbutton(self.win, text='/',
                                  variable=self.divcond)
        self.percond = tk.BooleanVar()
        self.percond.set(False)
        self.per = tk.Checkbutton(self.win, text='Пер',
                                  variable=self.percond)
        self.ploshcond = tk.BooleanVar()
        self.ploshcond.set(False)
        self.plosh = tk.Checkbutton(self.win, text='Пл',
                                    variable=self.ploshcond)
        self.lab3 = tk.Label(self.win, text='Выберите операции: ')
        self.lab3.grid(row=2, column=0)
        self.plus.grid(row=2, column=1)
        self.minus.grid(row=2, column=2)
        self.multi.grid(row=3, column=1)
        self.div.grid(row=3, column=2)

        self.count = tk.Button(self.win, text='Вычислить!', command=self.calculate)
        self.select = tk.Button(self.win, text='Выбрать всё!', command=self.select_all)
        self.clear_nums = tk.Button(self.win, text='Очистить поля!', command=self.clear_num)
        self.clear = tk.Button(self.win, text='Очистить выбор!', command=self.clear_all)
        self.rect = tk.Button(self.win, text='Нарисовать прямоугольник', command=self.print_rect)
        self.leave = tk.Button(self.win, text='Выйти', command=self.quite)
        self.change_places = tk.Button(self.win, text='Поменять местами', command=self.change)
        self.count.grid(row=5, column=2)
        self.clear.grid(row=5, column=0)
        self.select.grid(row=5, column=1)
        self.clear_nums.grid(row=6, column=0)
        self.rect.grid(row=6, column=1)
        self.leave.grid(row=7, column=2)
        self.change_places.grid(row=6, column=2)
        self.c = tk.Canvas(self.win, width=100, height=100)
        self.c.grid(row=8, column=0)
        self.var = tk.IntVar()
        self.var.set(0)
        self.rad1 = tk.Radiobutton(self.win, text='Калькулятор', variable=self.var, value=0,
                                   command=self.select_type)
        self.rad2 = tk.Radiobutton(self.win, text='Прямоугольник', variable=self.var, value=1,
                                   command=self.select_type)
        self.rad1.grid(row=0, column=0)
        self.rad2.grid(row=0, column=1)
        self.res = tk.Label(self.win)
        self.menu = tk.Menu(self.win)
        self.file = tk.Menu(self.menu)
        self.file.add_command(label='Выход', command=self.quite)
        self.menu.add_cascade(label='Файл', menu=self.file)
        self.operations = tk.Menu(self.menu)
        self.operations.add_command(label='Поменять местами', command=self.change)
        self.operations.add_command(label='Очистить поля', command=self.clear_num)
        self.operations.add_command(label='Очистить выбор', command=self.clear_all)
        self.operations.add_command(label='Вычислить', command=self.calculate)
        self.operations.add_command(label='Выбрать все', command=self.select_all)
        self.operations.add_command(label='Нарисовать прямоугольник', command=self.print_rect)
        self.menu.add_cascade(label='Операции', menu=self.operations)
        self.info = tk.Menu(self.menu)
        self.info.add_command(label='Информация', command=self.watch_info)
        self.menu.add_cascade(label='Справка', menu=self.info)
        self.win.config(menu=self.menu)

        self.win.mainloop()

    def calculate(self):
        self.res.config(text='')

        try:
            a = float(
                self.entry1.get())  # почему-то, если гет хасунуть в флоат - работает, а если сначала гетнуть и во флоат - нет
            b = float(self.entry2.get())
            print(a, b)
            print(self.var.get())
        except ValueError:
            txt = 'Вводите только числа!'
            self.res.config(text=txt)

        else:
            print(self.pluscond.get(), self.minuscond.get())
            if self.var.get() == 0:
                txt = ''
                if self.pluscond.get():
                    txt += f'Сумма: {round(a + b, 2)} \n'
                    print('+')
                if self.minuscond.get():
                    txt += f'Разность: {round(a - b, 2)} \n'
                    print('-')
                if self.multicond.get():
                    txt += f'Произведение: {round(a * b, 2)} \n'
                    print('*')
                if self.divcond.get():
                    try:
                        txt += f'Частное: {round(a / b, 2)} \n'
                        print('/')
                    except ZeroDivisionError:
                        txt += 'На ноль делить нельзя!'

            elif self.var.get() == 1:
                if a >= 0 and b >= 0:
                    txt = ''
                    if self.percond.get():
                        txt += f'Периметр: {round(2 * (a + b), 2)} \n'

                        print('P')
                    if self.ploshcond.get():
                        txt += f'Площадь: {round(a * b, 2)} \n'

                        print('S')
                else:
                    txt = 'Такого прямоугольника \n не существует!'

        self.res.config(text=txt)
        self.res.grid(row=2, column=3, rowspan=4)

    def select_type(self):
        if self.var.get() == 0:
            self.plus.grid(row=2, column=1)
            self.minus.grid(row=2, column=2)
            self.multi.grid(row=3, column=1)
            self.div.grid(row=3, column=2)
            self.per.grid_forget()
            self.plosh.grid_forget()
        elif self.var.get() == 1:
            self.plus.grid_forget()
            self.minus.grid_forget()
            self.multi.grid_forget()
            self.div.grid_forget()
            self.per.grid(row=2, column=1)
            self.plosh.grid(row=2, column=2)

    def select_all(self):
        if self.var.get() == 0:
            for cond in (self.pluscond, self.minuscond, self.multicond, self.divcond):
                cond.set(True)
        if self.var.get() == 1:
            for cond in (self.percond, self.ploshcond):
                cond.set(True)

    def clear_all(self):
        if self.var.get() == 0:
            for cond in (self.pluscond, self.minuscond, self.multicond, self.divcond):
                cond.set(False)
        if self.var.get() == 1:
            for cond in (self.percond, self.ploshcond):
                cond.set(False)

    def clear_num(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.res.config(text='')

    def print_rect(self):
        try:
            f = float(self.entry1.get())
            s = float(self.entry2.get())
        except:
            pass
        else:
            if f >= 0 and s >= 0:
                self.c.delete("all")
                self.c.create_rectangle(10, 10, f + 10, s + 10, fill='green')
    def change(self):
        f = self.entry1.get()
        s = self.entry2.get()
        self.entry1.delete(0, tk.END)
        self.entry1.insert(0, s)
        self.entry2.delete(0, tk.END)
        self.entry2.insert(0, f)
    def watch_info(self):
        pass
    #     messagebox.showinfo('Информация','Это самый лучший в мире по скорости и точности вычислений калькулятор '
    #                                         'во всей галактике \nЗдесь вы можете посчитать: сумму, разность, произведение, частное, \n'
    #                                                              'а также площадь и периметр прямоугольника. Удачи!')

    def quite(self):
        self.win.quit()


c = Calculator()
