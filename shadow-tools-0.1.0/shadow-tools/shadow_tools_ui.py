# -*- coding: utf-8 -*-

#    This file is part of Shadow Tools.

#    Shadow Tools is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Shadow Tools is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
#    Shadow Tools  Copyright (C) 2013  Pedram Veisi

# Form implementation generated from reading ui file 'shadow_tools.ui'
#
# Created: Mon Apr 22 19:52:28 2013
#      by: PyQt4 UI code generator 4.9.1
#


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ShadowTools(object):
    def setupUi(self, ShadowTools):
        ShadowTools.setObjectName(_fromUtf8("ShadowTools"))
        ShadowTools.resize(650, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/icon-window.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ShadowTools.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(ShadowTools)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vertical_layout = QtGui.QVBoxLayout()
        self.vertical_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.vertical_layout.setObjectName(_fromUtf8("vertical_layout"))
        self.selec_shadow_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.selec_shadow_label.setFont(font)
        self.selec_shadow_label.setObjectName(_fromUtf8("selec_shadow_label"))
        self.vertical_layout.addWidget(self.selec_shadow_label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.browse_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.browse_lineEdit.setObjectName(_fromUtf8("browse_lineEdit"))
        self.horizontalLayout.addWidget(self.browse_lineEdit)
        self.browse_button = QtGui.QPushButton(self.centralwidget)
        self.browse_button.setObjectName(_fromUtf8("browse_button"))
        self.horizontalLayout.addWidget(self.browse_button)
        self.vertical_layout.addLayout(self.horizontalLayout)
        self.outer_gridLayout = QtGui.QGridLayout()
        self.outer_gridLayout.setObjectName(_fromUtf8("outer_gridLayout"))
        self.users_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.users_label.setFont(font)
        self.users_label.setObjectName(_fromUtf8("users_label"))
        self.outer_gridLayout.addWidget(self.users_label, 0, 0, 1, 1)
        self.inner_gridLayout = QtGui.QGridLayout()
        self.inner_gridLayout.setObjectName(_fromUtf8("inner_gridLayout"))
        self.warning_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.warning_label.setFont(font)
        self.warning_label.setObjectName(_fromUtf8("warning_label"))
        self.inner_gridLayout.addWidget(self.warning_label, 3, 0, 1, 2)
        self.restore_hash_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.restore_hash_label.setFont(font)
        self.restore_hash_label.setObjectName(_fromUtf8("restore_hash_label"))
        self.inner_gridLayout.addWidget(self.restore_hash_label, 8, 0, 1, 1)
        self.selected_username_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.selected_username_label.setFont(font)
        self.selected_username_label.setText(_fromUtf8(""))
        self.selected_username_label.setObjectName(_fromUtf8("selected_username_label"))
        self.inner_gridLayout.addWidget(self.selected_username_label, 1, 1, 1, 1)
        self.selected_user_label = QtGui.QLabel(self.centralwidget)
        self.selected_user_label.setEnabled(True)
        self.selected_user_label.setText(_fromUtf8(""))
        self.selected_user_label.setObjectName(_fromUtf8("selected_user_label"))
        self.inner_gridLayout.addWidget(self.selected_user_label, 1, 0, 1, 1)
        self.chg_pass_lable = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chg_pass_lable.setFont(font)
        self.chg_pass_lable.setObjectName(_fromUtf8("chg_pass_lable"))
        self.inner_gridLayout.addWidget(self.chg_pass_lable, 6, 0, 1, 1)
        self.chg_pass_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.chg_pass_lineEdit.setEnabled(False)
        self.chg_pass_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.chg_pass_lineEdit.setObjectName(_fromUtf8("chg_pass_lineEdit"))
        self.inner_gridLayout.addWidget(self.chg_pass_lineEdit, 7, 0, 1, 1)
        self.current_hash_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.current_hash_lineEdit.setEnabled(False)
        self.current_hash_lineEdit.setReadOnly(True)
        self.current_hash_lineEdit.setObjectName(_fromUtf8("current_hash_lineEdit"))
        self.inner_gridLayout.addWidget(self.current_hash_lineEdit, 5, 0, 1, 1)
        self.restore_hash_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.restore_hash_lineEdit.setEnabled(False)
        self.restore_hash_lineEdit.setObjectName(_fromUtf8("restore_hash_lineEdit"))
        self.inner_gridLayout.addWidget(self.restore_hash_lineEdit, 9, 0, 1, 1)
        self.copy_to_clipboard_button = QtGui.QPushButton(self.centralwidget)
        self.copy_to_clipboard_button.setEnabled(False)
        self.copy_to_clipboard_button.setObjectName(_fromUtf8("copy_to_clipboard_button"))
        self.inner_gridLayout.addWidget(self.copy_to_clipboard_button, 5, 1, 1, 1)
        self.chg_pass_button = QtGui.QPushButton(self.centralwidget)
        self.chg_pass_button.setEnabled(False)
        self.chg_pass_button.setObjectName(_fromUtf8("chg_pass_button"))
        self.inner_gridLayout.addWidget(self.chg_pass_button, 7, 1, 1, 1)
        self.restore_hash_button = QtGui.QPushButton(self.centralwidget)
        self.restore_hash_button.setEnabled(False)
        self.restore_hash_button.setObjectName(_fromUtf8("restore_hash_button"))
        self.inner_gridLayout.addWidget(self.restore_hash_button, 9, 1, 1, 1)
        self.current_hash_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.current_hash_label.setFont(font)
        self.current_hash_label.setObjectName(_fromUtf8("current_hash_label"))
        self.inner_gridLayout.addWidget(self.current_hash_label, 4, 0, 1, 1)
        self.outer_gridLayout.addLayout(self.inner_gridLayout, 1, 1, 1, 1)
        self.users_listview = QtGui.QListWidget(self.centralwidget)
        self.users_listview.setObjectName(_fromUtf8("users_listview"))
        self.outer_gridLayout.addWidget(self.users_listview, 1, 0, 1, 1)
        self.outer_gridLayout.setColumnStretch(0, 1)
        self.outer_gridLayout.setColumnStretch(1, 3)
        self.vertical_layout.addLayout(self.outer_gridLayout)
        self.gridLayout.addLayout(self.vertical_layout, 0, 0, 1, 1)
        ShadowTools.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ShadowTools)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ShadowTools.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(ShadowTools)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        ShadowTools.setStatusBar(self.statusBar)

        self.retranslateUi(ShadowTools)
        QtCore.QMetaObject.connectSlotsByName(ShadowTools)

    def retranslateUi(self, ShadowTools):
        ShadowTools.setWindowTitle(QtGui.QApplication.translate("ShadowTools", "Shadow Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.selec_shadow_label.setText(QtGui.QApplication.translate("ShadowTools", "Select Shadow File", None, QtGui.QApplication.UnicodeUTF8))
        self.browse_button.setText(QtGui.QApplication.translate("ShadowTools", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.users_label.setText(QtGui.QApplication.translate("ShadowTools", "Users:", None, QtGui.QApplication.UnicodeUTF8))
        self.warning_label.setText(QtGui.QApplication.translate("ShadowTools", "<html><head/><body><p><span style=\" color:#dd0000;\">Warning: </span><span style=\" font-weight:400; font-style:italic; color:#000000;\">Without current hash, you won\'t be able to restore the password. </span><span style=\" font-style:italic; color:#000000;\">Save it!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.restore_hash_label.setText(QtGui.QApplication.translate("ShadowTools", "Restore Hash:", None, QtGui.QApplication.UnicodeUTF8))
        self.chg_pass_lable.setText(QtGui.QApplication.translate("ShadowTools", "Change Password to:", None, QtGui.QApplication.UnicodeUTF8))
        self.copy_to_clipboard_button.setText(QtGui.QApplication.translate("ShadowTools", "Copy To ClipBoard", None, QtGui.QApplication.UnicodeUTF8))
        self.chg_pass_button.setText(QtGui.QApplication.translate("ShadowTools", "Change Password", None, QtGui.QApplication.UnicodeUTF8))
        self.restore_hash_button.setText(QtGui.QApplication.translate("ShadowTools", "Restore Hash", None, QtGui.QApplication.UnicodeUTF8))
        self.current_hash_label.setText(QtGui.QApplication.translate("ShadowTools", "Current Hash:", None, QtGui.QApplication.UnicodeUTF8))

