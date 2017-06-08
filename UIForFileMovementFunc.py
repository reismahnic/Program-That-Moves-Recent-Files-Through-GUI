#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.6.1
#
# Author:       Reis Mahnic
#
# Purpose:      Moves recently edited files from one folder to another.
#              
#
# Tested OS:  This code was written and tested to work with Windows 10.

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3
import shutil
import datetime as dt
from tkinter.filedialog import askdirectory
from tkinter import filedialog


# Be sure to import our other modules 
# so we can have access to them
import UIForFileMovement






# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

def selectSourceDirectory(self):
    source = filedialog.askdirectory()
    self.sourceReturn.set(source)
def selectDestinationDirectory(self):
    destination = filedialog.askdirectory()
    self.destinationReturn.set(destination)
def setFileSource(self):
    #List the source folder and destination folder
    source = self.sourceReturn.get()
    destination = self.destinationReturn.get()
    print(source)
    print(destination)

    #Define the current time and the time period we want to look back at
    now = dt.datetime.now()
    before = now - dt.timedelta(hours=24)

    #Print the list of file names
    files = os.listdir(source)

    for root,dirs,files in os.walk(source):
        for file_name in files:
            path = os.path.join(root,file_name)
            st = os.stat(path)    
            mod_time = dt.datetime.fromtimestamp(st.st_mtime)
            if mod_time > before:
                #Move all files in Folder A to Folder B
                shutil.move(os.path.join(root, file_name), destination)

