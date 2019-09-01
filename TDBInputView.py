#! /bin/python3

from PyQt5 import uic,QtWidgets, QtGui, QtCore

"""
dev notes
----------
Inside input boxes (single/multiline)
Ctrl + l => (ctrl + small L) change selection to lowercase
Ctrl + u => Change first letter of selection to uppercase others to lowercase. (Hint) can select a space to make all lowercase)
ctrl + i => Insert an opening <i> tag and place the cursor just before letter "i"
"""

import TDBUtil, math

class MainInput(QtWidgets.QMainWindow):

    def __init__(self, allPublisherListModel, bkPublisherListModel, contributorModel):
        """

        :param allPublisherListModel: A QListStringModel Representing files
        """
        super(MainInput, self).__init__()
        uic.loadUi('./ui/main_input.ui', self)
        #print ("Size before {}".format(self.size()))

        # custom ui tweaks
        for i in self.findChildren(QtWidgets.QPushButton):
            #print(i.objectName())
            self.resize_button(i,2)

        # additional out of .ui controls
        self.completerPublishers = QtWidgets.QCompleter()
        
        # setup models
        self.allPublisherModel = allPublisherListModel
        self.bkPublisherModel = bkPublisherListModel
        self.contributorModel = contributorModel
        self.qtstylesmodel = self.init_style_model()

        #setup proxy models
        self.allpublisherSortModel = QtCore.QSortFilterProxyModel()
        self.allpublisherSortModel.setSourceModel(self.allPublisherModel)
        self.allpublisherSortModel.sort(0, QtCore.Qt.DescendingOrder) # sort ascending is default

        #bind controls to models
        self.completerPublishers.setModel(self.allpublisherSortModel)
        self.listViewBkPublishers.setModel(self.bkPublisherModel)
        self.tableViewContributor.setModel(self.contributorModel)
        self.comboBoxQtStyles.setModel(self.qtstylesmodel)

        # do other stuff e.g. binding to completers
        self.completerPublishers.setCaseSensitivity(QtCore.Qt.CaseInsensitive);
        self.lineEditPublisher.setCompleter(self.completerPublishers)

        # manage the connections

        # tab 1
        self.comboBoxQtStyles.currentIndexChanged.connect(self.change_style)
        self.pushButtonAddPublisher.clicked.connect(self.add_bk_publisher)
        self.pushButtonDeletePublisher.clicked.connect(self.delete_bk_publisher)
        self.pushButtonMovePublisherUp.clicked.connect(self.move_publisher_row_up)
        self.pushButtonMovePublisherDown.clicked.connect(self.move_publisher_row_down)

        self.lineEditPrice.textEdited.connect(self.calc_discount)
        self.comboBoxDiscount.currentIndexChanged.connect(self.calc_discount)

        self.pushButtonAddContrib.clicked.connect(self.add_contrib)
        self.pushButtonDeleteContrib.clicked.connect(self.delete_contrib)
        self.pushButtonMoveContribUp.clicked.connect(self.move_contrib_row_up)
        self.pushButtonMoveContribDown.clicked.connect(self.move_contrib_row_down)

        #tab 2
        self.pushButtonCopyTDBTitle.clicked.connect(self.copy_tdb_title)
        self.pushButtonTDBCopyISBN.clicked.connect(self.copy_tdb_isbn)
        self.pushButtonTDBCopyTags.clicked.connect(self.copy_tdb_tags)
        self.pushButtonTDBCopyLongDesc.clicked.connect(self.copy_tdb_long_desc)
        self.pushButtonTDBCopyShortDesc.clicked.connect(self.copy_tdb_short_desc)
        self.pushButtonTDBCopyAboutContribs.clicked.connect(self.copy_tdb_abt_contribs)
        self.pushButtonTDBOtherDataPopup.clicked.connect(self.show_tdb_other_data_popup)
        #tab 3

        #keyboard shortcuts
        self.bind_keybd_shortcuts()

        self.show()

    def resize_button(self,btnWidget,padding):
        width = btnWidget.fontMetrics().size(QtCore.Qt.TextShowMnemonic, btnWidget.text()).width() + padding
        btnWidget.setMinimumWidth(width)

    def init_style_model(self):
        data = QtWidgets.QStyleFactory.keys()
        model = QtCore.QStringListModel(data)
        return model

    def change_style(self):
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(self.comboBoxQtStyles.currentText()))

    def get_title(self):
        return self.lineEditTitle.text()

    def get_subtitle(self):
        return self.lineEditSubtitle.text()

    def make_tdb_title(self):
        tdb_title = "{}: {}".format(self.get_title(),self.get_subtitle())
        return tdb_title

    def copy_tdb_title(self):
        tdb_title = self.make_tdb_title()
        TDBUtil.copy_to_clipboard(tdb_title)
        print ("Title text copied to clipboard")

    def get_isbn(self):
        return self.lineEditISBN.text()

    def copy_tdb_isbn(self):
        TDBUtil.copy_to_clipboard(self.get_isbn())
        print("ISBN text copied to clipboard")

    def get_tags(self):
        return self.lineEditTags.text()

    def copy_tdb_tags(self):
        TDBUtil.copy_to_clipboard(self.get_tags())
        print("Tags text copied to clipboard")

    def get_long_desc_txt(self):
        return TDBUtil.get_QPlainTextEdit_text(self.plainTextEditLongDesc)

    def copy_tdb_long_desc(self):
        TDBUtil.copy_to_clipboard(self.get_long_desc_txt())
        print("Long desc text copied to clipboard")

    def get_short_desc(self):
        return TDBUtil.get_QPlainTextEdit_text(self.plainTextEditShortDesc)

    def validate_tdb_short_desc_fields(self):
        msgbox = QtWidgets.QMessageBox()
        if self.get_short_desc() == "":
            msgbox.setText("Short description cannot be empty")
            msgbox.setIcon(msgbox.Critical)

    def get_binding(self):
        return self.comboBoxBinding.currentText()

    def get_page_count(self):
        self.lineEditPageCount.text()

    def get_year(self):
        return self.lineEditYear.text()

    def get_selected_publisher(self):
        """
        Gets the selected publisher
        :return: string containing publisher name
        """
        return self.lineEditPublisher.text()

    def add_bk_publisher(self):
        publisher = self.get_selected_publisher()
        # get modelindex at selection point
        sel_idxs = self.listViewBkPublishers.selectedIndexes()
        if (len(sel_idxs) == 0):
            self.bkPublisherModel.insertRow(0)
            model_index = self.bkPublisherModel.index(0)
            self.listViewBkPublishers.setCurrentIndex(model_index)
        else:
            model_index = sel_idxs[0]
            self.bkPublisherModel.insertRow(model_index.row() + 1)
            model_index = self.bkPublisherModel.index(model_index.row() + 1)
            self.listViewBkPublishers.setCurrentIndex(model_index)

        self.bkPublisherModel.setData(model_index,publisher)

    def delete_bk_publisher(self):
        # get modelindex at selection point
        sel_idxs = self.listViewBkPublishers.selectedIndexes()
        if (len(sel_idxs) > 0):
            model_index = sel_idxs[0]
            self.bkPublisherModel.removeRow(model_index.row())
        else:
            TDBUtil.make_msgbox("", "Please select a publisher to delete", QtWidgets.QMessageBox.Information)

    def move_publisher_row_up(self):
        if (self.bkPublisherModel.rowCount() <2):
            m = QtWidgets.QMessageBox()
            m.setText("need at least 2 rows to move")
            m.setIcon(m.Information)
            m.show()
            m.exec()
            return
        sel_idxs = self.listViewBkPublishers.selectedIndexes()
        if (len(sel_idxs) > 0):
            curr_row_model_index = sel_idxs[0]
            if (curr_row_model_index.row() == 0):
                print("top most row - cannot move further")
                return
            curr_row_data = curr_row_model_index.data()
            prev_row_model_index = self.bkPublisherModel.index(curr_row_model_index.row() - 1)
            prev_row_data = prev_row_model_index.data()
            self.bkPublisherModel.setData(curr_row_model_index,prev_row_data)
            self.bkPublisherModel.setData(prev_row_model_index,curr_row_data)
            self.listViewBkPublishers.setCurrentIndex(prev_row_model_index)
        else:
            TDBUtil.make_msgbox("", "Please select a publisher to move.", QtWidgets.QMessageBox.Information)

    def move_publisher_row_down(self):
        if (self.bkPublisherModel.rowCount() < 2):
            m = QtWidgets.QMessageBox()
            m.setText("need at least 2 rows to move")
            m.setIcon(m.Information)
            m.show()
            m.exec()
            return
        sel_idxs = self.listViewBkPublishers.selectedIndexes()
        if (len(sel_idxs) > 0):
            curr_row_model_index = sel_idxs[0]
            if (curr_row_model_index.row() == (self.bkPublisherModel.rowCount() - 1)):
                print("Bottom most row - cannot move further")
                return
            curr_row_data = curr_row_model_index.data()
            next_row_model_index = self.bkPublisherModel.index(curr_row_model_index.row() + 1)
            prev_row_data = next_row_model_index.data()
            self.bkPublisherModel.setData(curr_row_model_index, prev_row_data)
            self.bkPublisherModel.setData(next_row_model_index, curr_row_data)
            self.listViewBkPublishers.setCurrentIndex(next_row_model_index)
        else:
            TDBUtil.make_msgbox("", "Please select a publisher to move.", QtWidgets.QMessageBox.Information)

    def calc_discount(self):
        if (self.lineEditPrice.text() == ""):
            return
        try:
            price = float(self.lineEditPrice.text())
            discount = float(self.comboBoxDiscount.currentText())
            discounted_price = price - (price * (discount/100))
            round_up_disc_price = math.ceil(discounted_price/10)*10
            print("Prince: {} Discount: {}%".format(price,discount))
            self.labelPriceAfterDiscount.setText("={}({})".format(discounted_price,round_up_disc_price))
            #print(self.labelPriceAfterDiscount.text())
        except(ValueError):
            TDBUtil.make_msgbox("","Price must be a number",QtWidgets.QMessageBox.Critical)

    def add_contrib(self):

        col_contrib_type = self.comboBoxContribType.currentText()
        col_contrib_val = self.lineEditContribValue.text()
        if (col_contrib_val == ""):
            TDBUtil.make_msgbox("","Contributor name cannot be blank",QtWidgets.QMessageBox.Warning)
            return
        cont_type_item = QtGui.QStandardItem(col_contrib_type)
        cont_type_item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        cont_val_item = QtGui.QStandardItem(col_contrib_val)
        cont_val_item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsEditable)
        self.contributorModel.appendRow([cont_type_item,cont_val_item])

    def  delete_contrib(self):
        sel_idxs = self.tableViewContributor.selectedIndexes()
        print(type(sel_idxs))
        if (len(sel_idxs) > 0):
            model_idx = sel_idxs[0]
            print(model_idx.row())
            self.contributorModel.removeRow(model_idx.row())

    def move_contrib_row_up(self):
        if (self.contributorModel.rowCount() < 2):
            TDBUtil.make_msgbox("", "need at least 2 rows to move", QtWidgets.QMessageBox.Information)
            return
        sel_idxs = self.tableViewContributor.selectedIndexes()
        if (len(sel_idxs) > 0):
            curr_row_model_index = sel_idxs[0]
            active_row = curr_row_model_index.row()
            active_col = curr_row_model_index.column()
            if (active_row ==0):
                print("Top most row - cannot move further")
                return
            curr_item_list = self.contributorModel.takeRow(active_row)
            self.contributorModel.insertRow(active_row - 1, curr_item_list)
            #selection code
            sel_model = self.tableViewContributor.selectionModel()

            # recompute mi from model
            print("---------")
            print("({},{})".format(active_row, active_col))
            print("({},{})".format(active_row - 1, active_col))
            # active_row = curr_row_model_index.row()
            # active_col = curr_row_model_index.column()

            model_index_topLeft = self.contributorModel.index(active_row - 1, active_col, QtCore.QModelIndex())
            model_index_topRight = self.contributorModel.index(active_row - 1, active_col, QtCore.QModelIndex())
            selection = QtCore.QItemSelection(model_index_topLeft, model_index_topRight)
            # sel_model.clear()
            sel_model.select(selection, QtCore.QItemSelectionModel.ClearAndSelect)

        else:
            TDBUtil.make_msgbox("", "Please select a publisher to move.", QtWidgets.QMessageBox.Information)

    def move_contrib_row_down(self):
        if (self.contributorModel.rowCount() < 2):
            TDBUtil.make_msgbox("","need at least 2 rows to move",QtWidgets.QMessageBox.Information)
            return
        sel_idxs = self.tableViewContributor.selectedIndexes()
        if (len(sel_idxs) > 0):
            curr_row_model_index = sel_idxs[0]
            active_row = curr_row_model_index.row()
            active_col = curr_row_model_index.column()
            if (active_row  == (self.contributorModel.rowCount() - 1)):
                print("Bottom most row - cannot move further")
                return
            curr_item_list = self.contributorModel.takeRow(active_row)
            self.contributorModel.insertRow(active_row + 1,curr_item_list)
            sel_model = self.tableViewContributor.selectionModel()


            #recompute mi from model
            print ("---------")
            print("({},{})".format(active_row,active_col))
            print("({},{})".format(active_row+1,active_col))
            #active_row = curr_row_model_index.row()
            #active_col = curr_row_model_index.column()

            model_index_topLeft = self.contributorModel.index(active_row+1,active_col,QtCore.QModelIndex())
            model_index_topRight = self.contributorModel.index(active_row + 1,active_col,QtCore.QModelIndex())
            selection = QtCore.QItemSelection(model_index_topLeft, model_index_topRight)
            #sel_model.clear()
            sel_model.select(selection,QtCore.QItemSelectionModel.ClearAndSelect)
        else:
            TDBUtil.make_msgbox("", "Please select a publisher to move.", QtWidgets.QMessageBox.Information)

    #tab 2
    def make_tdb_short_desc(self):
        publishers = []
        authors= []
        contributors = []
        editors = []
        illustrators = []
        translators = []

        for i in range(self.bkPublisherModel.rowCount()):
            model_index = self.bkPublisherModel.index(i)
            publishers.append(model_index.data())

        if (len(publishers) == 0):
            TDBUtil.make_msgbox("","Publishers cannot be blank",QtWidgets.QMessageBox.Critical)
            return

        for i in range(self.contributorModel.rowCount()):
            type_idx = self.contributorModel.index(i,0,QtCore.QModelIndex())
            val_idx = self.contributorModel.index(i,1,QtCore.QModelIndex())
            type_item = self.contributorModel.itemFromIndex(type_idx)
            val_item = self.contributorModel.itemFromIndex(val_idx)

            if (type_item.text() == "Author"):
                authors.extend(val_item.text())
            elif (type_item.text() == "Editor"):
                editors.extend(val_item.text())
            elif (type_item.text() == "Illustrator"):
                illustrators.extend(val_item.text())
            elif (type_item.text() == "Translator"):
                translators.extend(val_item.text())
            elif (type_item.text() == "Contributor"):
                contributors.extend(val_item.text())

        # Prepare list
        txt = ""
        if len(authors) > 0:
            txt += "Author{}: {}\n".format("s" if len(authors)> 1 else "", ",".join(authors))
        if len(contributors) > 0:
            txt += "Contributor{}:{}\n".format("s" if len(contributors)> 1 else "", ",".join(contributors))
        if len(editors) > 0:
            txt += "Edited by {}\n".format("s" if len(editors)> 1 else "", ",".join(editors))
        if len(translators) > 0:
            txt += "Translated by {}\n".format("s" if len(translators)> 1 else "", ",".join(translators))
        if len(illustrators) > 0:
            txt += "Illustrated by {}\n".format("s" if len(illustrators)> 1 else "", ",".join(illustrators))

        txt += "\n"
        # 9789352640645 | HB | pp. 256 | 2016 | HarperCollins
        txt += "{} | {} | pp. {} | {} | {}\n\n".format(self.get_isbn(),
                                                       self.get_binding(),
                                                       self.get_page_count(),
                                                       self.get_year(),
                                                       ", ".join(publishers)
                                                       )
        txt += '<p style="text-align: justify;">{}</p>\n\n'.format(self.get_short_desc())
        txt += '<h6 style="color: #4caf50;" align="justify">Ships in 2-4 days</h6>'

        return txt


    def copy_tdb_short_desc(self):
        TDBUtil.copy_to_clipboard(self.make_tdb_short_desc())
        print("Short desc text copied to clipboard")

    def get_about_contribs(self):
        return TDBUtil.get_QPlainTextEdit_text(self.plainTextEditAboutContribs)

    def copy_tdb_abt_contribs(self):
        TDBUtil.copy_to_clipboard( self.get_about_contribs())
        print("About Author/contributor(s) text copied to clipboard")

    def show_tdb_other_data_popup(self):
        print("TODO: display popup window with dims, weight etc - always on top")
        pass

    def insert_html_i_tag_at_pos(self,QWidgetParent):
        print(type(QWidgetParent) == QtWidgets.QLineEdit)
        if TDBUtil.isQPlainText_or_QTextEdit(QWidgetParent):
            print ("multine text detected")
            TDBUtil.insert_text_QPlainText_or_QTextEdit(QWidgetParent, "<i>", -2)
        elif TDBUtil.isQLineEdit(QWidgetParent):
            print("Single line text detected")
            TDBUtil.insert_text_QLineEdit(QWidgetParent,"<i>",-2)
    # shortcut stuff
    def bind_keybd_shortcuts(self):
        self.make_shortcut_insert_html_tag(self.plainTextEditLongDesc)
        self.make_shortcut_insert_html_tag(self.plainTextEditShortDesc)
        self.make_shortcut_insert_html_tag(self.plainTextEditAboutContribs)
        self.make_shortcut_insert_html_tag(self.lineEditTitle)

    def on_ambiguous_keyb_shortcut(self):
        print("WARNING: Ambiguous shortcut detected -- ignoring")

    def make_shortcut_insert_html_tag(self, QWidgetParent):
        # this will bind the keyboard shortcut only to the specific parents for which it is called
        # to be only called on
        # make the shortcut
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+/"),
                            QWidgetParent,
                            lambda:self.insert_html_i_tag_at_pos(QWidgetParent),
                            self.on_ambiguous_keyb_shortcut,QtCore.Qt.WidgetShortcut)

