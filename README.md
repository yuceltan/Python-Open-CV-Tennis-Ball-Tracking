# Python Open CV Tennis Ball Tracking
 
CONTENT:

1-Description of the project
2-Purpose of the project
3-Used methods
4-Screenshot of the program
5-Source code of the program

1-Description of the project

In this project main purpose is using of the opencv with Python OOP, in this way we can identify many objects centroid,shape and their colors this project aims for this.

2-Purpose of the project

Purpose of this project identify tennis balls with OOP and program can identify many things such as, shape, color, centroid… 

3- Used methods

I used 4 different libraries in my program first one is “cv2”,second one is “imutils”, third one is “numpy”, last one is ”tkinter” also I created a tennis_ball_detect, it is a abstract class in this way I defined my methods in this class “def centroid()” in this method I wrote tennis ball detecting, this program calculate tennis ball’s centroid and it identify green tennis ball(you can change it from GREEN_RANGE).In “def interface()”I created my interface in this interface I created three different buttons for my program first button call def centroid() in this way if you click this button it open tennis ball detect program and if you click second button (Color Control) this button call “def tracker()” thanks to this method you can change camera settings for tennis ball detecting than you have to write this parameters to GREEN_RANGE.

Third button is Exit button I used “def exitcode()” method for this button than I created a class from “tennis_ball_detect class”its name is “general_control” in this class there are all methods and their parameters also if you want to read a video file you can do it in program you have to write your video file’s name  in “def centroid()”. In centroid method I added contour with these codes “mask=cv2.erode(mask,None,iterations=3)and mask=cv2.dilate(mask,None,iterations=3)”than I used if for calculate tennis ball detect and centroid with this algorithm -



