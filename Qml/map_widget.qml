import QtQuick 2.1
import QtLocation 5.6
import QtPositioning 5.6



Rectangle {
    id: mapArea
    width: 560
    height: 480

    Plugin {
        id: mapPlugin
        name: "mapboxgl"
    }
    
    //latitude: 51.467852 longitude: -112.712256
    property variant initLoc: QtPositioning.coordinate(43.5314187, -80.227686)
    Map {
        anchors.fill: parent
        plugin: mapPlugin
        zoomLevel: 14
        center: initLoc
    }
    Rectangle {
        width: parent.width * 0.25
        height: parent.height * 0.050
        anchors{
            top: mapArea.top
            left: mapArea.left
            topMargin: 8
            leftMargin: 9
        }
        border {
            color: "black"
            width: 1
        }
    }
}