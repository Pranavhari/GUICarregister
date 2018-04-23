from tkinter import *
from tkinter import ttk
from shutil import copyfile
import os
master = Tk()
count=0

def addrec():

    f = open('open.txt', 'a')
    vehicle = s1.get()
    type = s2.get()
    company=s3.get()
    engine=s4.get()
    mileage=s5.get()

    f.writelines(vehicle.ljust(10) + type.ljust(10) + company.ljust(10)+engine.ljust(10)+mileage.ljust(10)+"\n")
    f.close()


def nextrec():
    global count
    f=open('open.txt','r')
    i=0
    while(i<=count):
        l=f.readline()
        i=i+1
    list1=l.split()
    if list1.__len__() != 0:
        s1.set(list1[0])
        s2.set(list1[1])
        s3.set(list1[2])
        s4.set(list1[3])
        s5.set(list1[4])
        count = count + 1
    f.close()
    l6.config(text=count)

def prevrec():
    global count
    if count!=1:
        f=open('open.txt','r')
        i=0
        count = count - 1
        while(i<count):
            l=f.readline()
            i=i+1
        list1=l.split()
        s1.set(list1[0])
        s2.set(list1[1])
        s3.set(list1[2])
        s4.set(list1[3])
        s5.set(list1[4])
        f.close()
        l6.config(text=count)

def deleterec():
    infile = open('open.txt', 'r').readlines()
    with open('output.txt', 'w') as outfile:
        for index, line in enumerate(infile):
            if index != count-1:
                outfile.write(line)
    copyfile("output.txt","open.txt")
    os.remove("output.txt")

def show_entry_fields():
    print("VEHICLE Name: %s\nTYPE OF VEHICLE: %s" % (s1.get(), s2.get()))

s1 = StringVar()
s2 = StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()

label1 = ttk.Label(master, text="VEHICLE NAME")
label1.grid(row=0,pady=4)

l2 = Label(master, text="TYPE")
l2.grid(row=1,pady=4)

l3 = Label(master, text="COMPANY NAME")
l3.grid(row=2,pady=4)

l4 = Label(master, text="ENGINE SIZE")
l4.grid(row=0,column=2,columnspan=4,pady=4)

l5 = Label(master, text="MILEAGE")
l5.grid(row=1,column=2,columnspan=4,pady=4)

l6 = Label(master, text="LINE NO.")
l6.grid(row=2,column=2,columnspan=4,pady=4)

e1 = Entry(master,textvariable=s1)
e1.grid(row=0, column=1,pady=4)

e2 = Entry(master,textvariable=s2)
e2.grid(row=1, column=1,pady=4)

e3 = Entry(master,textvariable=s3)
e3.grid(row=2, column=1,pady=4)

e4 = Entry(master,textvariable=s4)
e4.grid(row=0, column=6,columnspan=4,pady=4)

e5 = Entry(master,textvariable=s5)
e5.grid(row=1, column=6,columnspan=4,pady=4)

e6 = Entry(master,textvariable=s6)
e6.grid(row=2, column=6,columnspan=4,pady=4)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='SHOW', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='ADD', command=addrec).grid(row=3, column=2, sticky=W, pady=4)
Button(master, text='>', command=nextrec).grid(row=3, column=3, sticky=W, pady=4)
Button(master, text='<', command=prevrec).grid(row=3, column=4, sticky=W, pady=4)
Button(master, text='DELETE', command=deleterec).grid(row=3, column=5, sticky=W, pady=4)
master.mainloop()
