import sys

from PySide2 import QtCore, QtGui, QtUiTools, QtWidgets, QtWebEngineCore, QtWebEngineWidgets, QtQuickWidgets
from PySide2.QtWebEngineWidgets import QWebEngineSettings



class Controller(QtWidgets.QMainWindow, QtWidgets.QVBoxLayout):
  def __init__(self, parent=None):
	QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

  def qmlLoader(self, qmlUrl):
    tempLayout = QtWidgets.QVBoxLayout()
    view = QtQuickWidgets.QQuickWidget()
    view.setSource(QtCore.QUrl(qmlUrl))
    tempLayout.addWidget(view)
    return tempLayout

  def window_loader(self, uifilename, parent=None):
  	loader = QtUiTools.QUiLoader()
  	uifile = QtCore.QFile(uifilename)
  	uifile.open(QtCore.QFile.ReadOnly)
  	gui = loader.load(uifile, parent)
  	uifile.close()
	return gui

  def setWebVid(self, ui, cam, camurl, parent=None):
	camlayout = QtWidgets.QVBoxLayout()
	ui.webview = QtWebEngineWidgets.QWebEngineView()
	ui.webview.setUrl(QtCore.QUrl(camurl))
	camlayout.addWidget(ui.webview)
	cam.setLayout(camlayout)
	return cam

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = Controller()
  ui = MainWindow.window_loader("single_screen.ui")

  cam1 = MainWindow.setWebVid(ui, ui.cam1, "http://192.168.0.31:4946/stream?topic=/cam1/image_raw&type=ros_compressed")
  cam2 = MainWindow.setWebVid(ui, ui.cam2, "http://192.168.0.31:4946/stream?topic=/cam2/image_raw&type=ros_compressed")
  cam3 = MainWindow.setWebVid(ui, ui.cam3, "http://192.168.0.31:4946/stream?topic=/cam3/image_raw&type=ros_compressed")

  ui.mapBox.setLayout(MainWindow.qmlLoader('map_widget.qml'))
  
  ui.show()
  sys.exit(app.exec_())
