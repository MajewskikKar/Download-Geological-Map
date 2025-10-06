from qgis.PyQt.QtWidgets import *

class OutputFile:
    def __init__(self,dlg):
        self.dlg = dlg

    def select_output_file(self):
        directory = QFileDialog.getExistingDirectory(
            self.dlg,
            "Select directory to save files",
            "",
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)  
        self.dlg.save_dir_lineEdit.setText(directory) 