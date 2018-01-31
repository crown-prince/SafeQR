# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SafeQR_UI.ui'
#
# Created: Wed Jan 31 11:39:09 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(355, 417)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/images/logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.Load_IMG = QtGui.QPushButton(MainWindow)
        self.Load_IMG.setGeometry(QtCore.QRect(20, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Batang"))
        self.Load_IMG.setFont(font)
        self.Load_IMG.setObjectName(_fromUtf8("Load_IMG"))
        self.output = QtGui.QTextBrowser(MainWindow)
        self.output.setGeometry(QtCore.QRect(130, 241, 201, 161))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Batang"))
        font.setPointSize(11)
        self.output.setFont(font)
        self.output.setObjectName(_fromUtf8("output"))
        self.label = QtGui.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(130, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Batang"))
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.WhiteList = QtGui.QPushButton(MainWindow)
        self.WhiteList.setGeometry(QtCore.QRect(14, 250, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Batang"))
        self.WhiteList.setFont(font)
        self.WhiteList.setObjectName(_fromUtf8("WhiteList"))
        self.Md5 = QtGui.QPushButton(MainWindow)
        self.Md5.setGeometry(QtCore.QRect(14, 300, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Batang"))
        self.Md5.setFont(font)
        self.Md5.setObjectName(_fromUtf8("Md5"))
        self.scan = QtGui.QPushButton(MainWindow)
        self.scan.setGeometry(QtCore.QRect(14, 350, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Batang"))
        self.scan.setFont(font)
        self.scan.setObjectName(_fromUtf8("scan"))
        self.label_2 = QtGui.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(130, 30, 191, 151))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SafeQR", None))
        self.Load_IMG.setText(_translate("MainWindow", "Load IMG", None))
        self.label.setText(_translate("MainWindow", "Output", None))
        self.WhiteList.setText(_translate("MainWindow", "Domain Test", None))
        self.Md5.setText(_translate("MainWindow", "Pathfinder", None))
        self.scan.setText(_translate("MainWindow", "Cloud Sandbox", None))

