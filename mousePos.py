import pyautogui
import time
width, height = pyautogui.size() # 取得螢幕寬度、高度
print('screen size = ',width, height)

#每隔一段時間取得滑鼠座標
for i in range(20):
    time.sleep(1) # 暫停一秒
    xloc, yloc = pyautogui.position() # 獲得滑鼠游標
    print(xloc,yloc)