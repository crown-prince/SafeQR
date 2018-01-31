#coding: utf-8
import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        self.resize(350,250)
        self.setWindowTitle('SafeQR')
        self.setGeometry(300,300,400,250) 
        self.setWindowTitle('SafeQR') #标题栏

        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exit = QtGui.QAction(QtGui.QIcon('images/logo.ico'),'Exit',self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT('quit()'))
        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit)

app = QtGui.QApplication(sys.argv) #启动QT程序
main = MainWindow()
main.show()
"""widget = QtGui.QWidget() #PyQt4中所有用户界面类的弗雷
widget.resize(400, 250) #改变窗口大小 """
sys.exit(app.exec_())
