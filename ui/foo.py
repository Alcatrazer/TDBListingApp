
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,comboBoxModel):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #combo box code
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 20, 171, 34))
        self.comboBox.setObjectName("comboBox")
        
        # supply model and sort it
        self.model = comboBoxModel
        self.sortModel = QtCore.QSortFilterProxyModel()
        self.sortModel.setSourceModel(self.model)
        #self.sortModel.sort(0) # sort ascending is default # = #1
        #self.sortModel.sort(1) # sort ascending is default # = #2
        #self.sortModel.sort(0,QtCore.Qt.AscendingOrder) # sort ascending is default # = #3
        self.sortModel.sort(1,QtCore.Qt.DescendingOrder) # sort ascending is default # = #4

        #bind model to combobox
        self.comboBox.setModel(self.sortModel)
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))




if __name__ == "__main__":
    import sys
    def init_model():
        data = ["SAGE Response","HarperCollins",  "SAGE Select", "Pratham Books"]
        model = QtCore.QStringListModel(data)
        return model
    
    def main():
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        model = init_model()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow,model)
        MainWindow.show()
        sys.exit(app.exec_())
    
    main()
