#!/usr/bin/python -tt

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

import os, sys, crypt
from PyQt4 import QtGui, QtCore

sys.path.append('/usr/share/pyshared/shadow-tools')
from shadow_tools_ui import Ui_ShadowTools

APP_NAME = 'Shadow Tool'
SHADOW_SPECIAL_CHARS = '!*'

class UI(QtGui.QMainWindow):
    
    def __init__(self):        
        
        self.file_addr = ''
        self.file_content = ''
        self.user_pass_dict = {}
        self.selected_user = ''
        
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_ShadowTools()
        self.ui.setupUi(self)
        self.center()
        self.show() 
        self.execute()         

    def center(self):        
        fg = self.frameGeometry()
        ag = QtGui.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(ag)
        self.move(fg.topLeft())
        
        
    def read_shadow_file(self):
        ''' (UI) -> NoneType
        
        Reads the desired file in read mode. 
        '''
        # Check for permission
        self.file_addr = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/')
        
        # Set Text in EditText field
        self.ui.browse_lineEdit.setText(self.file_addr)
        
        file = open(self.file_addr, 'r')
        
        #Check for a correct shadow file
        try:
            self.file_content = file.readlines()
        except UnicodeDecodeError:
            self.handle_wrong_file()
            return
                    
        file.close()
        self.load_users()

    def load_users(self):
                       
        # get list of users
        line_number = 0
        try:
            for line in self.file_content:
                tokenized_line = line.split(':')
                if tokenized_line[1] not in SHADOW_SPECIAL_CHARS:
                    self.user_pass_dict[tokenized_line[0]] = [tokenized_line[1], line_number]
                        
                line_number += 1
        except IndexError:
                self.handle_wrong_file()
                return
        
        if len(self.user_pass_dict) == 0:
            self.handle_wrong_file()
            return
        
        
        self.ui.users_listview.clear()
        for user in self.user_pass_dict:
            item = QtGui.QListWidgetItem(user)
            self.ui.users_listview.addItem(item)    
    
    def handle_wrong_file(self):
        ''' (NoneType) -> NoneType
        
        Called in case of wrong shadow file.
        '''
        print("Not a shadow file!")
        self.ui.browse_lineEdit.setText("Not a shadow file!")
    
    def handle_listview(self, qmodelindex):
        
        self.ui.current_hash_lineEdit.setEnabled(True)
        self.ui.chg_pass_lineEdit.setEnabled(True)
        self.ui.restore_hash_lineEdit.setEnabled(True)
        self.ui.copy_to_clipboard_button.setEnabled(True)
        self.ui.chg_pass_button.setEnabled(True)
        self.ui.restore_hash_button.setEnabled(True)
        self.selected_user = str(self.ui.users_listview.currentItem().text())
        self.ui.selected_user_label.setText("Selected User:")
        self.ui.selected_username_label.setText(self.selected_user)
        self.ui.current_hash_lineEdit.setText(self.user_pass_dict[self.selected_user][0])
        
    def restore_hash(self):

        provided_hash = str(self.ui.restore_hash_lineEdit.text())
        
        prompt_msg = "Restore hash for '{0}'?".format(self.selected_user)
        prompt = QtGui.QMessageBox.information(self, 'Confirm changes', prompt_msg, QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Ok)
        
        if prompt == QtGui.QMessageBox.Ok:
            self.modify_write_shadow(provided_hash)
            
        # Check for success
        self.ui.statusBar.showMessage("Hash restored!")    
                
    def change_password(self):

        provided_pass = str(self.ui.chg_pass_lineEdit.text())
             
        prompt_msg = "Change password for '{0}'?".format(self.selected_user)
        prompt = QtGui.QMessageBox.information(self, 'Confirm changes', prompt_msg, QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Ok)

        if prompt == QtGui.QMessageBox.Ok:
            encrypted_pass = crypt.crypt(provided_pass, '$6$ShadowTools$')
            self.ui.chg_pass_lineEdit.setText('')
            self.modify_write_shadow(encrypted_pass)
            
            # Check for success
            self.ui.statusBar.showMessage("Password updated!")

            
    def modify_write_shadow(self, new_hash):
            # Modify Shadow file content
            line_number = self.user_pass_dict[self.selected_user][1]
            target_line = self.file_content[line_number]
            tokenized_target_line = target_line.split(':')
            tokenized_target_line[1] = new_hash
            modified_target_line = ':'.join(tokenized_target_line)
            self.file_content[line_number] = modified_target_line
            
            # Write changes to Shadow file
            shadow_file = open(self.file_addr, 'w')
            for line in self.file_content:
                shadow_file.write(line)
            
            shadow_file.close()
        
    def copy_to_clipboard(self):
        current_hash = self.ui.current_hash_lineEdit.text()
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(current_hash)

    def execute(self):
        ''' (UI) -> NoneType
        
        Main functionality of the application.
        '''
        self.ui.browse_button.clicked.connect(lambda: self.read_shadow_file())
        QtCore.QObject.connect(self.ui.users_listview, QtCore.SIGNAL("clicked(QModelIndex)"), self.handle_listview)
        self.ui.chg_pass_button.clicked.connect(lambda: self.change_password())
        self.ui.copy_to_clipboard_button.clicked.connect(lambda: self.copy_to_clipboard())
        self.ui.restore_hash_button.clicked.connect(lambda: self.restore_hash())
        
def main():

    # Checks for root permission
    if os.geteuid() != 0:
        print('Root permission required!')
        # Handle in GUI 
    else:

        app = QtGui.QApplication(sys.argv)     
        ui = UI()  # @UnusedVariable
        sys.exit(app.exec_())
             
if __name__ == '__main__':
    main()
