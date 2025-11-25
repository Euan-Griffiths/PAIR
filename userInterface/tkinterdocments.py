from tkinter import *
from tkinter import ttk
from astropy.io import fits
from matplotlib import pyplot as plt


class Main():
    def __init__(self,root):
        root.title("Fits File Converter (FFC)")
        mainframe = ttk.Frame(root,padding=(3,3,12,12))
        mainframe.grid(column=0,row=0,sticky=(N,E,S,W))
        
        
    
    def getDimension(self):
        pass
    
root =Tk()
Main(root)
root.mainloop()