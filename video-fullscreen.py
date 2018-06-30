# usage: python video-fullscreen.py
# usage: python video-fullscreen.py --video videos/example_01.mp4
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


cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

fps = FPS().start()
realtime_fps = 0

while True:
    start = time.time()

    frame = vs.read()
    frame = imutils.resize(frame, width=1366)
    # frame = cv2.resize(frame, (1366, 768))

    cv2.rectangle(frame, (0, int(frame.shape[0] * 0.965)),
                  (frame.shape[1], frame.shape[0]), (255, 255, 255), -1)
    label = "{}: {:.2f}".format("fps", realtime_fps)
    cv2.putText(frame, label, (10, int(frame.shape[0] * 0.99)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, "temperature:", (210, int(frame.shape[0] * 0.99)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, "lastgesture:", (410, int(frame.shape[0] * 0.99)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)

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
