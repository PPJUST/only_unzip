# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_v1 ԭ�ļ�pxjqih.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class MyLabel(QLabel):
    dropSignal = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)  # 设置可拖入

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            drop_path = [url.toLocalFile() for url in urls]  # 获取多个文件的路径的列表
            self.dropSignal.emit(drop_path)  # 发送文件列表信号

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(292, 254)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFrameShape(QFrame.NoFrame)
        self.splitter.setLineWidth(1)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(0)
        self.splitter.setChildrenCollapsible(True)
        self.button_page_main = QPushButton(self.splitter)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.button_page_main)
        self.button_page_main.setObjectName(u"button_page_main")
        self.button_page_main.setMinimumSize(QSize(0, 50))
        self.button_page_main.setMaximumSize(QSize(16777215, 16777215))
        self.button_page_main.setAutoRepeat(False)
        self.button_page_main.setAutoDefault(False)
        self.button_page_main.setFlat(False)
        self.splitter.addWidget(self.button_page_main)
        self.button_page_password = QPushButton(self.splitter)
        self.buttonGroup.addButton(self.button_page_password)
        self.button_page_password.setObjectName(u"button_page_password")
        self.button_page_password.setMinimumSize(QSize(0, 50))
        self.button_page_password.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.addWidget(self.button_page_password)
        self.button_page_setting = QPushButton(self.splitter)
        self.buttonGroup.addButton(self.button_page_setting)
        self.button_page_setting.setObjectName(u"button_page_setting")
        self.button_page_setting.setMinimumSize(QSize(0, 50))
        self.button_page_setting.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.addWidget(self.button_page_setting)

        self.horizontalLayout.addWidget(self.splitter, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setAcceptDrops(False)
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 0)
        self.label_icon = MyLabel(self.page)
        self.label_icon.setObjectName(u"label_icon")
        self.label_icon.setAcceptDrops(True)
        self.label_icon.setFrameShape(QFrame.NoFrame)
        self.label_icon.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_icon)

        self.line_3 = QFrame(self.page)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.splitter_2 = QSplitter(self.page)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_3 = QLabel(self.splitter_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(60, 20))
        self.splitter_2.addWidget(self.label_3)
        self.label_current_file = QLabel(self.splitter_2)
        self.label_current_file.setObjectName(u"label_current_file")
        self.splitter_2.addWidget(self.label_current_file)

        self.verticalLayout_3.addWidget(self.splitter_2)

        self.splitter_3 = QSplitter(self.page)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(self.splitter_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(60, 20))
        self.splitter_3.addWidget(self.label_4)
        self.label_schedule = QLabel(self.splitter_3)
        self.label_schedule.setObjectName(u"label_schedule")
        self.splitter_3.addWidget(self.label_schedule)

        self.verticalLayout_3.addWidget(self.splitter_3)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text_password = QPlainTextEdit(self.page_2)
        self.text_password.setObjectName(u"text_password")

        self.verticalLayout_2.addWidget(self.text_password)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button_update_password = QPushButton(self.page_2)
        self.button_update_password.setObjectName(u"button_update_password")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_update_password.sizePolicy().hasHeightForWidth())
        self.button_update_password.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.button_update_password)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.button_export_password = QPushButton(self.page_2)
        self.button_export_password.setObjectName(u"button_export_password")

        self.verticalLayout.addWidget(self.button_export_password)

        self.button_export_password_with_number = QPushButton(self.page_2)
        self.button_export_password_with_number.setObjectName(u"button_export_password_with_number")

        self.verticalLayout.addWidget(self.button_export_password_with_number)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_model_unzip = QCheckBox(self.page_3)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.checkBox_model_unzip)
        self.checkBox_model_unzip.setObjectName(u"checkBox_model_unzip")

        self.verticalLayout_4.addWidget(self.checkBox_model_unzip)

        self.checkBox_model_test = QCheckBox(self.page_3)
        self.buttonGroup_2.addButton(self.checkBox_model_test)
        self.checkBox_model_test.setObjectName(u"checkBox_model_test")

        self.verticalLayout_4.addWidget(self.checkBox_model_test)

        self.line = QFrame(self.page_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.checkBox_delect_zip = QCheckBox(self.page_3)
        self.checkBox_delect_zip.setObjectName(u"checkBox_delect_zip")

        self.verticalLayout_4.addWidget(self.checkBox_delect_zip)

        self.line_2 = QFrame(self.page_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.checkBox_nested_folders = QCheckBox(self.page_3)
        self.checkBox_nested_folders.setObjectName(u"checkBox_nested_folders")
        self.checkBox_nested_folders.setChecked(False)

        self.verticalLayout_4.addWidget(self.checkBox_nested_folders)

        self.checkBox_nested_zip = QCheckBox(self.page_3)
        self.checkBox_nested_zip.setObjectName(u"checkBox_nested_zip")

        self.verticalLayout_4.addWidget(self.checkBox_nested_zip)

        self.checkBox_check_zip = QCheckBox(self.page_3)
        self.checkBox_check_zip.setObjectName(u"checkBox_check_zip")
        self.checkBox_check_zip.setChecked(False)

        self.verticalLayout_4.addWidget(self.checkBox_check_zip)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.button_page_main.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_page_main.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875\u9762", None))
        self.button_page_password.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\u6846", None))
        self.button_page_setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label_icon.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u6807", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6587\u4ef6\uff1a", None))
        self.label_current_file.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u6587\u4ef6", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5ea6\uff1a", None))
        self.label_schedule.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u8fdb\u5ea6", None))
        self.button_update_password.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None))
        self.button_export_password.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.button_export_password_with_number.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa(\u542b\u6b21\u6570)", None))
        self.checkBox_model_unzip.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u538b\u6a21\u5f0f", None))
        self.checkBox_model_test.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u6a21\u5f0f", None))
        self.checkBox_delect_zip.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u5220\u9664\u539f\u6587\u4ef6", None))
        self.checkBox_nested_folders.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u5904\u7406\u5957\u5a03\u6587\u4ef6\u5939", None))
        self.checkBox_nested_zip.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u5904\u7406\u5957\u5a03\u538b\u7f29\u5305", None))
        self.checkBox_check_zip.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u4ec5\u8bc6\u522b\u538b\u7f29\u5305(\u57fa\u4e8emagic\u5e93)", None))
    # retranslateUi
