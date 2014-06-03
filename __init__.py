# -*- coding: utf-8 -*-
"""
/***************************************************************************
 wktexport
                                 A QGIS plugin
 wktexport
                             -------------------
        begin                : 2014-05-29
        copyright            : (C) 2014 by faber
        email                : faberk76@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load wktexport class from file wktexport
    from wktexport import wktexport
    return wktexport(iface)
