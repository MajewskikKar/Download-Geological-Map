from qgis.PyQt.QtWidgets import *

class GuiUtils:
    def __init__(self, dlg):
        self.dlg = dlg

    def checkbox_changed(self):

        use10k = self.dlg.checkBox_10k.isChecked()
        use50k = self.dlg.checkBox_50k.isChecked()
        use200k = self.dlg.checkBox_200k.isChecked()
        
        self.check_for_multiple_checkboxes(use10k, use50k, use200k)
        self.fill_listwidget(use10k, use50k, use200k)

    def check_for_multiple_checkboxes(self, use10k, use50k, use200k):
        sender = self.dlg.sender()
        if sender == self.dlg.checkBox_10k and use10k:
            self.dlg.checkBox_50k.setEnabled(False)
            self.dlg.checkBox_200k.setEnabled(False)
        if sender == self.dlg.checkBox_50k and use50k:
            #self.dlg.checkBox_10k.setEnabled(False)
            self.dlg.checkBox_200k.setEnabled(False)
        if sender == self.dlg.checkBox_200k and use200k:
            #self.dlg.checkBox_10k.setEnabled(False)
            self.dlg.checkBox_50k.setEnabled(False)
        if sender == self.dlg.checkBox_10k and not use10k:
            self.dlg.checkBox_50k.setEnabled(True)
            self.dlg.checkBox_200k.setEnabled(True)
        if sender == self.dlg.checkBox_50k and not use50k:
            #self.dlg.checkBox_10k.setEnabled(True)
            self.dlg.checkBox_200k.setEnabled(True)
        if sender == self.dlg.checkBox_200k and not use200k:
            #self.dlg.checkBox_10k.setEnabled(True)
            self.dlg.checkBox_50k.setEnabled(True)

    def fill_listwidget(self, use10k, use50k, use200k):
        self.dlg.listWidget.clear()

        if use10k:
            map10k_items = ['mapa geologiczna tatr']
            for item_text_10k in map10k_items:
                item_10k = QListWidgetItem(item_text_10k)
                self.dlg.listWidget.addItem(item_10k)
  
        elif use50k:
            map50k_items = ['mapa geologiczna','tekst do mapy geologicznej', 
                            'mapa litogenetyczna','mapa geośrodowiskowa plansza A', 'mapa geośrodowiskowa plansza B']
            for item_text_50k in map50k_items:
                item_50k = QListWidgetItem(item_text_50k)
                self.dlg.listWidget.addItem(item_50k)

        elif use200k:
            map200k_items = ['mapa geologiczna planasza A', 'mapa geologiczna planasza B',
                            'mapa geologiczna tekst']
            for item_text_200k in map200k_items:
                item_200k = QListWidgetItem(item_text_200k)
                self.dlg.listWidget.addItem(item_200k)
        