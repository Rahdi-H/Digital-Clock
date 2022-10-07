from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mn = time.strftime('%M')
    sec= time.strftime('%S')
    am = time.strftime('%p')
    lab_hr.config(text=hr)
    lab_mn.config(text=mn)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_hr.after(200, date_time)

def mont_time():
    time = datetime.datetime.now()
    date = time.strftime("%d")
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')
    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    lab_date.after(200, mont_time)

clock = Tk()
clock.title('Digital Clock')
clock.geometry('1000x500')
clock.config(bg='#006666')

lab_hr = Label(clock, text='00', font=('Arial', 60, 'bold'), bg='#003333', fg='white')
lab_hr.place(x=120, y=45, height=110, width=100)
lab_hr_txt = Label(clock, text='Hour', font=('Arial', 20, 'bold'), bg='#003333', fg='white')
lab_hr_txt.place(x=120, y=190, height=30, width=100)

lab_mn = Label(clock, text='00', font=('Arial', 60, 'bold'), bg='#003333', fg='white')
lab_mn.place(x=340, y=45, height=110, width=100)
lab_mn_txt = Label(clock, text='Min', font=('Arial', 20, 'bold'), bg='#003333', fg='white')
lab_mn_txt.place(x=340, y=190, height=30, width=100)

lab_sec = Label(clock, text='00', font=('Arial', 60, 'bold'), bg='#003333', fg='white')
lab_sec.place(x=560, y=45, height=110, width=100)
lab_hr_txt = Label(clock, text='Sec', font=('Arial', 20, 'bold'), bg='#003333', fg='white')
lab_hr_txt.place(x=560, y=190, height=30, width=100)

lab_am = Label(clock, text='00', font=('Arial', 40, 'bold'), bg='#003333', fg='white')
lab_am.place(x=780, y=45, height=110, width=100)
lab_am_txt = Label(clock, text='AM/PM', font=('Arial', 15, 'bold'), bg='#003333', fg='white')
lab_am_txt.place(x=780, y=190, height=30, width=100)

lab_date = Label(clock, text='00', font=('Arial', 60, 'bold'), bg='#003333', fg='white')
lab_date.place(x=120, y=270, height=110, width=100)
lab_date_txt = Label(clock, text='Date', font=('Arial', 20, 'bold'), bg='#003333', fg='white')
lab_date_txt.place(x=120, y=410, height=30, width=100)

lab_mo = Label(clock, text='00', font=('Arial', 60, 'bold'), bg='#003333', fg='white')
lab_mo.place(x=340, y=270, height=110, width=100)
lab_mo_txt = Label(clock, text='Month', font=('Arial', 20, 'bold'), bg='#003333', fg='white')
lab_mo_txt.place(x=340, y=410, height=30, width=100)

lab_year = Label(clock, text='00', font=('Arial', 60, 'bold'), bg='#003333', fg='white')
lab_year.place(x=560, y=270, height=110, width=100)
lab_year_txt = Label(clock, text='Year', font=('Arial', 20, 'bold'), bg='#003333', fg='white')
lab_year_txt.place(x=560, y=410, height=30, width=100)

lab_day = Label(clock, text='00', font=('Arial', 60, 'bold'), bg='#003333', fg='white')
lab_day.place(x=780, y=270, height=110, width=100)
lab_day_txt = Label(clock, text='Day', font=('Arial', 20, 'bold'), bg='#003333', fg='white')
lab_day_txt.place(x=780, y=410, height=30, width=100)

date_time()
mont_time()
clock.mainloop()