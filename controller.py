import sys
import PySide2

from PySide2 import QtCore, QtGui, QtUiTools, QtWidgets
from PySide2.QtCore import *
from PySide2.QtQuickWidgets import *
from PySide2.QtQml import *
from PySide2.QtQuick import QQuickView, QQuickItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout
from PySide2 import QtWebEngineCore
from PySide2.QtWebEngineWidgets import *
from PySide2 import QtWebEngineWidgets
from PySide2.QtWebEngineWidgets import QWebEngineSettings
from PySide2 import QtLocation


class Controller(QtWidgets.QMainWindow, QtWidgets.QVBoxLayout):
  def __init__(self, parent=None):

	  QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

  def window_loader(self, uifilename, parent=None):
  	loader = QtUiTools.QUiLoader()
  	uifile = QtCore.QFile(uifilename)
  	uifile.open(QtCore.QFile.ReadOnly)
  	gui = loader.load(uifile, parent)
  	uifile.close()
	return gui

  #def setWebVid(self, cam, camurl):

  def setWebVid(self, ui, cam, camurl, parent=None):
	  
	  camlayout = QtWidgets.QVBoxLayout()
	  ui.webview = QtWebEngineWidgets.QWebEngineView()
	  ui.webview.setUrl(QUrl(camurl))
	  camlayout.addWidget(ui.webview)
	  cam.setLayout(camlayout)

	  return cam

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = Controller()
  ui = MainWindow.window_loader("ugrt_bs.ui")

  cam1 = MainWindow.setWebVid(ui, ui.cam1, "http://192.168.0.31:4946/stream?topic=/cam1/image_raw&type=ros_compressed")
  cam2 = MainWindow.setWebVid(ui, ui.cam2, "http://192.168.0.31:4946/stream?topic=/cam2/image_raw&type=ros_compressed")
  cam3 = MainWindow.setWebVid(ui, ui.cam3, "http://192.168.0.31:4946/stream?topic=/cam3/image_raw&type=ros_compressed")

  mapLayout = QtWidgets.QVBoxLayout()
  view = QQuickWidget()
  view.setSource(QUrl('test.qml'))
  mapLayout.addWidget(view)
  ui.mapBox.setLayout(mapLayout)
  
  ui.show()
  sys.exit(app.exec_())
