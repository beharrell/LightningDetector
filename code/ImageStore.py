import queue
import os

class ImageStore():
    def __init__(self):
        self.imageQueue = queue.Queue(30)
        self.safeDirCount = 0
        self.picCount = 0

    def add(self, image, saveThisImage) :
        if saveThisImage :
            image.save("Lightning" + str(self.picCount) + ".jpg")
            self.picCount+=1
        self.imageQueue.put(image)
        if (self.imageQueue.full()):
            self.imageQueue.get()

    def SaveImageQueue(self):
        dirName = ".\\Save%d"%self.safeDirCount
        if not os.path.isdir(dirName):
            os.makedirs(dirName)
        self.safeDirCount+=1
        saveCount = 0
        while not self.imageQueue.empty():
            image = self.imageQueue.get()
            image.save("%s\\%d.jpg" % (dirName, saveCount))
            saveCount+=1