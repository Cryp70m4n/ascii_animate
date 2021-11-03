import cv2
import os
import sys

def FrameCapture(path):

    vidObj = cv2.VideoCapture(path)

    count = 0

    success = 1

    while success:
        try:
            success, image = vidObj.read()

            cv2.imwrite("frames/frame%d.jpg" % count, image)

            count += 1
            print("loading:",count)

        except Exception as e:
            os.system(f"python3 ascii_animate.py {count-1}")



if len(sys.argv) < 2:
    print("[X]-Missing an argument")
    print("[!]-Usage python3 runner.py video.mp4")
    sys.exit(0)


video_name=sys.argv[1]
FrameCapture(video_name)
