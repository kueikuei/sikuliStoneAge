     # 檢測是否還在戰鬥
        # 如果還在戰鬥直接登出省時間
    timer = 0
    while not exists("1526572518625-1.png"):
        wait(1)
        timer = timer +1
        if(timer>1):           
            click(systemLocation)
            wait(1)
            click("1526994564988.png")
            wait(0.1)
            click("1526994587978.png")
            wait(2) #5秒保險  
    
    while not exists("1526572518625-1.png"):    #避免無法登入   
        click("1526994587978.png")
    wait(0.3)