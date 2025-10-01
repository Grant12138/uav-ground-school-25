import cv2
import numpy as np

def get_limits(color):
    hsv_color = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)

    hue = hsv_color[0][0][0]

    if hue >= 165: # red hue wrap-around
        lower_limit = np.array([hue - 10, 100, 100], dtype = np.uint8)
        upper_limit = np.array([180, 255, 255], dtype=np.unit8)
    elif hue <= 15:
        lower_limit = np.array([0, 100, 100], dtype=np.uint8)
        upper_limit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lower_limit = np.array([hue - 10, 100, 100], dtype = np.uint8)
        upper_limit = np.array([hue + 10, 255, 255], dtype = np.uint8)
    
    return lower_limit, upper_limit

def main():
    img = cv2.imread("week1/Images/Cal Logo.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # cv2.imshow("Cal Logo", img)

    lower_limit, upper_limit = get_limits((255, 0, 0))

    cv2.imshow("Blue mask", cv2.inRange(img, lower_limit, upper_limit))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()