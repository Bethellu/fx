stopTime = 0
counting = True
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . 5 5 5 5 5 5 . . . . . 
            . . . 5 5 5 5 5 5 5 5 5 5 . . . 
            . . . 5 5 5 5 5 5 5 5 5 5 . . . 
            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
            . . . 5 5 5 5 5 5 5 5 5 5 . . . 
            . . . 5 5 5 5 5 5 5 5 5 5 . . . 
            . . . . . 5 5 5 5 5 5 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
mySprite.set_stay_in_screen(True)
mySprite.left = 0
mySprite.fx = 30
mySprite.vx = 90
for index in range(3):
    mySprite.vx = 80
    pause(1000)
"""

per 100/1000 ms update.

stoptime per 1/10ms.

"""

def on_update_interval():
    global stopTime, counting
    if counting:
        stopTime += 0.1
        if mySprite.vx == 0:
            counting = False
            mySprite.say_text("" + str(stopTime) + "sec", 5000, False)
game.on_update_interval(100, on_update_interval)
