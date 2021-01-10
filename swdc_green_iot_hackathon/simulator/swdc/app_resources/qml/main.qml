import QtQuick 2.0
import QtQuick.Controls 2.10
import QtGraphicalEffects 1.0


Rectangle {
    id: rootitem

    property Gradient juicyOrange: Gradient {
            GradientStop { position: 0.0; color: "#ffc837" }
            GradientStop { position: 0.5; color: "#ff8008" }
    }

    anchors.fill: parent

    RadialGradient {
        id: backgroundFill
        anchors.fill: parent
        gradient: rootitem.juicyOrange
    }

    Swdc {
        width: parent.width * 0.8
        height: width * 0.3
        anchors.centerIn: parent
        color: "white"
    }

    QRcode{}
}

