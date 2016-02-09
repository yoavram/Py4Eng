# -*- coding: utf-8 -*-
"""
GUI for plotting sine and cosine functions.

Created on Tue Feb  9 12:30:45 2016

@author: yoav@yoavram.com
"""
import sys
# https://srinikom.github.io/pyside-docs/index.html
from PySide.QtCore import *
from PySide.QtGui import *
from trigoplot_design import Ui_MainWindow

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import numpy as np
import seaborn as sns
sns.set(
    style='white',
    palette='muted'
)

figsize = (6, 4)
dpi = 100
color_palettes = ('deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind')

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # button
        self.pushButton.clicked.connect(self.plot)
        
        # color list
        for cp in color_palettes:
            QListWidgetItem(cp, self.colorListWidget)
        self.colorListWidget.item(0).setSelected(True)
       
        # combobox 
        self.wComboBox.addItem('w=1')
        self.wComboBox.addItem('w=2')
        self.wComboBox.addItem('w=3')
        self.wComboBox.addItem('w=4')
               
        # plot widget
        self.fig = matplotlib.figure.Figure(figsize=figsize, dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.plotWidget)
                
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.plotWidget)
        
        left_vbox = QVBoxLayout()
        left_vbox.addWidget(self.canvas)
        left_vbox.addWidget(self.mpl_toolbar)

        hbox = QHBoxLayout()
        hbox.addLayout(left_vbox)
        self.plotWidget.setLayout(hbox)
        
        
    def plot(self):
        sns.set_color_codes(self.colorListWidget.currentItem().text())

        w = self.wComboBox.currentText()
        if w:
            w = int(w[-1])
        else:
            w = 1
                
        if self.sinRadBtn.isChecked():
            f = np.sin
            c = 'r'
        elif self.cosRadBtn.isChecked():
            f = np.cos
            c = 'b'
            
        x = np.linspace(0, 2 * np.pi, 100)
        y = f(w * x)
        self.ax.plot(x, y)
        self.ax.set(
            xlabel='x',
            ylabel='y',
            xlim=(-0.1, 2 * np.pi + 0.1),
            ylim=(-1.1, 1.1)
        )
        self.fig.tight_layout()
        self.canvas.draw()
        
        for i in range(x.size):
            xi = QTableWidgetItem("{:.4f}".format(x[i]))
            self.tableWidget.setItem(i, 0, xi)
            yi = QTableWidgetItem("{:.4f}".format(y[i]))
            self.tableWidget.setItem(i, 1, yi)
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())