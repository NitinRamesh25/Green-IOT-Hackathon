from PySide2.QtGui import *
from PySide2.QtQuick import *


class ImageProvider(QQuickImageProvider):
    def __init__(self):
        super(ImageProvider, self).__init__(QQuickImageProvider.Image)

    def requestImage(self, id, size, requestedSize):
        if id == 'ip.jpg':
            return QImage('generated/ip.jpg')

        return None
