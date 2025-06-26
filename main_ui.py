# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSplitter, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        Form.setStyleSheet(u"/* Styles pour le conteneur info_frame */\n"
"#info_frame {\n"
"  background-color: #1e1e1e; /* gris fonc\u00e9 / quasi noir */\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"/* Style g\u00e9n\u00e9ral des labels, champs de texte, boutons, etc. */\n"
"#info_frame QLabel,\n"
"#info_frame QLineEdit,\n"
"#info_frame QComboBox,\n"
"#function_frame QPushButton,\n"
"QHeaderView::section {\n"
"  font-family: Segoe UI Semibold;\n"
"  font-size: 12px;\n"
"  color: #f0f0f0; /* texte clair sur fond fonc\u00e9 */\n"
"}\n"
"\n"
"/* Champs de saisie et bo\u00eetes d\u00e9roulantes */\n"
"#info_frame QLineEdit,\n"
"#info_frame QComboBox {\n"
"  padding: 4px 5px;\n"
"  background-color: #2a2a2a;\n"
"  border: 1px solid #5a5a5a;\n"
"  border-radius: 2px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"/* Styles quand le champ a le focus */\n"
"#info_frame QLineEdit:focus,\n"
"#info_frame QComboBox:focus {\n"
"  border-color: #3399ff;\n"
"}\n"
"\n"
"/* Partie d\u00e9roulante des ComboBox */\n"
"QComboBox::drop-down {\n"
"  b"
                        "ackground: transparent;\n"
"  border: none;\n"
"  margin-right: 5px;\n"
"}\n"
"\n"
"/* Fl\u00e8che de ComboBox */\n"
"QComboBox::down-arrow {\n"
"  image: url(:/icons/expand_more_light.svg); /* Utilise une ic\u00f4ne claire adapt\u00e9e au dark mode */\n"
"}\n"
"\n"
"/* Frame de r\u00e9sultats */\n"
"#result_frame {\n"
"  background-color: #1e1e1e;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"/* Tableau */\n"
"QTableWidget {\n"
"  border-radius: 5px;\n"
"  border: 1px solid #3a3a3a;\n"
"  background-color: #121212;\n"
"  color: #e0e0e0;\n"
"}\n"
"\n"
"/* En-t\u00eate de tableau */\n"
"QHeaderView::section {\n"
"  border: none;\n"
"  border-bottom: 1px solid #3399ff;\n"
"  background-color: #1c1c1c;\n"
"  color: #dcdcdc;\n"
"  text-align: left;\n"
"  padding: 3px 5px;\n"
"}\n"
"\n"
"/* \u00c9l\u00e9ments du tableau */\n"
"QTableWidget::item {\n"
"  border-bottom: 1px solid #3399ff;\n"
"  padding-left: 5px;\n"
"  color: #ffffff;\n"
"}")
        self.centralwidget = QWidget(Form)
        self.centralwidget.setObjectName(u"centralwidget")
        self.info_frame = QFrame(self.centralwidget)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setGeometry(QRect(30, 100, 751, 111))
        self.info_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.splitter_7 = QSplitter(self.info_frame)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setGeometry(QRect(80, 20, 575, 79))
        self.splitter_7.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_3 = QSplitter(self.splitter_7)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.splitter = QSplitter(self.splitter_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.label_6 = QLabel(self.splitter)
        self.label_6.setObjectName(u"label_6")
        self.splitter.addWidget(self.label_6)
        self.label_5 = QLabel(self.splitter)
        self.label_5.setObjectName(u"label_5")
        self.splitter.addWidget(self.label_5)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.splitter.addWidget(self.label)
        self.splitter_3.addWidget(self.splitter)
        self.splitter_2 = QSplitter(self.splitter_3)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.lineEdit_2 = QLineEdit(self.splitter_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.splitter_2.addWidget(self.lineEdit_2)
        self.lineEdit = QLineEdit(self.splitter_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.splitter_2.addWidget(self.lineEdit)
        self.lineEdit_4 = QLineEdit(self.splitter_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.splitter_2.addWidget(self.lineEdit_4)
        self.splitter_3.addWidget(self.splitter_2)
        self.splitter_7.addWidget(self.splitter_3)
        self.splitter_6 = QSplitter(self.splitter_7)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_4 = QSplitter(self.splitter_6)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Orientation.Vertical)
        self.label_2 = QLabel(self.splitter_4)
        self.label_2.setObjectName(u"label_2")
        self.splitter_4.addWidget(self.label_2)
        self.label_3 = QLabel(self.splitter_4)
        self.label_3.setObjectName(u"label_3")
        self.splitter_4.addWidget(self.label_3)
        self.label_7 = QLabel(self.splitter_4)
        self.label_7.setObjectName(u"label_7")
        self.splitter_4.addWidget(self.label_7)
        self.splitter_6.addWidget(self.splitter_4)
        self.splitter_5 = QSplitter(self.splitter_6)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Orientation.Vertical)
        self.lineEdit_5 = QLineEdit(self.splitter_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.splitter_5.addWidget(self.lineEdit_5)
        self.comboBox = QComboBox(self.splitter_5)
        self.comboBox.setObjectName(u"comboBox")
        self.splitter_5.addWidget(self.comboBox)
        self.comboBox_2 = QComboBox(self.splitter_5)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.splitter_5.addWidget(self.comboBox_2)
        self.splitter_6.addWidget(self.splitter_5)
        self.splitter_7.addWidget(self.splitter_6)
        self.function_frame = QFrame(self.centralwidget)
        self.function_frame.setObjectName(u"function_frame")
        self.function_frame.setGeometry(QRect(30, 230, 751, 51))
        self.function_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.function_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.delete_btn = QPushButton(self.function_frame)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setGeometry(QRect(600, 10, 90, 30))
        icon = QIcon()
        icon.addFile(u"icons/delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_btn.setIcon(icon)
        self.add_btn = QPushButton(self.function_frame)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(20, 10, 90, 30))
        icon1 = QIcon()
        icon1.addFile(u"icons/add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_btn.setIcon(icon1)
        self.add_btn.setIconSize(QSize(20, 20))
        self.search_btn = QPushButton(self.function_frame)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(370, 10, 90, 30))
        icon2 = QIcon()
        icon2.addFile(u"icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_btn.setIcon(icon2)
        self.select_btn = QPushButton(self.function_frame)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setGeometry(QRect(255, 10, 90, 30))
        icon3 = QIcon()
        icon3.addFile(u"icons/select.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.select_btn.setIcon(icon3)
        self.update_btn = QPushButton(self.function_frame)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setGeometry(QRect(140, 10, 90, 30))
        icon4 = QIcon()
        icon4.addFile(u"icons/update.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.update_btn.setIcon(icon4)
        self.clear_btn = QPushButton(self.function_frame)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(485, 10, 90, 30))
        icon5 = QIcon()
        icon5.addFile(u"icons/clear.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clear_btn.setIcon(icon5)
        self.result_frame = QFrame(self.centralwidget)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setGeometry(QRect(30, 300, 751, 201))
        self.result_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.result_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.tableWidget = QTableWidget(self.result_frame)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 30, 681, 131))
        self.tableWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(29, 20, 751, 61))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(10, 0, 701, 51))
        font = QFont()
        font.setFamilies([u"Script MT"])
        font.setPointSize(30)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Form.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Form)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        Form.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Form)
        self.statusbar.setObjectName(u"statusbar")
        Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Student ID", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.label.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"State", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"City", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Email Address", None))
        self.delete_btn.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.add_btn.setText(QCoreApplication.translate("Form", u"Add", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.select_btn.setText(QCoreApplication.translate("Form", u"Select", None))
        self.update_btn.setText(QCoreApplication.translate("Form", u"Update", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"Clear", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Studend ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"First Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Last Name", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"City", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"State", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Email Address", None));
        self.title_label.setText(QCoreApplication.translate("Form", u"Students Information System", None))
    # retranslateUi

