import cv2
# import pyautogui

# Clicking each page of the notebook and then 
# saving it with proper name for uploading 
# it is a task of daily routine that I find boring

def PhotoClick() :
    num = 1   
    # img = input(print("Name of the file  "))
    img = input("Name of the file  ")
    Camera = True
    while(Camera):
        function = input("Please press Enter to click the next photo and press 2 to end the process..  ")
        Camera = False
        if(function == ''):
            videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            result = True
            while(result):
                # Reading the frames when camera is on
                ret, frame = videoCaptureObject.read()
                # imwrite() is a function to store image
                imageName = img + str(num) + ".png"
                cv2.imwrite(imageName,frame)
                result = False
                num = num + 1
            videoCaptureObject.release()
            # closes all windows that camera might have open
            cv2.destroyAllWindows()
            Camera = True
        if(function == '2'):
            Camera = False

            



PhotoClick()