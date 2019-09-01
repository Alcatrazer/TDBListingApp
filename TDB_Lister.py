#! /usr/bin/python3


from PyQt5 import uic, QtWidgets,QtCore, QtGui
import TDBInputView
import sys
import signal


if __name__ == '__main__':
    
    """
    <begin>
    By default you cannot kill a QT app from the shell. This class allows you to periodically cede control back to python so that it can 
    respond to keyboard interrupts id run from the shell.

    License:GPL
    Credit: altendky for the original idea see https://github.com/altendky/stlib/blob/master/epyqlib/utils/qt.py#L1125-L1137
    """
    
    def sigint_handler(signal_number, stack_frame):
        QtWidgets.QApplication.exit(128 + signal_number)


    def setup_sigint():
        signal.signal(signal.SIGINT, sigint_handler)

        # Regularly give Python a chance to receive signals such as ctrl+c
        timer = QtCore.QTimer()
        timer.start(200)
        timer.timeout.connect(lambda: None)

        return timer
    """
    <end>
    """
    def init_all_publisher_model():
        data = ["SAGE Response","HarperCollins", "Pratham Books","SAGE Select","A very long publisher publisher publisher publisher  publisher"]
        model = QtCore.QStringListModel(data)
        return model

    def init_bk_publisher_model():
        data = []
        model = QtCore.QStringListModel(data)
        return model

    def init_contributors_model():
        data = [[1,2],[3,4]]
        model = QtGui.QStandardItemModel(0,2)
        model.setHeaderData(0,QtCore.Qt.Horizontal,"Type")
        model.setHeaderData(1,QtCore.Qt.Horizontal,"Value")
        """
        r_num =  0
        for row in data:
            item = QtGui.QStandardItem("item ({},{})".format((row[0]), row[1]))
            print(item)
            for i in range(len(row)):
                print("({},{})".format(r_num,i))
                model.setItem(r_num,i,item)
            r_num += 1
        """
        return model

    def main():
        app = QtWidgets.QApplication(sys.argv)
        allpublisherModel = init_all_publisher_model()
        bkpublishermodel = init_bk_publisher_model()
        contributorsmodel = init_contributors_model()
        window = TDBInputView.MainInput(allpublisherModel,bkpublishermodel,contributorsmodel)
        # call the sigint handler
        setup_sigint()
        window.show()
        sys.exit(app.exec_())

    # call it
    main()
