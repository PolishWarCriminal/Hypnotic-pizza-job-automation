import cv2
import numpy as np
import pyautogui
from PIL import Image, ImageChops
import sys, os
import time
import keyboard
import threading

############################################# INTERRUPTS ####################################################################################################################################################################################
############################################# INTERRUPTS ###############################################################################################################################################################################
running = False
kill = False

def handle_stop():
    global running
    running = False
    print("Stop signal received.")
    
def handle_start():
    global running
    running = True
    print("start signal received.")
    
def handle_kill():
    global kill
    print("killing program")
    kill = True

############################################# GREEN BUTTON PRESSING #################################################################################################################################################################################################################################
############################################# GREEN BUTTON PRESSING ####################################################################################################################################################################################
noBut = 0
time.sleep(1)
def find_specific_color(image, target_color, tolerance=10):
    # Convert the target color from RGB to BGR (OpenCV uses BGR format)
    target_color_bgr = target_color[::-1]
    
    # Define the lower and upper bounds with the tolerance
    lower_bound = np.array([
        max(0, target_color_bgr[0] - tolerance),
        max(0, target_color_bgr[1] - tolerance),
        max(0, target_color_bgr[2] - tolerance)
    ])
    upper_bound = np.array([
        min(255, target_color_bgr[0] + tolerance),
        min(255, target_color_bgr[1] + tolerance),
        min(255, target_color_bgr[2] + tolerance)
    ])
    
    # Convert the screenshot image to BGR
    bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # Find pixels within the color range
    mask = cv2.inRange(bgr_image, lower_bound, upper_bound)
    
    # Find contours for the color
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        # Assume it's the green button if the shape is roughly circular
        if 0.8 < w / h < 1.2:  # Check for roughly circular shapes
            return x + w // 2, y + h // 2  # Return the center coordinates
    return None


def main():
    global noBut
    global running
    keyboard.on_press_key('e', lambda _: handle_start())
    keyboard.on_press_key('q', lambda _: handle_stop())
    keyboard.on_press_key('0', lambda _: handle_kill())
    target_color = (82, 255, 0) 
    while True:
        if kill == True:
            break
        while running == True:
            while noBut <= 25:
                screenshot = pyautogui.screenshot()
                frame = np.array(screenshot)
                green_button_pos = find_specific_color(frame, target_color)
                if green_button_pos:
                    pyautogui.click(green_button_pos)
                    time.sleep(0.1)
                else:
                    print("Green button not found.")
                    noBut += 1   
        noBut = 0                                               
    


#################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################

############################################# CHECKING PIZZA TYPE ####################################################################################################################################################################################
############################################# CHECKING PIZZA TYPE ####################################################################################################################################################################################

tomato_pizza = cv2.imread("C:\\python\\Automation\\Tomato.PNG", cv2.IMREAD_COLOR)
artichoke_pizza = cv2.imread("C:\\python\\Automation\\Artichoke.PNG", cv2.IMREAD_COLOR)
Squid_pizza = cv2.imread("C:\\python\\Automation\\Squid.PNG", cv2.IMREAD_COLOR)
Sausage_pizza = cv2.imread("C:\\python\\Automation\\Sausage.PNG", cv2.IMREAD_COLOR)
Tuna_pizza = cv2.imread("C:\\python\\Automation\\Tuna.PNG", cv2.IMREAD_COLOR)
Olive_pizza = cv2.imread("C:\\python\\Automation\\Olive.PNG", cv2.IMREAD_COLOR)



# M = Making
M_Tom_Pizza = 0
M_Art_Pizza = 0
M_Squ_Pizza = 0
M_Sau_Pizza = 0
M_Tun_Pizza = 0
M_Olv_Pizza = 0


def checkpizzatypes():

   
    screenshotpizzamenu = pyautogui.screenshot()
    SSPizzamenuNP = np.array(screenshotpizzamenu)
    screen_image = cv2.cvtColor(SSPizzamenuNP, cv2.COLOR_RGB2BGR)
    cv2.imshow("N", SSPizzamenuNP)
    cv2.waitKey()
    cv2.imshow("screenim", screen_image)
    cv2.waitKey()

    #screen_image = cv2.imread("C:\\python\\Automation\\Screen.PNG", cv2.IMREAD_UNCHANGED) ####CHANGE IN FUTURE FOR SCREENSHOT



    Tomresult = cv2.matchTemplate(screen_image, tomato_pizza, cv2.TM_CCOEFF_NORMED)
    min_val, maxTom_val, min_loc, maxTom_loc = cv2.minMaxLoc(Tomresult)
    print(maxTom_val)
    cv2.imshow("result",Tomresult)
    cv2.waitKey()

    Artresult = cv2.matchTemplate(screen_image, artichoke_pizza, cv2.TM_CCOEFF_NORMED)
    min_val, maxArt_val, min_loc, maxArt_loc = cv2.minMaxLoc(Artresult)
    cv2.imshow("result",Artresult)
    cv2.waitKey()

    Squresult = cv2.matchTemplate(screen_image, Squid_pizza, cv2.TM_CCOEFF_NORMED)
    min_val, maxSqu_val, min_loc, maxSqu_loc = cv2.minMaxLoc(Squresult)
    cv2.imshow("result",Squresult)
    cv2.waitKey()

    Sauresult = cv2.matchTemplate(screen_image, Sausage_pizza, cv2.TM_CCOEFF_NORMED)
    min_val, maxSau_val, min_loc, maxSau_loc = cv2.minMaxLoc(Sauresult)
    cv2.imshow("result",Sauresult)
    cv2.waitKey()

    Tunresult = cv2.matchTemplate(screen_image, Tuna_pizza, cv2.TM_CCOEFF_NORMED)
    min_val, maxTun_val, min_loc, maxTun_loc = cv2.minMaxLoc(Tunresult)
    cv2.imshow("result",Tunresult)
    cv2.waitKey()

    Olvresult = cv2.matchTemplate(screen_image, Olive_pizza, cv2.TM_CCOEFF_NORMED)
    min_val, maxOlv_val, min_loc, maxOlv_loc = cv2.minMaxLoc(Olvresult)
    cv2.imshow("result",Olvresult)
    cv2.waitKey()

    if maxTom_val >0.8:
        M_Tom_Pizza = 1
        pyautogui.click(maxTom_loc)
    elif maxArt_val > 0.8:
        M_Art_Pizza = 1
        pyautogui.click(maxArt_loc)
    elif maxSqu_val > 0.8:
        M_Squ_Pizza = 1
        pyautogui.click(maxSqu_loc)
    elif maxSau_val > 0.8:
        M_Sau_Pizza = 1
        pyautogui.click(maxSau_loc)
    elif maxTun_val > 0.8:
        M_Tun_Pizza = 1
        pyautogui.click(maxTun_loc)
    elif maxOlv_val > 0.8:
        M_Olv_Pizza = 1
        pyautogui.click(maxOlv_loc)


##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################


############################################# SELECTING PIZZA TOPPING #################################################################################################################################################################################################################################
############################################# SELECTING PIZZA TOPPING #################################################################################################################################################################################################################################

def PickPizza():
    if M_Tom_Pizza == 1:
        pyautogui.click(1097,729)    
    elif M_Art_Pizza == 1:
        pyautogui.click(1307,442)
    elif M_Squ_Pizza == 1:
        pyautogui.click(1107,571)
    elif M_Sau_Pizza == 1:
        pyautogui.click(1301,5592)
    elif M_Tun_Pizza == 1:
        pyautogui.click(1071,427)
    elif M_Olv_Pizza == 1:
        pyautogui.click(1272,720)

    M_Tom_Pizza = 0
    M_Art_Pizza = 0
    M_Squ_Pizza = 0
    M_Sau_Pizza = 0
    M_Tun_Pizza = 0
    M_Olv_Pizza = 0


##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################


############################################# SCHEDULING#################################################################################################################################################################################################################################
############################################# SCHEDULING #################################################################################################################################################################################################################################


time.sleep(5)
while True:
    checkpizzatypes()
    main()
    main()
    time.sleep(3)
    PickPizza()
