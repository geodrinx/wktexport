# -*- coding: utf-8 -*-
"""
/***************************************************************************
 wktexport
                                 A QGIS plugin
 wktexport
                              -------------------
        begin                : 2014-05-29
        copyright            : (C) 2014 by geodrinx
        email                : geodrinx@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from wktexportdialog import wktexportDialog
import os.path
import qgis

import datetime
import time

from qgis.gui import QgsMessageBar

#----------------------------------------------------------------------------
def wkt_Write(self, adesso):	
        
				iface = qgis.utils.iface

				layer = iface.mapCanvas().currentLayer()

				if(layer == None):
				  return(-1)

				nomeLayer = str(layer.name())
				filePath = str(layer.source())
				direct = os.path.dirname(filePath)
				out_folder = direct + '/_wktExport'
				
				if not os.path.exists(out_folder):
				   os.mkdir( out_folder )
                             
				nomeGML = ("/%s_%s.wkt") % (nomeLayer, adesso)         				

        #  Apro il file WKT in scrittura
        
				kml=open(out_folder + nomeGML, 'w')

				layer = self.iface.mapCanvas().currentLayer()
				
				if layer:
				  if layer.type() == layer.VectorLayer:				
				    
				    name = layer.source();
				    nomeLayer = layer.name()
				    nomeLay   = nomeLayer.replace(" ","_")
 				                				    				    
				    iter = layer.getFeatures()            				    
				    for feat in iter:
				                  				      
				      # fetch geometry
				      geom = feat.geometry()
				      
				      testoWKT = geom.exportToWkt() + "\n"

				      kml.write (testoWKT)
				        				        
				kml.close()
				
				return(0)
              
              
              	        
#----------------------------------------------------------------------------				        
class wktexport:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'wktexport_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = wktexportDialog()


#----------------------------------------------------------------------------
    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/wktexport/icon.png"),
            u"wktexport", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&wktexport", self.action)

#----------------------------------------------------------------------------
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&wktexport", self.action)
        self.iface.removeToolBarIcon(self.action)


#----------------------------------------------------------------------------
    # run method that performs all the real work
    def run(self):

				adesso = str(datetime.datetime.now())
				adesso = adesso.replace(" ","_")
				adesso = adesso.replace(":","_")
				adesso = adesso.replace(".","_")  

				ret = wkt_Write(self, adesso)

				if(ret == 0): 
				  self.iface.messageBar().pushMessage("WKT_EXPORTER:   ",
                                                "File WKT saved",
                                                QgsMessageBar.INFO, 3)
				else:
				  self.iface.messageBar().pushMessage("WKT_EXPORTER:   ",
                                                "No Layer selected",
                                                QgsMessageBar.WARNING, 3)
