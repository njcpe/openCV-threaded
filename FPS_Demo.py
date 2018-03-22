# import the necessary packages
from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-ip", type=str, help="ip addr of camera server ex: 192.169.0.1:1000")
#ap.add_argument("-d", "--display", type=int, default=-1, help="Whether or not frames should be displayed")
args = vars(ap.parse_args())
hoststr = args["ip"]

# grab a pointer to the video stream and initialize the FPS counter
print("[INFO] sampling frames from webcam at " + hoststr + "...")
stream = cv2.VideoCapture('http://' + hoststr + '/video')
fps = FPS().start()

# loop over some frames
while (cv2.waitKey(1) != 27):
	# grab the frame from the stream and resize it to have a maximum
	# width of 400 pixels
	(grabbed, frame) = stream.read()  
	frame = imutils.resize(frame, width=400)

	# check to see if the frame should be displayed to our screen
	#if args["display"] > 0:
	cv2.imshow("Frame", frame)
	
	# update the FPS counter
	fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
stream.release()
cv2.destroyAllWindows()

# created a *threaded* video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from webcam...")
vs = WebcamVideoStream(src='http://192.168.0.3:8080/video').start()
fps = FPS().start()

# loop over some frames...this time using the threaded stream
while (cv2.waitKey(1) != 27):
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# check to see if the frame should be displayed to our screen
	#if args["display"] > 0:
	cv2.imshow("Frame", frame)
	
	# update the FPS counter
	fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()