import sys
import cv2 
import imutils
import serial
import time
from yoloDet import YoloTRT

serial_port = "/dev/ttyUSB0"

engine_path = "yolov5/build/model.engine"

WIDTH = 600

ser = serial.Serial(serial_port, 9600)

# use path for library and engine file
model = YoloTRT(library="yolov5/build/libmyplugins.so", engine=engine_path, conf=0.5, yolo_ver="v5")

#cap = cv2.VideoCapture("videos/testvideo.mp4")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=WIDTH)
    detections, t = model.Inference(frame)
    #for obj in detections:
    #   print(obj['class'], obj['conf'], obj['box'])
    n_shrimp = len(detections)
    print(n_shrimp)
    if (n_shrimp > -1):
    	ser.write(str(n_shrimp).encode())
    print("FPS: {} sec".format(1/t))
    cv2.imshow("Output", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    time.sleep(0.05)
cap.release()
cv2.destroyAllWindows()
ser.close()
sys.exit()
quit()
