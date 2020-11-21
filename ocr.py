import pyautogui
import cv2
import pytesseract
import numpy as np

def convert_img(img,threshold): 
    for x in range(img.shape[0]): 
        for y in range(img.shape[1]):
            if img[x][y] > threshold: 
                img[x][y] = 255 
            else: 
                img[x][y] = 0 
    return img


def main():
    # SetVariable("tessedit_char_whitelist", "0123456789")
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img1 = pyautogui.screenshot(region=[855,522,50,80]) # x,y,w,h
    img2 = pyautogui.screenshot(region=[905,522,50,80]) # x,y,w,h
    img3 = pyautogui.screenshot(region=[955,522,50,80]) # x,y,w,h
    img4 = pyautogui.screenshot(region=[1005,522,50,80]) # x,y,w,h
    img1 = cv2.cvtColor(np.asarray(img1),cv2.COLOR_RGB2BGR)
    img2 = cv2.cvtColor(np.asarray(img2),cv2.COLOR_RGB2BGR)
    img3 = cv2.cvtColor(np.asarray(img3),cv2.COLOR_RGB2BGR)
    img4 = cv2.cvtColor(np.asarray(img4),cv2.COLOR_RGB2BGR)

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    # canny = cv2.Canny(blurred, 30, 150)

    # con_img = convert_img(gray,240)

    code1 = pytesseract.image_to_string(img1,config='tessedit_char_whitelist=0123456789 --psm 6')
    code2 = pytesseract.image_to_string(img2,config='tessedit_char_whitelist=0123456789 --psm 6')
    code3 = pytesseract.image_to_string(img3,config='tessedit_char_whitelist=0123456789 --psm 6')
    code4 = pytesseract.image_to_string(img4,config='tessedit_char_whitelist=0123456789 --psm 6')
    print(code1)
    print(code2)
    print(code3)
    print(code4)
    # cv2.imwrite('screenshot.png',img)
    cv2.imshow("123",img1)
    cv2.waitKey(0)
    cv2.imshow("123",img2)
    cv2.waitKey(0)
    cv2.imshow("123",img3)
    cv2.waitKey(0)
    cv2.imshow("123",img4)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()