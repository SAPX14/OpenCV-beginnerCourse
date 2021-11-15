import cv2 as cv 

# this function is designed to resize the dimensions of video , photo , or live video i.e web cam 

def rescaleFrame(frame ,scale=0.75):           # function takes 2 parameter , frame and scale

    width = int(frame.shape[1]*scale)          # rembember this syntax !! 
    height = int(frame.shape[0]*scale)
    dimensions = (width ,height)               # dimension var is assigned for a tuple of width and height
    return cv.resize(frame ,dimensions ,interpolation=cv.INTER_AREA)

# this function can only be used for live video captures such as web cam
def changeRes(width ,heigth):
    video.set(3 ,width)                        # .set function takes 1 value and 1 argument
    video.set(4 ,heigth)

# image resizing

img = cv.imread("Photos/doge.jpg")             # reads image to access file location 
resized_img = rescaleFrame(img)                # var set to call function and provide img parameter
cv.imshow('Doge', img)                         # orignal img
cv.imshow('Doge resized', resized_img)         # resized img

# playing a video and resizing using cv2

video = cv.VideoCapture("Videos/bahubali.mp4") # creating a var for video capture

while True:                                    # while loop is used to loop into frames of video
    isTrue, frame = video.read()               # isTrue is boolean argument for loop , frame is var for reading the video

    resized_video = rescaleFrame(frame ,scale=0.5) # var declared to call function with 2 paramter , note that scale value can be customized

    cv.imshow("Bahubali" , frame)   # displaying the original video
    cv.imshow("Bahubali resized" , resized_video) # display the resized video

    ''' if waitkey(20) means video plays for 20 seconds and 'd' key is pressed the while loop breaks
        0xFF==ord('d') is an in built command to quit the loop and it can be assingned any key
    '''
    if cv.waitKey(20) & 0xFF==ord('d'): 
        break

video.release()                                # it releases or sets free the video variable from loop
cv.destroyAllWindows()                         # destroyes or closes all open windows    