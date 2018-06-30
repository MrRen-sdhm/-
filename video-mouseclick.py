# usage:
# python video-mouseclick.py
# python video-mouseclick.py --video videos/example_01.mp4

# import the necessary packages
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2

realtime_fps = 0
click = 0

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=False,
                help="path to input video file")
args = vars(ap.parse_args())

if args.get("video", None) is None:
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    # vs = VideoStream(usePiCamera=True).start()
    time.sleep(0.5)
else:
    print("[INFO] starting video file thread...")
    vs = FileVideoStream(args["video"]).start()
    time.sleep(1.0)


def click_and_crop(event, x, y, flags, param):
    # left mouse button clicked
    global click
    if event == cv2.EVENT_LBUTTONDOWN:
        click = 1


cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Frame", click_and_crop)
cv2.setWindowProperty("Frame", 0, 1)

fps = FPS().start()

while True:
    start = time.time()

    frame = vs.read()
    # frame = imutils.resize(frame, width=1366)
    # frame = cv2.resize(frame, (1366, 768))
    frame = cv2.resize(frame, (0, 0), fx=1.125, fy=1,
                       interpolation=cv2.INTER_NEAREST)

    cv2.rectangle(frame, (0, int(frame.shape[0] * 0.92)),
                  (frame.shape[1], frame.shape[0]), (255, 255, 255), -1)
    label = "{}: {:.1f}".format("fps", realtime_fps)
    cv2.putText(frame, label, (5, int(frame.shape[0] * 0.972)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv2.putText(frame, "temperature: 30", (90, int(frame.shape[0] * 0.972)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv2.putText(frame, "lastgesture: 5", (240, int(frame.shape[0] * 0.972)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    cv2.imshow("Frame", frame)
    # cv2.imshow("frame", frame)

    if args.get("video", None) is not None:
        time.sleep(0.05)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if click == 1:
        break

    if args.get("video", None) is not None:
        key = cv2.waitKey(1)
        if vs.more() is False:
            break

    fps.update()

    end = time.time()
    realtime_fps = 1 / (end - start)
    # print("[INFO] classification took {:.5} seconds".format(realtime_fps))

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
