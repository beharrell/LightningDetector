from PIL import Image
import cv2
import time
from ImageStore import ImageStore
from FrameRate import FrameRate 
from ElapseTimer import ElapseTimer
from Recogniser import Recogniser
#from Camera import Camera
from Camera import DummyCamera

print("Starting app")
picCount = 0
captureNextFrame = False
frameRate = FrameRate()
lightningSurpressTimer = ElapseTimer(1, False)
store = ImageStore()
recogniser = Recogniser()
#mainCamera = Camera()
mainCamera = DummyCamera()

cap = cv2.VideoCapture('..\\video\\lightningVideo.mp4')
#cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open image source")


while(True):
    detectedLightening = False
    savedImage = False
    ret, frame = cap.read() 
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    rgbArray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    image = Image.fromarray(rgbArray)

    if (captureNextFrame) :
        cv2.imshow("next",frame)
        captureNextFrame = False
    else:
        refTime = time.time()
        detectedLightening = recogniser.ContainsLightning(image)
        diff = time.time() - refTime
        #("detect time %1.1f" % (1000 * diff))
        

    if frameRate.Update() : 
        print("%1.1f fps" % frameRate.rate)
        
    if lightningSurpressTimer.Update():
        savedImage = detectedLightening
        if savedImage:
            cv2.imshow('dectected',frame)
            captureNextFrame = True
            mainCamera.TakePhoto() 
            lightningSurpressTimer.Reset()

    store.add(image, savedImage)

    # Display the resulting frame
    cv2.imshow('frame',frame)

    key =  cv2.waitKey(1) & 0xFF    
    if key == ord('q'):
        break
    if key == ord(' '):
        store.SaveImageQueue()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

