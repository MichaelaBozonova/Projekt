from kodovac import Kodovac  # ze souboru kodovac.py vkladame tridu Kodovac
from PyQt5 import QtWidgets, uic

class MainWindow():
    window = None

    def set_window(self, window):
        self.window = window

    def zasifrovani(self):
        kodovac = Kodovac()  # vytvorime objekt, ktery ukladame do promene kodovac
        zasifrovany_text = kodovac.sifrovat(
           self.window.lineEdit_vstup.text())  # sifruje text, ktery uklada do promenne zasifrovany_text
        self.window.lineEdit_sifra.setText(zasifrovany_text)

    def desifrovani(self):
        kodovac = Kodovac()  # vytvorime objekt, ktery ukladame do promene kodovac
        desifrovany_text = kodovac.desifrovat(
            self.window.lineEdit_sifra.text())  # desifruje text, ktery uklada do promenne desifrovany_text
        self.window.lineEdit_desifrovat.setText(desifrovany_text)

def main():
    app = QtWidgets.QApplication([])
    window = QtWidgets.QDialog()

    with open('Projekt.ui') as f:
        uic.loadUi(f, window)

    mw = MainWindow()
    mw.set_window(window)
    x = QtWidgets.QLineEdit()

    window.pushButton_zasifrovat.clicked.connect(mw.zasifrovani)
    window.show()

    window.pushButton_desifrovat.clicked.connect(mw.desifrovani)
    window.show()

    return app.exec()
main()

