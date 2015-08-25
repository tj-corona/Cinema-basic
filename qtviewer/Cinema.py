
#!/usr/bin/python

# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from PySide import QtXml

# import json
import json as simplejson

# import Python Image Library
import PIL.ImageFile

# Import cinema IO
sys.path.insert(0, "C:\\Users\\tj.corona\\Desktop\\Cinema-basic\\")
sys.path

import IO.cinema_store

# Show it in Qt
app = QApplication(sys.argv)

# set up UI
from MainWindow import *
mainWindow = MainWindow()
mainWindow.show()

# Enter Qt application main loop
app.exec_()
sys.exit()
