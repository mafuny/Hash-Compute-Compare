from PyQt5 import QtWidgets, QtGui, uic
import sys
import hashlib
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.browseButton.clicked.connect(self.fileBrowse)
        self.browseButton2.clicked.connect(self.fileBrowse2)
        self.hash_compute.clicked.connect(self.compute)
        self.show()

    def fileBrowse(self):
        self.fileEdit.setText(QFileDialog.getOpenFileName(self, 'Open file', '/home')[0])

    def fileBrowse2(self):
        self.fileEdit2.setText(QFileDialog.getOpenFileName(self, 'Open file', '/home')[0])

    def compute(self):
        if self.fileEdit.text() == "" and self.fileEdit2.text() == "":
            print('Empty')
            pass
        elif self.fileEdit.text() != "" and self.fileEdit2.text() == "":
            hash_sum = self.hash(self.fileEdit.text())
            print("1st: "+hash_sum)
            dialog.resultsShow(hash_sum, None)
        elif self.fileEdit.text() == "" and self.fileEdit2.text() != "":
            hash_sum = self.hash(self.fileEdit2.text())
            print("2nd: "+hash_sum)
            dialog.resultsShow(None, hash_sum)
        elif self.fileEdit.text() != "" and self.fileEdit2.text() != "":
            hash_sum = self.hash(self.fileEdit.text())
            hash_sum2 = self.hash(self.fileEdit2.text())
            print("1st: "+hash_sum)
            print("2nd: "+hash_sum2)
            dialog.resultsShow(hash_sum, hash_sum2)

    def hash(self, filename):
        hash_object = hashlib.sha256()
        with open(filename, 'rb') as f:
            while True:
                data = f.read(65536)
                if not data:
                    break
                hash_object.update(data)
        file_hash = hash_object.hexdigest()
        return file_hash


class Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('dialog.ui', self)

    def resultsShow(self, hash1, hash2):
        if hash1 and not hash2:
            self.label.setText("Hash 1st = "+hash1)
        elif hash2 and not hash1:
            self.label_2.setText("Hash 2nd = "+hash2)
        elif hash2 and hash1:
            self.label.setText("Hash 1st = "+hash1)
            self.label_2.setText("Hash 2nd = "+hash2)
            if hash1 == hash2:
                self.label_3.setText("Hash is equal, file equals too")
            else:
                self.label_3.setText("Hash is not equal, files is not equal too")
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
dialog = Dialog()
app.exec_()
