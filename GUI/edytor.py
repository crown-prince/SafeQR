# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edytor.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_notepad(object):
    def setupUi(self, notepad):
        notepad.setObjectName(_fromUtf8("notepad"))
        notepad.resize(400, 300)
        self.button_save = QtGui.QPushButton(notepad)
        self.button_save.setGeometry(QtCore.QRect(270, 20, 111, 31))
        self.button_save.setObjectName(_fromUtf8("button_save"))
        self.button_open = QtGui.QPushButton(notepad)
        self.button_open.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.button_open.setObjectName(_fromUtf8("button_open"))
        self.editor_window = QtGui.QTextEdit(notepad)
        self.editor_window.setGeometry(QtCore.QRect(33, 90, 331, 171))
        self.editor_window.setObjectName(_fromUtf8("editor_window"))
        self.pushButton_2 = QtGui.QPushButton(notepad)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 20, 111, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(notepad)
        QtCore.QObject.connect(self.button_save, QtCore.SIGNAL(_fromUtf8("clicked()")), notepad.close)
        QtCore.QMetaObject.connectSlotsByName(notepad)

    def retranslateUi(self, notepad):
        notepad.setWindowTitle(_translate("notepad", "notepad", None))
        self.button_save.setText(_translate("notepad", "关闭", None))
        self.button_open.setText(_translate("notepad", "打开", None))
        self.pushButton_2.setText(_translate("notepad", "保存", None))

