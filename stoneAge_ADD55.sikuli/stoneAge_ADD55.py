# 55隨機pk

# ----------------前提設定----------------- # 
# 開啟五隻人物、並且都在醫院
# 戰寵第一位、騎寵第二位
# 先把人物位置都定好
## 隊員方向面對隊長
# 隊長人物在最後視窗
# ----------------前提設定----------------- # 


# 引用package
#import threading
#import time# 引用package

systemLocation = Location(748, 614)

#pointer = 0
# 視窗切換與設定 by location
def switchWindow():
    

    #click("1526652852632.png")
    # 隊長位置
    #wait(0.1)
    #click(Location(842, 662))
    
    #type(Key.RIGHT)
    #keyDown(Key.ENTER)
    #keyUp()

    

    # 戰鬥結束後隊長取消團隊  
    #click("1526660308320.png")  

    # 開啟組隊
    #click("1526718752895.png")
    #if exists("1526718966234.png"):
    #    click(Location(145, 76))
    #click("1526718796932.png")

    # 隊員1開始加入
    click("1526652852632.png")
    #click(Location(228, 665))
    wait(0.1)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()   
    # 檢測是否還在pk
    while not exists("1526660308320.png"):
        #wait(1)
        type(Key.ESC)
        click("1526994564988.png")
        wait(0.1)
        click("1526994587978.png")
        wait(5)
    #click("1526660308320.png")
    
    MemberbattleSetting()

     # 隊員2開始加入
    click("1526652852632.png")
    wait(0.1)
    #click(Location(345, 664))
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()  
    while not exists("1526660308320.png"):
        #wait(1)
        type(Key.ESC)
        click("1526994564988.png")
        wait(0.1)
        click("1526994587978.png")
        wait(5)
    #click("1526660308320.png")

    MemberbattleSetting()

    # 隊員3開始加入
    #click("1526652852632.png")
    #wait(0.1)
    #click(Location(517, 663))
    #wait(0.1)
    #while not exists("1526660308320.png"):
    #    wait(1)
   # click("1526660308320.png")

    #MemberbattleSetting()

    # 隊員4開始加入
    #click("1526652852632.png")
    #wait(0.1)
    #click(Location(677, 664))
    #wait(0.1)
    #while not exists("1526660308320.png"):
    #    wait(1)
    #click("1526660308320.png")

    #MemberbattleSetting()

    # 隊長動作
    click("1526652852632-1.png")
    wait(0.1)
    #click(Location(842, 662))
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()
    if exists("1526572518625-1.png"):
        LeaderbattleSetting()

    #透過非定時寫法
    # 假如進入戰鬥
    #while exists("1526572518625-1.png"):
    #   wait(1)

    #戰鬥結束後重新啟動
    while not exists("1526572518625-1.png"):
        #wait(1)
        type(Key.ESC)
        click("1526994564988.png")
        wait(0.1)
        click("1526994587978.png")
    
        wait(5)
    # 隊長等隊員
    #click("1526718443462.png")
    
    switchWindow()
    
    #重複構造定時器
    #timer = threading.Timer(120,switchWindow) #每n秒重複執行
    #timer.start()

def MemberbattleSetting(): 
    # 更換寵物狀態
    #click(Location(290, 617))

    #click(Location(42, 70)) #防呆機制
    #wait(0.1)
    #while not exists("1526573167502.png"):
        #click(Location(42, 70))

    #wait(0.1)

    #click(Location(41, 122)) #防呆機制
    #wait(0.1)
    #while not exists("1526573101833.png"):
 #       click(Location(41, 122))

    click(systemLocation)
    
    # 關閉AI
    if exists("1526660560282.png"):
        click("1526660560282.png")
        
    wait(0.1)

    # 關閉systemLocation
    click("1526659575850.png")

def LeaderbattleSetting(): 
    # 更換寵物狀態
    
    #click(Location(290, 617))
    #click(Location(42,70)) #防呆機制
    #wait(0.1)
   # while not exists("1526573167502.png"):
        #click(Location(42, 70))

    #wait(0.1)

    #click(Location(41,122)) #防呆機制
    #wait(0.1)
    #while not exists("1526573101833.png"):
 #       click(Location(41, 122))
    
    # 開始PK
    click(systemLocation)

    # 關閉AI
    if exists("1526654646564.png"):
        click("1526654646564.png")
        
    click("1526572108497.png")
    wait(0.1)

    #選擇當天pk選項
    pk_pos = "1526994127450.png"
    click(pk_pos)

    #if exists("1526739916478.png"):
    if exists("1526995805693.png"):
        wait(1)

    # 改為自動戰鬥
   # click(systemLocation)
    #try:
 #       click("1526831872731.png")
       # click("1526659575850-1.png")
    #except:
     #   wait(1)
    
    # 一定要進入比賽才繼續往下走
    pointer = 0
    while exists("1526572518625-1.png"):
        wait(1)
        pointer = pointer + 1
        if(pointer>150):
            type(Key.ESC)
            click("1526572108497.png")
            click("1526996440330.png")
            LeaderbattleSetting()

    # pk結束後才往下走
    while not exists("1526572518625-1.png"):
        click(systemLocation)
        click("1526831872731.png")
        click("1526659575850-1.png")
        wait(1)

#global timer
# 首次執行
switchWindow()
#timer = threading.Timer(2,switchWindow)
#timer.start()

# 關掉定時器
#timer.cancel(300) #60s測試
