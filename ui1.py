 # -*- coding: utf-8 -*-
"""
Created on Thu May 13 19:16:24 2021

@author: user
"""

from tkinter import *
from PTL import Image,ImageTk
from tkinter import filedialog
import pytesseract
import pyttsx3

import os
from tkinter import messagebox

pytesseract.pytesseract.tesseract_cmd=r'c:\programfiles(x86)\Tesseract-0CR\tesseract.exe'
root=Tk()
root.title("Tkinter Window")
root.geometry("800*500")
frame2=Frame(root).pack()
farme1==Frame(root).pack()
frame0=frame(root)
frame0.pack()

def browse():
    browz=filedialog.askopenfilenmae(initiladir=os.getcwd()),title="select image file",filetypes=("PNG file","*.png"),("JPG file","*.jpg"),("All file","*.*"
    lo=Image.open(browz)
    load=lo.resize((300,200))
    render=ImageTk.photoImage(load)
    img=Label(root,image=render,bg="brown")
    img.imag=render
   

