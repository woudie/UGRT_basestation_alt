import sys
import os
import signal
import rospy
import roslaunch
from PySide2 import QtCore, QtGui, QtUiTools, QtWidgets, QtWebEngineCore, QtWebEngineWidgets, QtQuickWidgets, QtQuickWidgets
from PySide2.QtWebEngineWidgets import QWebEngineSettings


class Controller(QtWidgets.QMainWindow, QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)

        signal.signal(signal.SIGINT, signal.SIG_DFL)
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.ui = self.initBaseStation("Ui/single_screen.ui")

        self.setWebVid(self.ui, self.ui.cam1, "http://192.168.0.31:4946/stream?topic=/cam1/image_raw&type=ros_compressed")
        self.setWebVid(self.ui, self.ui.cam2, "http://192.168.0.31:4946/stream?topic=/cam2/image_raw&type=ros_compressed")
        self.setWebVid(self.ui, self.ui.cam3, "http://192.168.0.31:4946/stream?topic=/cam3/image_raw&type=ros_compressed")

        self.ui.mapBox.setLayout(self.qmlLoader('Qml/map_widget.qml'))

    def qmlLoader(self, qmlUrl):
        tempLayout = QtWidgets.QVBoxLayout()
        view = QtQuickWidgets.QQuickWidget()
        view.setSource(QtCore.QUrl(qmlUrl))
        tempLayout.addWidget(view)
        return tempLayout

    def initBaseStation(self, uiFilename, parent=None):
        uiloader = QtUiTools.QUiLoader()
        uiFile = QtCore.QFile(uiFilename)
        uiFile.open(QtCore.QFile.ReadOnly)
        gui = uiloader.load(uiFile, parent)
        uiFile.close()
        return gui

    def setWebVid(self, ui, cam, camurl, parent=None):
        camlayout = QtWidgets.QVBoxLayout()
        ui.webview = QtWebEngineWidgets.QWebEngineView()
        ui.webview.setUrl(QtCore.QUrl(camurl))
        camlayout.addWidget(ui.webview)
        cam.setLayout(camlayout)
        return cam


if __name__ == "__main__":
    basestation = QtWidgets.QApplication(sys.argv)
    basestationWindow = Controller()
    basestationWindow.ui.show()
    sys.exit(basestation.exec_())
