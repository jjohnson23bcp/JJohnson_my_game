# File created by John Johnson
'''
My goal is:

Atari Breakout 
Main Goal:
Ball that bounces off the blocks at the top of the screen and makes them disappear
Other Goals:
Platform at bottom of screen which player controls and the ball can bounce off
Ball increases in velocity when it collides with the top layer of platforms
Ball can collide with the walls and ceiling, but not floor
If ball goes through the floor, reset the ball
Limited number of times the ball can be reset
Keep score for platforms hit
'''
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 
# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite
# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
# create game class in order to pass properties to the sprites file
class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        # allows screen to be activated
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # caption of the screen window
        pg.display.set_caption("Breakout")
        # game clock
        self.clock = pg.time.Clock()
        # start running the game
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        self.score = 0
        # call all the sprites
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)        
        self.all_sprites.add(self.player)
        # platform list to add all the platforms
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        # calls in mobs
        for i in range(0,1):
            m = Mob(20,20,(255,255,255))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()
    # activates necessary game functions
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    # allows game to be exited
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            # if event.type == pg.KEYDOWN:
            #     if event.key == pg.K_SPACE:
            #         self.player.jump()
    # responsible for changes within the game
    def update(self):
        self.all_sprites.update()
        # if platform hits the player, reverse player velocity
        mhits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if mhits:
            if abs(self.player.vel.x) > abs(self.player.vel.y):
                self.player.vel.x *= -1
            else:
                self.player.vel.y *= -1
        # if player collides with a certain type of platform, either the platform disappears or the player bounces
        if self.player.vel.y == 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
    # draws the screen
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # is this a method or a function?
        pg.display.flip()
    # function to draw text on the screen
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    # function that will give coordinates of wherever the mouse clicks
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)
# instantiate the game class...
g = Game()
# kick off the game loop
while g.running:
    g.new()
# quits the game
pg.quit()