import sys, os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from app_new import Ui_MainWindow

class MainW (QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        
        self.enter = QShortcut(QKeySequence("Return"), self)
        self.enter.activated.connect(self.get_input)

        
        self.newMenu.clicked.connect(self.newTab)
        self.setPref.clicked.connect(self.changeTerminalBox)
  

    def get_input(self):
        command = self.commandInput.text()
        self.terminal_box.append("$~  ")

        if command == "clear" or command=="clr":
            self.clear()

        elif command =="os_name":
            self.os_n()

        elif command =="ls":
            self.system()

        elif command =="cur":
            self.current()

        elif "mkd" in command:
            try:
                if "-" in command:
                    plc = command.find("-")
                    param = command[plc+1:]
                    self.make_dir(param)
                    self.terminal_box.insertPlainText(f"Directory {param} was created.")
            except FileExistsError:
                self.terminal_box.insertPlainText("That directory currently exists.")

        elif "crt" in command:
            try:
                if "-" in command:
                    plc = command.find("-")
                    param = command[plc+1:]
                    self.make_file(param)
                    self.terminal_box.insertPlainText(f"File {param} was created.")
            except FileExistsError:
                self.terminal_box.insertPlainText("That file currently exists.")
        
        elif "rmv" in command:
            try:
                if "-" in command:
                    plc = command.find("-")
                    param = command[plc+1:]
                    self.delete_file(param)
                    self.terminal_box.insertPlainText(f"File {param} was deleted.")
            except:
                self.terminal_box.insertPlainText("That file doesn't exist.")
        

        else:
            self.terminal_box.insertPlainText('Not a valid command.')
        self.terminal_box.append("")
        self.commandInput.clear()
        
    def clear(self):
        self.terminal_box.clear()

    def os_n(self):
        self.terminal_box.insertPlainText(os.name)

    def system(self):
        self.terminal_box.insertPlainText(str(os.listdir()))

    def make_dir(self,parameter):
        os.mkdir(parameter)
        

    def make_file(self,parameter):
        os.system(f'touch {parameter}')
        
    def delete_file(self,parameter):
        os.remove(parameter)
    
    def current(self):
        cr = os.getcwd()
        self.terminal_box.insertPlainText(cr)

    def changeTerminalBox(self):
        rgb = self.terminal_bg.text()
        bg = self.bg_color_edit.text()
        cm = self.text_color.text()
        fn = self.sizeEdit.text()
        if len(bg) > 2 or  len(rgb) > 2 or len(cm) > 2 or len(fn) > 0:

            self.terminal_bg.setStyleSheet("background-color: rgb(255,255,255);")
            self.text_color.setStyleSheet("background-color: rgb(255,255,255);") 
            self.bg_color_edit.setStyleSheet("background-color: rgb(255,255,255);") 
            self.sizeEdit.setStyleSheet("background-color: rgb(255,255,255);") 
            self.setPref.setStyleSheet("background-color: rgb(255,255,255);") 
            self.newMenu.setStyleSheet("background-color: rgb(255,255,255);") 


            if len(bg) > 2:
                self.setStyleSheet(f"background-color: rgb{bg};")


            elif len(cm) > 2:  
                self.commandInput.setStyleSheet(f"color: rgb{cm};")
                self.terminal_box.setStyleSheet(f"color: rgb{cm};background-color: rgb{rgb};")

               
            elif len(rgb) > 2:
                self.terminal_box.setStyleSheet(f"color: rgb{rgb};background-color: rgb{rgb};")

            elif len(fn) > 0:
                print("Deneme")
                self.terminal_box.setFont(QFont(f'{fn}'))
            
    def newTab(self):
       print("Currently not working.")



if __name__ == '__main__':

    app = QApplication(sys.argv)
    myapp = MainW()
    myapp.show()
    sys.exit(app.exec_())
