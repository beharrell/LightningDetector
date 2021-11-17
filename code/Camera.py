import socket

class Camera:
    def __init__(self):
        self.ConnectToCamera()

    def ConnectToCamera(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.client.bind(("192.168.1.132", 1234))
        self.connectedToCamera = False
        self.cameraAddress = ""
        while not self.connectedToCamera:
            data, self.cameraAddress = self.client.recvfrom(1024)
            if (data == b'Anyone here?'):
                self.client.sendto(b"hello", self.cameraAddress)
                self.connectedToCamera = True

    def TakePhoto(self):
        if (self.connectedToCamera):
            self.client.sendto(b'SHUTTER', self.cameraAddress)



class DummyCamera:
    def __init__(self):
        pass
    def TakePhoto(self):
        pass
