# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './main_input.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(389, 790)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lineEditISBN = QtWidgets.QLineEdit(self.tab)
        self.lineEditISBN.setObjectName("lineEditISBN")
        self.horizontalLayout_4.addWidget(self.lineEditISBN)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEditTitle = QtWidgets.QLineEdit(self.tab)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.horizontalLayout.addWidget(self.lineEditTitle)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.comboBoxContribType = QtWidgets.QComboBox(self.tab)
        self.comboBoxContribType.setObjectName("comboBoxContribType")
        self.comboBoxContribType.addItem("")
        self.comboBoxContribType.addItem("")
        self.comboBoxContribType.addItem("")
        self.comboBoxContribType.addItem("")
        self.comboBoxContribType.addItem("")
        self.horizontalLayout_16.addWidget(self.comboBoxContribType)
        self.lineEditContribValue = QtWidgets.QLineEdit(self.tab)
        self.lineEditContribValue.setObjectName("lineEditContribValue")
        self.horizontalLayout_16.addWidget(self.lineEditContribValue)
        self.pushButtonAddContrib = QtWidgets.QPushButton(self.tab)
        self.pushButtonAddContrib.setObjectName("pushButtonAddContrib")
        self.horizontalLayout_16.addWidget(self.pushButtonAddContrib)
        self.gridLayout.addLayout(self.horizontalLayout_16, 14, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 13, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.lineEditTags = QtWidgets.QLineEdit(self.tab)
        self.lineEditTags.setObjectName("lineEditTags")
        self.horizontalLayout_6.addWidget(self.lineEditTags)
        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.comboBoxQtStyles = QtWidgets.QComboBox(self.tab)
        self.comboBoxQtStyles.setObjectName("comboBoxQtStyles")
        self.horizontalLayout_14.addWidget(self.comboBoxQtStyles)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)
        self.toolButton_3 = QtWidgets.QToolButton(self.tab)
        self.toolButton_3.setEnabled(False)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_14.addWidget(self.toolButton_3)
        self.toolButton_4 = QtWidgets.QToolButton(self.tab)
        self.toolButton_4.setEnabled(False)
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_14.addWidget(self.toolButton_4)
        self.gridLayout.addLayout(self.horizontalLayout_14, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.lineEditWidth = QtWidgets.QLineEdit(self.tab)
        self.lineEditWidth.setObjectName("lineEditWidth")
        self.horizontalLayout_7.addWidget(self.lineEditWidth)
        self.label_14 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMaximumSize(QtCore.QSize(20, 51))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.lineEditHeight = QtWidgets.QLineEdit(self.tab)
        self.lineEditHeight.setObjectName("lineEditHeight")
        self.horizontalLayout_7.addWidget(self.lineEditHeight)
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.lineEditDepth = QtWidgets.QLineEdit(self.tab)
        self.lineEditDepth.setObjectName("lineEditDepth")
        self.horizontalLayout_7.addWidget(self.lineEditDepth)
        self.gridLayout.addLayout(self.horizontalLayout_7, 10, 0, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.listViewBkPublishers = QtWidgets.QListView(self.tab)
        self.listViewBkPublishers.setObjectName("listViewBkPublishers")
        self.horizontalLayout_18.addWidget(self.listViewBkPublishers)
        self.pushButtonDeletePublisher = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeletePublisher.sizePolicy().hasHeightForWidth())
        self.pushButtonDeletePublisher.setSizePolicy(sizePolicy)
        self.pushButtonDeletePublisher.setObjectName("pushButtonDeletePublisher")
        self.horizontalLayout_18.addWidget(self.pushButtonDeletePublisher)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButtonMovePublisherUp = QtWidgets.QPushButton(self.tab)
        self.pushButtonMovePublisherUp.setObjectName("pushButtonMovePublisherUp")
        self.verticalLayout_2.addWidget(self.pushButtonMovePublisherUp)
        self.pushButtonMovePublisherDown = QtWidgets.QPushButton(self.tab)
        self.pushButtonMovePublisherDown.setObjectName("pushButtonMovePublisherDown")
        self.verticalLayout_2.addWidget(self.pushButtonMovePublisherDown)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_18.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_18, 9, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEditSubtitle = QtWidgets.QLineEdit(self.tab)
        self.lineEditSubtitle.setObjectName("lineEditSubtitle")
        self.horizontalLayout_2.addWidget(self.lineEditSubtitle)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBoxBinding = QtWidgets.QComboBox(self.tab)
        self.comboBoxBinding.setObjectName("comboBoxBinding")
        self.comboBoxBinding.addItem("")
        self.comboBoxBinding.addItem("")
        self.comboBoxBinding.addItem("")
        self.comboBoxBinding.addItem("")
        self.comboBoxBinding.addItem("")
        self.comboBoxBinding.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBoxBinding)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEditPageCount = QtWidgets.QLineEdit(self.tab)
        self.lineEditPageCount.setObjectName("lineEditPageCount")
        self.horizontalLayout_3.addWidget(self.lineEditPageCount)
        self.label_Year = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Year.sizePolicy().hasHeightForWidth())
        self.label_Year.setSizePolicy(sizePolicy)
        self.label_Year.setObjectName("label_Year")
        self.horizontalLayout_3.addWidget(self.label_Year)
        self.lineEditYear = QtWidgets.QLineEdit(self.tab)
        self.lineEditYear.setObjectName("lineEditYear")
        self.horizontalLayout_3.addWidget(self.lineEditYear)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_8.addWidget(self.label_16)
        self.lineEditBkWeight = QtWidgets.QLineEdit(self.tab)
        self.lineEditBkWeight.setObjectName("lineEditBkWeight")
        self.horizontalLayout_8.addWidget(self.lineEditBkWeight)
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        self.lineEditPkgWeight = QtWidgets.QLineEdit(self.tab)
        self.lineEditPkgWeight.setObjectName("lineEditPkgWeight")
        self.horizontalLayout_8.addWidget(self.lineEditPkgWeight)
        self.gridLayout.addLayout(self.horizontalLayout_8, 11, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.comboBoxPublishers = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPublishers.sizePolicy().hasHeightForWidth())
        self.comboBoxPublishers.setSizePolicy(sizePolicy)
        self.comboBoxPublishers.setObjectName("comboBoxPublishers")
        self.horizontalLayout_9.addWidget(self.comboBoxPublishers)
        self.pushButtonAddPublisher = QtWidgets.QPushButton(self.tab)
        self.pushButtonAddPublisher.setObjectName("pushButtonAddPublisher")
        self.horizontalLayout_9.addWidget(self.pushButtonAddPublisher)
        self.gridLayout.addLayout(self.horizontalLayout_9, 8, 0, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_19.addWidget(self.label_18)
        self.lineEditPrice = QtWidgets.QLineEdit(self.tab)
        self.lineEditPrice.setObjectName("lineEditPrice")
        self.horizontalLayout_19.addWidget(self.lineEditPrice)
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_19.addWidget(self.label_19)
        self.comboBoxDiscount = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDiscount.sizePolicy().hasHeightForWidth())
        self.comboBoxDiscount.setSizePolicy(sizePolicy)
        self.comboBoxDiscount.setMaximumSize(QtCore.QSize(49, 16777215))
        self.comboBoxDiscount.setObjectName("comboBoxDiscount")
        self.comboBoxDiscount.addItem("")
        self.comboBoxDiscount.addItem("")
        self.comboBoxDiscount.addItem("")
        self.horizontalLayout_19.addWidget(self.comboBoxDiscount)
        self.labelPriceAfterDiscount = QtWidgets.QLabel(self.tab)
        self.labelPriceAfterDiscount.setObjectName("labelPriceAfterDiscount")
        self.horizontalLayout_19.addWidget(self.labelPriceAfterDiscount)
        self.gridLayout.addLayout(self.horizontalLayout_19, 12, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.tableViewContributor = QtWidgets.QTableView(self.tab)
        self.tableViewContributor.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableViewContributor.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableViewContributor.setObjectName("tableViewContributor")
        self.tableViewContributor.horizontalHeader().setVisible(True)
        self.tableViewContributor.horizontalHeader().setDefaultSectionSize(150)
        self.tableViewContributor.horizontalHeader().setHighlightSections(True)
        self.tableViewContributor.verticalHeader().setVisible(True)
        self.horizontalLayout_17.addWidget(self.tableViewContributor)
        self.pushButtonDeleteContrib = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeleteContrib.sizePolicy().hasHeightForWidth())
        self.pushButtonDeleteContrib.setSizePolicy(sizePolicy)
        self.pushButtonDeleteContrib.setObjectName("pushButtonDeleteContrib")
        self.horizontalLayout_17.addWidget(self.pushButtonDeleteContrib)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.pushButtonMoveContribUp = QtWidgets.QPushButton(self.tab)
        self.pushButtonMoveContribUp.setObjectName("pushButtonMoveContribUp")
        self.verticalLayout_3.addWidget(self.pushButtonMoveContribUp)
        self.pushButtonMoveContribDown = QtWidgets.QPushButton(self.tab)
        self.pushButtonMoveContribDown.setObjectName("pushButtonMoveContribDown")
        self.verticalLayout_3.addWidget(self.pushButtonMoveContribDown)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_17.addLayout(self.verticalLayout_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_17, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAcceptDrops(False)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.plainTextEditLongDesc = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEditLongDesc.setObjectName("plainTextEditLongDesc")
        self.gridLayout_2.addWidget(self.plainTextEditLongDesc, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.plainTextEditShortDesc = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEditShortDesc.setObjectName("plainTextEditShortDesc")
        self.gridLayout_2.addWidget(self.plainTextEditShortDesc, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.plainTextEditAboutContribs = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEditAboutContribs.setObjectName("plainTextEditAboutContribs")
        self.gridLayout_2.addWidget(self.plainTextEditAboutContribs, 5, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.toolBox = QtWidgets.QToolBox(self.tab_3)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 96, 96))
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 206, 490))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.pushButtonTDBCopyTags = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonTDBCopyTags.setObjectName("pushButtonTDBCopyTags")
        self.gridLayout_12.addWidget(self.pushButtonTDBCopyTags, 2, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButtonCopyTDBTitle = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonCopyTDBTitle.setObjectName("pushButtonCopyTDBTitle")
        self.horizontalLayout_13.addWidget(self.pushButtonCopyTDBTitle)
        self.pushButtonTDBCopyISBN = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonTDBCopyISBN.setObjectName("pushButtonTDBCopyISBN")
        self.horizontalLayout_13.addWidget(self.pushButtonTDBCopyISBN)
        self.gridLayout_12.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButtonPrevwLongDesc = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonPrevwLongDesc.setObjectName("pushButtonPrevwLongDesc")
        self.horizontalLayout_11.addWidget(self.pushButtonPrevwLongDesc)
        self.pushButtonTDBCopyLongDesc = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonTDBCopyLongDesc.setObjectName("pushButtonTDBCopyLongDesc")
        self.horizontalLayout_11.addWidget(self.pushButtonTDBCopyLongDesc)
        self.gridLayout_10.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButtonPrevwShrtDesc = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonPrevwShrtDesc.setObjectName("pushButtonPrevwShrtDesc")
        self.horizontalLayout_10.addWidget(self.pushButtonPrevwShrtDesc)
        self.pushButtonTDBCopyShortDesc = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonTDBCopyShortDesc.setObjectName("pushButtonTDBCopyShortDesc")
        self.horizontalLayout_10.addWidget(self.pushButtonTDBCopyShortDesc)
        self.gridLayout_11.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButtonPrevwAbtContribs = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonPrevwAbtContribs.setObjectName("pushButtonPrevwAbtContribs")
        self.horizontalLayout_12.addWidget(self.pushButtonPrevwAbtContribs)
        self.pushButtonTDBCopyAboutContribs = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonTDBCopyAboutContribs.setObjectName("pushButtonTDBCopyAboutContribs")
        self.horizontalLayout_12.addWidget(self.pushButtonTDBCopyAboutContribs)
        self.gridLayout_13.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButtonTDBOtherDataPopup = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButtonTDBOtherDataPopup.setObjectName("pushButtonTDBOtherDataPopup")
        self.horizontalLayout_15.addWidget(self.pushButtonTDBOtherDataPopup)
        self.gridLayout_14.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox_6, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.gridLayout_8.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 4, 0, 1, 1)
        self.toolBox.addItem(self.page, "")
        self.gridLayout_9.addWidget(self.toolBox, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_QwikHelp = QtWidgets.QLabel(self.tab_4)
        self.label_QwikHelp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_QwikHelp.setWordWrap(True)
        self.label_QwikHelp.setObjectName("label_QwikHelp")
        self.gridLayout_6.addWidget(self.label_QwikHelp, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_6.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 389, 32))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setEnabled(False)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.label_6.setBuddy(self.lineEditISBN)
        self.label_2.setBuddy(self.lineEditTitle)
        self.label_11.setBuddy(self.lineEditTags)
        self.label_12.setBuddy(self.lineEditWidth)
        self.label_14.setBuddy(self.lineEditHeight)
        self.label_15.setBuddy(self.lineEditDepth)
        self.label_3.setBuddy(self.lineEditSubtitle)
        self.label_4.setBuddy(self.comboBoxBinding)
        self.label_5.setBuddy(self.lineEditPageCount)
        self.label_Year.setBuddy(self.lineEditYear)
        self.label_16.setBuddy(self.lineEditBkWeight)
        self.label_17.setBuddy(self.lineEditPkgWeight)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.lineEditTitle)
        MainWindow.setTabOrder(self.lineEditTitle, self.lineEditSubtitle)
        MainWindow.setTabOrder(self.lineEditSubtitle, self.comboBoxBinding)
        MainWindow.setTabOrder(self.comboBoxBinding, self.lineEditPageCount)
        MainWindow.setTabOrder(self.lineEditPageCount, self.lineEditYear)
        MainWindow.setTabOrder(self.lineEditYear, self.lineEditISBN)
        MainWindow.setTabOrder(self.lineEditISBN, self.lineEditTags)
        MainWindow.setTabOrder(self.lineEditTags, self.comboBoxPublishers)
        MainWindow.setTabOrder(self.comboBoxPublishers, self.lineEditWidth)
        MainWindow.setTabOrder(self.lineEditWidth, self.lineEditHeight)
        MainWindow.setTabOrder(self.lineEditHeight, self.lineEditDepth)
        MainWindow.setTabOrder(self.lineEditDepth, self.lineEditBkWeight)
        MainWindow.setTabOrder(self.lineEditBkWeight, self.lineEditPkgWeight)
        MainWindow.setTabOrder(self.lineEditPkgWeight, self.plainTextEditLongDesc)
        MainWindow.setTabOrder(self.plainTextEditLongDesc, self.plainTextEditShortDesc)
        MainWindow.setTabOrder(self.plainTextEditShortDesc, self.plainTextEditAboutContribs)
        MainWindow.setTabOrder(self.plainTextEditAboutContribs, self.textBrowser)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TDB Lister"))
        self.label_6.setText(_translate("MainWindow", "ISBN:"))
        self.lineEditISBN.setText(_translate("MainWindow", "9789352640645"))
        self.label_2.setText(_translate("MainWindow", "Title:"))
        self.lineEditTitle.setText(_translate("MainWindow", "Title"))
        self.comboBoxContribType.setItemText(0, _translate("MainWindow", "Author"))
        self.comboBoxContribType.setItemText(1, _translate("MainWindow", "Editor"))
        self.comboBoxContribType.setItemText(2, _translate("MainWindow", "Illustrator"))
        self.comboBoxContribType.setItemText(3, _translate("MainWindow", "Translator"))
        self.comboBoxContribType.setItemText(4, _translate("MainWindow", "Contributor"))
        self.pushButtonAddContrib.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "Contributors"))
        self.label_11.setText(_translate("MainWindow", "&Tags:"))
        self.lineEditTags.setText(_translate("MainWindow", "Author1, Publisher,  Tag1, Tag2, Tag3"))
        self.toolButton_3.setText(_translate("MainWindow", "Clear fields"))
        self.toolButton_4.setText(_translate("MainWindow", "set font"))
        self.label_12.setText(_translate("MainWindow", "&Dims (cm):"))
        self.label_13.setText(_translate("MainWindow", "w:"))
        self.lineEditWidth.setText(_translate("MainWindow", "5"))
        self.label_14.setText(_translate("MainWindow", "h:"))
        self.lineEditHeight.setText(_translate("MainWindow", "6"))
        self.label_15.setText(_translate("MainWindow", "d:"))
        self.lineEditDepth.setText(_translate("MainWindow", "0.2"))
        self.pushButtonDeletePublisher.setText(_translate("MainWindow", "-"))
        self.pushButtonMovePublisherUp.setText(_translate("MainWindow", "up"))
        self.pushButtonMovePublisherDown.setText(_translate("MainWindow", "down"))
        self.label_3.setText(_translate("MainWindow", "S&ubtitle:"))
        self.lineEditSubtitle.setText(_translate("MainWindow", "Subtitle"))
        self.label_4.setText(_translate("MainWindow", "Bi&nding:"))
        self.comboBoxBinding.setItemText(0, _translate("MainWindow", "PB"))
        self.comboBoxBinding.setItemText(1, _translate("MainWindow", "HB"))
        self.comboBoxBinding.setItemText(2, _translate("MainWindow", "CS"))
        self.comboBoxBinding.setItemText(3, _translate("MainWindow", "EPUB"))
        self.comboBoxBinding.setItemText(4, _translate("MainWindow", "MOBI"))
        self.comboBoxBinding.setItemText(5, _translate("MainWindow", "PDF"))
        self.label_5.setText(_translate("MainWindow", "Pages"))
        self.lineEditPageCount.setText(_translate("MainWindow", "999"))
        self.label_Year.setText(_translate("MainWindow", "&Year:"))
        self.lineEditYear.setText(_translate("MainWindow", "1999"))
        self.label_16.setText(_translate("MainWindow", "Bk Wgt(&gms):"))
        self.lineEditBkWeight.setText(_translate("MainWindow", "135"))
        self.label_17.setText(_translate("MainWindow", "P&kg Wgt(gms):"))
        self.lineEditPkgWeight.setText(_translate("MainWindow", "150"))
        self.label_7.setText(_translate("MainWindow", "Publisher:"))
        self.pushButtonAddPublisher.setText(_translate("MainWindow", "+"))
        self.label_18.setText(_translate("MainWindow", "Price(Rs):"))
        self.lineEditPrice.setText(_translate("MainWindow", "100"))
        self.label_19.setText(_translate("MainWindow", "Discount%:"))
        self.comboBoxDiscount.setItemText(0, _translate("MainWindow", "10"))
        self.comboBoxDiscount.setItemText(1, _translate("MainWindow", "15"))
        self.comboBoxDiscount.setItemText(2, _translate("MainWindow", "TDB Auto"))
        self.labelPriceAfterDiscount.setText(_translate("MainWindow", "=0(0)"))
        self.pushButtonDeleteContrib.setText(_translate("MainWindow", "-"))
        self.pushButtonMoveContribUp.setText(_translate("MainWindow", "up"))
        self.pushButtonMoveContribDown.setText(_translate("MainWindow", "down"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Basic"))
        self.label_8.setText(_translate("MainWindow", "Long Description"))
        self.plainTextEditLongDesc.setPlainText(_translate("MainWindow", "This is a \n"
"Long Description"))
        self.label_9.setText(_translate("MainWindow", "Short Description"))
        self.plainTextEditShortDesc.setPlainText(_translate("MainWindow", "This is a\n"
"Short Description"))
        self.label_10.setText(_translate("MainWindow", "About Contributors"))
        self.plainTextEditAboutContribs.setPlainText(_translate("MainWindow", "Cotributor 1 is an author.\n"
"\n"
"Contributor 2 is an illustrator.\n"
"\n"
"Cotributor 3 is an author."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Paragraphs"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Title"))
        self.pushButtonTDBCopyTags.setText(_translate("MainWindow", "Copy tags"))
        self.pushButtonCopyTDBTitle.setText(_translate("MainWindow", "Copy Title"))
        self.pushButtonTDBCopyISBN.setText(_translate("MainWindow", "Copy isbn"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Long Desc"))
        self.pushButtonPrevwLongDesc.setText(_translate("MainWindow", "Preview"))
        self.pushButtonTDBCopyLongDesc.setText(_translate("MainWindow", "Copy"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Short Desc"))
        self.pushButtonPrevwShrtDesc.setText(_translate("MainWindow", "Preview"))
        self.pushButtonTDBCopyShortDesc.setText(_translate("MainWindow", "Copy"))
        self.groupBox_4.setTitle(_translate("MainWindow", "About Contributors"))
        self.pushButtonPrevwAbtContribs.setText(_translate("MainWindow", "Preview"))
        self.pushButtonTDBCopyAboutContribs.setText(_translate("MainWindow", "Copy"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Other data popup"))
        self.pushButtonTDBOtherDataPopup.setText(_translate("MainWindow", "show popup"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "TDB Tools"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tools"))
        self.label_QwikHelp.setText(_translate("MainWindow", "<html><head/><body><p>Keyboard Shortcuts:</p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Inside input boxes (single/multiline)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ctrl + l =&gt; (ctrl + small L) change selection to lowercase</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ctrl + u =&gt; Change first letter of selection to uppercase others to lowercase. (Hint) can select a space to make all lowercase)</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ctrl + / =&gt; Insert an opening &lt;i&gt; tag and place the cursor just before letter &quot;i&quot;</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.actionOpen.setText(_translate("MainWindow", "&Open"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))


import icons_rc
