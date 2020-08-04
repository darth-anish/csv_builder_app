#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:44:43 2020

@author: darth-anishman
"""
import pandas
import tkinter as tk
from tkinter import filedialog
import os


def file_input():
    global path
    path = ''
    path = filedialog.askopenfilename()
    print(path)
    
def analysis():
    data = pandas.read_csv(path)
    groups = data.groupby(col_name1.get())
    table = groups[col_name2.get()].mean()
    savename = filedialog.asksaveasfilename()
    savename = savename.split('.')[0] + '.csv'
    table.to_csv(savename)



    
    
window = tk.Tk()

col_name1 = tk.StringVar()
col_name2 = tk.StringVar()
frame= window.geometry("800x800")


tk.Label(frame, text='Feature to GroupBy').grid(row=0, column=0)
e1 = tk.Entry(frame, textvariable = col_name1).grid(row=0, column=1)

tk.Label(frame, text='Feature to maipulate').grid(row=1, column=0)
e2 = tk.Entry(frame, textvariable = col_name2).grid(row=1, column=1)


tk.Button(frame, text='Open', command=file_input())

tk.Button(frame, text='Generate', command = lambda: analysis()).grid(row=3, column=1)
window.mainloop()
