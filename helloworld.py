# encoding: utf-8

import gvsig

from gvsig import getResource
from gvsig.libs.formpanel import FormPanel
from org.gvsig.scripting.swing.api import ScriptingSwingLocator

from org.icepdf.ri.common import SwingController
from org.icepdf.ri.common import SwingViewBuilder

class HelloWorld(FormPanel):
  def __init__(self):
    FormPanel.__init__(self,getResource(__file__,"helloworld.xml"))
    
  def btnClose_click(self, event):
    self.hide()

  def btnViewPDF_click(self, event):
    manager = ScriptingSwingLocator.getUIManager()

    controller = SwingController()
    viewer = SwingViewBuilder(controller).buildViewerPanel()
    controller.openDocument(getResource(__file__,"doc/helloworld.pdf"))
    manager.showWindow(viewer,"README")
      
    
def main(*args):
  window = HelloWorld()
  window.showWindow("Hello world!!")
  