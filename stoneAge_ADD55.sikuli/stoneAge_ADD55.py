# 33隨機pk、55隨機pk

# ----------------前提設定----------------- # 
# 開啟五隻人物、並且都在醫院
# 戰鬥設定 - 戰寵騎寵設定好
# 掉線重連 - 離線掛網設定好
#         - 要設定好隊長隊員
# 隊員方向面對隊長
# 隊長人物在最前面視窗
# 再醫院左下角落
# ----------------前提設定----------------- # 

systemLocation = Location(748, 614)


def switchWindow():
    
    # 隊員1開始加入
    click("1526652852632-2.png")
    wait(0.1)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()   

    
    # 檢測是否還在戰鬥
    # 如果還在戰鬥直接登出省時間
    ckeckPKorNot()
    
    #wait(1)
    wait(0.3)
     # 隊員2開始加入
    click("1526652852632-2.png")
    wait(0.1)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()  

    
    # 檢測是否還在pk
    ckeckPKorNot()
    
    # 隊員3開始加入
    click("1526652852632-2.png")
    wait(0.1)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()  
    
    # 檢測是否還在pk
    ckeckPKorNot()

    # 隊員4開始加入
    click("1526652852632-2.png")
    wait(0.1)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()  

    # 檢測是否還在pk
    ckeckPKorNot()

    #wait(1)
    # 隊長動作
    click("1526652852632-3.png")
    wait(0.1)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()
  
    LeaderbattleSetting()

def ckeckPKorNot():
    # 檢測是否還在pk
    try:
        if not exists("1526572518625-5.png"):
            
            mouseMove(Location(748, 613))
            click(Location(748, 613))
            click("1526994564988-4.png")
            wait(0.1)
            click("1526994587978-4.png")
    
        while not exists("1526572518625-2.png"):    #避免燈不近來   
            click("1526994587978-4.png")
            
        click("1527171784489.png")
    except:
        wait(1)

def LeaderbattleSetting(): 

    # 開始PK
    try:
        click(systemLocation)
    
        # 關閉AI
        if exists("1526654646564-1.png"):
            click("1526654646564-1.png")
            
        click("1526572108497-1.png")
        wait(0.1)
    except:
        wait(0.2)

    #選擇當天pk選項
    pk_pos = "1527264739942.png"
    click(pk_pos)

    wait(0.1)

    if exists("1526995805693-1.png"):
        switchWindow()

    try:
        # 一定要進入比賽才繼續往下走
        pointer = 0
        while exists("1526572518625-3.png"):
            wait(1)
            pointer = pointer + 1
            if(pointer>30):
                click(systemLocation)
                click("1526572108497-1.png")
                click("1526996440330-1.png")
                LeaderbattleSetting()
    except:
        wait(1)

    # pk進入後才往下走
    while not exists("1526572518625-3.png"):
        # 開啟AI
        click(systemLocation)
        if exists("1526660560282-1.png"):
            click("1526660560282-1.png")
        click("1526659575850-2.png")
        wait(1)

        # 檢測是否還在pk
        pointer = 0
        while not exists("1526572518625-5.png"):
            pointer = pointer + 1
            if(pointer>30):
                mouseMove(Location(748, 613))
                click(Location(748, 613))
                click("1526994564988-4.png")
                wait(0.1)
                click("1526994587978-4.png")
                break
        while not exists("1526572518625-2.png"):    #避免燈不近來           
            click("1526994587978-4.png")
            
    # 飛掉的話等待切換到隊員一
        break
    switchWindow()

switchWindow()


