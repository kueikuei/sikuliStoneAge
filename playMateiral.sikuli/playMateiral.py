# ----------------前提設定----------------- # 
# 戰鬥設定 - 首回放火
# 設定素材打寶
# 設定掉線重連
# ----------------前提設定----------------- # 

import threading
import time
import random

#重複構造定時器
def dosthing():
    
    #player1
    click("1526652852632.png")
    wait(1)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()
    wait(2)
    paste(unicode("/疊加", "utf8"))
    wait(0.1)
    keyDown(Key.ENTER)
    keyUp()
    wait(2)

    # player2
    click("1526652852632.png")
    wait(1)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()
    wait(2)
    paste(unicode("/疊加", "utf8"))
    wait(0.1)
    keyDown(Key.ENTER)
    keyUp()
    wait(2)
    
    # player3
    click("1526652852632.png")
    wait(1)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()
    wait(2)
    paste(unicode("/疊加", "utf8"))
    wait(0.1)
    keyDown(Key.ENTER)
    keyUp()
    wait(2)

    # player4
    click("1526652852632.png")
    wait(1)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()
    wait(2)
    paste(unicode("/疊加", "utf8"))
    wait(0.1)
    keyDown(Key.ENTER)
    keyUp()
    wait(2)

    # player5
    click("1526652852632.png")
    wait(1)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()
    wait(2)
    paste(unicode("/疊加", "utf8"))
    wait(0.1)
    keyDown(Key.ENTER)
    keyUp()
    wait(2)

    #timer = threading.Timer(5,dosthing()) #每n秒重複執行
    wait(1800) #半小時
    timer = threading.Timer(5,dosthing()) #每n秒重複執行
    timer.start()

global timer
# 首次執行
timer = threading.Timer(60,dosthing())
timer.start()

# 關掉定時器
#timer.cancel(300) #60s測試

