from qgis.PyQt.QtWidgets import QMessageBox
from qgis.core import QgsVectorLayer, QgsProject
import os

class GridManager:
    def __init__(self, dlg, plugin_dir):
        self.dlg = dlg
        self.plugin_dir = plugin_dir
        
    def download_grid(self): 

        sender = self.dlg.sender()

        if sender == self.dlg.download50k_pushButton:
            path_50k = os.path.join(self.plugin_dir, "grids/50k/50k_grid.shp")
            grid_50k = QgsVectorLayer(path_50k, "50k_grid", "ogr")
            if not grid_50k.isValid():
                QMessageBox.critical(self.dlg, "Error", "Failed to load the vector layer.")
                return
            QgsProject.instance().addMapLayer(grid_50k)
            QMessageBox.information(self.dlg, "Info", "Pobrano siatkę 50k")

        if sender == self.dlg.download200k_pushButton:
            path_200k = os.path.join(self.plugin_dir, "grids/200k/200k_grid.shp")
            grid_200k = QgsVectorLayer(path_200k, "200k_grid", "ogr")
            if not grid_200k.isValid():
                QMessageBox.critical(self.dlg, "Error", "Failed to load the vector layer.")
                return
            QgsProject.instance().addMapLayer(grid_200k)
            QMessageBox.information(self.dlg, "Info", "Pobrano siatkę 200k")
        
        if sender == self.dlg.download10k_pushButton:
            path_10k = os.path.join(self.plugin_dir, "grids/10k/10k_grid.shp")
            grid_10k = QgsVectorLayer(path_10k, "10k_grid", "ogr")
            if not grid_10k.isValid():
                QMessageBox.critical(self.dlg, "Error", "Failed to load the vector layer.")
                return
            QgsProject.instance().addMapLayer(grid_10k)
            QMessageBox.information(self.dlg, "Info", "Pobrano siatkę 10k")