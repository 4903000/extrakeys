from krita import *

class ExtraKeys(Extension):

    def clamp(self, n, smallest, largest):
        return max(smallest, min(n, largest))
    
    def increase_flow(self):
        new_flow = self.clamp((Krita.instance().activeWindow().activeView().paintingFlow() + 0.1), 0, 1)
        Krita.instance().activeWindow().activeView().setPaintingFlow(new_flow)

    def decrease_flow(self):
        new_flow = self.clamp((Krita.instance().activeWindow().activeView().paintingFlow() - 0.1), 0, 1)
        Krita.instance().activeWindow().activeView().setPaintingFlow(new_flow)

    def __init__(self, parent):
        # This is initialising the parent, always important when subclassing.
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        increase_flow_action = window.createAction("increase_flow", "Increase painting flow")
        increase_flow_action.triggered.connect(self.increase_flow)
        decrease_flow_action = window.createAction("decrease_flow", "Decrease painting flow")
        decrease_flow_action.triggered.connect(self.decrease_flow)

# And add the extension to Krita's list of extensions:
