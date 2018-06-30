# usage: python video-roi.py
# usage: python video-roi.py --video videos/example_01.mp4
# import the necessary packages
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=False,
                help="path to input video file")
args = vars(ap.parse_args())

if args.get("video", None) is None:
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    # vs = VideoStream(usePiCamera=True).start()
    time.sleep(0.25)
else:
    print("[INFO] starting video file thread...")
    vs = FileVideoStream(args["video"]).start()
    time.sleep(1.0)

x0 = 150
y0 = 0
height = 480
width = (640 - 2 * x0)

fps = FPS().start()

while True:
    frame = vs.read()
    # frame = imutils.resize(frame, width=400)

    roi = frame.copy()[y0:y0 + height, x0:x0 + width]
    cv2.rectangle(frame, (x0, y0), (x0 + width, y0 + height), (0, 255, 0), 1)

    cv2.imshow("Frame", frame)
    cv2.imshow("roi", roi)

    if args.get("video", None) is not None:
        time.sleep(0.05)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    if args.get("video", None) is not None:
        key = cv2.waitKey(1)
        if vs.more() is False:
            break

    fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
