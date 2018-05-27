# 33隨機pk、55隨機pk 

# ----------------前提設定----------------- # 
# 開啟五隻人物、並且都在醫院
# 戰鬥設定 - 戰寵騎寵設定好
# 掉線重連 - 離線掛網設定好 
#         - 不用設定隊長
# ----------------前提設定----------------- # 

systemLocation = Location(748, 614)

pointer = 0
# 視窗切換與設定 by location
def switchWindow(pointer):
    if(pointer>4):
        pointer = 0

    click("1527350845494.png")
    wait(0.1)

    if(pointer==0):
        type(Key.RIGHT)
        keyDown(Key.ENTER)
        keyUp()
    elif(pointer==1):
        type(Key.RIGHT)
        type(Key.RIGHT)
        keyDown(Key.ENTER)
        keyUp()             
    elif(pointer==2):
        type(Key.RIGHT)
        type(Key.RIGHT)
        type(Key.RIGHT)
        keyDown(Key.ENTER)
        keyUp()  
    elif(pointer==3):
        type(Key.RIGHT)
        type(Key.RIGHT)
        type(Key.RIGHT)
        type(Key.RIGHT)
        keyDown(Key.ENTER)
        keyUp()  
    elif(pointer==4):
        type(Key.RIGHT)
        type(Key.RIGHT)
        type(Key.RIGHT)
        type(Key.RIGHT)
        type(Key.RIGHT)
        keyDown(Key.ENTER)
        keyUp() 

        # 避免不斷等待時間
             
    if not exists("1526572518625-2.png"): 
        click(systemLocation)
        if exists("1527351729160.png"):
            click("1527351729160.png")
        click("1527351780050.png")
            
    # 檢測是否還在戰鬥
        # 如果還在戰鬥直接登出省時間
    timer = 0
    while not exists("1526572518625-2.png"):
        wait(1)
        timer = timer +1
        if(timer>8):           
            click(systemLocation)
            wait(1)
            click("1527351812129.png")
            wait(0.1)            
            click("1527407866760.png")
            wait(2) #5秒保險  
            break
                
    while not exists("1526572518625-2.png"):    #避免無法登入   
        #click("1526994587978-1.png")
        click(systemLocation)
        wait(1)
        click(systemLocation)
    wait(0.3)

    # 代表戰鬥結束        
    if exists("1526572518625-2.png"):
        battleSetting()
        pointer = pointer + 1
        switchWindow(pointer)

def battleSetting(): 
    # 脫離團隊
    click("1527351289882.png")
    wait(0.1) 
    click(systemLocation)
    
    # 關閉AI
    if exists("1526654646564-1.png"):
        click("1526654646564-1.png")
        
    wait(0.1)

    # 先取消一次
    click("1527351981489.png")
    click("1527351991759.png")

    wait(0.1)
    #選擇當天pk選項
    click(systemLocation)
    click("1527351981489.png")
    pk_pos = "1527352028019.png"
    #pk_pos = "pk_pos.png"
    click(pk_pos)

    click(systemLocation)

    # 開啟AI
    # 假如太快進入戰鬥，畫面會完全不同，此時會有問題
    # try...except跳過
    try:
        click("1527352049643.png")
        click("1527351780050.png")
    except:
        wait(3)
        
        # 嘗試
        #click("1527352049643.png")
        #click("1527351780050.png")
        # 嘗試

# 首次執行
switchWindow(pointer)
