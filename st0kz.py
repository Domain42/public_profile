#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, uic

from Source.TickerApp import tickerapp

from Source.Ui.MainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        #self.installEventFilter(self)

#JR
    close_function = None
    def closeEvent(self, event):
        if not self.close_function is None:
            self.close_function(event)

'''
    def eventFilter(self, obj, event):
        if obj == self.ticker_entry:
            print(event.type())
            if event.type() == QEvent.KeyPress:
                if event.key() == Qt.Key_Up:
                    print('Up')
                    return True
                elif event.key() == Qt.Key_Down:
                    print('Down')
                    return True
            return False
        else:
            return super().eventFilter(obj, event)
'''
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
ta = tickerapp(window)

window.show()
app.exec()
