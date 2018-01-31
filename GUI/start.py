# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from edytor import Ui_notepad

class StartQt4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_notepad() #框主题名称
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.button_open, QtCore.SIGNAL("clicked()"), self.file_dialog)
        #button_open 对应打开按钮
        #self.file_dialog 信号对应的函数
        QtCore.QObject.connect(self.ui.button_save, QtCore.SIGNAL("clicked()"), self.file_save)
        QtCore.QObject.connect(self.ui.editor_window, QtCore.SIGNAL("textChanged()"), self.enable_save)
    def file_dialog(self):
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()
        from os.path import isfile
        if isfile(self.filename):
            import codecs
            text = codecs.open(self.filename, "r", "utf-8").read() #弹出文件选择对话框
            self.ui.editor_window.setPlainText(text)
            self.ui.button_save.setEnabled(False)
    def enable_save(self):
        self.ui.button_save.setEnabled(True) #使文章在有变动时，方可被保存
    def file_save(self):
        from os.path import isfile
        if isfile(self.filename):
            import codecs
            file = codecs.open(self.filename, "w", "utf-8")
            file.write(unicode(self.ui.editor_window.toPlainText()))
            file.close()
            self.ui.button_save.setEnabled(False)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQt4()
    myapp.show()
    sys.exit(app.exec_())
