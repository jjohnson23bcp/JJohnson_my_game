# file created by John Johnson
# game attributes
WIDTH = 800
HEIGHT = 600
PLAYER_VEL = 1
PLAYER_ACC = 1
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 0
MOB_VEL = 3
MOB_ACC = 2
MOB_FRICTION = -0.3
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(10, 10, 60, 20, (200,200,200), "disappearing"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (100,255,100), "bouncey"),
                 (125, HEIGHT - 350, 100, 5, (200,100,50), "disappearing"),
                 (80, 10, 60, 20, (200,200,200), "disappearing"),
                 (150, 10, 60, 20, (200,200,200), "disappearing"),
                 (220, 10, 60, 20, (200,200,200), "disappearing"),
                 (290, 10, 60, 20, (200,200,200), "disappearing"),
                 (360, 10, 60, 20, (200,200,200), "disappearing"),
                 (430, 10, 60, 20, (200,200,200), "disappearing"),
                 (500, 10, 60, 20, (200,200,200), "disappearing"),
                 (570, 10, 60, 20, (200,200,200), "disappearing"),
                 (640, 10, 60, 20, (200,200,200), "disappearing"),
                 (710, 10, 60, 20, (200,200,200), "disappearing")]