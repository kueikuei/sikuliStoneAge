pointer = 0
while not exists("1526660308320.png"):
    wait(1)
    pointer = pointer + 1
    if(pointer>2):
        #click("1527001646661.png")
        #wait(2)
        
        keyDown(Key.ESC)
        #mouseMove(Location(747, 612))
        wait(0.1)
  
        #click(Location(747, 612))
        #wait(3)
        #mouseMove(Location(187, 253))
        #click(Location(187, 253))
        click("1526994564988.png")
        wait(0.1)
        click("1526994587978.png")
        #dosthing()
        break
wait(5)
keyDown(Key.ESC)

def dosthing():
    wait(5)
    click("1526652852632.png")
    wait(0.1)
    type(Key.RIGHT)
    type(Key.RIGHT)
    keyDown(Key.ENTER)
    keyUp()   