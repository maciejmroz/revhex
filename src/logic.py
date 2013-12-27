import cocos
from random import choice
from random import randrange
from pyglet.window import key
from blockade import LinearProgress
from blockade import InverseLinearProgress
from blockade import Blockade
from game_config import Config

class ControlLayer(cocos.layer.Layer):
    
    is_event_handler = True
    
    def __init__(self,hud):
        super( ControlLayer, self ).__init__()
        self.blockades = []
        self.keys_pressed = set()
        self.hud = hud
        self.start_game()
        self.schedule(self.update)

    def start_game(self):
        for blockade in self.blockades:
            self.remove(blockade)
        self.blockades = []
        self.lifetime = 0.0
        self.last_new_layer = -Config.GENERATION_INTERVAL
        self.difficulty = 1.0
        self.tunnel_rotation = 0.0
        self.score = 0.0
        self.game_state = "in_game"
        self.hud.start_game()
        
    def stop_game(self):
        self.game_state = "post_game"
        self.hud.stop_game()
                
    def on_key_press (self, k, modifiers):
        self.keys_pressed.add(k)

    def on_key_release (self, k, modifiers):
        self.keys_pressed.remove(k)
        if self.game_state == 'post_game':
            if k == key.SPACE:
                self.start_game()
    
    def add_blockade(self):
        rc = LinearProgress(float(randrange(180)),0)
        sc = InverseLinearProgress(6.0,-1.0*self.difficulty)
        #sc = InverseLinearProgress(6.0,-0.1)
        blockade = Blockade (choice(Config.PATTERNS),
                             rotation_controller = rc,
                             scaling_controller = sc)
        self.blockades.append(blockade)
        self.add(blockade)
        
    def update_difficulty(self):
        self.difficulty = 1.0 + self.lifetime/45.0
        
    def update_tunnel_rotation(self,dt):
        if key.LEFT in self.keys_pressed:
            self.tunnel_rotation -= Config.ROTATION_SPEED * dt * self.difficulty
        elif key.RIGHT in self.keys_pressed:
            self.tunnel_rotation += Config.ROTATION_SPEED * dt * self.difficulty
        if self.tunnel_rotation < 0.0:
            self.tunnel_rotation += 360.0
        if self.tunnel_rotation > 360.0:
            self.tunnel_rotation -= 360.0
                
    def update(self,dt):
        if self.game_state == 'post_game':
            return
        self.lifetime += dt
        self.update_difficulty()
        self.update_tunnel_rotation(dt)
        if (self.lifetime - self.last_new_layer) > (Config.GENERATION_INTERVAL)/self.difficulty:
            if len(self.blockades) > (Config.MAX_BLOCKADES-1):
                self.remove(self.blockades[0])
                self.blockades.pop(0)
            self.add_blockade()
            self.last_new_layer = self.lifetime
        for blockade in self.blockades:
            blockade.rotation_offset = self.tunnel_rotation
            blockade.update(dt)
            if blockade.collide():
                self.stop_game()
                return
        self.score += dt * self.difficulty * Config.SCORE_SCALE
        self.hud.update_score(int(self.score))
