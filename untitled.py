# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.timex_list = QtWidgets.QListView(self.centralwidget)
        self.timex_list.setGeometry(QtCore.QRect(710, 0, 351, 801))
        self.timex_list.setObjectName("timex_list")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(400, 470, 121, 51))
        self.start.setObjectName("start")
        self.close1 = QtWidgets.QPushButton(self.centralwidget)
        self.close1.setGeometry(QtCore.QRect(10, 580, 321, 101))
        self.close1.setObjectName("close1")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 711, 197))
        self.calendarWidget.setObjectName("calendarWidget")
        self.time1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.time1.setGeometry(QtCore.QRect(150, 200, 131, 51))
        self.time1.setObjectName("time1")
        self.end = QtWidgets.QPushButton(self.centralwidget)
        self.end.setGeometry(QtCore.QRect(90, 470, 131, 51))
        self.end.setObjectName("end")
        self.time2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.time2.setGeometry(QtCore.QRect(310, 200, 131, 51))
        self.time2.setObjectName("time2")
        self.close2 = QtWidgets.QPushButton(self.centralwidget)
        self.close2.setGeometry(QtCore.QRect(350, 580, 311, 101))
        self.close2.setObjectName("close2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 210, 101, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 220, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 220, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 220, 21, 16))
        self.label_4.setObjectName("label_4")
        self.time3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.time3.setGeometry(QtCore.QRect(470, 202, 131, 51))
        self.time3.setObjectName("time3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 270, 101, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 280, 21, 16))
        self.label_6.setObjectName("label_6")
        self.time1_1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.time1_1.setGeometry(QtCore.QRect(150, 270, 131, 51))
        self.time1_1.setObjectName("time1_1")
        self.time2_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.time2_2.setGeometry(QtCore.QRect(310, 270, 131, 51))
        self.time2_2.setObjectName("time2_2")
        self.time3_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.time3_3.setGeometry(QtCore.QRect(470, 270, 131, 51))
        self.time3_3.setObjectName("time3_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 280, 16, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 280, 21, 16))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.close1.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "开始计时"))
        self.close1.setText(_translate("MainWindow", "关闭并不保存"))
        self.end.setText(_translate("MainWindow", "结束计时"))
        self.close2.setText(_translate("MainWindow", "关闭并保存"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#00aa00;\">开始时间</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">时</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">分</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">秒</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#00aa00;\">已用时间</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">时</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">分</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">秒</span></p></body></html>"))
