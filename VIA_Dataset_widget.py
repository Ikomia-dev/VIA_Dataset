from ikomia import utils, core, dataprocess
import VIA_Dataset_process as processMod
# PyQt GUI framework
from PyQt5.QtWidgets import *


# --------------------
# - Class which implements widget associated with the process
# - Inherits core.CProtocolTaskWidget from Ikomia API
# --------------------
class VIA_DatasetWidget(core.CProtocolTaskWidget):

    def __init__(self, param, parent):
        core.CProtocolTaskWidget.__init__(self, parent)

        if param is None:
            self.parameters = processMod.VIA_DatasetParam()
        else:
            self.parameters = param

        # Create layout : QGridLayout by default
        self.grid_layout = QGridLayout()

        self.browse_json = utils.append_browse_file(self.grid_layout, label="VIA json file",
                                                   path=self.parameters.via_json_path, filter="*.json")

        # PyQt -> Qt wrapping
        layout_ptr = utils.PyQtToQt(self.grid_layout)

        # Set widget layout
        self.setLayout(layout_ptr)

    def onApply(self):
        # Apply button clicked slot
        # Get parameters from widget
        self.parameters.via_json_path = self.browse_json.path

        # Send signal to launch the process
        self.emitApply(self.parameters)


#--------------------
#- Factory class to build process widget object
#- Inherits dataprocess.CWidgetFactory from Ikomia API
#--------------------
class VIA_DatasetWidgetFactory(dataprocess.CWidgetFactory):

    def __init__(self):
        dataprocess.CWidgetFactory.__init__(self)
        # Set the name of the process -> it must be the same as the one declared in the process factory class
        self.name = "VIA_Dataset"

    def create(self, param):
        # Create widget object
        return VIA_DatasetWidget(param, None)
