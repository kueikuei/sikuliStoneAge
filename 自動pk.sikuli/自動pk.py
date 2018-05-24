#請確定主要隊長視窗在右上角



while exists("1526572518625.png"):
    # 測試用
    #mouseMove(Location(394, 346))
    #rightClick(Location(402, 324))
    #click("1526572518625.png")
    # 測試用

    # 更換寵物狀態
    click(Location(290, 617))
    while not exists("1526573101833.png"):
        click(Location(47, 71))

    while not exists("1526573167502.png"):
        click(Location(46, 123))
    
    # 開始PK
    click(Location(748, 614))
    click("1526572108497.png")
    wait(5)

    #選擇當天pk選項
    pk_pos = Location(396, 386)
    click(pk_pos)
    wait(30)
    
    click(Location(748, 614))
    click("1526572187273.png")

    wait(300)





#判斷pk結束