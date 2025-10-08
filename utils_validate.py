from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtGui import QIntValidator

class Validate:
    def __init__(self, dlg, download_map):
        self.dlg = dlg
        self.download_map = download_map

    def validate_and_process(self):
        """Walidacja numeru arkusza i pobranie mapy"""
        lineedit = self.dlg.numer_ark_lineEdit.text()
        self.dlg.numer_ark_lineEdit.setValidator(QIntValidator(1,1082,self.dlg))
        linevalidator = self.dlg.numer_ark_lineEdit.validator()
        
        if not (self.dlg.checkBox_50k.isChecked() or self.dlg.checkBox_200k.isChecked()):
            QMessageBox.information(self.dlg, "Invalid", "Zaznacz skalę")
            return
        
        if not lineedit:
            QMessageBox.information(self.dlg, "Invalid", "Wpisz numer arkusza.")
            return

        state, _, _ = linevalidator.validate(lineedit, 0)
        if state != QIntValidator.Acceptable:
            QMessageBox.information(self.dlg, "Invalid", "Podana liczba jest niepoprawna.")
            self.dlg.raise_()
            self.dlg.activateWindow()
            return

        # jeśli wszystko poprawne, wywołujemy pobranie mapy
        #self.download_map.process_number(lineedit)
        self.download_map.process_number1(lineedit)

