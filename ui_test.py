# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'antifascist.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(671, 498)
        self.treeView = QtWidgets.QTreeView(Dialog)
        self.treeView.setGeometry(QtCore.QRect(30, 200, 621, 261))
        self.treeView.setObjectName("treeView")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 151, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 100, 151, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 140, 151, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar.setGeometry(QtCore.QRect(630, 200, 16, 261))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(300, 30, 351, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "srgan"))
        self.pushButton_2.setText(_translate("Dialog", "esrgan"))
        self.pushButton_3.setText(_translate("Dialog", "esrgan with cyclegan"))
