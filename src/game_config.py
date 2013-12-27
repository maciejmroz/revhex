

class Config():
    WIDTH = 900
    HEIGHT = 540
    GENERATION_INTERVAL = 1.3
    MAX_BLOCKADES = 5
    MAX_DIFFICULTY = 10.0
    ROTATION_SPEED = 180.0
    SCORE_SCALE = 20.0

    #pattern is 12 sectors 30 degrees each
    #0 - empty sector
    #1,2,3,4 - sector sized 30-120 degrees
    PATTERNS=(
              (2,0,0,0,0,2,0,0,0,0),
              (1,0,1,0,1,0,1,0,1,0,1,0),
              (4,0,0,4,0,0),
              (4,4,0,0,0,0),
              (2,0,0,2,0,0,2,0,0),
              (3,0,3,0,3,0),
              (3,3,3,0,0,0)
              )    
    
    BLOCK_SPRITES=[
                     "sector1.png",
                     "sector2.png",
                     "sector3.png",
                     "sector4.png"
                     ]
    
    SHIP_IMAGE = 'ship.png'
    BACKGROUND_IMAGE = 'images.jpg'
    END_IMAGE = 'summary.png'

    PSY_SPRITES=[
                 "nebula.jpg"
                 ]