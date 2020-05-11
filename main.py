from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import *
import sys
import imaplib
import getpass
import email
import email.header
import time
import os


EMAIL_ACCOUNT = "xxxxxxxx"
EMAIL_PASSWORD = "xxxxxxx"
EMAIL_FOLDER = "Inbox"
coord = 0
space0 = "" 
space1 = "" 
space2 = "" 
space3 = "" 
space4 = "" 
space5 = "" 
space6 = "" 
space7 = "" 
space8 = "" 
space9 = "" 
space0b = "" 
space1b = "" 
space2b = "" 
space3b = "" 
space4b = "" 
space5b = "" 
space6b = "" 
space7b = "" 
space8b = "" 
space9b = "" 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(220, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 220, 350))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        itema = 0
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Property"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("MainWindow", ""))
        self.tableWidget.setSortingEnabled(__sortingEnabled)



    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    def process_mailbox():
        global coord
        global space0
        global space1
        global space2
        global space3
        global space4
        global space5
        global space6
        global space7
        global space8 
        global space9
        global space0b
        global space1b
        global space2b
        global space3b
        global space4b
        global space5b 
        global space6b
        global space7b 
        global space8b 
        global space9b
        M = imaplib.IMAP4_SSL('outlook.office365.com')
        try:
            rv, data = M.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        except imaplib.IMAP4.error:
            print ("LOGIN FAILED!!! ")
            sys.exit(1)
        rv, data = M.select(EMAIL_FOLDER)
        if rv == 'OK':
            print("Processing mailbox...\n")
            rv, data = M.search(None, "(UNSEEN)")
            if rv != 'OK':
                print("No messages found!")
                return
            else:
                for num in data[0].split():
                    rv, data = M.fetch(num, '(RFC822)')
                    if rv != 'OK':
                        print("ERROR getting message", num)
                        return
                    else:
                        msg = email.message_from_bytes(data[0][1])
                        hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
                        subject = str(hdr)
                        split_message = subject.split("-----")
                        ui_update1 = str(split_message[1])
                        ui_update2 = str(split_message[0])
                        alist = [space0, space1, space2, space3, space4, space5, space6, space7, space8, space9]
                        blist = [space0b, space1b, space2b, space3b, space4b, space5b, space6b, space7b, space8b, space9b]
                        if space9 != "":
                            space0 = space1
                            space1 = space2
                            space2 = space3
                            space3 = space4
                            space4 = space5
                            space5 = space6
                            space6 = space7
                            space7 = space8
                            space8 = space9
                            space9 = ui_update1
                            space0b = space1b
                            space1b = space2b
                            space2b = space3b
                            space3b = space4b
                            space4b = space5b
                            space5b = space6b
                            space6b = space7b
                            space7b = space8b
                            space8b = space9b
                            space9b = ui_update2
                        for i in alist:
                            if i == "":
                                if i  == space0:
                                    space0 = ui_update1
                                elif i  == space1:
                                    space1 = ui_update1
                                elif i  == space2:
                                    space2 = ui_update1
                                elif i  == space3:
                                    space3 = ui_update1
                                elif i  == space4:
                                    space4 = ui_update1
                                elif i  == space5:
                                    space5 = ui_update1
                                elif i  == space6:
                                    space6 = ui_update1
                                elif i  == space7:
                                    space7 = ui_update1
                                elif i  == space8:
                                    space8 = ui_update1
                                elif i  == space9:
                                    space9 = ui_update1
                                break
                            else:
                                pass
                        for i in blist:
                            if i == "":
                                if i  == space0b:
                                    space0b = ui_update2
                                elif i  == space1b:
                                    space1b = ui_update2
                                elif i  == space2b:
                                    space2b = ui_update2
                                elif i  == space3b:
                                    space3b = ui_update2
                                elif i  == space4b:
                                    space4b = ui_update2
                                elif i  == space5b:
                                    space5b = ui_update2
                                elif i  == space6b:
                                    space6b = ui_update2
                                elif i  == space7b:
                                    space7b = ui_update2
                                elif i  == space8b:
                                    space8b = ui_update2
                                elif i  == space9b:
                                    space9b = ui_update2
                                break
                            else:
                                pass
                        ui.tableWidget.item(0,0).setText(space0)
                        ui.tableWidget.item(0,1).setText(space0b)
                        ui.tableWidget.item(1,0).setText(space1)
                        ui.tableWidget.item(1,1).setText(space1b)
                        ui.tableWidget.item(2,0).setText(space2)
                        ui.tableWidget.item(2,1).setText(space2b)
                        ui.tableWidget.item(3,0).setText(space3)
                        ui.tableWidget.item(3,1).setText(space3b)
                        ui.tableWidget.item(4,0).setText(space4)
                        ui.tableWidget.item(4,1).setText(space4b)
                        ui.tableWidget.item(5,0).setText(space5)
                        ui.tableWidget.item(5,1).setText(space5b)
                        ui.tableWidget.item(6,0).setText(space6)
                        ui.tableWidget.item(6,1).setText(space6b)
                        ui.tableWidget.item(7,0).setText(space7)
                        ui.tableWidget.item(7,1).setText(space7b)
                        ui.tableWidget.item(8,0).setText(space8)
                        ui.tableWidget.item(8,1).setText(space8b)
                        ui.tableWidget.item(9,0).setText(space9)
                        ui.tableWidget.item(9,1).setText(space9b)
                        if coord < 9:
                            coord +=1
                        else:
                            coord = 0
                            coord +=1
                        

                os.system('cls')
                M.logout()
        else:
            print("ERROR: Unable to open mailbox ", rv)
    timer = QtCore.QTimer()
    timer.timeout.connect(process_mailbox)
    timer.start(5000)
    sys.exit(app.exec_())
