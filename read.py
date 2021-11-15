import cv2 as cv

# displaying an image using cv2

img = cv.imread("Photos/doge.jpg") # reads image to access file location 
cv.imshow('Doge',img)     # displays image in python window
cv.waitKey(0)             # waitkey 0 means photo will be diplayed for infinite amount of time 


# playing a video using cv2

video = cv.VideoCapture("Videos/bahubali.mp4") # creating a var for video capture

while True:                                    # while loop is used to loop into frames of video
    isTrue, frame = video.read()  # isTrue is boolean argument for loop , frame is var for reading the video
    cv.imshow("Bahubali",frame)   # displaying the video

    ''' if waitkey(20) means video plays for 20 seconds and 'd' key is pressed the while loop breaks
        0xFF==ord('d') is an in built command to quit the loop and it can be assingned any key
    '''
    if cv.waitKey(20) & 0xFF==ord('d'): 
        break

video.release()                  # it releases or sets free the video variable from loop
cv.destroyAllWindows()           # destroyes or closes all open windows