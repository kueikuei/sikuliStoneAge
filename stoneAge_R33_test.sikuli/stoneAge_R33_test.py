# 33隨機pk - test
# 單人測試版

# 引用package
import threading
import time# 引用package

systemLocation = Location(748, 614)


# 視窗切換與設定 by location
def switchWindow():
    click("1526652852632.png")
    #mouseMove(Location(562, 747))
    wait(2)
    click(Location(228, 665))
    if exists("1526572518625.png"):
        battleSetting()

    
    #重複構造定時器
    timer = threading.Timer(5,switchWindow) #每n秒重複執行
    timer.start()


def battleSetting(): 
    # 更換寵物狀態
    click(Location(290, 617))
    while not exists("1526573167502.png"):
        click(Location(42, 70))

    wait(3)

    while not exists("1526573101833.png"):
        click(Location(41, 122))
    
    # 開始PK
    click(systemLocation)

    # 關閉AI
    if exists("1526654646564.png"):
        click("1526654646564.png")
        
    click("1526572108497.png")
    wait(5)

    #選擇當天pk選項
    pk_pos = Location(396, 386)
    click(pk_pos)

    # 改為自動戰鬥
    click(systemLocation)
    click("1526572187273.png")

    # 關閉systemLocation
    click("1526659575850.png")

global timer
# 首次執行
timer = threading.Timer(2,switchWindow)
timer.start()

# 關掉定時器
timer.cancel(300) #60s測試


