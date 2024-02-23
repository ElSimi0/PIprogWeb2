# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:22:37 2024

@author: sameg
"""
#!/usr/bin/env python3

from tkinter import *
import chistes

def click():
    label1 = Label(root, text=f"Hola {entrada.get()}!")
    label1.pack()

root = Tk()

entrada = Entry(root)
entrada.pack()


boton = Button(root, text="CLICK", command=click, fg="black", bg="blue")
boton.pack()

root.mainloop()

