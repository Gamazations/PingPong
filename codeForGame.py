## Ping Pong - A game by Fadi & Abdullah
## Ping Pong is a game where you have to get the ball past your opponents paddle. We coded that game-- however, we added a twist!
## In our version of Ping Pong, powerups exist that can change the score and you are able to play different modes-- play against a real 
## person, against a Bot we made, and even an "Impossible" difficulty. First to 7 points wins the game! Have fun!

## Introduction Screen for the start of the game
introductionScreen = Group(
    Rect(0, 0, 400, 400, fill=gradient('darkRed', 'darkBlue', start='left')),
    Label('Ping Pong', 200, 100, fill='white', bold=True, size=40),
    Label('A game by Fadi & Abdullah', 200, 150, fill='white', font='caveat', size=20),
    Label('Controls: W, S', 100, 250, fill='white', size=15),
    Label('Controls: Up, Down', 290, 250, fill='white', size=15),
    Label('Select your mode:', 200, 275, fill='white', size=20))
    
## Different buttons of the different modes set on the home screen.
play1v1 = Label('Play 1v1', 200, 300, fill='white', size=20)
impossible=Label('Play Impossible Mode', 200, 375, fill='white', size=20)
playVsBot=Label('Play VS Bot', 200, 337.5, fill='white', size=20)

## This sets the homescreen as the first screen you see.
introductionScreen.visible=True

## The different backgrounds for the different gamemodes that exist    
defaultBackground = Rect(0, 0, 400, 400, fill=gradient('darkRed', 'darkBlue', start='left'))
versingBotBackground = Rect(0, 0, 400, 400, fill=gradient('darkRed', 'darkGreen', start='left'))
versingBotBackgroundImpossible = Rect(0, 0, 400, 400, fill=gradient('darkRed', 'darkGreen', start='left'))


## The different backgrounds that set the win screen for the different modes of the game.
redBackgroundWin = Group(
    Rect(0, 0, 400, 400, fill='darkRed'),
    Label('RED WINS!', 200, 200, fill='black', bold=True, size=50),
    Label('Click r to restart!', 200, 350, fill='white', size=20),
    Label('Click h to go to homescreen!', 200, 375, fill='white', size=20)
    )
blueBackgroundWin = Group(
    Rect(0, 0, 400, 400, fill='darkBlue'),
    Label('BLUE WINS', 200, 200, fill='black', bold=True, size=50),
    Label('Click r to restart!', 200, 350, fill='white', size=20),
    Label('Click h to go to homescreen!', 200, 375, fill='white', size=20)
    )
    
botBackgroundWin = Group(
    Rect(0, 0, 400, 400, fill='darkGreen'),
    Label('YOU LOST! BOT WINS!', 200, 200, fill='black', bold=True, size=30),
    Label('Click r to restart!', 200, 350, fill='white', size=20),
    Label('Click h to go to homescreen!', 200, 375, fill='white', size=20)
    )
    
userVersusBotBackgroundVictory = Group(
    Rect(0, 0, 400, 400, fill='darkRed'),
    Label('YOU WIN!', 200, 150, fill='black', bold=True, size=50),
    Label('You beat the bot!', 200, 200, fill='black', bold=True, size=20),
    Label('Click r to restart!', 200, 350, fill='white', size=20),
    Label('Click h to go to homescreen!', 200, 375, fill='white', size=20)
    )

botBackgroundWinImpossible = Group(
    Rect(0, 0, 400, 400, fill='darkGreen'),
    Label('YOU LOST! BOT WINS!', 200, 200, fill='black', bold=True, size=30),
    Label('Click r to restart!', 200, 350, fill='white', size=20),
    Label('Click h to go to homescreen!', 200, 375, fill='white', size=20)
    )
userVersusBotBackgroundVictoryImpossible = Group(
    Rect(0, 0, 400, 400, fill='darkRed'),
    Label('YOU WIN!', 200, 150, fill='black', bold=True, size=50),
    Label('You beat the bot!', 200, 200, fill='black', bold=True, size=20),
    Label('Thats impossible!', 200, 230, fill='gold', bold=True, size=20),
    Label('Click r to restart!', 200, 350, fill='white', size=20),
    Label('Click h to go to homescreen!', 200, 375, fill='white', size=20)
    )
    
## Setting all other backgrounds invisible so whenever first run, it starts with only the home screen.
defaultBackground.visible=False
blueBackgroundWin.visible=False
redBackgroundWin.visible=False
versingBotBackground.visible=False
botBackgroundWin.visible=False
userVersusBotBackgroundVictory.visible=False
versingBotBackgroundImpossible.visible=False
botBackgroundWinImpossible.visible=False
userVersusBotBackgroundVictoryImpossible.visible=False


## Different sprites and characters on the canvas
user1 = Rect(25, 200, 15, 75, fill='red')
user2 = Rect(360, 200, 15, 75, fill='blue')
bot = Rect(360, 200, 15, 75, fill='green')
scoreUser1 = Label(0, 100, 35, size=30, fill='red')
scoreUser2 = Label(0, 300, 35, size=30, fill='blue')
scoreBot = Label(0, 300, 35, size=30, fill='green')
CenterLine = Line(200, 0, 200, 400, fill='white', lineWidth=3)
pingPongBall = Circle(200, 200, 10, fill=gradient('white', 'lightGray', start='top'))

## Defines the ping pong ball's movement to start the game.
pingPongBall.dx = 6
pingPongBall.dy = 5

## The sprites for the powerups in the game
plusOnePoint = Group(
    Circle(0, 0, 20, fill='green'),
    Label('+1', 0, 0, size=20)
    )
minusOnePoint = Group(
    Circle(0, 0, 20, fill='red'),
    Label('-1', 0, 0, size=20)
    )
plusTwoPoints = Group(
    Circle(0, 0, 20, fill='gold'),
    Label('+2', 0, 0, size=20)
    )

## Setting the sprites that should not be visible at the start of the game invisible.
plusOnePoint.visible = False
minusOnePoint.visible=False
plusTwoPoints.visible=False
CenterLine.visible=False
bot.visible=False
scoreBot.visible=False

## A function defined to randomly create a chance to spawn a powerup. And then further have it spawn in a random place on the canvas.
def spawnPowerup():
    if randrange(1, 5)==1:
        plusOnePoint.centerX=randrange(100, 300)
        plusOnePoint.centerY=randrange(100, 300)
        plusOnePoint.visible=True
    if randrange(1, 10)==1:
        minusOnePoint.centerX=randrange(100, 300)
        minusOnePoint.centerY=randrange(100, 300)
        minusOnePoint.visible=True
    if randrange(1, 15)==1:
        plusTwoPoints.centerX=randrange(100, 300)
        plusTwoPoints.centerY=randrange(100, 300)
        plusTwoPoints.visible=True
        
## All these functions are used to switch between backgrounds depending on scenarios in the game. Calling wins screen when necessary, or the
## appropriate backgrounds.
def showIntroductionScreen():
    introductionScreen.visible=True
    play1v1.visible=True
    playVsBot.visible=True
    impossible.visible=True
    defaultBackground.visible=False
    CenterLine.visible=False
    redBackgroundWin.visible=False
    blueBackgroundWin.visible=False
    versingBotBackgroundImpossible.visible=False
    botBackgroundWinImpossible.visible=False
    plusOnePoint.visible=False
    plusTwoPoints.visible=False
    minusOnePoint.visible=False
    userVersusBotBackgroundVictoryImpossible.visible=False
    versingBotBackground.visible=False
    botBackgroundWin.visible=False
    userVersusBotBackgroundVictory.visible=False
 
def showDefaultBackground():
    introductionScreen.visible=False
    play1v1.visible=False
    playVsBot.visible=False
    impossible.visible=False
    defaultBackground.visible=True
    CenterLine.visible=True
    redBackgroundWin.visible=False
    blueBackgroundWin.visible=False
    versingBotBackgroundImpossible.visible=False
    botBackgroundWinImpossible.visible=False
    userVersusBotBackgroundVictoryImpossible.visible=False
    versingBotBackground.visible=False
    botBackgroundWin.visible=False
    userVersusBotBackgroundVictory.visible=False
    
def showRedBackgroundWin():
    introductionScreen.visible=False
    play1v1.visible=False
    playVsBot.visible=False
    impossible.visible=False
    defaultBackground.visible=False
    CenterLine.visible=False
    redBackgroundWin.visible=True
    blueBackgroundWin.visible=False
    plusOnePoint.visible=False
    plusTwoPoints.visible=False
    minusOnePoint.visible=False
    versingBotBackgroundImpossible.visible=False
    botBackgroundWinImpossible.visible=False
    userVersusBotBackgroundVictoryImpossible.visible=False
    versingBotBackground.visible=False
    botBackgroundWin.visible=False
    userVersusBotBackgroundVictory.visible=False
    
def showBlueBackgroundWin():
    introductionScreen.visible=False
    play1v1.visible=False
    playVsBot.visible=False
    impossible.visible=False
    defaultBackground.visible=False
    CenterLine.visible=False
    redBackgroundWin.visible=False
    blueBackgroundWin.visible=True
    plusOnePoint.visible=False
    plusTwoPoints.visible=False
    minusOnePoint.visible=False
    versingBotBackgroundImpossible.visible=False
    botBackgroundWinImpossible.visible=False
    userVersusBotBackgroundVictoryImpossible.visible=False
    versingBotBackground.visible=False
    botBackgroundWin.visible=False
    userVersusBotBackgroundVictory.visible=False
    
def showVersingBotBackground():
    introductionScreen.visible=False
    play1v1.visible=False
    playVsBot.visible=False
    impossible.visible=False
    defaultBackground.visible=False
    CenterLine.visible=True
    redBackgroundWin.visible=False
    blueBackgroundWin.visible=False
    versingBotBackgroundImpossible.visible=False
    botBackgroundWinImpossible.visible=False
    userVersusBotBackgroundVictoryImpossible.visible=False
    versingBotBackground.visible=True
    botBackgroundWin.visible=False
    userVersusBotBackgroundVictory.visible=False
    
def showBotBackgroundWin():
    introductionScreen.visible=False
    play1v1.visible=False
    playVsBot.visible=False
    impossible.visible=False
    defaultBackground.visible=False
    CenterLine.visible=False
    redBackgroundWin.visible=False
    blueBackgroundWin.visible=False
    plusOnePoint.visible=False
    plusTwoPoints.visible=False
    minusOnePoint.visible=False
    versingBotBackgroundImpossible.visible=False
    botBackgroundWinImpossible.visible=False
    userVersusBotBackgroundVictoryImpossible.visible=False
    versingBotBackground.visible=False
    botBackgroundWin.visible=True
    userVersusBotBackgroundVictory.visible=False
    
def showUserVersusBotBackgroundVictory():
    introductionScreen.visible=False
    play1v1.visible=False
    playVsBot.visible=False
    impossible.visible=False
    defaultBackground.visible=False
    CenterLine.visible=False
    redBackgroundWin.visible=False
    blueBackgroundWin.visible=False
    plusOnePoint.visible=False
    plusTwoPoints.visible=False
    minusOnePoint.visible=False
    versingBotBackgroundImpossible.visible=False
    botBackgroundWinImpossible.visible=False
    userVersusBotBackgroundVictoryImpossible.visible=False
    versingBotBackground.visible=True
    botBackgroundWin.visible=False
    userVersusBotBackgroundVictory.visible=True
    

def showVersingBotBackgroundImpossible():
    introductionScreen.visible=False
    play1v1.visible=False
    playVsBot.visible=False
    impossible.visible=False
    defaultBackground.visible=False
    CenterLine.visible=True
    redBackgroundWin.visible=False
    blueBackgroundWin.visible=False
    versingBotBackgroundImpossible.visible=True
    botBackgroundWinImpossible.visible=False
    userVersusBotBackgroundVictoryImpossible.visible=False
    versingBotBackground.visible=False
    botBackgroundWin.visible=False
    userVersusBotBackgroundVictory.visible=False
    
def showBotBackgroundWinImpossible():
    introductionScreen.visible=False
    play1v1.visible=False
    playVsBot.visible=False
    impossible.visible=False
    defaultBackground.visible=False
    CenterLine.visible=False
    redBackgroundWin.visible=False
    blueBackgroundWin.visible=False
    plusOnePoint.visible=False
    plusTwoPoints.visible=False
    minusOnePoint.visible=False
    versingBotBackgroundImpossible.visible=False
    botBackgroundWinImpossible.visible=True
    userVersusBotBackgroundVictoryImpossible.visible=False
    versingBotBackground.visible=False
    botBackgroundWin.visible=False
    userVersusBotBackgroundVictory.visible=False

def showUserVersusBotBackgroundVictoryImpossible():
    introductionScreen.visible=False
    play1v1.visible=False
    playVsBot.visible=False
    impossible.visible=False
    defaultBackground.visible=False
    CenterLine.visible=False
    redBackgroundWin.visible=False
    blueBackgroundWin.visible=False
    versingBotBackgroundImpossible.visible=False
    botBackgroundWinImpossible.visible=False
    userVersusBotBackgroundVictoryImpossible.visible=True
    versingBotBackground.visible=False
    botBackgroundWin.visible=False
    userVersusBotBackgroundVictory.visible=False
 
## A function defined to set the ping pong ball's position upon a win screen being shown, so that the ball doesn't move on the win screen.   
def pingPongBallWin():
    pingPongBall.centerX=200
    pingPongBall.centerY=250

## A wraparound function for the users so that they are able to wrap around the canvas in their movement.
def offScreen():
    if user1.top > 400:
        user1.top = 0
    if user1.bottom < 0:
        user1.top = 380
    if user2.top > 400:
        user2.top = 40
    if user2.bottom < 0:
        user2.top=380

## A function used to add to the score of the users whenever they have scored a point normally-- without powerups.
def addScore():
    if scoreUser2.visible==True:
        if (pingPongBall.centerX<-2):
            pingPongBall.centerX=200
            pingPongBall.centerY=200
            scoreUser2.value+=1
    if scoreBot.visible==True:
        if (pingPongBall.centerX<-2):
            pingPongBall.centerX=200
            pingPongBall.centerY=200
            scoreBot.value+=1
    if (pingPongBall.centerX>402):
        pingPongBall.centerX=200
        pingPongBall.centerY=200
        scoreUser1.value+=1

## onKeyHold utilized to be able to move the different users around with keys on the keyboard, such as W, S, up and down.    
def onKeyHold(keys):
    if defaultBackground.visible==True:
        if ('w' in keys):
            user1.centerY-=15
        if ('s' in keys):
            user1.centerY+=15
    
        if ('up' in keys):
            user2.centerY-=15
        if ('down' in keys):
            user2.centerY+=15
    if versingBotBackground.visible==True:
        if ('w' in keys):
            user1.centerY-=15
        if ('s' in keys):
            user1.centerY+=15
        if ('up' in keys):
            user1.centerY-=15
        if ('down' in keys):
            user1.centerY+=15
    
    ## If impossible mode is selected, the movement for your user is trippled in speed to ensure a challenge.
    elif (versingBotBackgroundImpossible.visible==True):
        if ('w' in keys):
            user1.centerY-=45
        if ('s' in keys):
            user1.centerY+=45
        if ('up' in keys):
            user1.centerY-=45
        if ('down' in keys):
            user1.centerY+=45
    
    ## Calling offScreen function so that the wraparound will work correctly upon the usage of the keys.   
    offScreen()

## A function that sets the winner when a user or the bot reaches a certain amount of points.
def setWinner():
    if scoreUser1.value>6:
        if defaultBackground.visible==True:
            showRedBackgroundWin()
            pingPongBallWin()
        if versingBotBackground.visible==True:
            showUserVersusBotBackgroundVictory()
            pingPongBallWin()
        if versingBotBackgroundImpossible.visible==True:
            showUserVersusBotBackgroundVictoryImpossible()
            pingPongBallWin()
            
            
    if scoreUser2.value>6:
        showBlueBackgroundWin()
        pingPongBallWin()
    if scoreBot.value>6:
        if versingBotBackground.visible==True:
            showBotBackgroundWin()
            pingPongBallWin()
        if versingBotBackgroundImpossible.visible==True:
            showBotBackgroundWinImpossible()
            pingPongBallWin()

## onMousePress is utilized for when someone clicks on one of the buttons for the modes, it will set the screen to that mode and take
## you to that mode so you can play it.
def onMousePress(mouseX, mouseY): 
    if play1v1.hits(mouseX, mouseY):
        showDefaultBackground()
    if playVsBot.hits(mouseX, mouseY):
        showVersingBotBackground()
        bot.visible=True
        scoreUser2.visible=False
        user2.visible=False
        scoreBot.visible=True
    if impossible.hits(mouseX, mouseY):
        showVersingBotBackgroundImpossible()
        bot.visible=True
        scoreUser2.visible=False
        user2.visible=False
        scoreBot.visible=True

## When hovering on one of the modes on the home screen, it will enlargen the option to show that you are selected that mode.
def onMouseMove(mouseX, mouseY):
    if play1v1.hits(mouseX, mouseY):
        play1v1.size=30
    if not(play1v1.hits(mouseX, mouseY)):
        play1v1.size=20
    if (playVsBot.hits(mouseX, mouseY)):
        playVsBot.size=30
    if not(playVsBot.hits(mouseX, mouseY)):
        playVsBot.size=20
    if impossible.hits(mouseX, mouseY):
        impossible.size=30
    if not(impossible.hits(mouseX, mouseY)):
        impossible.size=20

## onKeyPress is used so that if you click "r" after a user or bot wins, you can reset the score and play again. Additionally, if you click
## "h", it takes you back to the home screen where you can select a different mode.
def onKeyPress(key):
    if key=='r':
        if blueBackgroundWin.visible==True or redBackgroundWin.visible==True:
            showDefaultBackground()
            scoreUser1.value=0
            scoreUser2.value=0
            scoreBot.value=0
        if botBackgroundWin.visible==True or userVersusBotBackgroundVictory.visible==True:
            showVersingBotBackground()
            pingPongBall.centerX+=pingPongBall.dx
            pingPongBall.centerY+=pingPongBall.dy
            scoreUser1.value=0
            scoreBot.value=0
        if botBackgroundWinImpossible.visible==True or userVersusBotBackgroundVictoryImpossible.visible==True:
            showVersingBotBackgroundImpossible()
            pingPongBall.centerX+=pingPongBall.dx
            pingPongBall.centerY+=pingPongBall.dy
            scoreUser1.value=0
            scoreBot.value=0
            
    if key=='h':
        showIntroductionScreen()
        bot.visible=False
        scoreBot.visible=False
        scoreUser2.visible=True
        user2.visible=True
        scoreUser1.value=0
        scoreUser2.value=0
        scoreBot.value=0
        pingPongBall.centerX=200
        pingPongBall.centerY=200
        
## onStep was used for many different things that are constantly run to keep gameplay smooth and functional. u
def onStep():
    ## This allows for the movement of the Ping Pong Ball if someone has decided to play 1v1 mode.
    if defaultBackground.visible==True:
        pingPongBall.centerX+=pingPongBall.dx
        pingPongBall.centerY+=pingPongBall.dy
        ## This ensures that the bot will not interfere with the gameplay even if it is hidden in 1v1 mode.
        bot.centerY=user2.centerY
        ## This adds or substracts the necessary points when someone collects powerups in 1v1 mode.
        if pingPongBall.hitsShape(plusOnePoint):
            if pingPongBall.dx>0:
                scoreUser1.value+=1
                plusOnePoint.visible=False
                plusOnePoint.centerY=500
            if pingPongBall.dx<0:
                scoreUser2.value+=1
                plusOnePoint.visible=False
                plusOnePoint.centerY=500
        if pingPongBall.hitsShape(minusOnePoint):
            if pingPongBall.dx>0:
                scoreUser2.value-=1
                minusOnePoint.visible=False
                minusOnePoint.centerY=500
            if pingPongBall.dx<0:
                scoreUser1.value-=1
                minusOnePoint.visible=False
                minusOnePoint.centerY=500
        if pingPongBall.hitsShape(plusTwoPoints):
            if pingPongBall.dx>0:
                scoreUser1.value+=2
                plusTwoPoints.visible=False
                plusTwoPoints.centerY=500
            if pingPongBall.dx<0:
                scoreUser2.value+=2
                plusTwoPoints.visible=False
                plusTwoPoints.centerY=500

    ## This allows for the movement of the Ping Pong Ball if someone has decided to play VS Bot mode.
    if versingBotBackground.visible==True:
        pingPongBall.centerX+=pingPongBall.dx
        pingPongBall.centerY+=pingPongBall.dy
        ## This allows for the Bot to follow the ping pong ball, to make it a challenge and make the user have to collect points via
        ## powerups to win.
        bot.centerY=pingPongBall.centerY
        ## This adds or substracts the necessary points when someone collects powerups in VS Bot mode.
        if pingPongBall.hitsShape(plusOnePoint):
            if pingPongBall.dx>0:
                scoreUser1.value+=1
                plusOnePoint.visible=False
                plusOnePoint.centerY=500
            if pingPongBall.dx<0:
                scoreBot.value+=1
                plusOnePoint.visible=False
                plusOnePoint.centerY=500
        if pingPongBall.hitsShape(minusOnePoint):
            if pingPongBall.dx>0:
                scoreBot.value-=1
                minusOnePoint.visible=False
                minusOnePoint.centerY=500
            if pingPongBall.dx<0:
                scoreUser1.value-=1
                minusOnePoint.visible=False
                minusOnePoint.centerY=500
        if pingPongBall.hitsShape(plusTwoPoints):
            if pingPongBall.dx>0:
                scoreUser1.value+=2
                plusTwoPoints.visible=False
                plusTwoPoints.centerY=500
            if pingPongBall.dx<0:
                scoreBot.value+=2
                plusTwoPoints.visible=False
                plusTwoPoints.centerY=500
    
    ## This allows for the movement of the Ping Pong Ball if someone has decided to play Impossible mode.     
    if versingBotBackgroundImpossible.visible==True:
        pingPongBall.centerX+=pingPongBall.dx
        pingPongBall.centerY+=pingPongBall.dy
        ## This allows for the Bot to follow the ping pong ball, to make it a challenge and make the user have to collect points via
        ## powerups to win.
        bot.centerY=pingPongBall.centerY
        ## This adds or substracts the necessary points when someone collects powerups in Impossible mode.
        if pingPongBall.hitsShape(plusOnePoint):
            if pingPongBall.dx>0:
                scoreUser1.value+=1
                plusOnePoint.visible=False
                plusOnePoint.centerY=500
            if pingPongBall.dx<0:
                scoreBot.value+=1
                plusOnePoint.visible=False
                plusOnePoint.centerY=500
        if pingPongBall.hitsShape(minusOnePoint):
            if pingPongBall.dx>0:
                scoreBot.value-=1
                minusOnePoint.visible=False
                minusOnePoint.centerY=500
            if pingPongBall.dx<0:
                scoreUser1.value-=1
                minusOnePoint.visible=False
                minusOnePoint.centerY=500
        if pingPongBall.hitsShape(plusTwoPoints):
            if pingPongBall.dx>0:
                scoreUser1.value+=2
                plusTwoPoints.visible=False
                plusTwoPoints.centerY=500
            if pingPongBall.dx<0:
                scoreBot.value+=2
                plusTwoPoints.visible=False
                plusTwoPoints.centerY=500
    
    ## If the Impossible Mode is not chosen, then the speed is set to a normal place to ensure a "possible" gameplay.
    if not(versingBotBackgroundImpossible.visible==True):
        if pingPongBall.hitsShape(user1):
            spawnPowerup()
            pingPongBall.dx=6
        
        if pingPongBall.hitsShape(user2):
            spawnPowerup()
            pingPongBall.dx=-6
    
        if pingPongBall.hitsShape(bot):
            spawnPowerup()
            pingPongBall.dx=-6
    ## If however the above is false, and Impossible mode is chosen, then the speed is set to a more challenging level in Impossible Mode.
    else:
        if pingPongBall.hitsShape(user1):
            spawnPowerup()
            pingPongBall.dx=12
        
        if pingPongBall.hitsShape(user2):
            spawnPowerup()
            pingPongBall.dx=-12
    
        if pingPongBall.hitsShape(bot):
            spawnPowerup()
            pingPongBall.dx=-12
    ## This sets the dy value randomly so that upon hit of the users it can allow for the ball to go in a completely different way to ensure
    ## a level of uniqueness and randomness.
    if (pingPongBall.hitsShape(user1) or pingPongBall.hitsShape(user2)):
        if (pingPongBall.centerY<100):
            pingPongBall.dy=randrange(-15,15)
        elif (pingPongBall.centerY<150):
            pingPongBall.dy=randrange(-15,15)
        elif (pingPongBall.centerY<200):
            pingPongBall.dy=randrange(-15,15)
        elif (pingPongBall.centerY>250):
            pingPongBall.dy=randrange(-15,15)
        elif (pingPongBall.centerY>300):
            pingPongBall.dy=randrange(-15,15)
        elif (pingPongBall.centerY>350):
            pingPongBall.dy=randrange(-15,15)
    ## This sets the dy value randomly so that upon hit of the user or the bot it can allow for the ball to go in a 
    ## completely different way to ensure a level of uniqueness and randomness.      
    if pingPongBall.hitsShape(bot):
        if (pingPongBall.centerY<100):
            pingPongBall.dy=randrange(-15,15)
        elif (pingPongBall.centerY<150):
            pingPongBall.dy=randrange(-15,15)
        elif (pingPongBall.centerY<200):
            pingPongBall.dy=randrange(-15,15)
        elif (pingPongBall.centerY>250):
            pingPongBall.dy=randrange(-15,15)
        elif (pingPongBall.centerY>300):
            pingPongBall.dy=randrange(-15,15)
        elif (pingPongBall.centerY>350):
            pingPongBall.dy=randrange(-15,15)
    
    ## This allows for the Ping Pong ball to bounce back if it touches the top or bottom of the screen. 
    if (pingPongBall.centerY<0):
        pingPongBall.dy=10
    if (pingPongBall.centerY>=400):
        pingPongBall.dy=-10
    
    ## This calls the function to set the winner after someone reaches the set amount of points    
    setWinner()
    ## This calls the function to add the score when someone scores by getting it past the paddle.
    addScore()
