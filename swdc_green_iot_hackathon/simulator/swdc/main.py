from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtQuick import *
import sys

from app_resources import qml_rc
from image_provider import ImageProvider
import qrcode_generator

from mqtt_thread import MqttThread


def main():
    if len(sys.argv) < 2:
        print('Incorrect number of arguments')
        return

    if 'container' not in sys.argv[1]:
        print('Argument should be one of these: container1, container2 .etc.')
        return

    container_id = sys.argv[1]
    qrcode_generator.generate(container_id, 'generated', 'ip')

    app = QGuiApplication()

    view = QQuickView()
    view.setTitle('Smart Waste Disposal Container - Simulator')
    view.engine().addImageProvider("ImageProvider", ImageProvider())
    view.setSource(QUrl('qrc:/qml/main.qml'))
    view.setMinimumSize(QSize(900, 500))

    root = view.rootObject()
    swdc = root.findChild(QObject, "swdc")

    thread = MqttThread(view, container_id)
    thread.open_partition.connect(swdc.openPartition)
    thread.start()

    view.show()
    app.exec_()


if __name__ == '__main__':
    main()
