# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifydatetime.ui'
#
# Created: Wed Dec 12 13:28:52 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DateTimeDialog(object):
    def setupUi(self, DateTimeDialog):
        DateTimeDialog.setObjectName("DateTimeDialog")
        DateTimeDialog.resize(509, 452)
        self.buttonBox = QtGui.QDialogButtonBox(DateTimeDialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 410, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.qddatettime_frame = QtGui.QFrame(DateTimeDialog)
        self.qddatettime_frame.setGeometry(QtCore.QRect(9, 120, 481, 141))
        self.qddatettime_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qddatettime_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.qddatettime_frame.setObjectName("qddatettime_frame")
        self.gridLayoutWidget = QtGui.QWidget(self.qddatettime_frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 441, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.qddatetime_gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.qddatetime_gridLayout.setContentsMargins(10, 10, -1, -1)
        self.qddatetime_gridLayout.setObjectName("qddatetime_gridLayout")
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.qddatetime_gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.qddatetime_gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.qddatetime_gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.qddt_modifydate = QtGui.QLineEdit(self.gridLayoutWidget)
        self.qddt_modifydate.setMaximumSize(QtCore.QSize(180, 16777215))
        self.qddt_modifydate.setObjectName("qddt_modifydate")
        self.qddatetime_gridLayout.addWidget(self.qddt_modifydate, 1, 1, 1, 1)
        self.chk_qddt_modifydate = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chk_qddt_modifydate.setText("")
        self.chk_qddt_modifydate.setChecked(True)
        self.chk_qddt_modifydate.setObjectName("chk_qddt_modifydate")
        self.qddatetime_gridLayout.addWidget(self.chk_qddt_modifydate, 1, 3, 1, 1)
        self.qddt_datetimeoriginal = QtGui.QLineEdit(self.gridLayoutWidget)
        self.qddt_datetimeoriginal.setMaximumSize(QtCore.QSize(180, 16777215))
        self.qddt_datetimeoriginal.setObjectName("qddt_datetimeoriginal")
        self.qddatetime_gridLayout.addWidget(self.qddt_datetimeoriginal, 2, 1, 1, 1)
        self.qddt_createdate = QtGui.QLineEdit(self.gridLayoutWidget)
        self.qddt_createdate.setMaximumSize(QtCore.QSize(180, 16777215))
        self.qddt_createdate.setObjectName("qddt_createdate")
        self.qddatetime_gridLayout.addWidget(self.qddt_createdate, 3, 1, 1, 1)
        self.chk_qddt_datetimeoriginal = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chk_qddt_datetimeoriginal.setText("")
        self.chk_qddt_datetimeoriginal.setChecked(True)
        self.chk_qddt_datetimeoriginal.setObjectName("chk_qddt_datetimeoriginal")
        self.qddatetime_gridLayout.addWidget(self.chk_qddt_datetimeoriginal, 2, 3, 1, 1)
        self.chk_qddt_createdate = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chk_qddt_createdate.setText("")
        self.chk_qddt_createdate.setChecked(True)
        self.chk_qddt_createdate.setObjectName("chk_qddt_createdate")
        self.qddatetime_gridLayout.addWidget(self.chk_qddt_createdate, 3, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.qddatetime_gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.qddatetime_gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.chk_qddt_updatexmp = QtGui.QCheckBox(DateTimeDialog)
        self.chk_qddt_updatexmp.setGeometry(QtCore.QRect(10, 390, 351, 17))
        self.chk_qddt_updatexmp.setObjectName("chk_qddt_updatexmp")
        self.qddt_lbl = QtGui.QLabel(DateTimeDialog)
        self.qddt_lbl.setGeometry(QtCore.QRect(12, 10, 471, 91))
        self.qddt_lbl.setWordWrap(True)
        self.qddt_lbl.setObjectName("qddt_lbl")
        self.frame = QtGui.QFrame(DateTimeDialog)
        self.frame.setGeometry(QtCore.QRect(10, 280, 481, 91))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget_2 = QtGui.QWidget(self.frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 471, 62))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setContentsMargins(10, 10, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.chk_qddt_forward = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.chk_qddt_forward.setObjectName("chk_qddt_forward")
        self.gridLayout.addWidget(self.chk_qddt_forward, 1, 2, 1, 1)
        self.qddt_shiftdatetime = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.qddt_shiftdatetime.setMaximumSize(QtCore.QSize(180, 16777215))
        self.qddt_shiftdatetime.setObjectName("qddt_shiftdatetime")
        self.gridLayout.addWidget(self.qddt_shiftdatetime, 1, 1, 1, 1)
        self.chk_qddt_shift = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.chk_qddt_shift.setObjectName("chk_qddt_shift")
        self.gridLayout.addWidget(self.chk_qddt_shift, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.retranslateUi(DateTimeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DateTimeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DateTimeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DateTimeDialog)

    def retranslateUi(self, DateTimeDialog):
        DateTimeDialog.setWindowTitle(QtGui.QApplication.translate("DateTimeDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DateTimeDialog", "ModifyDate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DateTimeDialog", "DateTimeOriginal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DateTimeDialog", "CreateDate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DateTimeDialog", "YYYY:MM:DD hh:mm:ss", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DateTimeDialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_qddt_updatexmp.setText(QtGui.QApplication.translate("DateTimeDialog", "Update xmp values as well", None, QtGui.QApplication.UnicodeUTF8))
        self.qddt_lbl.setText(QtGui.QApplication.translate("DateTimeDialog", "This dialog gives you the option to modify the several date/time tags in the exif information. It works on the selected images.\n"
"You can also use the Shift function to shift the date/time forward or backward (in the future or in the past) for the selected fields and the selected images.\n"
"The corresponding xmp values can be updated at the same time.", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_qddt_forward.setText(QtGui.QApplication.translate("DateTimeDialog", "forward in time", None, QtGui.QApplication.UnicodeUTF8))
        self.qddt_shiftdatetime.setToolTip(QtGui.QApplication.translate("DateTimeDialog", "This field determines the shift in YYYY:MM:DD hh:mm:ss", None, QtGui.QApplication.UnicodeUTF8))
        self.qddt_shiftdatetime.setStatusTip(QtGui.QApplication.translate("DateTimeDialog", "This field determines the shift in YYYY:MM:DD hh:mm:ss", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_qddt_shift.setText(QtGui.QApplication.translate("DateTimeDialog", "shift above date/times", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DateTimeDialog", "shift value", None, QtGui.QApplication.UnicodeUTF8))

