import QtQuick 2.0

Image {
    id: qrcode

    source: "image://ImageProvider/ip.jpg"
    state: "cornered"

    states: [
        State {
           name: "cornered"
           AnchorChanges {
               target: qrcode
               anchors.right: rootitem.right
               anchors.bottom: rootitem.bottom
           }
           PropertyChanges {
               target: qrcode
               width: rootitem.height * 0.25
               height: width
           }
        },
        State {
           name: "centered"
           AnchorChanges {
               target: qrcode
               anchors.horizontalCenter: rootitem.horizontalCenter
               anchors.verticalCenter: rootitem.verticalCenter
           }
           PropertyChanges {
               target: qrcode
               width: rootitem.height * 0.8
               height: width
           }
        }
    ]

    transitions: Transition {
        AnchorAnimation { duration: 200 }
    }

    MouseArea {
        anchors.fill: parent

        onClicked: {
            if(qrcode.state == "cornered")
                qrcode.state = "centered";
            else if (qrcode.state == "centered")
                qrcode.state = "cornered";
        }
    }
}