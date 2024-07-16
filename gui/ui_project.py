from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 649)
        MainWindow.setStyleSheet("background-color:rgb(245, 250, 254)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(16, 15, 25);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -10, 1041, 101))
        self.widget.setStyleSheet("QWidget{\n"
"background-color: rgb(31, 29, 51);\n"
"}\n"
"QPushButton{\n"
"    color:white;\n"
"    text-align:center;\n"
"    height:100%;\n"
"    border:none;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    background-color: #f5f5f5;\n"
"    color: black;\n"
"    padding: 5px;\n"
"}")
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 1041, 104))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchBar = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.searchBar.setFont(font)
        self.searchBar.setObjectName("searchBar")
        self.horizontalLayout.addWidget(self.searchBar)
        self.searchButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("QPushButton:pressed {\n"
"    background-color:rgb(16, 15, 25);\n"
"}\n"
"")
        self.searchButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/search-13-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 100, 221, 551))
        self.widget_2.setStyleSheet("QWidget{\n"
"background-color: rgb(31, 29, 51);\n"
"}\n"
"QPushButton{\n"
"    color:white;\n"
"    text-align:center;\n"
"    height:100%;\n"
"    border:none;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: rgb(16, 15, 25);\n"
"}\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.statisticaButton = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.statisticaButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/pie-chart-5-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statisticaButton.setIcon(icon1)
        self.statisticaButton.setCheckable(True)
        self.statisticaButton.setAutoExclusive(True)
        self.statisticaButton.setObjectName("statisticaButton")
        self.verticalLayout.addWidget(self.statisticaButton)
        self.pozitiveButton = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pozitiveButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/positive-dynamic-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pozitiveButton.setIcon(icon2)
        self.pozitiveButton.setCheckable(True)
        self.pozitiveButton.setAutoExclusive(True)
        self.pozitiveButton.setObjectName("pozitiveButton")
        self.verticalLayout.addWidget(self.pozitiveButton)
        self.negativeButton = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.negativeButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/negative-dynamic-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.negativeButton.setIcon(icon3)
        self.negativeButton.setCheckable(True)
        self.negativeButton.setAutoExclusive(True)
        self.negativeButton.setObjectName("negativeButton")
        self.verticalLayout.addWidget(self.negativeButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 112, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.setariButton = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.setariButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/settings-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setariButton.setIcon(icon4)
        self.setariButton.setCheckable(True)
        self.setariButton.setAutoExclusive(True)
        self.setariButton.setObjectName("setariButton")
        self.verticalLayout_2.addWidget(self.setariButton)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(219, 99, 821, 551))
        self.stackedWidget.setStyleSheet("QWidget{\n"
"    background-color: rgb(16, 15, 25);\n"
"}\n"
"QLabel {\n"
"    color: white;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    background-color: #f5f5f5;\n"
"    color: black;\n"
"    padding: 5px;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.statisticaPage = QtWidgets.QWidget()
        self.statisticaPage.setObjectName("statisticaPage")
        self.stackedWidget.addWidget(self.statisticaPage)
        self.pozitivePage = QtWidgets.QWidget()
        self.pozitivePage.setObjectName("pozitivePage")
        self.stackedWidget.addWidget(self.pozitivePage)
        self.negativePage = QtWidgets.QWidget()
        self.negativePage.setObjectName("negativePage")
        self.label_3 = QtWidgets.QLabel(self.negativePage)
        self.label_3.setGeometry(QtCore.QRect(380, 260, 101, 41))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.negativePage)
        self.setariPage = QtWidgets.QWidget()
        self.setariPage.setStyleSheet("QLable{\n"
"text-align:center;\n"
"}")
        self.setariPage.setObjectName("setariPage")
        self.layoutWidget1 = QtWidgets.QWidget(self.setariPage)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 90, 431, 221))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 30)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"    text-align:center;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.usernameBar = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usernameBar.setFont(font)
        self.usernameBar.setObjectName("usernameBar")
        self.horizontalLayout_3.addWidget(self.usernameBar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(64)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.emailBar = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.emailBar.setFont(font)
        self.emailBar.setObjectName("emailBar")
        self.horizontalLayout_4.addWidget(self.emailBar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(48)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.parolaBar = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parolaBar.setFont(font)
        self.parolaBar.setObjectName("parolaBar")
        self.horizontalLayout_5.addWidget(self.parolaBar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.layoutWidget2 = QtWidgets.QWidget(self.setariPage)
        self.layoutWidget2.setGeometry(QtCore.QRect(170, 360, 431, 111))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.salveazaButon = QtWidgets.QPushButton(self.layoutWidget2)
        self.salveazaButon.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.salveazaButon.setFont(font)
        self.salveazaButon.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    text-align:center;\n"
"    height:100%;\n"
"    background-color:rgb(31, 29, 51);\n"
"}")
        self.salveazaButon.setAutoRepeatDelay(300)
        self.salveazaButon.setObjectName("salveazaButon")
        self.horizontalLayout_6.addWidget(self.salveazaButon)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.stackedWidget.addWidget(self.setariPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.statisticaButton.setText(_translate("MainWindow", "Statistica"))
        self.pozitiveButton.setText(_translate("MainWindow", "Pozitive"))
        self.negativeButton.setText(_translate("MainWindow", "Negative"))
        self.setariButton.setText(_translate("MainWindow", "Setari"))
        self.label_3.setText(_translate("MainWindow", "NEGATIVE"))
        self.label_4.setText(_translate("MainWindow", "CONT TWITTER:"))
        self.label_5.setText(_translate("MainWindow", "USERNAME: "))
        self.label_6.setText(_translate("MainWindow", "EMAIL:"))
        self.label_7.setText(_translate("MainWindow", "PAROLA:"))
        self.salveazaButon.setText(_translate("MainWindow", "SALVEAZA"))
import gui.resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
