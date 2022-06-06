from abc import ABC, abstractmethod
import cv2
import imutils
import numpy as np

from tkinter import *


class tennis_ball_detect(ABC):
    @abstractmethod
    def centroid(self):
        pass

    @abstractmethod
    def interface(self,window):
        self.window=window

    @abstractmethod
    def exitcode(self):
        pass




window=Tk()
window.geometry("700x700")
window.title("Tennis Ball Detect Yüceltan Ebiri")
class general_control(tennis_ball_detect):

    def centroid(self):
        cap = cv2.VideoCapture(0)
        video_file = ''  # ''ab03.mp4'
        WIDTH = 600
        HIGH = 480
        ONLY_MAX = False
        GREEN_RANGE = ((8, 73, 110), (145, 255, 255))

        colorLower, colorUpper = GREEN_RANGE

        if len(video_file) == 0:
            kamera = cv2.VideoCapture(0)
        else:
            kamera = cv2.VideoCapture(video_file)


        cv2.moveWindow('frame', 120, 120)

        while True:
            (ok, frame) = kamera.read()


            if len(video_file) > 0 and not ok:
                break

            frame = imutils.resize(frame, WIDTH, HIGH)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            mask = cv2.inRange(hsv, colorLower, colorUpper)
            mask = cv2.erode(mask, None, iterations=3)
            mask = cv2.dilate(mask, None, iterations=3)

            mask_copy = mask.copy()

            cnts = cv2.findContours(mask_copy, cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)[-2]

            if len(cnts) > 0:
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)

                if M["m00"] != 0:
                    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                else:
                    # set values as what you need in the situation
                    center = 0

                # only proceed if the radius meets a minimum size
                if radius > 10:
                    # draw the circle and centroid on the frame,
                    # then update the list of tracked points
                    cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                    cv2.circle(frame, center, 3, (0, 0, 255), -1)
                    cv2.putText(frame, "centroid", (center[0] + 10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4,
                                (0, 0, 255),
                                1)
                    cv2.putText(frame, "(" + str(center[0]) + "," + str(center[1]) + ")",
                                (center[0] + 10, center[1] + 15),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
            cv2.imshow("mask",mask)
            cv2.imshow("yuceltan", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def tracker(self):
        frameWidth = 640
        frameHeight = 480
        cap1 = cv2.VideoCapture(0)
        cap1.set(3, frameWidth)
        cap1.set(4, frameHeight)
        cap1.set(10, 150)

        def empty(a):
            pass

        cv2.namedWindow("HSV")
        cv2.resizeWindow("HSV", 640, 240)
        cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
        cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
        cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
        cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
        cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
        cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

        while True:

            _, img = cap1.read()
            imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            h_min = cv2.getTrackbarPos("HUE Min", "HSV")
            h_max = cv2.getTrackbarPos("HUE Max", "HSV")
            s_min = cv2.getTrackbarPos("SAT Min", "HSV")
            s_max = cv2.getTrackbarPos("SAT Max", "HSV")
            v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
            v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
            print(h_min)

            lower = np.array([h_min, s_min, v_min])
            upper = np.array([h_max, s_max, v_max])
            mask = cv2.inRange(imgHsv, lower, upper)
            result = cv2.bitwise_and(img, img, mask=mask)

            mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
            hStack = np.hstack([img, mask, result])
            # cv2.imshow('Original', img)
            # cv2.imshow('HSV Color Space', imgHsv)
            # cv2.imshow('Mask', mask)
            # cv2.imshow('Result', result)
            cv2.imshow('Horizontal Stacking', hStack)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap1.release()
        cv2.destroyAllWindows()

    def exitcode(self):
        exit()

    def interface(self,window):

        self.window=window



        self.label1 = Label(window, text='Yüceltan Ebiri', relief="solid", width=20, font=("arial", 19, "bold"))
        self.label1.place(x=140, y=55)

        self.label2 = Label(window, text='180444074', width=20, font=("arial", 19, "bold"))
        self.label2.place(x=140, y=10)

        self.label3 = Label(window, text='Instructions', width=20, font=("arial", 35, "bold"))
        self.label3.place(x=5, y=100)

        self.label4 = Label(window, text='You can use Color Control button to make\n the ball look clearly ', width=80, font=("arial", 15, "bold"))
        self.label4.place(x=-170, y=160)

        self.greet_button = Button(self.window, text="TENNIS BALL", width=32, bg='red', fg='white', command=self.centroid)
        self.greet_button.pack()
        self.greet_button.place(x=160, y=280)

        self.color_button = Button(self.window, text="Color Control", width=32, bg='red', fg='white', command=self.tracker)
        self.color_button.pack()
        self.color_button.place(x=160, y=380)


        self.close_button = Button(self.window, text="Çıkış", width=32, bg='red', fg='white', command=self.exitcode)
        self.close_button.pack()
        self.close_button.place(x=160, y=480)


b1=general_control()
b1.interface(window)
window.mainloop()











