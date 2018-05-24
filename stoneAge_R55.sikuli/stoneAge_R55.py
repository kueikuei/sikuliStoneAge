# 55隨機pk

# ----------------前提設定----------------- # 
# 開啟五隻人物、並且都在醫院
# 戰鬥設定好戰寵騎寵

# ----------------前提設定----------------- # 

L1 = Location(234, 660)
L2 = Location(392, 665)
L3 = Location(550, 671)
L4 = Location(772, 651)
L5 = Location(908, 658)

systemLocation = Location(748, 614)

locationList = [L1,L2,L3,L4,L5]

pointer = 0

# 視窗切換與設定 by location
def switchWindow(pointer):

    click("1526652852632.png")
    wait(0.1)
    click(locationList[pointer])

    # 檢測是否還在戰鬥
    # 如果還在戰鬥:
    if not exists("1526572518625-1.png"):
        click(systemLocation)
        if not exists("1526832621719.png"):
            click("1526832621719.png")

    # 代表戰鬥結束        
    if exists("1526572518625-1.png"):
        
        battleSetting()

def battleSetting(): 
    # 脫離團隊
    click("1526832676608.png")
    
    click(systemLocation)
    
    # 關閉AI
    if exists("1526654646564-1.png"):
        click("1526654646564-1.png")
        
    wait(0.1)

    #選擇當天pk選項
    click("1526834404011.png")
    pk_pos = "1526831758224.png"
    click(pk_pos)

    click(systemLocation)
    # 開啟AI
    try:
        click("1526831872731.png")
        click("1526659575850.png")
    except:
        wait(1)

        # 假如太快戰鬥畫面被切斷
        while not exists("1526832070861.png"):
            pointer = pointer + 1
            click("1526652852632.png")
            wait(0.1)
            switchWindow(pointer)

    pointer = pointer + 1
    switchWindow(pointer)

switchWindow(pointer)

