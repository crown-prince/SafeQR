# -*- coding: utf-8 -*-
import sys 
from PyQt4 import QtCore, QtGui
from SafeQR_UI import Ui_MainWindow
import zbar
from PIL import Image

filename = "code.png"
class MainWindow(QtGui.QMainWindow): 
    def __init__(self, parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.Load_IMG, QtCore.SIGNAL("clicked()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.WhiteList, QtCore.SIGNAL("clicked()"), self.domain_test)
    def file_dialog(self):
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()
        global filename
        filename = str(self.filename)
       # import codecs
       # filename = codecs.open(self.filename, "r", "utf-8").read()
        print(filename)
        png=QtGui.QPixmap(filename)	
        self.ui.label_2.setPixmap(png)
    def domain_test(self):
        global filename
        score = 100
        scanner = zbar.ImageScanner()
        scanner.parse_config('enable')
        img = Image.open(filename).convert('L')
        w , h = img.size
        raw = img.tostring()
        zimg = zbar.Image(w, h, 'Y800', raw)
        scanner.scan(zimg)

        for s in zimg:
            self.ui.output.append("The %s is: %s" %(s.type, s.data))
    
        #提取域名
        domain = ""
        flag = 0
        begin = 0
        end = 0
        j = 0 
        print(s.data)
        for i in s.data:
            if flag == 0 and i == '/':
                begin = j + 2
                flag = 1
            elif flag == 1 and i == '/':
                flag = 2
            elif flag == 2 and i == '/':
                end = j - 1
                break
            j = j + 1
        #print begin 
        #print end
        
        domain = s.data[begin:end + 1]
        self.ui.output.append("The Domain is: %s" %(domain))
        
        #比对白名单
        flag = 0
        WhiteUrl = list()
        for line in open("WhiteList.config"):
            WhiteUrl.append(line.strip())
            #print line
        for test in WhiteUrl:
            if test == domain:
                self.ui.output.append("%s must be a Safe URl" % (test))
                flag = 1
        if flag == 0:
            self.ui.output.append("Score - 10")

if __name__ == "__main__": 
    app = QtGui.QApplication(sys.argv)   
    myapp = MainWindow() 
    myapp.show() 
    sys.exit(app.exec_())