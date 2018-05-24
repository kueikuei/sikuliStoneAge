# 55隨機pk

# ----------------前提設定----------------- # 
# 開啟五隻人物、並且都在醫院
# 戰寵騎寵設定好
# 離線掛網設定好
## 隊員方向面對隊長
# 隊長人物在最前面視窗
# 再醫院左下角落
# ----------------前提設定----------------- # 

systemLocation = Location(748, 614)

def switchWindow():
    
    # 隊員1開始加入
    click("1526652852632.png")
    wait(0.1)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()   
    
    # 檢測是否還在pk
    pointer = 0
    while not exists("1526660308320.png"):
        wait(1)
        pointer = pointer + 1
        if(pointer>30):
            keyDown(Key.ESC)
            wait(0.3)
            click("1526994564988.png")
            wait(0.1)
            click("1526994587978.png")
            pointer = 0
            break
    wait(5)
    keyDown(Key.ESC)
        
     # 隊員2開始加入
    click("1526652852632.png")
    wait(0.1)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()  
    
    # 檢測是否還在pk
    pointer = 0
    while not exists("1526660308320.png"):
        wait(1)
        pointer = pointer + 1
        if(pointer>30):
            keyDown(Key.ESC)
            wait(0.1)
            click("1526994564988.png")
            wait(0.1)
            click("1526994587978.png")
            pointer = 0
            break
    wait(5)
    keyDown(Key.ESC)
    
    # 隊長動作
    click("1526652852632-1.png")
    wait(0.1)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()
    
    # 檢測是否還在pk
    pointer = 0
    while not exists("1526660308320.png"):
        wait(1)
        pointer = pointer + 1
        if(pointer>30): # 等30秒
            keyDown(Key.ESC)
            wait(0.1)
            click("1526994564988.png")
            wait(0.1)
            click("1526994587978.png")
            break
    wait(5)
    keyDown(Key.ESC)

    LeaderbattleSetting()

def LeaderbattleSetting(): 

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

    if exists("1526995805693.png"):
        wait(1)

    # 一定要進入比賽才繼續往下走
    pointer = 0
    while exists("1526572518625-1.png"):
        wait(1)
        pointer = pointer + 1
        if(pointer>30):
            type(Key.ESC)
            click("1526572108497.png")
            click("1526996440330.png")
            LeaderbattleSetting()

    # pk進入後才往下走
    pointer = 0
    while not exists("1526572518625-1.png"):
        click(systemLocation)
        if exists("1526831872731.png"):           
            click("1526831872731.png")

        wait(1)
        pointer = pointer + 1
        if(pointer>150): #一場戰鬥不能打太久
            type(Key.ESC)
            click("1526994564988.png")
            wait(0.1)
            click("1526994587978.png")
            break
    wait(5)
    keyDown(Key.ESC)

    switchWindow()

switchWindow()


