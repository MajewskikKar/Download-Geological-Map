import os
import requests
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.core import QgsRasterLayer, QgsProject
from qgis.PyQt.QtWidgets import *

class DownloadMap:

    def __init__(self, dlg):
        self.dlg = dlg
  
    def execute_file(self, output_path, mapa_geologiczna_download, number_checked):
            try:
                with open(output_path, 'wb') as file:
                    file.write(mapa_geologiczna_download.content)
                raster_layer = QgsRasterLayer(output_path, f'SMGP {number_checked}')
                if raster_layer.isValid():
                    QgsProject.instance().addMapLayer(raster_layer)
                    QMessageBox.information(self.dlg, "Info", f"Zapisano arkusz w: {output_path}")
                else:
                    QMessageBox.critical(self.dlg, "Error", "Szukany arkusz nie istnieje")

                
            except Exception as e:
                QMessageBox.critical(self.dlg, "Error", f"Failed to save file: {e}")      

    def process_number(self, lineedit_value):
        selected_item = self.dlg.listWidget.currentItem()
        number = str(lineedit_value)
        number_checked = number.zfill(4)
        output_dir = self.dlg.save_dir_lineEdit.text()

        if selected_item is None:
            QMessageBox.information(self.dlg, "Invalid", "Wybierz rodzaj mapy do pobrania.")
            self.dlg.raise_()
            self.dlg.activateWindow()
            return
        
        if selected_item.text() == 'mapa geologiczna':
            mapa_geologiczna_link = f'https://bazadata.pgi.gov.pl/data/smgp/arkusze_skany/smgp{number_checked}.jpg'
            mapa_geologiczna_download = requests.get(mapa_geologiczna_link)
            filename = f'smgp{number}.jpg'
            output_path = os.path.join(output_dir, filename) 
            if output_path:
                self.execute_file(output_path, mapa_geologiczna_download, number_checked)

        elif selected_item.text() == 'tekst do mapy geologicznej':
            tekst_do_mapy_geologicznej_link = f'https://bazadata.pgi.gov.pl/data/smgp/arkusze_txt/smgp{number_checked}.pdf'
            tekst_do_mapy_geologicznej_download = requests.get(tekst_do_mapy_geologicznej_link)
            filename = f'smgp{number}_tekst.pdf'
            output_path = os.path.join(output_dir, filename) 
            if output_path:
                self.execute_file(output_path, tekst_do_mapy_geologicznej_download, number_checked)

        elif selected_item.text() == 'mapa litogenetyczna':
            mapa_geologiczna_link = f'https://bazadata.pgi.gov.pl/data/mlp/mlp{number_checked}.jpg'
            mapa_litogenetyczna_download = requests.get(mapa_geologiczna_link)
            filename = f'mlp{number}.jpg'
            output_path = os.path.join(output_dir, filename) 
            if output_path:
                self.execute_file(output_path, mapa_litogenetyczna_download, number_checked)
        elif selected_item.text() == 'mapa geośrodowiskowa plansza A':
            mapa_geosrodowiskowa_A_link = f'https://bazadata.pgi.gov.pl/data/mgsp/A/mgspA{number_checked}.jpg'
            mapa_geosrodowiskowa_A_download = requests.get(mapa_geosrodowiskowa_A_link)
            filename = f'mgsp{number}_A.jpg'
            output_path = os.path.join(output_dir, filename) 
            if output_path:
                self.execute_file(output_path, mapa_geosrodowiskowa_A_download, number_checked)

        elif selected_item.text() == 'mapa geośrodowiskowa plansza B':
            mapa_geosrodowiskowa_B_link = f'https://bazadata.pgi.gov.pl/data/mgsp/B/mgspB{number_checked}.jpg'
            mapa_geosrodowiskowa_B_download = requests.get(mapa_geosrodowiskowa_B_link)
            filename = f'mgsp{number}_B.jpg'
            output_path = os.path.join(output_dir, filename) 
            if output_path:
                self.execute_file(output_path, mapa_geosrodowiskowa_B_download, number_checked)
        
        elif selected_item.text() == 'mapa geologiczna planasza A':
        
            mapa_geologiczna_200_plansza_A_link_new = f'https://bazadata.pgi.gov.pl/data/mgp200/mapy/edycja2/mgp200A{number}-edycja2.jpg' 
            mapa_geologiczna_200_plansza_A_link_old = f'https://bazadata.pgi.gov.pl/data/mgp200/mapy/edycja1/mgp200A{number}-edycja1.jpg'
            try_new = requests.get(mapa_geologiczna_200_plansza_A_link_new)
            try_old = requests.get(mapa_geologiczna_200_plansza_A_link_old)
            filename = f'mgp200_{number}A.jpg'
            output_path = os.path.join(output_dir, filename) 

            if try_new.status_code == 200:
                self.execute_file(output_path, try_new, number_checked)
            elif try_old.status_code == 200:
                self.execute_file(output_path, try_old, number_checked)
            
        elif selected_item.text() == 'mapa geologiczna planasza B':
        
            mapa_geologiczna_200_plansza_B_link_new = f'https://bazadata.pgi.gov.pl/data/mgp200/mapy/edycja2/mgp200B{number}-edycja2.jpg' 
            mapa_geologiczna_200_plansza_B_link_old = f'https://bazadata.pgi.gov.pl/data/mgp200/mapy/edycja1/mgp200B{number}-edycja1.jpg'
            try_new = requests.get(mapa_geologiczna_200_plansza_B_link_new)
            try_old = requests.get(mapa_geologiczna_200_plansza_B_link_old)
            filename = f'mgp200_{number}B.jpg'
            output_path = os.path.join(output_dir, filename) 

            if try_new.status_code == 200:
                self.execute_file(output_path, try_new, number_checked)
            elif try_old.status_code == 200:
                self.execute_file(output_path, try_old, number_checked)
            
        elif selected_item.text() == 'mapa geologiczna tekst':
            
            mapa_geologoiczna_200_tekst_link = f'https://bazadata.pgi.gov.pl/data/mgp200/txt/edycja1/mgp200txt{number}-edycja1.pdf'
            mapa_geologoiczna_200_tekst_download = requests.get(mapa_geologoiczna_200_tekst_link)
            filename = f'mgp200_{number}_tekst.jpg'
            output_path = os.path.join(output_dir, filename) 
            if output_path:
                self.execute_file(output_path, mapa_geologoiczna_200_tekst_download, number_checked)