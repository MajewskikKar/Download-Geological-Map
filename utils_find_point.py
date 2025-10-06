from qgis.PyQt.QtWidgets import *
from qgis.gui import QgsMapToolEmitPoint
from qgis.core import  QgsProject, QgsCoordinateReferenceSystem, QgsCoordinateTransform

class FindPoint:

    def __init__(self, dlg, iface, grid_10k, grid_50k, grid_200k):
        self.dlg = dlg
        self.canvas = iface.mapCanvas()
        self.grid_10k = grid_10k
        self.grid_50k = grid_50k
        self.grid_200k = grid_200k

    def click_find(self):
        self.PointTool = QgsMapToolEmitPoint(self.canvas)
        self.PointTool.canvasClicked.connect(lambda point, button: self.point_clicked(point))
        self.canvas.setMapTool(self.PointTool)

    def point_clicked(self, point):
        #transforming point to WGS84
        cooridnate_source = QgsProject.instance().crs()
        coordinate_output = QgsCoordinateReferenceSystem("EPSG:4326") 
        transform = QgsCoordinateTransform(cooridnate_source, coordinate_output, QgsProject.instance())
        point_to_wgs = transform.transform(point)

        #getting x and y coordinates in WGS84
        x_wgs = str(round((point_to_wgs.x()),6))
        y_wgs = str(round(point_to_wgs.y(),6))


        #validating if any of the checkboxes is checked
        if (self.dlg.checkBox_50k.isChecked() == False and self.dlg.checkBox_200k.isChecked() == False and self.dlg.checkBox_10k.isChecked() == False):
            QMessageBox.information(self.dlg, "Invalid", "Zaznacz siatkę 50k lub 200k.")
       
        #checking where clicked point is in the grid of 50k and 200k
        if self.dlg.checkBox_50k.isChecked():
            for feature in self.grid_50k.getFeatures():
                xmin = feature['XMIN']
                xmax = feature['XMAX']
                ymin = feature['YMIN']
                ymax = feature['YMAX']
                if (xmin  <= x_wgs <= xmax) and (ymin <= y_wgs <=ymax):
                    input_number_50k = feature['NR_ARK']
                    self.dlg.numer_ark_lineEdit.setText(input_number_50k)

        if self.dlg.checkBox_200k.isChecked():
            for feature in self.grid_200k.getFeatures():
                xmin = feature['xmin']
                xmax = feature['xmax']
                ymin = feature['ymin']
                ymax = feature['ymax']
                if (xmin  <= x_wgs <= xmax) and (ymin <= y_wgs <=ymax):
                    input_number_200k = feature['NUMER']
                    self.dlg.numer_ark_lineEdit.setText(input_number_200k)
        

        self.canvas.unsetMapTool(self.PointTool)
        self.dlg.activateWindow()