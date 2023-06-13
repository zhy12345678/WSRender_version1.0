# -*- coding: utf-8 -*-
"""
Created on 7th.Mar.2023
@author: Hanyu Zhao
@email: hanniezhaohaha@gmail.com
@file: GUI Overview for the main page of WSRender
@description:
"""

import os
import sys
from optparse import OptionParser

try:
    from PyQt5.QtCore import QSize,Qt
    from PyQt5.QtWidgets import QApplication,QPushButton,QMainWindow
except ImportError:
    from PySide2.QtWidgets import QApplication,QPushButton,QWidget,QHBoxLayout
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("WSRender")
        button=QPushButton("Press Me!")

        #set the contral widget of the Window
        self.setCentralWidget(button)

#if you know you won't use command line arguments QApplication([]) works too.
app=QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window=MainWindow()
window.show() #window is hideen at first

#start the event loop
app.exec() #调动事件循环


#Your application won't reach here until you exit and the event
# loop has stopped.




