from Processor import Process
import Reporter
from pathlib import Path
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("project.ui", self)
        self.handle()
        self.setFixedSize(700 ,350)

    def browsefiles(self):
        fname = QFileDialog.getExistingDirectory(self, "Open file", "C:\\")
        self.filename.setText(fname)

    def browsefiles2(self):
        fname = QFileDialog.getExistingDirectory(self, "Open file", "C:\\")
        self.filename2.setText(fname)

    def handle(self):
        self.browse.clicked.connect(self.browsefiles)
        self.browse2.clicked.connect(self.browsefiles2)
        self.okbtn.clicked.connect(self.sure)

    def sure(self):
        if not self.filename.text() or not self.filename2.text():
            QMessageBox.warning(self,"Error", "Please select both folders")
        else:
            dialog = Surewindow()
            if dialog.exec_() == QDialog.Accepted:
             self.Start()

    def Start(self):
        d1 = self.filename.text()
        d2 = self.filename2.text()
        input_path = Path(rf"{d1}")
        output_path = Path(rf"{d2}")
        subfolder = self.checkBox.isChecked()

        out = Process(input_path, output_path, subfolder)
        if out == True:
            Reporter.logger.info("Done")
            QMessageBox.warning(self,"Done!","process completed.")

class Surewindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("sure.ui", self)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.setFixedSize(400 ,350)

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()