import cv2

def is_camera_available():

    cap = cv2.VideoCapture(0)    
    
    if cap.isOpened():
        cap.release()
        return True
    else:
        return False

if __name__ == "__main__":
    camera_available = is_camera_available()
    if camera_available:
        print("Camera is available.")
    else:
        print("Camera is not available.")
