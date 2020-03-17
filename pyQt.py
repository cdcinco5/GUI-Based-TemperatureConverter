import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from decimal import Decimal

# Depends on the path of the ui file
qtcreator_file  = '/home/cdcinco/Desktop/Local Repo/GUI-Based-TemperatureConverter/UI/TempConvert.ui' # ui file here
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.FahConvert.clicked.connect(self.FahtoCel)
        self.CelConvert.clicked.connect(self.CeltoFah)
        
    def FahtoCel(self):
        tempC = Decimal((self.Fahrenheit.toPlainText()-32)*5/9,1)
        self.Celsius.setPlainText(str(tempC))


    def CeltoFah(self):
        tempF = Decimal((self.Celsius.toPlainText())*9/5+32,1)
        self.Fahrenheit.setPlainText(str(tempF))
           

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())