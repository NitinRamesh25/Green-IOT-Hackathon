import QtQuick 2.0

Rectangle {
    id: partition
    property int partitionCount
    property string name
    property string wasteType

    width: parent.width / partitionCount
    height: parent.height

    Rectangle{
        id: topRect
        anchors.top: parent.top
        color: "#009999"
        border.color: "white"
        border.width: 2
        width: parent.width
        height: parent.height
    }
    Rectangle{
        id: bottomRect
        anchors.bottom: parent.bottom
        color: "#000000"
        border.color: "white"
        border.width: 2
        width: parent.width
        height: 0
    }

    SequentialAnimation {
        id: openAnimation
        running: false
        ParallelAnimation {
            NumberAnimation { target: topRect; property: "height"; to: 0; duration: 1000 }
            NumberAnimation { target: bottomRect; property: "height"; to: partition.height ; duration: 1000 }
        }
        ParallelAnimation {
            NumberAnimation { target: topRect; property: "height"; to: partition.height; duration: 1000 }
            NumberAnimation { target: bottomRect; property: "height"; to: 0 ; duration: 1000 }
        }
    }

    Text {
        id: myLabel
        anchors.centerIn: partition
        text: openAnimation.running ? wasteType : name
        color: "white"
    }

    function open() {
        openAnimation.start()
    }
}
