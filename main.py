#in the name of Allah

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QFont, QPixmap, QPolygon
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect, QRectF
import sys
import time


class DrawArea(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.setGeometry(50, 50, 1200, 800)
        self.setWindowTitle('Painter training')
        self.setObjectName("MainWindow")
        self.resize(1200, 1000)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 311, 231))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 121, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 113, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 100, 113, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 160, 113, 28))
        self.lineEdit_3.setObjectName("lineEdit_3")
               
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Settings"))
        self.label.setText(_translate("MainWindow", "Thickness:"))
        self.label_2.setText(_translate("MainWindow", "Delay:"))
        self.label_3.setText(_translate("MainWindow", "Number of ticks:"))
        self.lineEdit.setText("20")
        self.lineEdit_2.setText("100")

        self.lineEdit_3.setText("40") # change number of lines

        self.begin_x = 500
        self.begin_y = 300
        self.end_x = 1000
        self.end_y = 800
        self.counter = 0
        self.step = 30
        self.current_line = 0
        self.thickness = self.lineEdit.text()
        self.delay = self.lineEdit_2.text()
        self.lines_number = self.lineEdit_3.text()

    # def update_paint_event(self):
    #     self.thickness = qw.lineEdit.text()
    #     self.delay = qw.lineEdit_2.text()
    #     self.lines_number = qw.lineEdit_3.text()
        
    #     self.step = int(500 / int(self.lines_number))

    #     for i in range(int(self.lines_number)):
    #         time.sleep(0.1) 
    #         self.current_line += 1
    #         self.update()
            

    def paintEvent(self, event):
        
        self.thickness = self.lineEdit.text()
        self.delay = self.lineEdit_2.text()
        self.lines_number = self.lineEdit_3.text()
        
        self.step = int(500 / int(self.lines_number))
         
        painter = QPainter(self)
        painter.setPen(Qt.black)

        painter.drawLine(self.begin_x, self.end_y, self.end_x, self.end_y) # x-axis
        print(self.counter)
        for i in range(int(self.lines_number)):
            painter.drawLine(self.begin_x, self.begin_y + i * self.step, self.begin_x  + i * self.step ,self.end_y)
        self.counter += 1
            
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    qw = DrawArea()
    qw.show()   
    sys.exit(app.exec_())

