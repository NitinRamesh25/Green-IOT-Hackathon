import QtQuick 2.0

Rectangle {
    id: swdc
    objectName: "swdc"

    property int partitionCount: 3

    Row {
        anchors.fill: parent
        spacing: 0

        Partition {
            id: partition1
            partitionCount: swdc.partitionCount
            name: "Partition 1"
        }

        Partition {
            id: partition2
            partitionCount: swdc.partitionCount
            name: "Partition 2"
        }

        Partition {
            id: partition3
            partitionCount: swdc.partitionCount
            name: "Partition 2"
        }
    }

    function openPartition(partitionID, wasteType) {
        console.log("Got partitionID in qml");
        if(partitionID == "partition1") {
            partition1.wasteType = wasteType;
            partition1.open();
        }
        else if(partitionID == "partition2") {
            partition2.wasteType = wasteType;
            partition2.open();
        }
        else if(partitionID == "partition3") {
            partition3.wasteType = wasteType;
            partition3.open();
        }
    }
}