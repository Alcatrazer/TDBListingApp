from PyQt5 import QtWidgets

def copy_to_clipboard(data):
    clipboard = QtWidgets.QApplication.clipboard()
    clipboard.setText(data)

def get_QPlainTextEdit_text(Qwidget):
    text_doc = Qwidget.document()
    text = text_doc.toPlainText()
    return text

def insert_text_QLineEdit(QlineEdit, insertable_text, mvt_from_end_insert):
    """
    Inserts text into a QLineEdit control. Use ctlr+z to undo action

    :param QlineEdit: The QLineEditWidget we want to insert text in
    :param text_to_insert: String of text to insert
    :param mvt_from_end_insert: A positive or negative int value relative to the new cursor position after insert
    :return:
    """
    cpos = QlineEdit.cursorPosition() #cursor pos before insert
    QlineEdit.deselect()
    QlineEdit.insert(insertable_text)
    newcpos = QlineEdit.cursorPosition()
    QlineEdit.setCursorPosition(newcpos + mvt_from_end_insert)

def insert_text_QPlainText_or_QTextEdit(PlainText_or_QTextEdit, insertable_text, mvt_from_end_insert):
    """
    Inserts text into a QLineEdit control. Use ctlr+z to undo action

    :param line_edit_widget: The QPlainTex/QTextWidget we want to insert text in
    :param text_to_insert: String of text to insert
    :param mvt_from_end_insert: A positive or negative int value relative to the new cursor position after insert
    :return:
    """
    widgetTextCursor = PlainText_or_QTextEdit.textCursor()
    widgetTextCursor.insertText(insertable_text)
    widgetTextCursor.movePosition(widgetTextCursor.Left, widgetTextCursor.MoveAnchor, abs(mvt_from_end_insert))
    PlainText_or_QTextEdit.setTextCursor(widgetTextCursor)

def isQPlainText_or_QTextEdit(QWidget):
    if type(QWidget) in [QtWidgets.QPlainTextEdit, QtWidgets.QTextEdit]:
        return True
    else:
        return False

def isQLineEdit(QWidget):
    if type(QWidget) in [QtWidgets.QLineEdit]:
        return True
    else:
        return False

def make_msgbox(title,msg,icon_type):
    m = QtWidgets.QMessageBox()
    #m.setText("Please select a publisher to move.")
    m.setWindowTitle(title)
    m.setText(msg)
    m.setIcon(icon_type)
    m.show()
    m.exec()