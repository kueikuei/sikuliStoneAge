# ----------------前提設定----------------- # 
# 戰鬥設定 - 第一回合毀天
# 聊天限制五行
# ----------------前提設定----------------- # 

import threading
import time# 引用package
import random
#random.randint(0,99)

#重複構造定時器
def dosthing():
    #player1
    click("1526652852632.png")
    wait(1)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()
    wait(1)
    # random移動假裝
    #rightClick(Location(random.randint(-200,200), random.randint(-200,200)))
    click("1527327582643.png")

    wait(6)

    # player2
    click("1526652852632.png")
    wait(1)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()
    wait(1)
    # random移動假裝
    #rightClick(Location(random.randint(-200,200), random.randint(-200,200)))
    click("1527327582643.png")

    wait(5)
    #timer = threading.Timer(5,dosthing()) #每n秒重複執行
    timer = threading.Timer(random.randint(1,5),dosthing()) #每n秒重複執行
    timer.start()

global timer
# 首次執行
timer = threading.Timer(1,dosthing())
timer.start()

# 關掉定時器
#timer.cancel(300) #60s測試







