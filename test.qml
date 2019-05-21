import QtQuick 2.1
import QtLocation 5.6
import QtPositioning 5.6

Rectangle {
    id: mapArea
    width: 560
    height: 480
    anchors {
        topMargin: 10
        leftMargin: 10
    }
    Plugin {
        id: mapPlugin
        name: "esri"
    }
    Map {
        anchors.fill: parent
        plugin: mapPlugin
        zoomLevel: 14
        center {
            latitude: 51.467852
            longitude: -112.712256
        }
    }
    Rectangle {
        width: parent.width * 0.45
        height: parent.height * 0.10
        anchors{
            top: mapArea.top
            left: mapArea.left
            topMargin: 8
            leftMargin: 8
        }
        border {
            color: "black"
            width: 1
        }
    }
}