import threading
import time# 引用package
import random
#random.randint(0,99)

#重複構造定時器
def dosthing():
    #player1
    click("1526652852632.png")
    wait(0.1)
    click(Location(571, 666))
    
    # random移動假裝
    rightClick(Location(random.randint(-200,200), random.randint(-200,200)))

    wait(random.randint(1,10))
    # 移動回來
    click("1526815122780.png")
    #click(Location(369, 348))
    wait(5)

    # player2
    click("1526652852632.png")
    wait(0.1)
    click(Location(891, 654))
    
    # random移動假裝
    rightClick(Location(random.randint(-200,200), random.randint(-200,200)))

    wait(random.randint(1,5))
    # 移動回來
    click("1526815122780.png")
    #click(Location(369, 348))
    wait(5)
    timer = threading.Timer(5,dosthing()) #每n秒重複執行
    timer.start()

global timer
# 首次執行
timer = threading.Timer(1,dosthing())
timer.start()

# 關掉定時器
#timer.cancel(300) #60s測試







